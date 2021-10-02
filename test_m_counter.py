# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

import numpy as np
import random

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, FallingEdge, ClockCycles
from cocotb.binary import BinaryValue

@cocotb.test()
async def test_m_counter(dut):
    """ Mod counter """
    # Create a 10us period clock on port clk
    clock = Clock(dut.clk, 20, units="us")
    cocotb.fork(clock.start())

    # Reset system
    await FallingEdge(dut.clk)
    dut.reset <= 1
    await ClockCycles(dut.clk, 1)
    dut.reset <= 0
    await ClockCycles(dut.clk, 1)
    for i in range(19):
        observed = dut.count.value.get_value()
        expected = i % 5 
        print("expected = {}, observed = {}".format(expected, observed))
        assert observed == expected,\
                   "expected = %x, observed = %x" % (expected, observed)
        await ClockCycles(dut.clk, 1)
        # await FallingEdge(dut.clk)