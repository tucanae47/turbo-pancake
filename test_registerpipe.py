# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

import random

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, FallingEdge, ClockCycles, RisingEdge
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer


@cocotb.test()
async def test_registerpipe(dut):
    """ Register pipe """

    # Create a 10us period clock on port clk
    clock = Clock(dut.clock, 2, units="us")
    cocotb.fork(clock.start())

    dut.clear <= 0
    dut.clock_enable <= 1
    val = 1
    print("{}".format(val))
    dut.pipe_in <= val
    pipe_width = 8 
    ## piper equals the number we want to pipe to the last register 
    for piper in range(9):
        print("Current piper = {} ".format(piper))
        dut.pipe_in <= piper
        for i in range(pipe_width):
            await RisingEdge(dut.clock)
        c = dut.pipe_out.value
        countb = c.binstr   
        print("Current count_binary = {} ".format(c, countb))
        dut.clear <= 1
        await RisingEdge(dut.clock)
        dut.clear <= 0
        # c = dut.pipe_out