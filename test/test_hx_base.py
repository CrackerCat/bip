import sys

from ida_hexrays import *
from idaapi import ctree_visitor_t, CV_FAST, CV_PARENTS
from bip.hexrays import *
from bip.hexrays.cnode import *
from bip.base import *
# TODO make this compatible with pytest

# TODO: add test that ``HxCFunc.from_addr().lvars[0]._lvar.set_lvar_type(BipType.FromC("void *").pointed._get_tinfo_copy(), True)`` raise indeed a RuntimeError

## OLD
#class visit(ctree_visitor_t):
#
#    def __init__(self, func):
#        ctree_visitor_t.__init__(self, CV_FAST)
#        #ctree_visitor_t.__init__(self, CV_PARENTS)
#	self.func = func
#
#    def visit_expr(self, i):
#        print(GetHxCItem(i))
#	return 0
#
#    def visit_insn(self, i):
#        print(GetHxCItem(i))
#        return 0
#
#def test_visit00():
#    f = decompile(0x01800D2FF0)
#    visit(f).apply_to(f.body, None)


# this 

def pr(e):
    print(e)

# visit all statement and expression for all functions and print them.
# not included in the test because way too long
def visit_all_function00():
    for f in BipFunction.iter_all():
        try:
            f.hxfunc.hx_visit_all(pr)
        except BipDecompileError: # ida hexrays error
            pass # we ignore it

def visit_all_function01():
    for f in BipFunction.iter_all():
        try:
            f.hxfunc.visit_cnode(pr)
        except BipDecompileError: # ida hexrays error
            pass # we ignore it

# TODO: should make all those test with verification that the class is well
#   received & maybe more precise test ?
def test_hx_visitor00():
    hxf = HxCFunc.from_addr(0x01800D2FF0)
    hxf.hx_visit_list_expr([HxCExprCall], pr)

def test_hx_visitor01():
    hxf = HxCFunc.from_addr(0x01800D2FF0)
    hxf.hx_visit_expr(pr)

def test_hx_visitor02():
    hxf = HxCFunc.from_addr(0x01800D2FF0)
    hxf.hx_visit_stmt(pr)

def test_hx_visitor03():
    hxf = HxCFunc.from_addr(0x01800D2FF0)
    hxf.hx_visit_list_stmt([HxCStmtExpr], pr)

def test_hx_visitor04():
    hxf = HxCFunc.from_addr(0x01800D2FF0)
    hxf.hx_visit_all(pr)

def test_hx_visitor05():
    hxf = HxCFunc.from_addr(0x01800D2FF0)
    hxf.hx_visit_list_all([HxCExprCall, HxCStmtExpr], pr)

def text_hx_visitor06(): # test for the casm
    hxf = HxCFunc.from_addr(0x01800024A8)
    hxf.hx_visit_all(pr)

def test_cnode_visitor00():
    hxf = HxCFunc.from_addr(0x01800D2FF0)
    hxf.visit_cnode(pr)

def test_cnode_visitor01():
    hxf = HxCFunc.from_addr(0x0180002524)
    hxf.visit_cnode(pr)

def test_cnode_visitor02():
    hxf = HxCFunc.from_addr(0x01800D2FF0)
    hxf.visit_cnode_filterlist(pr, [CNodeStmtExpr])

def test_cnode_visitor03():
    hxf = HxCFunc.from_addr(0x01800D2FF0)
    hxf.visit_cnode_filterlist(pr, [CNodeExprCall])

def test_cnode_visitor04():
    hxf = HxCFunc.from_addr(0x01800D2FF0)
    hxf.visit_cnode_filterlist(pr, [CNodeExprCall, CNodeStmtExpr])





