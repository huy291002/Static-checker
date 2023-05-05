# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01e3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\7\27")
        buf.write("\u00fe\n\27\f\27\16\27\u0101\13\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\7\30\u010b\n\30\f\30\16\30\u010e")
        buf.write("\13\30\3\30\7\30\u0111\n\30\f\30\16\30\u0114\13\30\5\30")
        buf.write("\u0116\n\30\3\30\3\30\3\31\3\31\3\31\5\31\u011d\n\31\3")
        buf.write("\31\7\31\u0120\n\31\f\31\16\31\u0123\13\31\3\31\5\31\u0126")
        buf.write("\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0139\n\32\3")
        buf.write("\33\3\33\5\33\u013d\n\33\3\33\7\33\u0140\n\33\f\33\16")
        buf.write("\33\u0143\13\33\3\34\6\34\u0146\n\34\r\34\16\34\u0147")
        buf.write("\3\35\3\35\3\36\3\36\3\36\5\36\u014f\n\36\3\36\7\36\u0152")
        buf.write("\n\36\f\36\16\36\u0155\13\36\5\36\u0157\n\36\3\37\3\37")
        buf.write("\7\37\u015b\n\37\f\37\16\37\u015e\13\37\3 \3 \3 \5 \u0163")
        buf.write("\n \3 \6 \u0166\n \r \16 \u0167\3 \3 \3 \5 \u016d\n \3")
        buf.write(" \6 \u0170\n \r \16 \u0171\5 \u0174\n \3!\3!\3\"\3\"\3")
        buf.write("#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3")
        buf.write("*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3;\3;\3;")
        buf.write("\3;\7;\u01b7\n;\f;\16;\u01ba\13;\3;\3;\3;\3<\6<\u01c0")
        buf.write("\n<\r<\16<\u01c1\3<\3<\3=\3=\3=\3>\3>\3>\3>\3>\3>\7>\u01cf")
        buf.write("\n>\f>\16>\u01d2\13>\3>\3>\3?\3?\3?\3?\3?\7?\u01db\n?")
        buf.write("\f?\16?\u01de\13?\3?\3?\3?\3?\4\u00ff\u010c\2@\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\29\2;\2=\2?\2A\35C\36E\37G I!K\"M#O$Q%S&")
        buf.write("U\'W(Y)[*]+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66u\67w8")
        buf.write("y9{:};\3\2\f\3\2\f\f\3\2\63;\3\2\62;\4\2C\\c|\6\2\62;")
        buf.write("C\\aac|\6\2$$GHQQ^^\t\2))^^ddhhppttvv\5\2\n\f\16\17\"")
        buf.write("\"\7\2ddhhppttvv\4\2))^^\2\u01ff\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\3\177")
        buf.write("\3\2\2\2\5\u0084\3\2\2\2\7\u008a\3\2\2\2\t\u0092\3\2\2")
        buf.write("\2\13\u0095\3\2\2\2\r\u009a\3\2\2\2\17\u00a0\3\2\2\2\21")
        buf.write("\u00a6\3\2\2\2\23\u00aa\3\2\2\2\25\u00b3\3\2\2\2\27\u00b6")
        buf.write("\3\2\2\2\31\u00be\3\2\2\2\33\u00c5\3\2\2\2\35\u00cc\3")
        buf.write("\2\2\2\37\u00d1\3\2\2\2!\u00d7\3\2\2\2#\u00dc\3\2\2\2")
        buf.write("%\u00e0\3\2\2\2\'\u00e9\3\2\2\2)\u00ec\3\2\2\2+\u00f4")
        buf.write("\3\2\2\2-\u00fa\3\2\2\2/\u0107\3\2\2\2\61\u0125\3\2\2")
        buf.write("\2\63\u0138\3\2\2\2\65\u013c\3\2\2\2\67\u0145\3\2\2\2")
        buf.write("9\u0149\3\2\2\2;\u0156\3\2\2\2=\u0158\3\2\2\2?\u0173\3")
        buf.write("\2\2\2A\u0175\3\2\2\2C\u0177\3\2\2\2E\u0179\3\2\2\2G\u017b")
        buf.write("\3\2\2\2I\u017d\3\2\2\2K\u017f\3\2\2\2M\u0181\3\2\2\2")
        buf.write("O\u0184\3\2\2\2Q\u0187\3\2\2\2S\u018a\3\2\2\2U\u018d\3")
        buf.write("\2\2\2W\u018f\3\2\2\2Y\u0192\3\2\2\2[\u0194\3\2\2\2]\u0197")
        buf.write("\3\2\2\2_\u019a\3\2\2\2a\u019c\3\2\2\2c\u019e\3\2\2\2")
        buf.write("e\u01a0\3\2\2\2g\u01a2\3\2\2\2i\u01a4\3\2\2\2k\u01a6\3")
        buf.write("\2\2\2m\u01a8\3\2\2\2o\u01aa\3\2\2\2q\u01ac\3\2\2\2s\u01ae")
        buf.write("\3\2\2\2u\u01b0\3\2\2\2w\u01bf\3\2\2\2y\u01c5\3\2\2\2")
        buf.write("{\u01c8\3\2\2\2}\u01d5\3\2\2\2\177\u0080\7c\2\2\u0080")
        buf.write("\u0081\7w\2\2\u0081\u0082\7v\2\2\u0082\u0083\7q\2\2\u0083")
        buf.write("\4\3\2\2\2\u0084\u0085\7d\2\2\u0085\u0086\7t\2\2\u0086")
        buf.write("\u0087\7g\2\2\u0087\u0088\7c\2\2\u0088\u0089\7m\2\2\u0089")
        buf.write("\6\3\2\2\2\u008a\u008b\7d\2\2\u008b\u008c\7q\2\2\u008c")
        buf.write("\u008d\7q\2\2\u008d\u008e\7n\2\2\u008e\u008f\7g\2\2\u008f")
        buf.write("\u0090\7c\2\2\u0090\u0091\7p\2\2\u0091\b\3\2\2\2\u0092")
        buf.write("\u0093\7f\2\2\u0093\u0094\7q\2\2\u0094\n\3\2\2\2\u0095")
        buf.write("\u0096\7g\2\2\u0096\u0097\7n\2\2\u0097\u0098\7u\2\2\u0098")
        buf.write("\u0099\7g\2\2\u0099\f\3\2\2\2\u009a\u009b\7h\2\2\u009b")
        buf.write("\u009c\7c\2\2\u009c\u009d\7n\2\2\u009d\u009e\7u\2\2\u009e")
        buf.write("\u009f\7g\2\2\u009f\16\3\2\2\2\u00a0\u00a1\7h\2\2\u00a1")
        buf.write("\u00a2\7n\2\2\u00a2\u00a3\7q\2\2\u00a3\u00a4\7c\2\2\u00a4")
        buf.write("\u00a5\7v\2\2\u00a5\20\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7")
        buf.write("\u00a8\7q\2\2\u00a8\u00a9\7t\2\2\u00a9\22\3\2\2\2\u00aa")
        buf.write("\u00ab\7h\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad\7p\2\2\u00ad")
        buf.write("\u00ae\7e\2\2\u00ae\u00af\7v\2\2\u00af\u00b0\7k\2\2\u00b0")
        buf.write("\u00b1\7q\2\2\u00b1\u00b2\7p\2\2\u00b2\24\3\2\2\2\u00b3")
        buf.write("\u00b4\7k\2\2\u00b4\u00b5\7h\2\2\u00b5\26\3\2\2\2\u00b6")
        buf.write("\u00b7\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7v\2\2\u00b9")
        buf.write("\u00ba\7g\2\2\u00ba\u00bb\7i\2\2\u00bb\u00bc\7g\2\2\u00bc")
        buf.write("\u00bd\7t\2\2\u00bd\30\3\2\2\2\u00be\u00bf\7t\2\2\u00bf")
        buf.write("\u00c0\7g\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7w\2\2\u00c2")
        buf.write("\u00c3\7t\2\2\u00c3\u00c4\7p\2\2\u00c4\32\3\2\2\2\u00c5")
        buf.write("\u00c6\7u\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8\7t\2\2\u00c8")
        buf.write("\u00c9\7k\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb\7i\2\2\u00cb")
        buf.write("\34\3\2\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7t\2\2\u00ce")
        buf.write("\u00cf\7w\2\2\u00cf\u00d0\7g\2\2\u00d0\36\3\2\2\2\u00d1")
        buf.write("\u00d2\7y\2\2\u00d2\u00d3\7j\2\2\u00d3\u00d4\7k\2\2\u00d4")
        buf.write("\u00d5\7n\2\2\u00d5\u00d6\7g\2\2\u00d6 \3\2\2\2\u00d7")
        buf.write("\u00d8\7x\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7k\2\2\u00da")
        buf.write("\u00db\7f\2\2\u00db\"\3\2\2\2\u00dc\u00dd\7q\2\2\u00dd")
        buf.write("\u00de\7w\2\2\u00de\u00df\7v\2\2\u00df$\3\2\2\2\u00e0")
        buf.write("\u00e1\7e\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3\7p\2\2\u00e3")
        buf.write("\u00e4\7v\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6\7p\2\2\u00e6")
        buf.write("\u00e7\7w\2\2\u00e7\u00e8\7g\2\2\u00e8&\3\2\2\2\u00e9")
        buf.write("\u00ea\7q\2\2\u00ea\u00eb\7h\2\2\u00eb(\3\2\2\2\u00ec")
        buf.write("\u00ed\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7j\2\2\u00ef")
        buf.write("\u00f0\7g\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7k\2\2\u00f2")
        buf.write("\u00f3\7v\2\2\u00f3*\3\2\2\2\u00f4\u00f5\7c\2\2\u00f5")
        buf.write("\u00f6\7t\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8\7c\2\2\u00f8")
        buf.write("\u00f9\7{\2\2\u00f9,\3\2\2\2\u00fa\u00fb\7\61\2\2\u00fb")
        buf.write("\u00ff\7,\2\2\u00fc\u00fe\13\2\2\2\u00fd\u00fc\3\2\2\2")
        buf.write("\u00fe\u0101\3\2\2\2\u00ff\u0100\3\2\2\2\u00ff\u00fd\3")
        buf.write("\2\2\2\u0100\u0102\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0103")
        buf.write("\7,\2\2\u0103\u0104\7\61\2\2\u0104\u0105\3\2\2\2\u0105")
        buf.write("\u0106\b\27\2\2\u0106.\3\2\2\2\u0107\u0108\7\61\2\2\u0108")
        buf.write("\u0115\7\61\2\2\u0109\u010b\13\2\2\2\u010a\u0109\3\2\2")
        buf.write("\2\u010b\u010e\3\2\2\2\u010c\u010d\3\2\2\2\u010c\u010a")
        buf.write("\3\2\2\2\u010d\u0116\3\2\2\2\u010e\u010c\3\2\2\2\u010f")
        buf.write("\u0111\n\2\2\2\u0110\u010f\3\2\2\2\u0111\u0114\3\2\2\2")
        buf.write("\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0116\3")
        buf.write("\2\2\2\u0114\u0112\3\2\2\2\u0115\u010c\3\2\2\2\u0115\u0112")
        buf.write("\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\b\30\2\2\u0118")
        buf.write("\60\3\2\2\2\u0119\u0126\7\62\2\2\u011a\u0121\t\3\2\2\u011b")
        buf.write("\u011d\59\35\2\u011c\u011b\3\2\2\2\u011c\u011d\3\2\2\2")
        buf.write("\u011d\u011e\3\2\2\2\u011e\u0120\t\4\2\2\u011f\u011c\3")
        buf.write("\2\2\2\u0120\u0123\3\2\2\2\u0121\u011f\3\2\2\2\u0121\u0122")
        buf.write("\3\2\2\2\u0122\u0124\3\2\2\2\u0123\u0121\3\2\2\2\u0124")
        buf.write("\u0126\b\31\3\2\u0125\u0119\3\2\2\2\u0125\u011a\3\2\2")
        buf.write("\2\u0126\62\3\2\2\2\u0127\u0128\5;\36\2\u0128\u0129\5")
        buf.write("=\37\2\u0129\u012a\5? \2\u012a\u012b\b\32\4\2\u012b\u0139")
        buf.write("\3\2\2\2\u012c\u012d\5=\37\2\u012d\u012e\5? \2\u012e\u012f")
        buf.write("\b\32\5\2\u012f\u0139\3\2\2\2\u0130\u0131\5;\36\2\u0131")
        buf.write("\u0132\5=\37\2\u0132\u0133\b\32\6\2\u0133\u0139\3\2\2")
        buf.write("\2\u0134\u0135\5;\36\2\u0135\u0136\5? \2\u0136\u0137\b")
        buf.write("\32\7\2\u0137\u0139\3\2\2\2\u0138\u0127\3\2\2\2\u0138")
        buf.write("\u012c\3\2\2\2\u0138\u0130\3\2\2\2\u0138\u0134\3\2\2\2")
        buf.write("\u0139\64\3\2\2\2\u013a\u013d\t\5\2\2\u013b\u013d\59\35")
        buf.write("\2\u013c\u013a\3\2\2\2\u013c\u013b\3\2\2\2\u013d\u0141")
        buf.write("\3\2\2\2\u013e\u0140\t\6\2\2\u013f\u013e\3\2\2\2\u0140")
        buf.write("\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2")
        buf.write("\u0142\66\3\2\2\2\u0143\u0141\3\2\2\2\u0144\u0146\t\4")
        buf.write("\2\2\u0145\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0145")
        buf.write("\3\2\2\2\u0147\u0148\3\2\2\2\u01488\3\2\2\2\u0149\u014a")
        buf.write("\7a\2\2\u014a:\3\2\2\2\u014b\u0157\7\62\2\2\u014c\u0153")
        buf.write("\t\3\2\2\u014d\u014f\59\35\2\u014e\u014d\3\2\2\2\u014e")
        buf.write("\u014f\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0152\t\4\2\2")
        buf.write("\u0151\u014e\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3")
        buf.write("\2\2\2\u0153\u0154\3\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153")
        buf.write("\3\2\2\2\u0156\u014b\3\2\2\2\u0156\u014c\3\2\2\2\u0157")
        buf.write("<\3\2\2\2\u0158\u015c\5g\64\2\u0159\u015b\t\4\2\2\u015a")
        buf.write("\u0159\3\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3\2\2\2")
        buf.write("\u015c\u015d\3\2\2\2\u015d>\3\2\2\2\u015e\u015c\3\2\2")
        buf.write("\2\u015f\u0162\7g\2\2\u0160\u0163\5A!\2\u0161\u0163\5")
        buf.write("C\"\2\u0162\u0160\3\2\2\2\u0162\u0161\3\2\2\2\u0162\u0163")
        buf.write("\3\2\2\2\u0163\u0165\3\2\2\2\u0164\u0166\t\4\2\2\u0165")
        buf.write("\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0165\3\2\2\2")
        buf.write("\u0167\u0168\3\2\2\2\u0168\u0174\3\2\2\2\u0169\u016c\7")
        buf.write("G\2\2\u016a\u016d\5A!\2\u016b\u016d\5C\"\2\u016c\u016a")
        buf.write("\3\2\2\2\u016c\u016b\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("\u016f\3\2\2\2\u016e\u0170\t\4\2\2\u016f\u016e\3\2\2\2")
        buf.write("\u0170\u0171\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3")
        buf.write("\2\2\2\u0172\u0174\3\2\2\2\u0173\u015f\3\2\2\2\u0173\u0169")
        buf.write("\3\2\2\2\u0174@\3\2\2\2\u0175\u0176\7-\2\2\u0176B\3\2")
        buf.write("\2\2\u0177\u0178\7/\2\2\u0178D\3\2\2\2\u0179\u017a\7,")
        buf.write("\2\2\u017aF\3\2\2\2\u017b\u017c\7\61\2\2\u017cH\3\2\2")
        buf.write("\2\u017d\u017e\7\'\2\2\u017eJ\3\2\2\2\u017f\u0180\7#\2")
        buf.write("\2\u0180L\3\2\2\2\u0181\u0182\7(\2\2\u0182\u0183\7(\2")
        buf.write("\2\u0183N\3\2\2\2\u0184\u0185\7~\2\2\u0185\u0186\7~\2")
        buf.write("\2\u0186P\3\2\2\2\u0187\u0188\7?\2\2\u0188\u0189\7?\2")
        buf.write("\2\u0189R\3\2\2\2\u018a\u018b\7#\2\2\u018b\u018c\7?\2")
        buf.write("\2\u018cT\3\2\2\2\u018d\u018e\7>\2\2\u018eV\3\2\2\2\u018f")
        buf.write("\u0190\7>\2\2\u0190\u0191\7?\2\2\u0191X\3\2\2\2\u0192")
        buf.write("\u0193\7@\2\2\u0193Z\3\2\2\2\u0194\u0195\7@\2\2\u0195")
        buf.write("\u0196\7?\2\2\u0196\\\3\2\2\2\u0197\u0198\7<\2\2\u0198")
        buf.write("\u0199\7<\2\2\u0199^\3\2\2\2\u019a\u019b\7*\2\2\u019b")
        buf.write("`\3\2\2\2\u019c\u019d\7+\2\2\u019db\3\2\2\2\u019e\u019f")
        buf.write("\7]\2\2\u019fd\3\2\2\2\u01a0\u01a1\7_\2\2\u01a1f\3\2\2")
        buf.write("\2\u01a2\u01a3\7\60\2\2\u01a3h\3\2\2\2\u01a4\u01a5\7.")
        buf.write("\2\2\u01a5j\3\2\2\2\u01a6\u01a7\7=\2\2\u01a7l\3\2\2\2")
        buf.write("\u01a8\u01a9\7<\2\2\u01a9n\3\2\2\2\u01aa\u01ab\7}\2\2")
        buf.write("\u01abp\3\2\2\2\u01ac\u01ad\7\177\2\2\u01adr\3\2\2\2\u01ae")
        buf.write("\u01af\7?\2\2\u01aft\3\2\2\2\u01b0\u01b8\7$\2\2\u01b1")
        buf.write("\u01b7\n\7\2\2\u01b2\u01b3\7^\2\2\u01b3\u01b7\7$\2\2\u01b4")
        buf.write("\u01b5\7^\2\2\u01b5\u01b7\t\b\2\2\u01b6\u01b1\3\2\2\2")
        buf.write("\u01b6\u01b2\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01ba\3")
        buf.write("\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bb")
        buf.write("\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb\u01bc\7$\2\2\u01bc")
        buf.write("\u01bd\b;\b\2\u01bdv\3\2\2\2\u01be\u01c0\t\t\2\2\u01bf")
        buf.write("\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01bf\3\2\2\2")
        buf.write("\u01c1\u01c2\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c4\b")
        buf.write("<\2\2\u01c4x\3\2\2\2\u01c5\u01c6\13\2\2\2\u01c6\u01c7")
        buf.write("\b=\t\2\u01c7z\3\2\2\2\u01c8\u01d0\7$\2\2\u01c9\u01cf")
        buf.write("\n\7\2\2\u01ca\u01cb\7^\2\2\u01cb\u01cf\7$\2\2\u01cc\u01cd")
        buf.write("\7^\2\2\u01cd\u01cf\t\n\2\2\u01ce\u01c9\3\2\2\2\u01ce")
        buf.write("\u01ca\3\2\2\2\u01ce\u01cc\3\2\2\2\u01cf\u01d2\3\2\2\2")
        buf.write("\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d3\3")
        buf.write("\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d4\b>\n\2\u01d4|\3")
        buf.write("\2\2\2\u01d5\u01dc\7$\2\2\u01d6\u01db\n\7\2\2\u01d7\u01d8")
        buf.write("\7^\2\2\u01d8\u01db\7$\2\2\u01d9\u01db\t\13\2\2\u01da")
        buf.write("\u01d6\3\2\2\2\u01da\u01d7\3\2\2\2\u01da\u01d9\3\2\2\2")
        buf.write("\u01db\u01de\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01dd\3")
        buf.write("\2\2\2\u01dd\u01df\3\2\2\2\u01de\u01dc\3\2\2\2\u01df\u01e0")
        buf.write("\7^\2\2\u01e0\u01e1\n\n\2\2\u01e1\u01e2\b?\13\2\u01e2")
        buf.write("~\3\2\2\2\36\2\u00ff\u010c\u0112\u0115\u011c\u0121\u0125")
        buf.write("\u0138\u013c\u0141\u0147\u014e\u0153\u0156\u015c\u0162")
        buf.write("\u0167\u016c\u0171\u0173\u01b6\u01b8\u01c1\u01ce\u01d0")
        buf.write("\u01da\u01dc\f\b\2\2\3\31\2\3\32\3\3\32\4\3\32\5\3\32")
        buf.write("\6\3;\7\3=\b\3>\t\3?\n")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    ELSE = 5
    FALSE = 6
    FLOAT = 7
    FOR = 8
    FUNCTION = 9
    IF = 10
    INT = 11
    RETURN = 12
    STRING = 13
    TRUE = 14
    WHILE = 15
    VOID = 16
    OUT = 17
    CONTINUE = 18
    OF = 19
    INHERIT = 20
    ARRAY = 21
    CommentC = 22
    CommentCplus = 23
    Integer = 24
    Float = 25
    Identifiers = 26
    ADDOP = 27
    MINUSOP = 28
    MULOP = 29
    DIVOP = 30
    MODUOP = 31
    NEGATION = 32
    CONJUNCTION = 33
    DISJUNCTION = 34
    DOUEQ = 35
    DIFF = 36
    SMALLER = 37
    SMAEQ = 38
    GREATER = 39
    GREEQ = 40
    CONCAT = 41
    LB = 42
    RB = 43
    LSB = 44
    RSB = 45
    DOT = 46
    CM = 47
    SM = 48
    COLON = 49
    LCB = 50
    RCB = 51
    EQ = 52
    String = 53
    WS = 54
    ERROR_CHAR = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'.'", "','", 
            "';'", "':'", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INT", "RETURN", "STRING", "TRUE", 
            "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "CommentC", "CommentCplus", "Integer", "Float", "Identifiers", 
            "ADDOP", "MINUSOP", "MULOP", "DIVOP", "MODUOP", "NEGATION", 
            "CONJUNCTION", "DISJUNCTION", "DOUEQ", "DIFF", "SMALLER", "SMAEQ", 
            "GREATER", "GREEQ", "CONCAT", "LB", "RB", "LSB", "RSB", "DOT", 
            "CM", "SM", "COLON", "LCB", "RCB", "EQ", "String", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INT", "RETURN", "STRING", "TRUE", 
                  "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                  "CommentC", "CommentCplus", "Integer", "Float", "Identifiers", 
                  "Digit", "US", "Integerpart", "Decimalpart", "Exponentpart", 
                  "ADDOP", "MINUSOP", "MULOP", "DIVOP", "MODUOP", "NEGATION", 
                  "CONJUNCTION", "DISJUNCTION", "DOUEQ", "DIFF", "SMALLER", 
                  "SMAEQ", "GREATER", "GREEQ", "CONCAT", "LB", "RB", "LSB", 
                  "RSB", "DOT", "CM", "SM", "COLON", "LCB", "RCB", "EQ", 
                  "String", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[23] = self.Integer_action 
            actions[24] = self.Float_action 
            actions[57] = self.String_action 
            actions[59] = self.ERROR_CHAR_action 
            actions[60] = self.UNCLOSE_STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def Integer_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def Float_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

        if actionIndex == 2:
            self.text = self.text.replace("_","")
     

        if actionIndex == 3:
            self.text = self.text.replace("_","")
     

        if actionIndex == 4:
            self.text = self.text.replace("_","")
     

    def String_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.text =self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
            raise IllegalEscape(self.text[1:])
     


