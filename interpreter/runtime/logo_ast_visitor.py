class ASTVisitor:
    def visit(self, ast):
        if ast is None:
            return None

        return ast.accept(self)
