# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayliteral.
    def visitArrayliteral(self, ctx:MT22Parser.ArrayliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayprime.
    def visitArrayprime(self, ctx:MT22Parser.ArrayprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayelements.
    def visitArrayelements(self, ctx:MT22Parser.ArrayelementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayelement.
    def visitArrayelement(self, ctx:MT22Parser.ArrayelementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraytyp.
    def visitArraytyp(self, ctx:MT22Parser.ArraytypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayindexprime.
    def visitArrayindexprime(self, ctx:MT22Parser.ArrayindexprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayindexes.
    def visitArrayindexes(self, ctx:MT22Parser.ArrayindexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayindex.
    def visitArrayindex(self, ctx:MT22Parser.ArrayindexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#actomic.
    def visitActomic(self, ctx:MT22Parser.ActomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#elementtype.
    def visitElementtype(self, ctx:MT22Parser.ElementtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variablerecursive.
    def visitVariablerecursive(self, ctx:MT22Parser.VariablerecursiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#nonvardecl.
    def visitNonvardecl(self, ctx:MT22Parser.NonvardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifiersprime.
    def visitIdentifiersprime(self, ctx:MT22Parser.IdentifiersprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifierslist.
    def visitIdentifierslist(self, ctx:MT22Parser.IdentifierslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifiers.
    def visitIdentifiers(self, ctx:MT22Parser.IdentifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlements.
    def visitExprlements(self, ctx:MT22Parser.ExprlementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexpr.
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexop.
    def visitIndexop(self, ctx:MT22Parser.IndexopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcproto.
    def visitFuncproto(self, ctx:MT22Parser.FuncprotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returntyp.
    def visitReturntyp(self, ctx:MT22Parser.ReturntypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subpart.
    def visitSubpart(self, ctx:MT22Parser.SubpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcbody.
    def visitFuncbody(self, ctx:MT22Parser.FuncbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funccall.
    def visitFunccall(self, ctx:MT22Parser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argumentprime.
    def visitArgumentprime(self, ctx:MT22Parser.ArgumentprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argumentlists.
    def visitArgumentlists(self, ctx:MT22Parser.ArgumentlistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argumentlist.
    def visitArgumentlist(self, ctx:MT22Parser.ArgumentlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameterlist.
    def visitParameterlist(self, ctx:MT22Parser.ParameterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameters.
    def visitParameters(self, ctx:MT22Parser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignmentstmt.
    def visitAssignmentstmt(self, ctx:MT22Parser.AssignmentstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalar_variable.
    def visitScalar_variable(self, ctx:MT22Parser.Scalar_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_expression.
    def visitIndex_expression(self, ctx:MT22Parser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifstmt.
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#false_statement.
    def visitFalse_statement(self, ctx:MT22Parser.False_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forstmt.
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr.
    def visitInit_expr(self, ctx:MT22Parser.Init_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#condition_expr.
    def visitCondition_expr(self, ctx:MT22Parser.Condition_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#update_expr.
    def visitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whilestmt.
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr_while.
    def visitExpr_while(self, ctx:MT22Parser.Expr_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_whilestmt.
    def visitDo_whilestmt(self, ctx:MT22Parser.Do_whilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continuestmt.
    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnstmt.
    def visitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callstmt.
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block.
    def visitBlock(self, ctx:MT22Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmtprime.
    def visitBlock_stmtprime(self, ctx:MT22Parser.Block_stmtprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmts.
    def visitBlock_stmts(self, ctx:MT22Parser.Block_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statements.
    def visitStatements(self, ctx:MT22Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolean.
    def visitBoolean(self, ctx:MT22Parser.BooleanContext):
        return self.visitChildren(ctx)



del MT22Parser