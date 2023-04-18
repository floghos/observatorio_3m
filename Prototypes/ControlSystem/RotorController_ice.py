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
# Generated from file `RotorController.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module RotorModule
_M_RotorModule = Ice.openModule('RotorModule')
__name__ = 'RotorModule'

if 'Rotor' not in _M_RotorModule.__dict__:
    _M_RotorModule.Rotor = Ice.createTempClass()
    class Rotor(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_RotorModule.Rotor:
                raise RuntimeError('RotorModule.Rotor is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::RotorModule::Rotor')

        def ice_id(self, current=None):
            return '::RotorModule::Rotor'

        def ice_staticId():
            return '::RotorModule::Rotor'
        ice_staticId = staticmethod(ice_staticId)

        def gotoAltAzi(self, alt, azi, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_RotorModule._t_Rotor)

        __repr__ = __str__

    _M_RotorModule.RotorPrx = Ice.createTempClass()
    class RotorPrx(Ice.ObjectPrx):

        def gotoAltAzi(self, alt, azi, _ctx=None):
            return _M_RotorModule.Rotor._op_gotoAltAzi.invoke(self, ((alt, azi), _ctx))

        def begin_gotoAltAzi(self, alt, azi, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_RotorModule.Rotor._op_gotoAltAzi.begin(self, ((alt, azi), _response, _ex, _sent, _ctx))

        def end_gotoAltAzi(self, _r):
            return _M_RotorModule.Rotor._op_gotoAltAzi.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_RotorModule.RotorPrx.ice_checkedCast(proxy, '::RotorModule::Rotor', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_RotorModule.RotorPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::RotorModule::Rotor'
        ice_staticId = staticmethod(ice_staticId)

    _M_RotorModule._t_RotorPrx = IcePy.defineProxy('::RotorModule::Rotor', RotorPrx)

    _M_RotorModule._t_Rotor = IcePy.defineClass('::RotorModule::Rotor', Rotor, -1, (), True, False, None, (), ())
    Rotor._ice_type = _M_RotorModule._t_Rotor

    Rotor._op_gotoAltAzi = IcePy.Operation('gotoAltAzi', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_float, False, 0), ((), IcePy._t_float, False, 0)), (), None, ())

    _M_RotorModule.Rotor = Rotor
    del Rotor

    _M_RotorModule.RotorPrx = RotorPrx
    del RotorPrx

# End of module RotorModule
