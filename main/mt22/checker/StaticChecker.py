# from ctx import *
# from Visitor import Visitor
# from src.main.mt22.checker.StaticError import *
from AST import *
from Visitor import *
from StaticError import *
class Storeinfo:
    def __init__(self, name, typ, init_or_param,typofid):
        self.name = name
        self.typ = typ
        self.init_or_param = init_or_param
        self.typofid = typofid
class NoType(Type): pass
class Inferred:
    def infertype(env, name, typ):
        for symbol_list in env:
            for symbol in symbol_list:
                if symbol.name == name:
                    symbol.typ = typ
                    return typ
class GenEnv(Visitor):
    def __init__(self, ast=None):
        self.ast =ast

    def visit(self, ctx, o):
        return ctx.accept(self, o)

    def visitProgram(self, ctx: Program, o):
        o =[[]]
        for decl in ctx.decls:
            self.visit(decl, o)
        return o

    

    def visitFuncDecl(self, ctx: FuncDecl, o):
        # for decl in o[0]:
        #     if ctx.name in decl.keys():
        #         raise Redeclared(Function(), ctx.name)

        env = []
        for param in ctx.params:
            self.visit(param,env)
        o[0] += [Storeinfo(ctx.name, ctx.return_type, env,ctx.inherit)]
        
        return o

    def visitParamDecl(self, ctx: ParamDecl, o):
        #list_inherit = [[]]

        # if (ctx.inherit):
        #     list_inherit[0] += [{ctx.name: (ctx.typ, ctx.inherit)}]
        #     o[0] = o[0] + list_inherit[0]
        #
        # else:

        o += [[ctx.name, ctx.inherit, ctx.typ]]


        return o
        


    # def visitVarDecl(self, ctx: VarDecl, o):
    #     for decl in o[0]:
    #         if ctx.name in decl.keys():
    #             raise Redeclared(Variable(), ctx.name)
    #     o[0] += [{ctx.name: [ctx.typ, ctx.init]}]
    #     return o
        


class StaticChecker(Visitor):
    def __init__(self, asttree):
        self.asttree = asttree
    def check(self):
        return self.visitProgram(self.asttree, [])
    def visit(self, ctx, o):
        return ctx.accept(self, o)

    def visitIntegerType(self, ctx: IntegerType, o): return IntegerType()
    def visitFloatType(self, ctx: FloatType, o): return FloatType()
    def visitBooleanType(self, ctx: BooleanType, o): return BooleanType()
    def visitStringType(self, ctx: StringType, o): return StringType()

    def visitArrayType(self, ctx: ArrayType, o): 
        return ArrayType(ctx.dimensions,ctx.typ)

    def visitAutoType(self, ctx, param): return AutoType()
    def visitVoidType(self, ctx, param): return VoidType()

    def visitBinExpr(self, ctx: BinExpr, o): 
        e1 = self.visit(ctx.left, o)
        e2 = self.visit(ctx.right, o)
        # '+', '-', '*', '/'
        if ctx.op in ['+', '-', '*', '/']:
            if type(e1) is IntegerType and type(e2) is FloatType:
                return FloatType()
            elif type(e1) is FloatType and type(e2) is IntegerType:
                return FloatType()
            elif type(e1) is AutoType and type(e2) is not AutoType:
                if type(e2) is IntegerType:
                    e1 = IntegerType()
                    return IntegerType()
                elif type(e2) is FloatType:
                    e1 = FloatType()
                    return FloatType()
            elif type(e1) is not AutoType and type(e2) is AutoType:
                if type(e1) is IntegerType:
                    e2 = IntegerType()
                    return IntegerType()
                elif type(e1) is FloatType:
                    e2 = FloatType()
                    return FloatType()
            elif type(e1) != type(e2):
                raise TypeMismatchInExpression(ctx)
            else:
                return IntegerType()



        # '%'
        elif ctx.op in ['%']:
            if type(e1) is IntegerType and type(e2) is IntegerType:
                return IntegerType()
            elif type(e1) is IntegerType and type(e2) is AutoType:
                e2 = IntegerType()
                return IntegerType()
            elif type(e1) is AutoType and type(e2) is IntegerType:
                e1 = IntegerType()
                return IntegerType()
            elif type(e1) != type(e2) :
                raise TypeMismatchInExpression(ctx)


            return IntegerType()
        
        elif ctx.op in ['&&', '||']:
            if type(e1) is BooleanType and type(e2) is BooleanType:
                return BooleanType()
            elif type(e1) is BooleanType and type(e2) is AutoType:
                e2 = BooleanType()
                return BooleanType()
            elif type(e1) is AutoType and type(e2) is BooleanType:
                e1 = BooleanType()
                return BooleanType()
            elif type(e1) != type(e2) :
                raise TypeMismatchInExpression(ctx)

            return BooleanType()
        
        elif ctx.op in ['::']:
            if type(e1) is StringType and type(e2) is StringType:
                return StringType()
            elif type(e1) is StringType and type(e2) is AutoType:
                e2 = StringType()
                return StringType
            elif type(e1) is AutoType and type(e2) is StringType:
                e1 = StringType()
                return StringType
            elif type(e1) != type(e2) :
                raise TypeMismatchInExpression(ctx)

            return StringType()
        
        elif ctx.op in ['<', '>', '<=', '>=']:
            if type(e1) is IntegerType and type(e2) is FloatType:
                return BooleanType()
            elif type(e1) is FloatType and type(e2) is IntegerType:
                return BooleanType()
            elif type(e1) is AutoType and type(e2) is not AutoType:
                if type (e2) is IntegerType:
                    e1 = IntegerType()
                    return BooleanType()
                elif type(e2) is FloatType:
                    e1 = FloatType()
                    return BooleanType()
            elif type(e1) is not AutoType and type(e2) is AutoType:
                if type (e1) is IntegerType:
                    e2= IntegerType()
                    return BooleanType()
                elif type(e1) is FloatType:
                    e2 = FloatType()
                    return BooleanType()
            elif type(e1) != type(e2):
                raise TypeMismatchInExpression(ctx)

            return BooleanType()


            
        elif ctx.op in ['==', '!=']:
            if type(e1) is IntegerType and type(e2) is BooleanType:
                return BooleanType()
            elif type(e1) is BooleanType and type(e2) is IntegerType:
                return BooleanType()
            elif type(e1) is AutoType and type(e2) is not AutoType:
                if type (e2) is IntegerType:
                    e1 = IntegerType()
                elif type(e2) is BooleanType:
                    e1 = BooleanType()
            elif type(e1) is not AutoType and type(e2) is AutoType:
                if type (e1) is IntegerType:
                    e2 = IntegerType()
                elif type(e1) is BooleanType:
                    e2 = BooleanType()
            elif type(e1) != type(e2):
                raise TypeMismatchInExpression(ctx)

            else:

                return BooleanType()
           
        
        

    def visitUnExpr(self, ctx: UnExpr, o):
        e = self.visit(ctx.val, o)
        if ctx.op in ['!']:
            if type(e) is not BooleanType and type(e) is AutoType:
                e = BooleanType()
            elif type(e) is not BooleanType and type(e) is not AutoType:
                raise TypeMismatchInExpression(ctx)
            return BooleanType()

        if ctx.op in ['-']:
            if type(e) is FloatType:
                return FloatType()
            elif type(e) is IntegerType:
                return IntegerType()
            else:
                raise TypeMismatchInExpression(ctx)
    
    # a: integer;
    # 
    def visitId(self, ctx: Id, o):

        for info_list in o:
            for info in info_list:
                if type(info) is Storeinfo:
                    if ctx.name == info.name:
                        return info.typ

        raise Undeclared(Identifier(), ctx.name)





            
    
        
    def visitArrayCell(self, ctx:ArrayCell, o): 
        listofexpr = self.visit(ctx.cell, o )
        for i in listofexpr:
            if type(i) is not IntegerType:
                raise TypeMismatchInExpression(ctx)



    def visitIntegerLit(self, ctx: IntegerLit, o): return IntegerType()
    def visitFloatLit(self, ctx: FloatLit, o): return FloatType()
    def visitStringLit(self, ctx: StringLit, o): return StringType()
    def visitBooleanLit(self, ctx: BooleanLit, o): return BooleanType()
    def visitArrayLit(self, ctx: ArrayLit, o):
        type_array= self.visit(ctx.explist[0], o)  # IntegerType

        for i in range(1, len(ctx.explist)):
            type_i =self.visit(ctx.explist[i], o)
            if type(type_array) is ArrayType and type(type_i) is ArrayType:
                if type_array.dimensions != type_i.dimensions or type(type_array.typ) is not type(type_i.typ):
                    raise IllegalArrayLiteral(None)

            if type(type_array) != type(type_i):
                raise IllegalArrayLiteral(None)

        if type(type_array) is ArrayType:
            return ArrayType([len(ctx.explist)] + type_array.dimensions, type_array.typ)

        return ArrayType([len(ctx.explist)], type_array)
       
    def visitFuncCall(self, ctx: FuncCall, o):
        list_function = []
        #name = ""
        #env = GenEnv.visit(ctx, o[1])

        for i in range(0, len(o[1])):
            list_function += [o[1][i].name]

        typeoffunction = NoType()
        if ctx.name not in list_function:
            raise Undeclared(Function(), ctx.name)
        for i in range(0, len(o[1])):
            if ctx.name == o[1][i].name:
                list_typ_args = []
                list_typ_param = []
                for x in range(0, len(ctx.args)):
                    list_typ_args += [[ctx.args[x], self.visit(ctx.args[x], o)]]
                for x in range(0, len(o[1][i].init_or_param)):
                    list_typ_param += [[o[1][i].init_or_param[x][0], o[1][i].init_or_param[x][2]]]

                error_args = []
                infer_type = []
                if len(list_typ_args) > len(list_typ_param):

                    raise TypeMismatchInExpression(list_typ_args[len(list_typ_param)][0])

                elif len(list_typ_args) < len(list_typ_param):
                    raise TypeMismatchInExpression("")
                else:
                    argsindex = 0
                    for paramindex in range(0, len(list_typ_param)):
                        if (type(list_typ_args[argsindex][1]) != type(list_typ_param[paramindex][1])) :
                            if type(list_typ_param[paramindex][1]) is not AutoType and type(list_typ_args[paramindex][1]) is not AutoType:
                                if type(list_typ_args[argsindex][1]) is not IntegerType and type(list_typ_param[paramindex][1]) is not FloatType:
                                    error_args.append(list_typ_args[argsindex][0])
                        elif argsindex < len(list_typ_args):
                            argsindex = argsindex + 1
                    if len(error_args) > 0:
                        raise TypeMismatchInExpression(error_args[0])
                    else:
                        # infertype param
                        for paramindex in range(0, len(list_typ_param)):
                            if (type(list_typ_args[paramindex][1]) != type(list_typ_param[paramindex][1])):
                                if type(list_typ_param[paramindex][1]) is AutoType:
                                    list_typ_param[paramindex][1] = list_typ_args[paramindex][1]
                                elif type(list_typ_args[paramindex][1]) is AutoType:
                                    list_typ_args[paramindex][1] = list_typ_param[paramindex][1]

                        #original_param = 0
                        for paramindex in range(0, len(list_typ_param)):
                            if (type(list_typ_param[paramindex][1]) != type(o[1][i].init_or_param[paramindex][2])) :
                                if type(o[1][i].init_or_param[paramindex][2]) is AutoType:
                                    o[1][i].init_or_param[paramindex][2] = list_typ_param[paramindex][1]
                                elif type(list_typ_param[paramindex][1]) is AutoType:
                                    list_typ_param[paramindex][1] = o[1][i].init_or_param[paramindex][2]
                            # elif original_param < len(o[1][i].init_or_param):
                            #     original_param = original_param +1
                typeoffunction = o[1][i].typ

                break

        return typeoffunction






    def visitAssignStmt(self, ctx: AssignStmt, o):
        lhs = self.visit(ctx.lhs, o)
        rhs = self.visit(ctx.rhs, o)
        if type(lhs) not in [ IntegerType, FloatType, StringType, BooleanType, AutoType]:
            raise TypeMismatchInStatement(ctx)
        elif type(lhs) is FloatType and type(rhs) is IntegerType:
            return FloatType()
        elif type(lhs) is AutoType and type(rhs) is not AutoType:
            lhs = rhs
            for list_decl in o:
                for decl in list_decl:
                    if type(decl) is Storeinfo:
                        if decl.name == ctx.lhs.name and type(decl.typofid) is Parameter:
                            decl.typ = rhs
                    break
            return rhs
        elif type(rhs) is AutoType and type(lhs) is not AutoType:
            rhs = lhs
            for list_decl in o:
                for decl in list_decl:
                    if decl.name == ctx.rhs.name and type(decl.typofid) is Parameter:
                        decl.typ = lhs
                    break
            return lhs
        elif type(lhs) != type(rhs):
            raise TypeMismatchInStatement(ctx)


    def visitBlockStmt(self, ctx, o):
        # env = [[], []]
        # for decl in ctx.body:
        #     if type(decl) is VarDecl:
        #         self.visit(decl, env)
        #
        #     elif type(decl) is CallStmt:
        #         return ctx.body




        return ctx.body
    def visitIfStmt(self, ctx: IfStmt, o): 
        cond_expr = self.visit(ctx.cond, o)
        if type(cond_expr) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        elif type(ctx.tstmt) is BreakStmt or type(ctx.tstmt) is ContinueStmt:
            raise MustInLoop(ctx.tstmt)
        elif type(ctx.fstmt) is BreakStmt or type(ctx.fstmt) is ContinueStmt:
            raise MustInLoop(ctx.fstmt)
        if type(ctx.tstmt) is not BlockStmt:
            self.visit(ctx.tstmt, o)
        elif type(ctx.tstmt) is BlockStmt:
            env = []
            o.insert(0,env)
            for decl in ctx.tstmt.body:
                # if type(decl) is BreakStmt or type(decl) is ContinueStmt:
                #     raise MustInLoop(decl)
                # env = [[]]
                #env =[[[]]]

                if type(decl) is VarDecl:
                    # env = []
                    # o.insert(0, env)
                    self.visit(decl,o)
                if type(decl) is not VarDecl:
                    self.visit(decl,o)
            o.remove(env)
        if type(ctx.fstmt) is not BlockStmt:
            self.visit(ctx.fstmt,o)
        if type(ctx.fstmt) is BlockStmt:
            env = []
            o.insert(0, env)
            for decl in ctx.fstmt.body:
                # if type(decl) is BreakStmt or type(decl) is ContinueStmt:
                #     raise MustInLoop(decl)
                # env = [[]]
                # env =[[[]]]

                if type(decl) is VarDecl:
                    # env = []
                    # o.insert(0, env)
                    self.visit(decl, o)
                if type(decl) is not VarDecl:
                    self.visit(decl, o)

            o.remove(env)
        # else:
        #     a = []
        #return cond_expr

    def visitForStmt(self, ctx: ForStmt, o): 
        first_cond_lhs = self.visit(ctx.init.lhs, o)
        first_cond_rhs = self.visit(ctx.init.rhs, o)
        cond_expr = self.visit(ctx.cond, o)
        update_expr = self.visit(ctx.upd, o)
        if type(first_cond_lhs) is not IntegerType and type(first_cond_lhs) is AutoType:
            if type(first_cond_rhs) is IntegerType:
                first_cond_lhs = first_cond_rhs
            else:
                raise TypeMismatchInStatement(ctx.init)
        elif type(first_cond_lhs) is not IntegerType and type(first_cond_lhs) is not AutoType:
            raise TypeMismatchInStatement(ctx)
        elif type(cond_expr) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        elif type(update_expr) is not IntegerType:
            raise TypeMismatchInStatement(ctx)

        if type(ctx.stmt) is BlockStmt:
            env = []
            o.insert(0, env)
            for decl in ctx.stmt.body:
                if type(decl) is VarDecl:
                    self.visit(decl, o)
                if type(decl) is not VarDecl:
                    self.visit(decl, o)
            o.remove(env)




        
        
    def visitWhileStmt(self, ctx: WhileStmt, o):
        cond_expr = self.visit(ctx.cond, o)
        if type(cond_expr) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        if type(ctx.stmt) is BlockStmt:
            env = []
            o.insert(0, env)
            for decl in ctx.stmt.body:
                if type(decl) is VarDecl:
                    self.visit(decl, o)
                if type(decl) is not VarDecl:
                    self.visit(decl, o)
            o.remove(env)

    def visitDoWhileStmt(self, ctx: DoWhileStmt, o): 
        cond_expr = self.visit(ctx.cond, o)
        if type(cond_expr) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        if type(ctx.stmt) is BlockStmt:
            env = []
            o.insert(0, env)
            for decl in ctx.stmt.body:
                if type(decl) is VarDecl:
                    self.visit(decl, o)
                if type(decl) is not VarDecl:
                    self.visit(decl, o)
            o.remove(env)
        
    def visitBreakStmt(self, ctx: BreakStmt, o):
        return BreakStmt()

    def visitContinueStmt(self, ctx: ContinueStmt, o): return ContinueStmt()
    def visitReturnStmt(self, ctx: ReturnStmt, o):
        expr = self.visit(ctx.expr,o)
        for list in o:
            for element in list:
                if type(element) is not Storeinfo:
                    for i in range(0, o[1]):
                        if o[1][i].name == element[0]:
                            if type(o[1][i].typ) != type(element[1]):
                                if type(element[1]) is AutoType:
                                    element[1] = type(o[1][i].typ)
                                else:
                                    raise TypeMismatchInStatement(ctx)









         

    def visitCallStmt(self, ctx: CallStmt, o):
        if ctx.name == "super" or ctx.name == "preventDefault":
            return CallStmt(ctx.name, ctx.args)
        else:
            for i in range(0, len(o[1])):
                list_function += [o[1][i].name]

            #typeoffunction = NoType()
            if ctx.name not in list_function:
                raise Undeclared(Function(), ctx.name)
            for i in range(0, len(o[1])):
                if ctx.name == o[1][i].name:
                    list_typ_args = []
                    list_typ_param = []
                    for x in range(0, len(ctx.args)):
                        list_typ_args += [[ctx.args[x], self.visit(ctx.args[x], o)]]
                    for x in range(0, len(o[1][i].init_or_param)):
                        list_typ_param += [[o[1][i].init_or_param[x][0], o[1][i].init_or_param[x][2]]]

                    error_args = []
                    infer_type = []
                    if len(list_typ_args) > len(list_typ_param):

                        raise TypeMismatchInExpression(list_typ_args[len(list_typ_param)][0])

                    elif len(list_typ_args) < len(list_typ_param):
                        raise TypeMismatchInExpression("")
                    else:
                        argsindex = 0
                        for paramindex in range(0, len(list_typ_param)):
                            if (type(list_typ_args[argsindex][1]) != type(list_typ_param[paramindex][1])):
                                if type(list_typ_param[paramindex][1]) is not AutoType and type(
                                        list_typ_args[paramindex][1]) is not AutoType:
                                    if type(list_typ_args[argsindex][1]) is not IntegerType and type(
                                            list_typ_param[paramindex][1]) is not FloatType:
                                        error_args.append(list_typ_args[argsindex][0])
                            elif argsindex < len(list_typ_args):
                                argsindex = argsindex + 1
                        if len(error_args) > 0:
                            raise TypeMismatchInExpression(error_args[0])
                        else:
                            # infertype param
                            for paramindex in range(0, len(list_typ_param)):
                                if (type(list_typ_args[paramindex][1]) != type(list_typ_param[paramindex][1])):
                                    if type(list_typ_param[paramindex][1]) is AutoType:
                                        list_typ_param[paramindex][1] = list_typ_args[paramindex][1]
                                    elif type(list_typ_args[paramindex][1]) is AutoType:
                                        list_typ_args[paramindex][1] = list_typ_param[paramindex][1]

                            # original_param = 0
                            for paramindex in range(0, len(list_typ_param)):
                                if (type(list_typ_param[paramindex][1]) != type(o[1][i].init_or_param[paramindex][2])):
                                    if type(o[1][i].init_or_param[paramindex][2]) is AutoType:
                                        o[1][i].init_or_param[paramindex][2] = list_typ_param[paramindex][1]
                                    elif type(list_typ_param[paramindex][1]) is AutoType:
                                        list_typ_param[paramindex][1] = o[1][i].init_or_param[paramindex][2]
        return CallStmt(ctx.name, ctx.args)




    def visitVarDecl(self, ctx: VarDecl, o):
        #flag = False
        typ_var = self.visit(ctx.typ, o)
        sizeofarray = 1
        initial = None
        if type(ctx.init) is ArrayLit:
            try:
                initial = self.visit(ctx.init, o)
            except IllegalArrayLiteral:
                raise IllegalArrayLiteral(ctx.init)

            if initial.dimensions != typ_var.dimensions or type(initial.typ) is not type(typ_var.typ):
                raise TypeMismatchInVarDecl(ctx)
        else:
            if (ctx.init):
                initial = self.visit(ctx.init, o)

                for decl in o[0]:
                    if ctx.name == decl.name:
                        raise Redeclared(Variable(), ctx.name)
                if type(typ_var) is FloatType:
                    if type(initial) is AutoType:
                        if type(ctx.init) is FuncCall:
                            for i in range(0, len(o[1])):
                                if o[1][i].name == ctx.init.name:
                                    o[1][i].typ = typ_var
                    elif type(initial) is not IntegerType and type(initial) is not FloatType:
                        raise TypeMismatchInVarDecl(ctx)
                elif type(typ_var) is AutoType:
                    ctx.typ = self.visit(ctx.init,o)
                elif type(initial) is AutoType and type(ctx.init) is FuncCall:
                    for i in range(0, len(o[1])):
                        if o[1][i].name == ctx.init.name:
                            o[1][i].typ = typ_var


                elif type(typ_var) != type(initial):
                    raise TypeMismatchInVarDecl(ctx)
            else:
                for decl in o[0]:
                    if ctx.name == decl.name: #and type(decl[ctx.name][2]) is Variable:
                        raise Redeclared(Variable(), ctx.name)
                if type(typ_var) is AutoType:
                    raise Invalid(Variable(),ctx.name)

        # if type(typ_var) is FloatType:
        #         if type(typ_var) is FloatType and (type(initial) is IntegerType or type(initial) is FloatType):
        #             initial = FloatType()
        #         else:
        #             raise TypeMismatchInVarDecl(ctx)
        # elif type(typ_var) is AutoType:
        #     if len(o[0][0][ctx.name]) < 2:
        #         raise Invalid(Variable(),ctx.name)
        #     else:
        #         o[0][0][ctx.name][0] = type(initial)
        # elif type(typ_var) is ArrayType:
        #     return 1
        o[0] += [Storeinfo(ctx.name, ctx.typ, ctx.init,Variable())]
        return o

    # param: {ctx:name: [ctx.typ, ctx.inherit]}
    def visitParamDecl(self, ctx: ParamDecl, o):
        # list_param = [[]]
        # o[0] += list_param + o[0]



        for decl in o:
            if ctx.name in decl[0] :
                raise Redeclared(Parameter(), ctx.name)
        # for i in range(0, len(o[1])):
        #     if ctx.name == o[1][i].init_or_param[0]:
        #         if type(ctx.typ) is AutoType:
        #             if type(ctx.typ) != type(o[1][i].init_or_param[2]):
        #                 ctx.typ = self.visit(o[1][i].init_or_param[2],o)
        #     break


        o += [ [ctx.name,ctx.typ, ctx.inherit] ]

        return o





    # [ { ten: ( kieu ffunc, [list cac param], Function() ) } ]
    def visitFuncDecl(self, ctx: FuncDecl, o):
        for decl in o[0]:
            if ctx.name == decl.name :
                raise Redeclared(Function(), ctx.name)

        for i in range(0, len(o[1])):
            if ctx.name == o[1][i].name:
                if type(ctx.return_type) is AutoType:
                    if type(o[1][i].typ) != type(ctx.return_type):
                        ctx.return_type = self.visit(o[1][i].typ,o)
            break
        list_param = []

        list_function = []
        # check inherit
        if ctx.inherit:
            for i in range(0, len(o[1])):

                list_function += [o[1][i].name]
            #env = [[]] + [o[1]]
            # o.insert(2, env)
            env = [[[]]] + [o[1]]
            ## create new env for local


            if ctx.inherit not in list_function:
                raise Undeclared(Function(), ctx.inherit)
            else:

                ### CHECK REDECALRED PARAM
                for param in ctx.params:
                    self.visit(param, list_param)
                ### ASSIGN NEW TYPE PARAM
                for i in range(0, len(o[1])):
                    if ctx.name == o[1][i].name:
                        for paramindex in range(0, len(list_param)):
                            if type(list_param[paramindex][1]) is AutoType and type(o[1][i].init_or_param[paramindex][2]) is not AutoType:
                                list_param[paramindex][1] = o[1][i].init_or_param[paramindex][2]
                    break
                for param in list_param:
                    env[0][0] += [Storeinfo(param[0], param[1], param[2], Parameter())]
                env[0].insert(1, o[0])
                a = []
                for i in range(0, len(o[1])):
                    if ctx.name == o[1][i].name:
                        a += [ctx.name, ctx.return_type]
                #a = [ctx.name, ctx.return_type]

                env[0].insert(2, a)
                # for i in range(0, len(o[0])):
                #     env[0].append(o[0][i])
                if list_function.index(ctx.inherit) > list_function.index(ctx.name):
                    list_parent_param = []
                    list_inherit = []
                    for i in range(0, len(o[1])):
                        if o[1][i].name == ctx.inherit:
                            for param_decl in range(0, len(o[1][i].init_or_param)):
                                list_parent_param += [[o[1][i].init_or_param[param_decl][0], o[1][i].init_or_param[param_decl][1]]]
                            for param in list_parent_param:
                                if param[1]  is True:
                                    list_inherit += [param[0]]
                            for inherit_param in list_inherit:
                                if list_inherit.count(inherit_param) > 1:
                                    raise Redeclared(Parameter(), inherit_param)


                for param in list_param:
                    for i in range(0, len(o[1])):
                        if o[1][i].name == ctx.inherit:
                            for y in range(0, len(o[1][i].init_or_param)):
                                if o[1][i].init_or_param[y][0] == param[0]   and o[1][i].init_or_param[y][1] is True :
                                    raise Invalid(Parameter(), o[1][i].init_or_param[y][0])
                                elif o[1][i].init_or_param[y][0] != param[0]   and o[1][i].init_or_param[y][1] is True:
                                    env[0][0] += [Storeinfo(o[1][y].init_or_param[y][0], o[1][y].init_or_param[y][2], o[1][y].init_or_param[y][1], Parameter())]
                            break
            # for i in range(0, len(o[0])):
            #     env[0].append(o[0][i])

            #o.insert(2, env)
            # for param in list_param:
            #     env[0] += [Storeinfo(param[0], param[1], param[2], Parameter())]
            # for i in range(0, len(o[0])):
            #     env[0].append(o[0][i])
            block_decl = []
            block_decl.insert(0,self.visit(ctx.body,o))
            # check invalid
            if len(block_decl[0]) == 0:
                block_decl[0].insert(0,CallStmt("super", []))
                for i in range(0, len(o[1])):
                    if o[1][i].name == ctx.inherit:
                        list_typ_args = len(block_decl[0][0].args)
                        list_typ_param = []
                        for x in range(0, len(o[1][i].init_or_param)):
                            list_typ_param += [[o[1][i].init_or_param[x][0], type(o[1][i].init_or_param[x][2])]]
                        if list_typ_args < len(list_typ_param):
                            raise InvalidStatementInFunction(ctx.name)

            else:
                # check first statement

                if type(block_decl[0][0]) is CallStmt:
                    if block_decl[0][0].name == "super":
                        for i in range(0, len(o[1])):
                            if o[1][i].name == ctx.inherit:
                                if len(block_decl[0][0].args) == 0:
                                    list_typ_args = len(block_decl[0][0].args)
                                    list_typ_param = []
                                    for x in range(0, len(o[1][i].init_or_param)):
                                        list_typ_param += [[o[1][i].init_or_param[x][0], o[1][i].init_or_param[x][2]]]
                                    if list_typ_args < len(list_typ_param):
                                        raise TypeMismatchInExpression("")
                                else:
                                    list_typ_args = []
                                    list_typ_param = []
                                    for x in range(0, len(block_decl[0][0].args)):
                                        list_typ_args += [[block_decl[0][0].args[x], self.visit(block_decl[0][0].args[x], env[0]) ]]
                                    for x in range(0, len(o[1][i].init_or_param)):
                                        list_typ_param += [[o[1][i].init_or_param[x][0],o[1][i].init_or_param[x][2]]]
                                    error_args = []
                                    if len(list_typ_args) > len(list_typ_param):
                                        raise TypeMismatchInExpression(list_typ_args[len(list_typ_param)][0])
                                    elif len(list_typ_args) < len(list_typ_param):
                                        raise TypeMismatchInExpression("")
                                    else:

                                        argsindex = 0
                                        for paramindex in range(0, len(list_typ_param)):
                                            if (type(list_typ_args[paramindex][1]) != type(list_typ_param[paramindex][1])):
                                                if type(list_typ_param[paramindex][1]) is not AutoType and type(list_typ_args[paramindex][1]) is not AutoType:
                                                    if type(list_typ_args[paramindex][1]) is not IntegerType and type(list_typ_param[paramindex][1]) is not FloatType:
                                                        error_args.append(list_typ_args[paramindex][0])


                                        if len(error_args) > 0:
                                            raise TypeMismatchInExpression(error_args[0])
                                        else:
                                            for paramindex in range(0, len(list_typ_param)):
                                                if (type(list_typ_args[paramindex][1]) != type(list_typ_param[paramindex][1])):
                                                    if type(list_typ_param[paramindex][1]) is AutoType:
                                                        list_typ_param[paramindex][1] = list_typ_args[paramindex][1]
                                                    elif type(list_typ_args[paramindex][1]) is AutoType:
                                                        list_typ_args[paramindex][1] = list_typ_param[paramindex][1]

                        # for param in list_param:
                        #     env[0]+=[Storeinfo(param[0],param[1],param[2], Parameter())]
                        # for i in range(0, len(o[1])):
                        #     if o[1][i].name == ctx.name:
                        #         for x in range (0, len(o[1][i].init_or_param)):
                        #             if o[1][i].init_or_param[x][1] is True:
                        #                 env[0]+= [Storeinfo(o[1][i].init_or_param[x][0],o[1][i].init_or_param[x][2],o[1][i].init_or_param[x][1], Parameter())]
                        #     break
                    elif block_decl[0][0].name == "preventDefault" and len(block_decl[0][0].args) > 0:
                        raise TypeMismatchInExpression("")

                        # check local
                    # for list_decl in block_decl[0][1:]:
                    #
                    #     if type(list_decl) is VarDecl:
                    #         self.visit(list_decl, env)
                    #     else:
                    #         for i in range(0, len(o[0])):
                    #             env[0].append(o[0][i])
                    #         self.visit(list_decl, env)
                    #     if type(list_decl) is BreakStmt or type(list_decl) is ContinueStmt:
                    #         raise MustInLoop(list_decl)
                    # ## ASSIGN RETURN_TYPE
                    # for list_decl in env:
                    #     for decl in list_decl:
                    #         for info_func in o[1]:
                    #             if ctx.name == info_func.name:
                    #                 for i in range(0, len(info_func.init_or_param)):
                    #                     if decl.name == info_func.init_or_param[i][0]:
                    #                         if type(decl.typ) is not AutoType and type(
                    #                                 info_func.init_or_param[i][2]) is AutoType:
                    #                             info_func.init_or_param[i][2] = decl.typ
                    #                     break
                    elif  block_decl[0][0].name != "super" and block_decl[0][0].name != "preventDefault":
                        block_decl.insert(0,CallStmt("super", []))
                        for i in range(0, len(o[1])):
                            if o[1][i].name == ctx.inherit:
                                list_typ_args = len(block_decl[0].args)
                                list_typ_param = []
                                for x in range(0, len(o[1][i].init_or_param)):
                                    list_typ_param += [[o[1][i].init_or_param[x][0],o[1][i].init_or_param[x][2]]]
                                if list_typ_args < len(list_typ_param):
                                    raise InvalidStatementInFunction(ctx.name)
                        # for param in list_param:
                        #     env[0] += [Storeinfo(param[0], param[1], param[2], Parameter())]
                    # for list_decl in block_decl[0][1:]:
                    #     # for decl in list_decl:
                    #     if type(list_decl) is VarDecl:
                    #         self.visit(list_decl, env)
                    #     else:
                    #         for i in range(0, len(o[0])):
                    #             env[0].append(o[0][i])
                    #         self.visit(list_decl, env)
                    #     if type(list_decl) is BreakStmt or type(list_decl) is ContinueStmt:
                    #         raise MustInLoop(list_decl)
                    # ## ASSIGN RETURN_TYPE
                    # for list_decl in env:
                    #     for decl in list_decl:
                    #         for info_func in o[1]:
                    #             if ctx.name == info_func.name:
                    #                 for i in range(0, len(info_func.init_or_param)):
                    #                     if decl.name == info_func.init_or_param[i][0]:
                    #                         if type(decl.typ) is not AutoType and type(
                    #                                 info_func.init_or_param[i][2]) is AutoType:
                    #                             info_func.init_or_param[i][2] = decl.typ
                    #
                    #                    break
                    #env[0].insert(1, o[0])
                    for decl in range(1, len(block_decl[0])):
                        if type(block_decl[0][decl]) is VarDecl:
                            self.visit(block_decl[0][decl],env[0])
                        else:
                            self.visit(block_decl[0][decl],env[0])
                    env[0].remove(env[0][0])
                    # for list_decl in env:
                    #     for decl in list_decl:
                    #         if type(decl) is Storeinfo:
                    #             for info_func in env[1]:
                    #                 if ctx.name == info_func.name:
                    #                     for i in range(0, len(info_func.init_or_param)):
                    #                         if decl.name == info_func.init_or_param[i][0]:
                    #                             if type(decl.typ) is not AutoType and type(
                    #                                     info_func.init_or_param[i][2]) is AutoType:
                    #                                 info_func.init_or_param[i][2] = decl.typ
                    #
                    #                     break
                    # #self.visit(ctx.body, env)
                    # for i in range(0, len(o[1])):
                    #     if ctx.name == o[1][i].name:
                    #         for y in range(0, len(o[1][i].init_or_param)):
                    #             if list_param[y][0] == o[1][i].init_or_param[y][0]:
                    #                 if type(list_param[y][1]) is AutoType and type(o[1][i].init_or_param[y][2]) is not AutoType:
                    #                     list_param[y][1] = self.visit(o[1][i].init_or_param[y][2], o)
                    #     break

                else:
                    block_decl[0].insert(0, CallStmt("super", []))
                    for i in range(0, len(o[1])):
                        if o[1][i].name == ctx.inherit:
                            list_typ_args = len(block_decl[0][0].args)
                            list_typ_param = []
                            for x in range(0, len(o[1][i].init_or_param)):
                                list_typ_param += [[o[1][i].init_or_param[x][0], type(o[1][i].init_or_param[x][2])]]
                            if list_typ_args < len(list_typ_param):
                                raise InvalidStatementInFunction(ctx.name)
                        break
                    #LOCAL
                    for decl in range(1, len(block_decl[0])):
                        if type(block_decl[0][decl]) is VarDecl:
                            self.visit(block_decl[0][decl],env[0])
                        else:
                            self.visit(block_decl[0][decl],env[0])
                    # ASSIGN AUTO TYPE
                    env[0].remove(env[0][0])
                    # for list_decl in env:
                    #     for decl in list_decl:
                    #         if type(decl) is Storeinfo:
                    #             for info_func in env[1]:
                    #                 if ctx.name == info_func.name:
                    #                     for i in range(0, len(info_func.init_or_param)):
                    #                         if decl.name == info_func.init_or_param[i][0]:
                    #                             if type(decl.typ) is not AutoType and type(
                    #                                     info_func.init_or_param[i][2]) is AutoType:
                    #                                 info_func.init_or_param[i][2] = decl.typ
                    #
                    #                     break

        else:
            for param in ctx.params:
                self.visit(param, list_param)
            ### ASSIGN NEW TYPE PARAM
            for i in range(0, len(o[1])):
                if ctx.name == o[1][i].name:
                    for paramindex in range(0, len(list_param)):
                        if type(list_param[paramindex][1]) is AutoType and type( o[1][i].init_or_param[paramindex][2]) is not AutoType:
                            list_param[paramindex][1] = o[1][i].init_or_param[paramindex][2]
                break
            env = [[[]]] + [o[1]]
            #o.insert(2, env)
            for param in list_param:
                env[0][0] += [Storeinfo(param[0], param[1], param[2], Parameter())]
            env[0].insert(1, o[0])
            block_decl = []
            block_decl.insert(0,self.visit(ctx.body,env))
            if len(block_decl[0]) > 0:
                for i in range(0, len(block_decl[0])):
                    if type(block_decl[0][i]) is CallStmt:
                        if block_decl[0][i].name == "super" or block_decl[0][i].name == "preventDefault":
                            raise InvalidStatementInFunction(ctx.name)
                    else:
                        for list_decl in block_decl:
                            for decl in list_decl:
                                if type(decl) is VarDecl:
                                    self.visit(decl, env[0])
                                else:
                                    self.visit(decl, env[0])
                                if type(decl) is BreakStmt or type(decl) is ContinueStmt:
                                    raise MustInLoop(decl)
                env[0].remove(env[0][0])
                # for list_decl in env:
                #     for decl in list_decl:
                #         if type(decl) is Storeinfo:
                #             for info_func in env[1]:
                #                 if ctx.name == info_func.name:
                #                     for i in range(0, len(info_func.init_or_param)):
                #                         if decl.name == info_func.init_or_param[i][0]:
                #                             if type(decl.typ) is not AutoType and type(info_func.init_or_param[i][2]) is AutoType:
                #                                 info_func.init_or_param[i][2] = decl.typ
                #                         break


                #a = []

                   # for list_env in env:
                                    #     for symbol in list_env:
        o[0] += [Storeinfo(ctx.name ,ctx.return_type, list_param, Function())]
        #return o

    def visitProgram(self, ctx: Program, o):

        env = GenEnv().visit(ctx,o)
        o = [[]] + env
        for decl in ctx.decls:
            self.visit(decl,o)
        for decl in o[0]:
            if decl.name != "main" and type(decl.typ) is not VoidType:
                raise NoEntryPoint()

