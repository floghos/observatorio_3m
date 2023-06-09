# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2018 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.6.5
#
# <auto-generated>
#
# Generated from file `Printer.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Demo
_M_Demo = Ice.openModule('Demo')
__name__ = 'Demo'

if 'Printer' not in _M_Demo.__dict__:
    _M_Demo.Printer = Ice.createTempClass()
    class Printer(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_Demo.Printer:
                raise RuntimeError('Demo.Printer is an abstract class')

        def ice_ids(self, current=None):
            return ('::Demo::Printer', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Demo::Printer'

        def ice_staticId():
            return '::Demo::Printer'
        ice_staticId = staticmethod(ice_staticId)

        def printString(self, s, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_Printer)

        __repr__ = __str__

    _M_Demo.PrinterPrx = Ice.createTempClass()
    class PrinterPrx(Ice.ObjectPrx):

        def printString(self, s, _ctx=None):
            return _M_Demo.Printer._op_printString.invoke(self, ((s, ), _ctx))

        def begin_printString(self, s, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Demo.Printer._op_printString.begin(self, ((s, ), _response, _ex, _sent, _ctx))

        def end_printString(self, _r):
            return _M_Demo.Printer._op_printString.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Demo.PrinterPrx.ice_checkedCast(proxy, '::Demo::Printer', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Demo.PrinterPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::Demo::Printer'
        ice_staticId = staticmethod(ice_staticId)

    _M_Demo._t_PrinterPrx = IcePy.defineProxy('::Demo::Printer', PrinterPrx)

    _M_Demo._t_Printer = IcePy.defineClass('::Demo::Printer', Printer, -1, (), True, False, None, (), ())
    Printer._ice_type = _M_Demo._t_Printer

    Printer._op_printString = IcePy.Operation('printString', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())

    _M_Demo.Printer = Printer
    del Printer

    _M_Demo.PrinterPrx = PrinterPrx
    del PrinterPrx

# End of module Demo
