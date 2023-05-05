// Student ID: 2052106
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  decls EOF ;

arrayliteral: LCB arrayprime RCB;
arrayprime: arrayelements | ;
arrayelements: arrayelement CM arrayelements | arrayelement;
arrayelement: expr;
arraytyp: ARRAY LSB arrayindexprime RSB OF elementtype;
//dimension: (arrayindex(',' arrayindex)*);
arrayindexprime: arrayindexes ;
arrayindexes: arrayindex CM arrayindexes | arrayindex;
arrayindex: Integer;

actomic: INT | FLOAT | STRING | BOOLEAN;
elementtype: actomic;
decls: decl decls | decl;
decl: vardecl | funcdecl;

//variable
vardecl: variablerecursive SM | nonvardecl;
variablerecursive: Identifiers CM variablerecursive CM expr | Identifiers COLON typ EQ expr;
nonvardecl:  identifiersprime COLON typ SM;
identifiersprime: identifierslist ;
identifierslist: identifiers CM identifierslist | identifiers;
identifiers: Identifiers;
// vardecl: varlist COLON typ (EQ exprlist)? SM ;
// varlist: varelements | ;
// varelements: varelement CM varelements | varelement;
// varelement: idlist;
// idlist: Identifiers CM idlist | Identifiers;
typ: actomic
	| arraytyp
 	| AUTO;
exprlist: exprlements  ;
exprlements: expr CM exprlements | expr;

// localVariable
// 	:	Identifiers ',' localVariable ',' value | Identifiers ':' typ '=' value
// 	;
// localVariableDeclaration
// 	: localVariable ';'
// 	;
// value: Integer |;


expr: expr1 CONCAT expr1 | expr1;
expr1: expr2 (DOUEQ|DIFF|SMALLER|GREATER|SMAEQ|GREEQ) expr2	| expr2;
expr2: expr2 (CONJUNCTION|DISJUNCTION) expr3|expr3;
expr3: expr3 (ADDOP|MINUSOP) expr4 | expr4;
expr4: expr4 (MULOP|DIVOP|MODUOP) expr5 | expr5;
expr5: NEGATION expr5 | expr6;
expr6: MINUSOP expr6 | 	expr7;
expr7: expr7 (LSB|RSB)| expr8; // để tạm cho index operator
expr8: String |Integer|Float|Identifiers| boolean | funccall |subexpr|arrayliteral|indexop ; 
subexpr: LB expr RB;
// indexop:
indexop: Identifiers LSB exprlist RSB;
//function
funcdecl: funcproto funcbody;
funcproto: Identifiers COLON FUNCTION returntyp LB parameterlist RB (subpart)?;

returntyp: actomic|VOID|arraytyp|AUTO;
subpart: INHERIT Identifiers;
funcbody: block;
//function call
funccall: Identifiers LB argumentprime RB;
argumentprime: argumentlists | ;
argumentlists: argumentlist CM argumentlists | argumentlist;
argumentlist: expr;
// parameters
parameterlist: parameters |;
parameters: parameter CM parameters | parameter;
parameter: (INHERIT)? (OUT)? Identifiers COLON typ  ;

statement: block
		| assignmentstmt
		| ifstmt
		|forstmt
		|whilestmt
		|do_whilestmt
		|break_stmt
		|continuestmt
		|returnstmt
		|callstmt;
// assignment
assignmentstmt: lhs EQ expr SM;
//lhsprime: lhs lhsprime | lhs;
lhs: scalar_variable | index_expression;
scalar_variable: Identifiers;
index_expression: indexop;
// if statement
ifstmt: IF LB expr RB statement (false_statement)? ;
false_statement: ELSE statement;
// for statement
forstmt: FOR LB (lhs EQ init_expr CM condition_expr CM update_expr) RB statement ;
init_expr: expr;
condition_expr: expr;
update_expr: expr;
// while
whilestmt: WHILE LB expr_while RB statement;

expr_while: expr; 
//do_while
do_whilestmt: DO block WHILE LB expr_while RB SM;
// break
break_stmt: BREAK SM;
//continue
continuestmt: CONTINUE SM;
//return
returnstmt: RETURN (expr)? SM;
//call
callstmt: Identifiers LB argumentprime RB SM;
block : LCB block_stmtprime RCB;
block_stmtprime: block_stmts |;
block_stmts: block_stmt block_stmts | block_stmt;
block_stmt: vardecl | statements;
//block_stmtelement: statements | ;
statements: statement statements |statement ;


AUTO: 'auto'; 
BREAK: 'break'; 
BOOLEAN: 'boolean'; 
DO: 'do';  
ELSE: 'else' ; 
FALSE: 'false'; 
FLOAT: 'float'; 
FOR: 'for'; 
FUNCTION: 'function'; 
IF: 'if'; 
INT: 'integer'; 
RETURN: 'return'; 
STRING:'string'; 
TRUE: 'true'; 
WHILE: 'while'; 
VOID: 'void'; 
OUT: 'out'; 
CONTINUE: 'continue'; 
OF: 'of'; 
INHERIT: 'inherit'; 
ARRAY: 'array';
boolean: (TRUE | FALSE);
CommentC: '/''*' (.)*? '*''/' -> skip;
CommentCplus: '/''/' (.*?|(~'\n')*) ->skip;
// fragment Letter: [a-zA-z];
//Float: ('0'| [1-9](US?[0-9])*)(Decpart) | ('0'| [1-9](US?[0-9])*)(Decpart)?Expart;

Integer: '0'|[1-9](US?[0-9])* {self.text = self.text.replace('_','')} ;
Float: Integerpart Decimalpart Exponentpart {self.text = self.text.replace("_","")} |  Decimalpart Exponentpart {self.text = self.text.replace("_","")}| Integerpart Decimalpart {self.text = self.text.replace("_","")}| Integerpart Exponentpart {self.text = self.text.replace("_","")};
Identifiers: ([a-zA-Z]|US)([a-zA-Z0-9_])*;

fragment Digit: [0-9]+;
fragment US: '_'; //underscore
fragment Integerpart: ('0'| [1-9](US?[0-9])*) ;
fragment Decimalpart: DOT[0-9]*;
fragment Exponentpart: 'e'(ADDOP|MINUSOP)?[0-9]+|'E'(ADDOP|MINUSOP)?[0-9]+;



ADDOP: '+';
MINUSOP: '-';
MULOP: '*';
DIVOP: '/';
MODUOP: '%';
NEGATION: '!'; //exclamation mark
CONJUNCTION: '&&';
DISJUNCTION: '||';
DOUEQ: '==';
DIFF: '!=';
SMALLER: '<';
SMAEQ: '<=';
GREATER: '>';
GREEQ: '>=';
CONCAT: '::';
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
DOT: '.';
CM: ',';
SM: ';';
COLON: ':';
LCB: '{';
RCB: '}';
EQ: '=';

//Float:  ('0'| [1-9](US?[0-9])*)(Dot Digit | Dot Digit Notation Digit | Notation Digit ) {self.text = self.text.replace('_','')};
	
//fragment EscapeSequences: [\b\f\r\n\t'] ;
//fragment Escaped: '\\'[bfrt'];
String: '"'(~["EOF\\] | '\\''"' | '\\'[bfnrt'\\] )*'"' {self.text =self.text[1:-1]};



WS : [ \t\r\n\f\b]+ -> skip ; // skip spaces, tabs, newlines


//Floaterror: '.'('.')+ {raise ErrorToken ('.')};
//Interror: '0'US?([0-9])*{raise ErrorToken('0')};
ERROR_CHAR: .  {raise ErrorToken(self.text)};
UNCLOSE_STRING:  '"'(~["EOF\\] | '\\''"' |'\\'[bfnrt])* {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: '"'(~["EOF\\] | '\\''"' |'\''| '\\' )* '\\'~[bfrnt] {raise IllegalEscape(self.text[1:])};
