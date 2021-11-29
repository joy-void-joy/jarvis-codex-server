"""
Anonymize a piece of code returned by codex VA.
Anonymization consists of:

- Renaming variable names to generic ones: fib -> a, fact -> b
- Replace the return statements to a list of expressions it contains: return f"The sun is {temperature}°C" -> return [temperature]

This process is called before asking the verificator model what the code means. It is important so that it does not get confused by names and variables
(Without it, Codex could assume that if a function is named fib, then it is fibonnacci, regardless of the way it is actually implemented)
"""
from __future__ import annotations
from typing import Any

import ast
import string
import random

class Anonymizer(ast.NodeTransformer):
    def __init__(self):
        self.pool = string.ascii_letters
        self.current_number_letters = 1
        self.lut = {}
        self.context = {}

    ### Utils
    def _assign_name(self, node: Any, key="name"):
        if len(self.lut) >= len(self.pool) ** self.current_number_letters:
            self.current_number_letters += 1

        while (r := ''.join(random.choices(self.pool, k=self.current_number_letters))) in self.lut.values():
            pass

        self.lut[getattr(node, key)] = r
        setattr(node, key, r)
        return r


    ### Visitors
    def generic_visit(self, node: ast.AST, **kwargs) -> ast.AST:
        old_context = dict(self.context)
        self.context |= kwargs

        result =  super().generic_visit(node)

        self.context = old_context
        return result

        ## Transforms "return f'This is a {value} and {another}'" into "return [value, another]"
    def visit_Return(self, node: ast.Return) -> Any:
        if isinstance(node.value, ast.JoinedStr):
            result = ast.List([i.value for i in ast.walk(node) if isinstance(i, ast.FormattedValue)])
        elif isinstance(node.value, ast.Str):
            result = ast.List([])
        else:
            result = node.value

        return ast.Return(self.generic_visit(result))
    
        ## Anonymize variables/function/classes names
    def visit_ClassDef(self, node: ast.ClassDef) -> Any:
        self._assign_name(node)
        return self.generic_visit(node)

    
    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        if node.name.startswith('on_'):
            return self.generic_visit(node)

        self._assign_name(node)

        return self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> Any:
        return self.visit_FunctionDef(node)

    def visit_arg(self, node: ast.arg) -> Any:
        if node.arg == "self":
            return self.generic_visit(node)

        self._assign_name(node, key='arg')
        return self.generic_visit(node)
    

    def visit_Name(self, node: ast.Name) -> Any:
        try:
            # Name is already assigned
            node.id = self.lut[node.id]
        except KeyError as e:
            # Name is new and has to be declared. This can only happen if we are storing the variable (as in: number = 42 -> n = 42)
            if isinstance(node.ctx, ast.Store):
                self._assign_name(node, 'id')
            else:
                raise e
        finally:
            return self.generic_visit(node)

def anonymize(code):
    return ast.unparse(Anonymizer().visit(ast.parse(code)))

if __name__ == "__main__":
    import sys
    print("Enter code to be anonymized")
    code = sys.stdin.read()
    print(anonymize(code))