import unittest
from TestUtils import TestChecker
from TestUtils import TestAST
#from AST import *
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test_1(self):
    #     """test 1"""
    #     input = """a: integer = "huy";
    #                 a: integer;"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, StringLit(huy))"
    #     self.assertTrue(TestChecker.test(input, expect, 301))
    #
    # def test_2(self):
    #     """test 2"""
    #     input = """a: auto;"""
    #     expect = "Invalid Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 302))
    #
    # def test_3(self):
    #     """test 3"""
    #     input = """a,b: integer = 2, "huy";"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, StringLit(huy))"
    #     self.assertTrue(TestChecker.test(input, expect, 303))
    #
    # def test_4(self):
    #     """test 4"""
    #     input = """a,b: integer = 2, 3;
    #                 c: integer = 2.1;
    #                 d: auto;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FloatLit(2.1))"
    #     self.assertTrue(TestChecker.test(input, expect, 304))
    #
    # def test_5(self):
    #     """test 5"""
    #     input = """a,b: integer = 2, 3;
    #                 c: integer = 2.1;
    #                 a: float;
    #                 d: auto;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FloatLit(2.1))"
    #     self.assertTrue(TestChecker.test(input, expect, 305))
    #
    # def test_6(self):
    #     """test 6"""
    #     input = """a,b: integer = 2, 3;
    #
    #                 a: float;
    #                 d: auto;
    #                 """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 306))
    #
    # def test_7(self):
    #     """test 7"""
    #     input = """a,b: integer = 2, 3;
    #                 // c: integer = 2.1;
    #                 // c = a + 1;
    #                 e: float = a + 1;
    #                 d: auto;
    #                 """
    #     expect = "Invalid Variable: d"
    #     self.assertTrue(TestChecker.test(input, expect, 307))
    #
    #     def test_8(self):
    #         """test 8"""
    #         input = """a,b: float = 2.1, 3.1;
    #                     // c: integer = 2.1;
    #                     // c = a + 1;
    #                     e: integer = a + 1;
    #                     d: auto;
    #                     """
    #         expect = "Type mismatch in Variable Declaration: VarDecl(e, IntegerType, BinExpr(+, Id(a), IntegerLit(1)))"
    #         self.assertTrue(TestChecker.test(input, expect, 308))
    #
    # def test_9(self):
    #     """test 9"""
    #     input = """a,b,c: float = 2.1, 3,4;
    #                 // c: integer = 2.1;
    #                 // c = a + 1;
    #                 e: integer = f + 1;
    #                 d: auto;
    #                 """
    #     expect = "Undeclared Identifier: f"
    #     self.assertTrue(TestChecker.test(input, expect, 309))
    #
    # def test_10(self):
    #     """test 10"""
    #     input = """a: integer = b+1;
    #                 b: integer;
    #                 """
    #     expect = "Undeclared Identifier: b"
    #     self.assertTrue(TestChecker.test(input, expect, 310))
    #
    # def test_11(self):
    #     """test 11"""
    #     input = """a: array[4] of integer= {1,2,3,"huy"};
    #
    #                 """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 311))
    #
    # def test_12(self):
    #     """test 12"""
    #     input = """a,b,c: integer = 1 ,2, 2;
    #                 d: float;
    #                 e: boolean = 1;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(e, BooleanType, IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 312))
    #
    # def test_13(self):
    #     """test 13"""
    #     input = """a: float;
    #                 b: integer;
    #                 b: function integer(a: string){
    #                 a = a+1;
    #                 }
    #
    #                 """
    #     expect = "Redeclared Variable: b"
    #     self.assertTrue(TestChecker.test(input, expect, 313))
    #
    # def test_14(self):
    #     """test 14"""
    #     input = """a: array[4] of float= {12,2,3,3};
    #                 // b: array[4] of integer = {1.2,2,1,3}
    #
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([4], FloatType), ArrayLit([IntegerLit(12), IntegerLit(2), IntegerLit(3), IntegerLit(3)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 314))
    #
    # def test_15(self):
    #     """test 15 need to consider"""
    #     input = """a: array[4] of float= {1.2,2.1,3,3};
    #                 // b: array[4] of integer = {1.2,2,1,3}
    #
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([4], FloatType), ArrayLit([IntegerLit(12), IntegerLit(2), IntegerLit(3), IntegerLit(3)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 315))
    #
    # def test_16(self):
    #     """test 16 """
    #     input = """a: array[4] of float= {1.2,2.1,3,3};
    #                 a: array[4] of integer = {1.2,2,1,3};
    #
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([4], FloatType), ArrayLit([IntegerLit(12), IntegerLit(2), IntegerLit(3), IntegerLit(3)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 316))
    #
    # def test_17(self):
    #     """test 17 """
    #     input = """//a: array[4] of float= {1.2,2.1,3,3};
    #                 a: array[4] of float = {12.1,2.1,1.1,{1.2,2.2,3.2}};
    #                 """
    #     expect = "Illegal array literal: ArrayLit([FloatLit(12.1), FloatLit(2.1), FloatLit(1.1), ArrayLit([FloatLit(1.2), FloatLit(2.2), FloatLit(3.2)])])"
    #     self.assertTrue(TestChecker.test(input, expect, 317))
    # def test_18(self):
    #     """test 18 """
    #     input = """//a: array[4] of float= {1.2,2.1,3,3};
    #                a: array[4] of integer = {12,2,1,1,2};
    #                 // b: integer;
    #                 // c: boolean;
    #                 // a: integer;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([4], IntegerType), ArrayLit([IntegerLit(12), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(2)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 318))
    #
    # def test_19(self):
    #     """test 19 """
    #     input = """//a: array[4] of float= {1.2,2.1,3.2,3.1};
    #                a: array[4] of integer = {12,2,1,1};
    #                 // b: integer;
    #                 // c: boolean;
    #                 // a: integer;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([4], IntegerType), ArrayLit([IntegerLit(12), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(2)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 319))
    #
    # def test_20(self):
    #     """test 20 """
    #     input = """a: array[4] of boolean= {true,false,true,true};
    #                b: array[2,3] of integer = {12,2,1,1,3,4};
    #
    #                 huy: auto = 2;
    #                 foo: float = 2+huy;
    #                 hi: boolean;
    #                 foo: integer;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2, 3], IntegerType), ArrayLit([IntegerLit(12), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(2)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 320))
    #
    # def test_21(self):
    #     """test 21 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #
    #                 a: integer;
    #                 b: boolean = true;
    #                 c: boolean = false;
    #                 e: boolean = b + c;
    #                 d: function string(a: integer){
    #                     if (n == 0) return 1;
    #                 }
    #                 d: float;
    #                 """
    #     expect = "Type mismatch in expression: BinExpr(+, Id(b), Id(c))"
    #     self.assertTrue(TestChecker.test(input, expect, 321))
    #
    # def test_22(self):
    #     """test 22 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #
    #                 a: integer;
    #                 b: boolean = true;
    #                 c: boolean = false;
    #                 e: float = b || c;
    #                 d: function string(a: integer){
    #                     if (n == 0) return 1;
    #                 }
    #                 d: float;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(e, FloatType, BinExpr(||, Id(b), Id(c)))"
    #     self.assertTrue(TestChecker.test(input, expect, 322))
    #
    # def test_23(self):
    #     """test 23 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #
    #                 a: integer;
    #                 b: boolean = true;
    #                 c: boolean = false;
    #                 d: float ;
    #                 d: function string(a_param: integer, inherit d: string, d: float){
    #                     if (n == 0) return 1;
    #                 }
    #                 d: float;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(e, FloatType, BinExpr(||, Id(b), Id(c)))"
    #     self.assertTrue(TestChecker.test(input, expect, 323))
    #
    # def test_24(self):
    #     """test 24 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #
    #                 a: integer;
    #                 b: integer = a+1;
    #
    #                 foo: function integer(inherit c: integer,  d : integer, param: integer){
    #                    a = a+1;
    #                 }
    #                 d: function string(a_param: integer, d: string) inherit foo{
    #                     super(a,b)
    #                 }
    #                 foo: function float(e: integer){
    #                     a = a+1;
    #                 }
    #
    #
    #                 // d: float;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(e, FloatType, BinExpr(||, Id(b), Id(c)))"
    #     self.assertTrue(TestChecker.test(input, expect, 324))
    #
    # def test_25(self):
    #     """test 25 """
    #     input = """a: array[2,4] of boolean= { { { 1,2,3 }, { 4,5,6 } },  { { 11,12,13 }, {22,23} }, { { 21,22,23 }, { 24,25,26 } } };
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 //  a,b: integer;
    #                  // b: integer = a+1;
    #                 //a: integer;
    #
    #                 //foo: function integer(inherit a: string, inherit b : string){
    #                  //  a = a+1;
    #                 //}
    #                 //d: function string(a_param: integer, b: string) inherit foo{
    #                   //  if (n == 0) return 1;
    #                 //}
    #                 // d: float;
    #                 """
    #     expect = "Illegal array literal: ArrayLit([IntegerLit(22), IntegerLit(23)])"
    #     self.assertTrue(TestChecker.test(input, expect, 325))
    #
    # def test_26(self):
    #     """test 26 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 a: integer;
    #                 d: integer;
    #                 e: integer = a+1;
    #                 f: float;
    #                 foo: function integer(inherit c: integer,  a : integer, param: integer){
    #                    a = a+1;
    #                 }
    #                 bar: function string(a_param: integer, d: string) inherit foo{
    #                     super(d,e, f);
    #                     a = a+1;
    #                 }
    #                 // d: float;
    #                 """
    #     expect = "Invalid statement in function: bar"
    #     self.assertTrue(TestChecker.test(input, expect, 326))
    #
    #
    # def test_27(self):
    #     """test 27 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 a: integer;
    #                 d: integer;
    #                 e: integer = a+1;
    #                 f: float;
    #                 foo: function integer(inherit c: integer,  a : integer, param: integer){
    #                    a = a+1;
    #                 }
    #                 bar: function string(a_param: integer, d: string) inherit foo{
    #                     super(d,e, a);
    #                     a = a+1;
    #                 }
    #                 goo: function integer(inherit f: float, out d: string) inherit bar{
    #                     super(e,f);
    #                 }
    #                 // d: float;
    #                 """
    #     expect = "Invalid statement in function: goo"
    #     self.assertTrue(TestChecker.test(input, expect, 327))
    #
    # def test_28(self):
    #     """test 28 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 a: integer;
    #                 d: integer;
    #                 e: integer = a+1;
    #                 f: float;
    #                 goo: function integer(inherit f: float, out d: string) inherit bar{
    #                     super(e);
    #                 }
    #                 bar: function string(a_param: integer, d: string) inherit foo{
    #                     super(d,e, a);
    #                     a = a+1;
    #                 }
    #                 foo: function integer(inherit c: integer,  a : integer, param: integer){
    #                    a = a+1;
    #                 }
    #
    #
    #                 // d: float;
    #                 """
    #     expect = "Type mismatch in expression:"
    #     self.assertTrue(TestChecker.test(input, expect, 328))
    #
    # def test_29(self):
    #     """test 29 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 a: integer;
    #                 b: integer;
    #                 d: integer;
    #                 c:integer;
    #                 e: integer = a+1;
    #                 f: float;
    #                 g: string;
    #                 goo: function integer(inherit f: float, out d: string) inherit bar{
    #                     super(e,2.3);
    #                 }
    #                 bar: function string(a_param: integer, d: string) inherit foo{
    #                     super(a,b,c,d,e,f);
    #                     a = a+1;
    #                 }
    #                 foo: function integer(inherit c: integer,  a : integer){
    #                    a = a+1;
    #                 }
    #
    #
    #                 // d: float;
    #                 """
    #     expect = "Type mismatch in expression: FloatLit(2.3)"
    #     self.assertTrue(TestChecker.test(input, expect, 329))
    #
    #
    # def test_30(self):
    #     """test 30 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 a: integer;
    #                 b: integer;
    #                 d: integer;
    #                 c:integer;
    #                 e: integer = a+1;
    #                 f: float;
    #                 g: string;
    #                 inc : function void (out n : integer, a:float) inherit foo{} //1
    #                 foo : function auto (inherit m: float, n: integer){} //2
    #
    #
    #                 // d: float;
    #                 """
    #     expect = "Invalid statement in function: inc"
    #     self.assertTrue(TestChecker.test(input, expect, 330))
    #
    #
    # def test_31(self):
    #     """test 31 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 a: integer;
    #                 b: integer;
    #                 d: integer;
    #                 c:integer;
    #                 e: integer = a+1;
    #                 f: float;
    #                 g: string;
    #                 inc : function void (out n : integer, a:float) inherit foo{
    #                     if (a==1) a = a+1;
    #                 } //1
    #                 foo : function auto (inherit m: float, n: integer){} //2
    #
    #
    #                 // d: float;
    #                 """
    #     expect = "Invalid statement in function: inc"
    #     self.assertTrue(TestChecker.test(input, expect, 331))
    #
    # def test_32(self):
    #     """test 32 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 a: integer;
    #                 //e: integer = a+1;
    #                 //f: float;
    #                 g: string;
    #                 inc : function void (out n : integer, f:float) {
    #
    #                     a: string = "huy";
    #                     b: float = "huy";
    #                 } //1
    #                 foo : function auto (inherit m: float, n: integer){} //2
    #
    #
    #                 // d: float;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(b, FloatType, StringLit(huy))"
    #     self.assertTrue(TestChecker.test(input, expect, 332))
    #
    # def test_33(self):
    #     """test 33 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 //a: integer;
    #                 //d: integer;
    #                 //e: integer = a+1;
    #                 f: float;
    #                 goo: function integer(inherit f: float, d: string) inherit bar{
    #                     // super(e);
    #                 }
    #                 bar: function string(a_param: integer, inherit d: string) inherit foo{
    #                     super(d,e, a);
    #                     a = a+1;
    #                 }
    #                 foo: function integer(inherit c: integer,  a : integer, param: integer){
    #                    a = a+1;
    #                 }
    #
    #
    #                 // d: float;
    #                 """
    #     expect = "Invalid Parameter: d"
    #     self.assertTrue(TestChecker.test(input, expect, 333))
    #
    #
    # def test_34(self):
    #     """test 34 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 //a: integer;
    #                 //e: integer = a+1;
    #                 //f: float;
    #                 g: string;
    #                 inc : function void (out n : integer, f:float) {
    #                     super();
    #                     a: string = "huy";
    #                     b: float = "huy";
    #                 } //1
    #                 foo : function auto (inherit m: float, n: integer){} //2
    #
    #
    #                 // d: float;
    #                 """
    #     expect = "Invalid statement in function: inc"
    #     self.assertTrue(TestChecker.test(input, expect, 334))
    #
    # def test_35(self):
    #     """test 35 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 a: integer;
    #                 //e: integer = a+1;
    #                 //f: float;
    #                 g: string;
    #                 inc : function void (out n : integer, f:float) {
    #
    #                     a: string = "huy";
    #                     a = a+1_2;
    #                     b: float = 2.3;
    #                 } //1
    #                 f: integer = a+1;
    #                 e: auto;
    #                 foo : function auto (inherit m: float, n: integer){} //2
    #
    #
    #                 // d: float;
    #                 """
    #     expect = "Type mismatch in expression: BinExpr(+, Id(a), IntegerLit(12))"
    #     self.assertTrue(TestChecker.test(input, expect, 335))
    #
    # def test_36(self):
    #     """test 36 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 // a: integer;
    #                  //e: integer = a+1;
    #                  //f: float;
    #                 // g: string;
    #                 inc : function void (out n : integer, f:float) {
    #
    #                     a: string = "huy";
    #                     a = a:: "huy";
    #                     b: float = 2.3;
    #                 } //1
    #                 f: integer = a+1;
    #                 e: auto;
    #                 foo : function auto (inherit m: float, n: integer){} //2
    #
    #
    #                 // d: float;
    #                 """
    #     expect = "Invalid Variable: e"
    #     self.assertTrue(TestChecker.test(input, expect, 336))
    #
    # def test_37(self):
    #     """test 37"""
    #     input = """
    #
    #     foo : function auto (inherit n: float, b: integer){} //2
    #     inc : function void (out n : integer, a:float) inherit thien{} //1
    #     thien: integer;
    #     huy: float;
    #     """
    #     expect = "Undeclared Function: thien"
    #     self.assertTrue(TestChecker.test(input, expect, 337))
    #
    # def test_38(self):
    #     """test 38 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 a: integer;
    #                  //e: integer = a+1;
    #                  //f: float;
    #                 // g: string;
    #                 inc : function void (out n : integer, f:float) {
    #                     a = a+1;
    #
    #                 } //1
    #                 f: integer = a+1;
    #                 e: auto;
    #                 foo : function auto (inherit m: float, n: integer){} //2
    #
    #
    #                 // d: float;
    #                 """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 338))
    #
    # def test_39(self):
    #     """test 39 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 a: integer;
    #                  //e: integer = a+1;
    #                  //f: float;
    #                 // g: string;
    #                 inc : function void (out n : integer, f:float) {
    #                     a = a+1;
    #
    #                 } //1
    #                 f: integer = a+1;
    #                 e: auto =1;
    #                 foo : function auto (inherit m: float, n: integer){
    #                     f = e::"huy";
    #                 } //2
    #
    #
    #                 // d: float;
    #                 """
    #     expect = "Type mismatch in expression: BinExpr(::, Id(e), StringLit(huy))"
    #     self.assertTrue(TestChecker.test(input, expect, 339))
    #
    # def test_40(self):
    #     """test 40 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 a: integer;
    #                 //d: integer;
    #                 e: integer = 1;
    #                 f: float;
    #                 //goo: function integer(inherit f: float, d: string) inherit bar{
    #                   //  super(e);
    #                 //}
    #                 bar: function string(a_param: integer, d: string) inherit foo{
    #                     super(d,e, a);
    #                     a = a+1;
    #                 }
    #                 foo: function integer(inherit c: string,  a : integer, param: integer){
    #                    c = c::1;
    #                 }
    #
    #
    #                 d: float;
    #                 """
    #     expect = "Type mismatch in expression: BinExpr(::, Id(c), IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 340))
    #
    # def test_41(self):
    #     """test 41 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 a: string;
    #                 //d: integer;
    #                 // e: integer = 1;
    #                 f: float;
    #                 //goo: function integer(inherit f: float, d: string) inherit bar{
    #                   //  super(e);
    #                 //}
    #                 bar: function string(a_param: integer, d: string) inherit foo{
    #                     super(a,e, a_param);
    #                     a = a+1;
    #
    #                 }
    #                 foo: function integer(inherit c: string,  a : integer, param: integer){
    #                    c = c::1;
    #                 }
    #
    #
    #                 d: float;
    #                 """
    #     expect = "Undeclared Identifier: e"
    #     self.assertTrue(TestChecker.test(input, expect, 341))
    #
    # def test_42(self):
    #     """test 42 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #                 a: integer;
    #                 //d: integer;
    #                 e: integer = 1;
    #                 f: float;
    #                 //goo: function integer(inherit f: float, d: string) inherit bar{
    #                   //  super(e);
    #                 //}
    #                 bar: function string(a_param: integer, d: string) inherit foo{
    #                     super(d,e, a);
    #                     a = a+1;
    #                 }
    #                 foo: function integer(inherit c: string,  a : integer, param: integer){
    #                    a = a+1.2;
    #
    #                 }
    #
    #
    #                 d: float;
    #                 """
    #     expect = "Type mismatch in statement: AssignStmt(Id(a), BinExpr(+, Id(a), FloatLit(1.2)))"
    #     self.assertTrue(TestChecker.test(input, expect, 342))
    #
    #
    # def test_43(self):
    #     """test 43 """
    #     input = """a: integer;
    #                 b: float;
    #                 c: float;
    #                 main: function void(){
    #                     c = a + b;
    #                     e:auto;
    #                     }
    #
    #                 """
    #     expect = "Type mismatch in statement: AssignStmt(Id(a), BinExpr(+, Id(a), FloatLit(1.2)))"
    #     self.assertTrue(TestChecker.test(input, expect, 343))
    #
    # def test_44(self):
    #     """test 44 """
    #     input = """
    #                 a: integer = foo(1,"huy");
    #                 c: float = foo(1,"true");
    #                 foo: function auto(a: integer, b: string){}
    #                 e: auto;
    #                 """
    #     expect = "Invalid Variable: e"
    #     self.assertTrue(TestChecker.test(input, expect, 344))
    #
    # def test_45(self):
    #     """test 45 """
    #     input = """
    #                 a: integer = foo(1,"huy");
    #                 c: float = foo(1,"true");
    #                 foo: function string(a: integer, b: string){}
    #                 // main: function void(){}
    #                 e: auto = 2;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(foo, [IntegerLit(1), StringLit(huy)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 345))
    #
    #
    # def test_46(self):
    #     """test 46 """
    #     input = """
    #                 a: integer = foo(1,"huy");
    #                 f: float = foo(1,"true");
    #                 foo: function integer(a: integer, b: string){}
    #                 goo: function integer(f: string, e: float){
    #                     f = f+1;
    #                 }
    #                 main: function void(){}
    #                 e: auto = 2;
    #                 """
    #     expect = "Type mismatch in expression: BinExpr(+, Id(f), IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 346))
    #
    # def test_47(self):
    #     """test 47 """
    #     input = """
    #                 a: integer = foo(1,"huy");
    #                 f: auto = foo(1,"true");
    #                 foo: function integer(a: auto, b: string){}
    #                 goo: function integer(f: string, e: float){
    #                     f = f+1;
    #                 }
    #                 main: function void(){}
    #                 e: auto = 2;
    #                 """
    #     expect = "Type mismatch in expression: BinExpr(+, Id(f), IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 347))
    #
    #
    # def test_48(self):
    #     """test 48 """
    #     input = """
    #                 a: integer = foo(1,"huy");
    #                 f: float = foo(1,"true");
    #                 foo: function integer(e: string, b: string) inherit goo{
    #                     super(a,f);
    #                     a = a+1;
    #                 }
    #                 goo: function integer(f: auto, e: float){
    #                     f = f+1;
    #                 }
    #                 main: function void(){}
    #                 e: auto ;
    #                 """
    #     expect = "Invalid Variable: e"
    #     self.assertTrue(TestChecker.test(input, expect, 348 ))
    #
    # def test_49(self):
    #     """test 49 """
    #     input = """
    #                 foo: function void (a: integer) inherit bar{}
    #                 bar: function void (inherit a:integer) {}
    #                 main: function void(){}
    #                 """
    #     expect = "Invalid Parameter: a"
    #     self.assertTrue(TestChecker.test(input, expect, 349))
    #
    #
    # def test_50(self):
    #     """test 50 """
    #     input = """
    #                 a: integer = foo(1, "huy");
    #                 foo: function integer(a: auto, b: string){}
    #                 main: function void(){}
    #                 e: auto;
    #                 """
    #     expect = "Invalid Variable: e"
    #     self.assertTrue(TestChecker.test(input, expect, 350))
    #
    # def test_51(self):
    #     """test 51 """
    #     input = """
    #
    #                 a: float = foo(bar(),"huy");
    #                 // f: float = foo(1,"true");
    #                 foo: function auto(f: auto, h: string){}
    #
    #                 goo: function integer(f: string, e: float){
    #                     f = f+1;
    #                 }
    #                 main: function void(){}
    #                 e: auto = 2;
    #                 """
    #     expect = "Undeclared Function: bar"
    #     self.assertTrue(TestChecker.test(input, expect, 351))
    #
    # def test_52(self):
    #     """test 52"""
    #     input = """
    #
    #                 a: float = foo(1,"huy");
    #                 f: float = foo(1,"true");
    #                 foo: function auto(f: auto, h: float) inherit goo{
    #                     super(f,h);
    #                 }
    #
    #                 goo: function integer(f: string, e: float){
    #                     f = f+1;
    #                 }
    #                 main: function void(){}
    #                 e: auto ;
    #                 """
    #     expect = "Type mismatch in expression: BinExpr(+, Id(f), IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 352))
    #
    # def test_53(self):
    #     """test 53"""
    #     input = """
    #                 a: float = foo(1,"huy");
    #                 f: float = foo(1,"true");
    #                 goo: function integer(f: auto, e: float){
    #                     f = f+1;
    #                 }
    #                 foo: function auto(f: integer, h: float) inherit goo{
    #                     super(f,h);
    #                 }
    #
    #                 main: function void(){}
    #                 e: auto ;
    #                 """
    #     expect = "Invalid Variable: e"
    #     self.assertTrue(TestChecker.test(input, expect, 353))
    #
    # def test_54(self):
    #     """test 54"""
    #     input = """
    #                 //a: float = foo(1,"huy");
    #                 //f: float = foo(1,"true");
    #                 goo: function integer(f: auto, e: float){
    #                     f = f+1;
    #                 }
    #                 foo: function auto(f: integer, h: float) inherit goo{
    #                     super(f,h);
    #                 }
    #                 main: function void(){}
    #                 e: auto ;
    #                 """
    #     expect = "Invalid Variable: e"
    #     self.assertTrue(TestChecker.test(input, expect, 354))
    #
    # def test_55(self):
    #     """test 55"""
    #     input = """
    #              a: integer;
    #             foo: function auto (a: auto, b: float) inherit bar {  // a: integer in foo()
    #             super(1.2+a*2, !true);
    #              }
    #             b: string = bar(1_0, !!false);  // Implicit conversion, bar: string
    #             bar: function auto (a: auto, b: boolean) {}  // a: float in bar()
    #             c: integer = bar(1, 1==true);  // bar: string != integer
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FuncCall(bar, [IntegerLit(1), BinExpr(==, IntegerLit(1), BooleanLit(True))]))"
    #     self.assertTrue(TestChecker.test(input, expect, 355))
    #
    # def test_56(self):
    #     """ test 56 """
    #     input = """
    #     a: string;
    #     //_global: array [2] of integer = {1_0, 2_0};
    #     foo: function void (b: integer, d: string) inherit bar {
    #         super(b, b+bar(1, 2, d), d::"hello");
    #         x: boolean = !!false;
    #         y: auto = x && (1_2 > 2.3);
    #         while (bar(1, b+1, d)==2) { // Check Boolean condition in While
    #             x: auto = a;
    #             if (y && !y) {
    #                 x: float = x;
    #                // a: auto = _global[0];
    #             }
    #         }
    #     }
    #     bar: function auto (x: float, inherit a: integer, inherit c: auto) {}
    #     """
    #     expect = "[]"
    #     self.assertTrue(TestChecker.test(input, expect, 356))
    #
    #
    # def test_57(self):
    #     """ test 57 """
    #     input = """
    #     a: string;
    #     //_global: array [2] of integer = {1_0, 2_0};
    #     foo: function void (inherit d: integer, d: string) inherit bar {
    #         }
    #
    #     //bar: function auto (x: float, inherit a: integer, inherit c: auto) {}
    #     """
    #     expect = "Redeclared Parameter: d"
    #     self.assertTrue(TestChecker.test(input, expect, 357))
    #
    #
    # def test_58(self):
    #     """ test 58 """
    #     input = """
    #     a: string;
    #     y: float;
    #     huy: string;
    #     quan: integer;
    #     //_global: array [2] of integer = {1_0, 2_0};
    #     bar: function auto (x: float, inherit a: integer, inherit c: auto) {}
    #     foo: function void (inherit e: integer, d: string) inherit bar {
    #         super(y,2.0,huy);
    #         a: string;
    #         }
    #
    #     //
    #     """
    #     expect = "Type mismatch in expression: FloatLit(2.0)"
    #     self.assertTrue(TestChecker.test(input, expect, 358))
    #
    # def test_59(self):
    #     """ test 59 """
    #     input = """
    #     a: string;
    #     y: float;
    #     huy: string;
    #     quan: integer;
    #     //_global: array [2] of integer = {1_0, 2_0};
    #     bar: function auto (x: float, inherit a: integer, inherit c: auto) {}
    #     foo: function void (inherit e: integer, d: string) inherit bar {
    #         super(y,quan,huy);
    #         a: string;
    #         }
    #
    #     //
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 359))
    #
    #
    # def test_60(self):
    #     """ test 60 """
    #     input = """
    #     bar: function auto(inherit a:integer, a: string){}
    #     foo: function auto(x: float, b: boolean) inherit bar{
    #         super(1,"true");
    #         }
    #
    #
    #
    #     //
    #     """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 360))
    #
    #
    # def test_61(self):
    #     """ test 61 """
    #     input = """
    #     foo: function auto(x: float, b: boolean) inherit bar{
    #         super(1,"true");
    #         }
    #     bar: function auto(inherit a:integer, inherit a: string){}
    #
    #     //
    #     """
    #     expect = "Undeclared Function: bar"
    #     self.assertTrue(TestChecker.test(input, expect, 361))
    # def test_62(self):
    #     """ test 62 """
    #     input = """
    #     foo: function auto(x: float, d: boolean) inherit bar{
    #         preventDefault();
    #         a: string;
    #         e: auto;
    #         }
    #     bar: function auto(inherit a:integer, inherit b: string){}
    #
    #     //
    #     """
    #     expect = "Invalid Variable: e"
    #     self.assertTrue(TestChecker.test(input, expect, 362))
    #
    # def test_63(self):
    #     """ test 63 """
    #     input = """
    #     foo: function auto(x: float, d: boolean) inherit bar{
    #         preventDefault();
    #         a: integer;
    #         if (a == 1) {
    #         break;
    #         }
    #     }
    #     bar: function auto(inherit a:integer, inherit b: string){}
    #
    #     //
    #     """
    #     expect = "Must in loop: BreakStmt()"
    #     self.assertTrue(TestChecker.test(input, expect, 363))
    #
    #
    # def test_64(self):
    #     """ test 64 """
    #     input = """
    #     foo: function auto(x: float, d: boolean) inherit bar{
    #         preventDefault();
    #         a: integer;
    #         if (a == 1) {
    #         a = a+1;
    #         }
    #         else{continue;}
    #     }
    #     bar: function auto(inherit a:integer, inherit b: string){}
    #
    #     //
    #     """
    #     expect = "Must in loop: ContinueStmt()"
    #     self.assertTrue(TestChecker.test(input, expect, 364))
    #
    # def test_65(self):
    #     """ test 65 """
    #     input = """
    #     foo: function auto(x: float, d: boolean) inherit bar{
    #         preventDefault();
    #         break;
    #     }
    #     bar: function auto(inherit a:integer, inherit b: string){}
    #
    #     //
    #     """
    #     expect = "Must in loop: BreakStmt()"
    #     self.assertTrue(TestChecker.test(input, expect, 365))
    #
    # def test_66(self):
    #     """ test 66 """
    #     input = """
    #     foo: function auto(x: float, d: boolean) inherit bar{
    #         preventDefault();
    #     }
    #     bar: function auto(inherit a:integer, inherit b: string){
    #         continue;
    #     }
    #
    #     //
    #     """
    #     expect = "Must in loop: ContinueStmt()"
    #     self.assertTrue(TestChecker.test(input, expect, 366))
    #
    # def test_67(self):
    #     """ test 67 """
    #     input = """
    #     foo: function auto(x: float, d: boolean) inherit bar{
    #         preventDefault();
    #         c: boolean = true;
    #         if (d ==  c){
    #             a = a+1;
    #         }
    #         else{
    #             c = c+1;
    #         }
    #
    #     }
    #     bar: function auto(inherit a:integer, inherit b: string){
    #         continue;
    #     }
    #
    #     //
    #     """
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input, expect, 367))
    #
    #
    # def test_68(self):
    #     """ test 68 """
    #     input = """
    #     a: float = 2.0;
    #     foo: function auto(x: float, d: boolean) inherit bar{
    #         preventDefault();
    #         c: boolean = true;
    #         if (d ==  c){
    #             a = a+1;
    #         }
    #         else{
    #             c = c+1;
    #         }
    #
    #     }
    #     bar: function auto(inherit a:integer, inherit b: string){
    #         continue;
    #     }
    #
    #     //
    #     """
    #     expect = "Type mismatch in expression: BinExpr(+, Id(c), IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 368))
    #
    #
    # def test_69(self):
    #     """ test 69 """
    #     input = """
    #     a: float = 2.0;
    #     foo: function auto(x: float, d: boolean) inherit bar{
    #         preventDefault();
    #         a: string = "huy";
    #         c: boolean = true;
    #         if (d ==  c){
    #             a: boolean = d;
    #             a = a+1;
    #         }
    #         else{
    #             c = c+1;
    #         }
    #
    #     }
    #     bar: function auto(inherit a:integer, inherit b: string){
    #         continue;
    #     }
    #
    #     //
    #     """
    #     expect = "Type mismatch in expression: BinExpr(+, Id(a), IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 369))
    #
    # def test_70(self):
    #     """ test 70 """
    #     input = """
    #     a: integer = 2;
    #     d: boolean ;
    #     k: string;
    #     foo: function auto(x: float, huy: boolean) inherit bar{ //env =[a,x,huy,hello,b]
    #         super(a,k);
    #         thien: integer = 2_12;
    #         c: boolean = d;
    #         e: auto;
    #     }
    #     bar: function auto(inherit hello: integer, inherit b: string){
    #         continue;
    #     }
    #
    #     //
    #     """
    #     expect = "Invalid Variable: e"
    #     self.assertTrue(TestChecker.test(input, expect, 370))
    #
    # def test_71(self):
    #     """ test 71 """
    #     input = """
    #     a: float = 2.0;
    #
    #     foo: function auto(x: auto, d: boolean) inherit bar{
    #         preventDefault();
    #         a: string = "huy";
    #         c: boolean = true;
    #         if (d ==  c){
    #             a: boolean = d;
    #             x = a;
    #             x = x -2;
    #         }
    #         else{
    #             c = c+1;
    #         }
    #
    #     }
    #     bar: function auto(inherit a:integer, inherit b: string){
    #         continue;
    #     }
    #
    #     //
    #     """
    #     expect = "Type mismatch in expression: BinExpr(-, Id(x), IntegerLit(2))"
    #     self.assertTrue(TestChecker.test(input, expect, 371))
    #
    # def test_72(self):
    #     """ test 71 """
    #     input = """
    #     a: float = 2.0;
    #
    #     foo: function auto(x: auto, d: boolean) inherit bar{
    #         preventDefault();
    #         a: string = "huy";
    #         c: boolean = true;
    #         if (d ==  c){
    #             a: boolean = d;
    #             x = a;
    #
    #         }
    #         else{
    #             a: integer = 1;
    #             c = c+1;
    #         }
    #
    #     }
    #     bar: function auto(inherit a:integer, inherit b: string){
    #         continue;
    #     }
    #
    #     //
    #     """
    #     expect = "Type mismatch in expression: BinExpr(+, Id(c), IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 372))
    #
    # def test_73(self):
    #     """ test 73 """
    #     input = """
    #     a: float = 2.0;
    #
    #     foo: function auto(x: auto, d: boolean) inherit bar{
    #         preventDefault();
    #         a: string = "huy";
    #         c: boolean = true;
    #         if (d ==  c){
    #             a: boolean = d;
    #             x = a;
    #
    #         }
    #         else{
    #             a: integer = 1;
    #
    #         }
    #
    #     }
    #     bar: function auto(inherit a:integer, inherit b: string){
    #         a = a+1;
    #     }
    #
    #     //
    #     """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 373))
    #
    # def test_74(self):
    #     """ test 74"""
    #     input = """
    #     a: float = 2.0;
    #
    #     foo: function float(x: auto, d: boolean){
    #         return a;
    #
    #     }
    #
    #     //
    #     """
    #     expect = "Type mismatch in expression: BinExpr(+, Id(c), IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 374))
    # def test_75(self):
    #     """ Return Integer, function: Float in If Else Stmt """
    #     input = """
    #      a: integer = 1;
    #         inc : function string (out b: auto, inherit d: auto) inherit foo
    #         {
    #             super("thien", 1);
    #             i: float;
    #             for (b = 1, i< 10, i+1)
    #             {
    #             a = 1;
    #             }
    #         } //1
    #
    #         foo : function auto (inherit a: auto, inherit c: integer){
    #         return 2;
    #         } //2
    #
    #         d:integer = foo("thien" ,2);
    #
    #         c: string;
    #
    #         main: function void(){
    #         thien: integer = 1;
    #
    #         }
    #     """
    #     expect = "Type mismatch in statement: ReturnStmt(BinExpr(::, StringLit(x), Id(d)))"
    #     self.assertTrue(TestChecker.test(input, expect, 374))
    #
    #
    # def test_75(self):
    #     """test 75"""
    #     input = """a: integer = "huy";
    #                 a: integer;"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, StringLit(huy))"
    #     self.assertTrue(TestChecker.test(input, expect, 375))
    #
    # def test_76(self):
    #     """test 76"""
    #     input = """a: auto;"""
    #     expect = "Invalid Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 376))
    #
    # def test_77(self):
    #     """test 77"""
    #     input = """a,b: integer = 2, "huy";"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, StringLit(huy))"
    #     self.assertTrue(TestChecker.test(input, expect, 377))
    #
    # def test_78(self):
    #     """test 78"""
    #     input = """a,b: integer = 2, 3;
    #                 c: integer = 2.1;
    #                 d: auto;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FloatLit(2.1))"
    #     self.assertTrue(TestChecker.test(input, expect, 378))
    #
    # def test_79(self):
    #     """test 79"""
    #     input = """a,b: integer = 2, 3;
    #                 c: integer = 2.1;
    #                 a: float;
    #                 d: auto;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FloatLit(2.1))"
    #     self.assertTrue(TestChecker.test(input, expect, 379))
    #
    # def test_80(self):
    #     """test 80"""
    #     input = """a,b: integer = 2, 3;
    #
    #                 a: float;
    #                 d: auto;
    #                 """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input, expect, 380))
    #
    # def test_81(self):
    #     """test 81"""
    #     input = """a,b: integer = 2, 3;
    #                 // c: integer = 2.1;
    #                 // c = a + 1;
    #                 e: float = a + 1;
    #                 d: auto;
    #                 """
    #     expect = "Invalid Variable: d"
    #     self.assertTrue(TestChecker.test(input, expect, 381))
    #
    # def test_82(self):
    #     """test 82"""
    #     input = """a,b: float = 2.1, 3.1;
    #                 // c: integer = 2.1;
    #                 // c = a + 1;
    #                 e: integer = a + 1;
    #                 d: auto;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(e, IntegerType, BinExpr(+, Id(a), IntegerLit(1)))"
    #     self.assertTrue(TestChecker.test(input, expect, 382))
    #
    # def test_83(self):
    #     """test 83"""
    #     input = """a,b,c: float = 2.1, 3,4;
    #                 // c: integer = 2.1;
    #                 // c = a + 1;
    #                 e: integer = f + 1;
    #                 d: auto;
    #                 """
    #     expect = "Undeclared Identifier: f"
    #     self.assertTrue(TestChecker.test(input, expect, 383))
    #
    # def test_84(self):
    #     """test 84"""
    #     input = """a: integer = b+1;
    #                 b: integer;
    #                 """
    #     expect = "Undeclared Identifier: b"
    #     self.assertTrue(TestChecker.test(input, expect, 384))
    #
    # def test_85(self):
    #     """test 11"""
    #     input = """a: array[4] of integer= {1,2,3,"huy"};
    #
    #                 """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 385))
    #
    # def test_86(self):
    #     """test 12"""
    #     input = """a,b,c: integer = 1 ,2, 2;
    #                 d: float;
    #                 e: boolean = 1;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(e, BooleanType, IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 386))
    #
    # def test_87(self):
    #     """test 87"""
    #     input = """a: float;
    #                 b: integer;
    #                 b: function integer(a: string){
    #                 a = a+1;
    #                 }
    #
    #                 """
    #     expect = "Redeclared Variable: b"
    #     self.assertTrue(TestChecker.test(input, expect, 387))
    #
    # def test_88(self):
    #     """test 88"""
    #     input = """a: array[4] of float= {12,2,3,3};
    #                 // b: array[4] of integer = {1.2,2,1,3}
    #
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([4], FloatType), ArrayLit([IntegerLit(12), IntegerLit(2), IntegerLit(3), IntegerLit(3)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 388))
    #
    # def test_89(self):
    #     """test 89 need to consider"""
    #     input = """a: array[4] of float= {1.2,2.1,3,3};
    #                 // b: array[4] of integer = {1.2,2,1,3}
    #
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([4], FloatType), ArrayLit([IntegerLit(12), IntegerLit(2), IntegerLit(3), IntegerLit(3)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 389))
    #
    # def test_90(self):
    #     """test 91 """
    #     input = """a: array[4] of float= {1.2,2.1,3,3};
    #                 a: array[4] of integer = {1.2,2,1,3};
    #
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([4], FloatType), ArrayLit([IntegerLit(12), IntegerLit(2), IntegerLit(3), IntegerLit(3)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 391))
    #
    # def test_92(self):
    #     """test 92 """
    #     input = """//a: array[4] of float= {1.2,2.1,3,3};
    #                 a: array[4] of float = {12.1,2.1,1.1,{1.2,2.2,3.2}};
    #                 """
    #     expect = "Illegal array literal: ArrayLit([FloatLit(12.1), FloatLit(2.1), FloatLit(1.1), ArrayLit([FloatLit(1.2), FloatLit(2.2), FloatLit(3.2)])])"
    #     self.assertTrue(TestChecker.test(input, expect, 392))
    # def test_93(self):
    #     """test 93"""
    #     input = """//a: array[4] of float= {1.2,2.1,3,3};
    #                a: array[4] of integer = {12,2,1,1,2};
    #                 // b: integer;
    #                 // c: boolean;
    #                 // a: integer;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([4], IntegerType), ArrayLit([IntegerLit(12), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(2)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 393))
    #
    # def test_94(self):
    #     """test 94 """
    #     input = """//a: array[4] of float= {1.2,2.1,3.2,3.1};
    #                a: array[4] of integer = {12,2,1,1};
    #                 // b: integer;
    #                 // c: boolean;
    #                 // a: integer;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([4], IntegerType), ArrayLit([IntegerLit(12), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(2)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 394))
    #
    # def test_95(self):
    #     """test 95"""
    #     input = """a: array[4] of boolean= {true,false,true,true};
    #                b: array[2,3] of integer = {12,2,1,1,3,4};
    #
    #                 huy: auto = 2;
    #                 foo: float = 2+huy;
    #                 hi: boolean;
    #                 foo: integer;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2, 3], IntegerType), ArrayLit([IntegerLit(12), IntegerLit(2), IntegerLit(1), IntegerLit(1), IntegerLit(2)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 395))
    #
    # def test_96(self):
    #     """test 96 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #
    #                 a: integer;
    #                 b: boolean = true;
    #                 c: boolean = false;
    #                 e: boolean = b + c;
    #                 d: function string(a: integer){
    #                     if (n == 0) return 1;
    #                 }
    #                 d: float;
    #                 """
    #     expect = "Type mismatch in expression: BinExpr(+, Id(b), Id(c))"
    #     self.assertTrue(TestChecker.test(input, expect, 396))
    #
    # def test_97(self):
    #     """test 97 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #
    #                 a: integer;
    #                 b: boolean = true;
    #                 c: boolean = false;
    #                 e: float = b || c;
    #                 d: function string(a: integer){
    #                     if (n == 0) return 1;
    #                 }
    #                 d: float;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(e, FloatType, BinExpr(||, Id(b), Id(c)))"
    #     self.assertTrue(TestChecker.test(input, expect, 397))
    #
    # def test_98(self):
    #     """test 98"""
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #
    #                 a: integer;
    #                 b: boolean = true;
    #                 c: boolean = false;
    #                 d: float ;
    #                 d: function string(a_param: integer, inherit d: string, d: float){
    #                     if (n == 0) return 1;
    #                 }
    #                 d: float;
    #                 """
    #     expect = "Type mismatch in Variable Declaration: VarDecl(e, FloatType, BinExpr(||, Id(b), Id(c)))"
    #     self.assertTrue(TestChecker.test(input, expect, 398))
    #
    # def test_99(self):
    #     """test 99 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #
    #                 a: integer;
    #                 b: integer = a+1;
    #
    #                 foo: function integer(inherit c: integer,  d : integer, param: integer){
    #                    a = a+1;
    #                 }
    #                 d: function string(a_param: integer, d: string) inherit foo{
    #                     super(a,b);
    #                 }
    #                 foo: function float(e: integer){
    #                     a = a+1;
    #                 }
    #
    #
    #                 // d: float;
    #                 """
    #     expect = "Type mismatch in expression: "
    #     self.assertTrue(TestChecker.test(input, expect, 399))
    #
    # def test_100(self):
    #     """test 100 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #
    #                 a: array[2,4] of integer = {{1,2,4}, {2,3,6,7}};
    #
    #
    #                 // d: float;
    #                 """
    #     expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(4)]), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(6), IntegerLit(7)])]) "
    #     self.assertTrue(TestChecker.test(input, expect, 400))
    #
    # def test_100(self):
    #     """test 100 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #
    #                 //a: array[2,4] of integer = {{1,2,1.2,5}, {2,3,6,7}, {{1,2,"huy"}, {"huy",true,false}} };
    #                 //a: array [2, 3, 3] of integer = {{{1, 2, 3}, {1, 2, 5}, {1, 2, 4}}, {{2, 3, 1}, {1, 6}, {1, 3, 5}}};
    #                 //a: array [2, 3, 2, 3] of integer = { { { {1, 2, 3}, {2, 4, 5} }, { {2, 1, 3}, {5, 1, 7} }, { {3, 1, 2}, {1, 4, 5} } }, { { {2, 1, 0}, {3, 2, 1} }, { {6, 2, 3}, {4} }, { {3}, {1} } } };
    #                 // d: float;
    #                 a: array [2, 3, 2] of integer = { { {1, 2}, {3, 5}, {"a", "b"} }, {1, 2, 3} };
    #                 """
    #     expect = " Illegal array literal: ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(5)]), ArrayLit([StringLit(a), StringLit(b)])]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])])"
    #     self.assertTrue(TestChecker.test(input, expect, 400))
    #
    #
    # def test_101(self):
    #     """test 101 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #
    #                 //a: array[2,4] of integer = {{1,2,1.2,5}, {2,3,6,7}, {{1,2,"huy"}, {"huy",true,false}} };
    #                 //a: array [2, 3, 3] of integer = {{{1, 2, 3}, {1, 2, 5}, {1, 2, 4}}, {{2, 3, 1}, {1, 6}, {1, 3, 5}}};
    #                 //a: array [2, 3, 2, 3] of integer = { { { {1, 2, 3}, {2, 4, 5} }, { {2, 1, 3}, {5, 1, 7} }, { {3, 1, 2}, {1, 4, 5} } }, { { {2, 1, 0}, {3, 2, 1} }, { {6, 2, 3}, {4} }, { {3}, {1} } } };
    #                 // d: float;
    #                 //a: array [2,2] of integer = { { "a" , "b"::"c" }, { "hello", "1.5" } };
    #                 //a: array [2,2] of string = { { "a" , "b"::"c" }, { "hello", "1.5" } };
    #                 a: integer = 1;
    #                 b: string = "huy";
    #                 c: string;
    #                 d: string = b::c;
    #                 e: auto;
    #                 """
    #     expect = " Invalid Variable: e"
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_101(self):
    #     """test 101 """
    #     input = """// a: array[4] of boolean= {true,false,true,true};
    #                // b: array[2,3] of integer = {12,2,1,1,3,4};
    #
    #                 //a: array[2,4] of integer = {{1,2,1.2,5}, {2,3,6,7}, {{1,2,"huy"}, {"huy",true,false}} };
    #                 //a: array [2, 3, 3] of integer = {{{1, 2, 3}, {1, 2, 5}, {1, 2, 4}}, {{2, 3, 1}, {1, 6}, {1, 3, 5}}};
    #                 //a: array [2, 3, 2, 3] of integer = { { { {1, 2, 3}, {2, 4, 5} }, { {2, 1, 3}, {5, 1, 7} }, { {3, 1, 2}, {1, 4, 5} } }, { { {2, 1, 0}, {3, 2, 1} }, { {6, 2, 3}, {4} }, { {3}, {1} } } };
    #                 // d: float;
    #                 //a: array [2,2] of integer = { { "a" , "b"::"c" }, { "hello", "1.5" } };
    #                 //a: array [2,2] of string = { { "a" , "b"::"c" }, { "hello", "1.5" } };
    #                 a: integer = foo(1, "huy");
    #                 foo: function string(a: integer, a: string){}
    #                 """
    #     expect = " Invalid Variable: e"
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    def test_46(self):
        input = """
                foo: function void (a: integer) {}
                
                bar: function void(a: integer, b: string, a:float){}
                """
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input, expect, 346))










