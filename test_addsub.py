# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

import random

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, FallingEdge, ClockCycles
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer


@cocotb.test()
async def test_addsub(dut):
    """ Add Sub Bin """
    dut.add_sub = 0
    # dut.carry_in = 1
    # dut.A        = 1
    # dut.B        = 1

    await Timer(2, units='ns')
    # sel = np.dtype('int32').type(1)
    # print("selector  = {}".format(sel)f
    for i in range(18):
        # a = i
        # b = i
        dut.carry_in = 0
        dut.A        = i
        dut.B        = i
        await Timer(1, units='ns')
        s = dut.sum.value
        sumb = s.binstr   
        sum = s.integer
        carry = dut.carry_out.value.integer
        carries = dut.carries.value.integer 
        overflow = dut.overflow.value.integer 
        print("AB = {}, observed = {}, expected = {}".format(i, sum, i + i))
        print("bin AB = {}, observed = {}, expected = {}".format( f"{i:05b}" , sumb, f"{(i + i):05b}"))
        print("carry = {}, overflow = {}, carries = {}\n\n".format(carry, overflow, carries))