from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decls()))

    # arrayliteral: LCB arrayprime RCB;
    # arrayprime: arrayelements | ;
    # arrayelements: arrayelement CM arrayelements | arrayelement;
    # arrayelement: expr;
    def visitArrayliteral(self, ctx: MT22Parser.ArrayliteralContext):
        return ArrayLit(self.visit(ctx.arrayprime()))

    #
    def visitArrayprime(self, ctx: MT22Parser.ArrayprimeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.arrayelements())
        return []

    #
    def visitArrayelements(self, ctx: MT22Parser.ArrayelementsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.arrayelement())]
        return [self.visit(ctx.arrayelement())] + self.visit(ctx.arrayelements())

    #
    def visitArrayelement(self, ctx: MT22Parser.ArrayelementContext):
        return self.visit(ctx.expr())

    # arraytyp: ARRAY LSB arrayindexprime RSB OF elementtype;
    # arrayindexprime: arrayindexes ;
    # arrayindexes: arrayindex CM arrayindexes | arrayindex;
    # arrayindex: Integer;
    def visitArraytyp(self, ctx: MT22Parser.ArraytypContext):

        return ArrayType(self.visit(ctx.arrayindexprime()), self.visit(ctx.elementtype()))

    #
    def visitArrayindexprime(self, ctx: MT22Parser.ArrayindexprimeContext):
        return self.visit(ctx.arrayindexes())

    #
    def visitArrayindexes(self, ctx: MT22Parser.ArrayindexesContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.arrayindex())]
        return [self.visit(ctx.arrayindex())] + self.visit(ctx.arrayindexes())

    #
    def visitArrayindex(self, ctx: MT22Parser.ArrayindexContext):
        return int(ctx.Integer().getText())

    # actomic: INT | FLOAT | STRING | BOOLEAN;
    def visitActomic(self, ctx: MT22Parser.ActomicContext):
        if ctx.INT():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        return BooleanType()

    # elementtype: actomic;
    def visitElementtype(self, ctx: MT22Parser.ElementtypeContext):
        return self.visit(ctx.actomic())

    # decls: decl decls | decl;
    def visitDecls(self, ctx: MT22Parser.DeclsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.decl())
        return self.visit(ctx.decl()) + self.visit(ctx.decls())

    # decl: vardecl | funcdecl;
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        return self.visit(ctx.funcdecl())

    # vardecl: variablerecursive SM | nonvardecl;
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.nonvardecl():
            return self.visit(ctx.nonvardecl())
        res = self.visit(ctx.variablerecursive())
        listid = res[1][::-1]
        listexpr = res[2]
        x = tuple(zip(listid, listexpr))
        return [VarDecl(tup[0], res[0], tup[1]) for tup in x]

    # variablerecursive: Identifiers CM variablerecursive CM expr | Identifiers COLON typ EQ expr;
    def visitVariablerecursive(self, ctx: MT22Parser.VariablerecursiveContext):
        if ctx.typ():
            return [self.visit(ctx.typ()), [ctx.Identifiers().getText()], [self.visit(ctx.expr())]]
        result = self.visit(ctx.variablerecursive())
        result[1] += [ctx.Identifiers().getText()]
        result[2] += [self.visit(ctx.expr())]
        return result

    # nonvardecl:  identifiersprime COLON typ SM;
    def visitNonvardecl(self, ctx: MT22Parser.NonvardeclContext):
        identifiersprime = self.visit(ctx.identifiersprime())
        typ = self.visit(ctx.typ())
        return [VarDecl(x, typ) for x in identifiersprime]

        # identifiersprime: identifierslist ;

    # identifierslist: identifiers CM identifierslist | identifiers;
    # identifiers: Identifiers;
    def visitIdentifiersprime(self, ctx: MT22Parser.IdentifiersprimeContext):
        return self.visit(ctx.identifierslist())

    def visitIdentifierslist(self, ctx: MT22Parser.IdentifierslistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.identifiers())]
        return [self.visit(ctx.identifiers())] + self.visit(ctx.identifierslist())

    def visitIdentifiers(self, ctx: MT22Parser.IdentifiersContext):
        return ctx.Identifiers().getText()

    # typ: actomic| arraytyp| AUTO;
    def visitTyp(self, ctx: MT22Parser.TypContext):
        if ctx.actomic():
            return self.visit(ctx.actomic())
        elif ctx.arraytyp():
            return self.visit(ctx.arraytyp())
        elif ctx.AUTO():
            return AutoType()

    # exprlist: exprlements  ;
    # exprlements: expr CM exprlements | expr;
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        return self.visit(ctx.exprlements())

    def visitExprlements(self, ctx: MT22Parser.ExprlementsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprlements())

    # expr: expr1 CONCAT expr1 | expr1;
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.CONCAT().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        return self.visit(ctx.expr1(0))

    # expr1: expr2 (DOUEQ|DIFF|SMALLER|GREATER|SMAEQ|GREEQ) expr2	| expr2;
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.getChildCount() == 3:
            if ctx.DOUEQ():
                return BinExpr(ctx.DOUEQ().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
            elif ctx.DIFF():
                return BinExpr(ctx.DIFF().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
            elif ctx.SMALLER():
                return BinExpr(ctx.SMALLER().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
            elif ctx.GREATER():
                return BinExpr(ctx.GREATER().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
            elif ctx.SMAEQ():
                return BinExpr(ctx.SMAEQ().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
            elif ctx.GREEQ():
                return BinExpr(ctx.GREEQ().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        return self.visit(ctx.expr2(0))

    # expr2: expr2 (CONJUNCTION|DISJUNCTION) expr3|expr3;
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.getChildCount() == 3 and ctx.CONJUNCTION():
            return BinExpr(ctx.CONJUNCTION().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        elif ctx.getChildCount() == 3 and ctx.DISJUNCTION():
            return BinExpr(ctx.DISJUNCTION().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        else:
            return self.visit(ctx.expr3())

    # expr3: expr3 (ADDOP|MINUSOP) expr4 | expr4;
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.getChildCount() == 3 and ctx.ADDOP():
            return BinExpr(ctx.ADDOP().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        elif ctx.getChildCount() == 3 and ctx.MINUSOP():
            return BinExpr(ctx.MINUSOP().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        else:
            return self.visit(ctx.expr4())

    # expr4: expr4 (MULOP|DIVOP|MODUOP) expr5 | expr5;
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.getChildCount() == 3 and ctx.MULOP():
            return BinExpr(ctx.MULOP().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        elif ctx.getChildCount() == 3 and ctx.DIVOP():
            return BinExpr(ctx.DIVOP().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        elif ctx.getChildCount() == 3 and ctx.MODUOP():
            return BinExpr(ctx.MODUOP().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr5())

    # expr5: NEGATION expr5 | expr6;
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.NEGATION().getText(), self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())

    # expr6: MINUSOP expr6 | 	expr7;
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.MINUSOP().getText(), self.visit(ctx.expr6()))
        return self.visit(ctx.expr7())

    # expr7: expr7 (LSB|RSB)| expr8;
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.LSB():
            return UnExpr(ctx.LSB().getText(), self.visit(ctx.expr7()))
        elif ctx.RSB():
            return UnExpr(ctx.RSB().getText(), self.visit(ctx.expr7()))
        return self.visit(ctx.expr8())

    # expr8: String |Integer|Float|Identifiers| boolean | funccall |subexpr|arrayliteral|indexop ;
    def visitExpr8(self, ctx: MT22Parser.Expr8Context):
        if ctx.String():
            return StringLit(str(ctx.String().getText()))
        elif ctx.Integer():
            return IntegerLit(int(ctx.Integer().getText()))
        elif ctx.Float():
            if ctx.Float().getText()[0] == '.':
                if ctx.Float().getText()[1] == 'e' or ctx.Float().getText()[1] == 'E':
                    return FloatLit(float(0))
            return FloatLit(float(ctx.Float().getText()))
        elif ctx.Identifiers():
            return Id(ctx.Identifiers().getText())
        elif ctx.boolean():
            return BooleanLit(self.visit(ctx.boolean()))
        elif ctx.funccall():
            return self.visit(ctx.funccall())
        elif ctx.subexpr():
            return self.visit(ctx.subexpr())
        elif ctx.arrayliteral():
            return self.visit(ctx.arrayliteral())
        return self.visit(ctx.indexop())

    # subexpr: LB expr RB;
    def visitSubexpr(self, ctx: MT22Parser.SubexprContext):
        return self.visit(ctx.expr())

    # indexop: Identifiers LSB exprlist RSB;
    def visitIndexop(self, ctx: MT22Parser.IndexopContext):
        return ArrayCell(ctx.Identifiers().getText(), self.visit(ctx.exprlist()))

    # funcdecl: funcproto funcbody;

    # returntyp: actomic|VOID|arraytyp|AUTO;
    # subpart: INHERIT Identifiers;

    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        result = self.visit(ctx.funcproto())
        return [FuncDecl(result[0], result[1], result[2], result[3], self.visit(ctx.funcbody()))]

    # funcproto: Identifiers COLON FUNCTION returntyp LB parameterlist RB (subpart)?;
    def visitFuncproto(self, ctx: MT22Parser.FuncprotoContext):
        if ctx.getChildCount() == 8:
            return [ctx.Identifiers().getText(), self.visit(ctx.returntyp()),
                    self.visit(ctx.parameterlist()), self.visit(ctx.subpart())]
        return [ctx.Identifiers().getText(), self.visit(ctx.returntyp()),
                self.visit(ctx.parameterlist()), None]

    def visitReturntyp(self, ctx: MT22Parser.ReturntypContext):
        if ctx.VOID():
            return VoidType()
        elif ctx.arraytyp():
            return self.visit(ctx.arraytyp())
        elif ctx.AUTO():
            return AutoType()
        else:
            return self.visit(ctx.actomic())

    # subpart: INHERIT Identifiers;
    def visitSubpart(self, ctx: MT22Parser.SubpartContext):
        return ctx.Identifiers().getText()

    # funcbody: block;
    def visitFuncbody(self, ctx: MT22Parser.FuncbodyContext):
        return self.visit(ctx.block())

    # funccall: Identifiers LB argumentprime RB;
    def visitFunccall(self, ctx: MT22Parser.FunccallContext):
        return FuncCall(ctx.Identifiers().getText(), self.visit(ctx.argumentprime()))

    # argumentprime: argumentlists | ;
    # argumentlists: argumentlist CM argumentlists | argumentlist;
    # argumentlist: expr;
    def visitArgumentprime(self, ctx: MT22Parser.ArgumentprimeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.argumentlists())
        return []

    def visitArgumentlists(self, ctx: MT22Parser.ArgumentlistsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.argumentlist())]
        return [self.visit(ctx.argumentlist())] + self.visit(ctx.argumentlists())

    def visitArgumentlist(self, ctx: MT22Parser.ArgumentlistContext):
        return self.visit(ctx.expr())

    # parameterlist: parameters |;
    # parameters: parameter CM parameters | parameter;
    # parameter: (INHERIT)? (OUT)? Identifiers COLON typ  ;
    def visitParameterlist(self, ctx: MT22Parser.ParameterlistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.parameters())
        return []

    def visitParameters(self, ctx: MT22Parser.ParametersContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.parameter())]
        return [self.visit(ctx.parameter())] + self.visit(ctx.parameters())

    def visitParameter(self, ctx: MT22Parser.ParameterContext):
        if ctx.getChildCount() == 5:
            return ParamDecl(ctx.Identifiers().getText(), self.visit(ctx.typ()), True, True)
        elif ctx.getChildCount() == 4 and ctx.INHERIT():
            return ParamDecl(ctx.Identifiers().getText(), self.visit(ctx.typ()), False, True)
        elif ctx.getChildCount() == 4 and ctx.OUT():
            return ParamDecl(ctx.Identifiers().getText(), self.visit(ctx.typ()), True, False)
        else:
            return ParamDecl(ctx.Identifiers().getText(), self.visit(ctx.typ()), False, False)

    # statement: block | assignmentstmt | ifstmt |forstmt |whilestmt |do_whilestmt
    # |break_stmt |continuestmt |returnstmt|callstmt;
    def visitStatement(self, ctx: MT22Parser.StatementContext):
        if ctx.assignmentstmt():
            return self.visit(ctx.assignmentstmt())
        elif ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        elif ctx.forstmt():
            return self.visit(ctx.forstmt())
        elif ctx.whilestmt():
            return self.visit(ctx.whilestmt())
        elif ctx.do_whilestmt():
            return self.visit(ctx.do_whilestmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        elif ctx.continuestmt():
            return self.visit(ctx.continuestmt())
        elif ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        elif ctx.callstmt():
            return self.visit(ctx.callstmt())
        else:
            return self.visit(ctx.block())

    # assignmentstmt: lhs EQ expr SM;
    def visitAssignmentstmt(self, ctx: MT22Parser.AssignmentstmtContext):
        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expr()))

    # lhs: scalar_variable | index_expression;
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if (ctx.scalar_variable()):
            return self.visit(ctx.scalar_variable())
        else:
            return self.visit(ctx.index_expression())

    def visitScalar_variable(self, ctx: MT22Parser.Scalar_variableContext):
        return Id(ctx.Identifiers().getText())

    def visitIndex_expression(self, ctx: MT22Parser.Index_expressionContext):
        return self.visit(ctx.indexop())

    # ifstmt: IF LB expr RB statement (false_statement)? ;
    def visitIfstmt(self, ctx: MT22Parser.IfstmtContext):
        if ctx.getChildCount() == 6:
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.statement()), self.visit(ctx.false_statement()))
        return IfStmt(self.visit(ctx.expr()), self.visit(ctx.statement()))

    def visitFalse_statement(self, ctx: MT22Parser.False_statementContext):
        return self.visit(ctx.statement())

    # forstmt: FOR LB (lhs EQ init_expr CM condition_expr CM update_expr) RB statement ;
    def visitForstmt(self, ctx: MT22Parser.ForstmtContext):
        return ForStmt(AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.init_expr())), self.visit(ctx.condition_expr()),
                       self.visit(ctx.update_expr()), self.visit(ctx.statement()))

    # init_expr: Integer;
    def visitInit_expr(self, ctx: MT22Parser.Init_exprContext):
        return self.visit(ctx.expr())

    def visitCondition_expr(self, ctx: MT22Parser.Condition_exprContext):
        return self.visit(ctx.expr())

    def visitUpdate_expr(self, ctx: MT22Parser.Update_exprContext):
        return self.visit(ctx.expr())

    # whilestmt: WHILE LB expr_while RB statement;
    def visitWhilestmt(self, ctx: MT22Parser.WhilestmtContext):
        return WhileStmt(self.visit(ctx.expr_while()), self.visit(ctx.statement()))

    def visitExpr_while(self, ctx: MT22Parser.Expr_whileContext):
        return self.visit(ctx.expr())

    # do_whilestmt: DO block WHILE LB expr_while RB SM;
    def visitDo_whilestmt(self, ctx: MT22Parser.Do_whilestmtContext):
        return DoWhileStmt(self.visit(ctx.expr_while()), self.visit(ctx.block()))

    # break_stmt: BREAK SM;
    def visitBreak_stmt(self, ctx: MT22Parser.Break_stmtContext):
        return BreakStmt()

    # continuestmt: CONTINUE SM;
    def visitContinuestmt(sel, ctx: MT22Parser.ContinuestmtContext):
        return ContinueStmt()

    # returnstmt: RETURN (expr)? SM;
    def visitReturnstmt(self, ctx: MT22Parser.ReturnstmtContext):
        if ctx.getChildCount() == 3:
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt()

    # callstmt: Identifiers LB argumentprime RB SM;
    def visitCallstmt(self, ctx: MT22Parser.CallstmtContext):
        return CallStmt(ctx.Identifiers().getText(), self.visit(ctx.argumentprime()))

    # block : LCB block_stmtprime RCB;
    # block_stmtprime: block_stmts |;

    # block_stmt: vardecl | statement;
    def visitBlock(self, ctx: MT22Parser.BlockContext):
        return BlockStmt(self.visit(ctx.block_stmtprime()))

    def visitBlock_stmtprime(self, ctx: MT22Parser.Block_stmtprimeContext):
        if ctx.getChildCount() > 0:
            return self.visit(ctx.block_stmts())
        return []

    # block_stmts: block_stmt block_stmts | block_stmt;
    def visitBlock_stmts(self, ctx: MT22Parser.Block_stmtsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.block_stmt())
        return self.visit(ctx.block_stmt()) + self.visit(ctx.block_stmts())

    def visitBlock_stmt(self, ctx: MT22Parser.Block_stmtContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        else:
            return self.visit(ctx.statements())

    # statements: statement statements |statement ;
    def visitStatements(self, ctx: MT22Parser.StatementsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.statement())]
        return [self.visit(ctx.statement())] + self.visit(ctx.statements())

    # boolean: (TRUE | FALSE);
    def visitBoolean(self, ctx: MT22Parser.BooleanContext):
        if ctx.TRUE():
            return True
        return False