# -*- coding: utf-8 -*-

from algo.stmts.BlockStmt import BlockStmt
from .BaseStmt import *


class ForStmt(BlockStmt):
    def __init__(self, variable: str, begin: AstNode, end: AstNode, children: CodeBlock, step: AstNode = None):
        super().__init__(children)
        self.variable = variable
        self.begin = begin
        self.end = end
        self.step = step

    def __str__(self):
        return "[For %s = %s -> %s [%s] %s]" % (self.variable, self.begin, self.end, self.step, super().__str__())

    def __repr__(self):
        return "ForStmt(%r, %r, %r, %r, %r)" % (self.variable, self.begin, self.end, self.children, self.step)

    def python_header(self) -> str:
        return "for %s in irange(%s, %s, %s):" % (
            self.variable, self.begin.python(), self.end.python(), "None" if self.step is None else self.step.python())

    def get_children(self) -> List[AstNode]:
        return self.begin.flatten() + self.end.flatten() + (
            [] if self.step is None else self.step.flatten()) + super().get_children()
