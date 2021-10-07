# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

import random

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, FallingEdge, ClockCycles, RisingEdge
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer


@cocotb.test()
async def test_countbin(dut):
    """ Count Bin """

    # Create a 10us period clock on port clk
    clock = Clock(dut.clock, 2, units="us")
    cocotb.fork(clock.start())

    dut.clear <= 1
    dut.up_down <= 0
    dut.run <= 1
    dut.load <= 0
    dut.load_count <= 0
    dut.carry_in <= 0
    await RisingEdge(dut.clock)

    dut.clear <= 0
    count = 0
    # count = dut.count.value.get_value()
    # print("Current count = {}".format(count))
    for i in range(30):
        # count = dut.count.value.get_value()
        c = dut.count.value
        countb = c.binstr   
        count = c.integer
        carry = dut.carry_out.value.integer
        carries = dut.carries.value.integer 
        overflow = dut.overflow.value.integer 

        print("Current count_binary = {} , {}".format(countb, count))
        await RisingEdge(dut.clock)
        # await ClockCycles(dut.clock, 1)
