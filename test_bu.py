# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0
# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles, with_timeout
import random

async def RST(dut):
    dut.rst  <= 1

    #await RisingEdge(dut.clk)
    await ClockCycles(dut.clk, 2)
    dut.rst <= 0;
    #await RisingEdge(dut.clk)
    await ClockCycles(dut.clk, 2)

@cocotb.test()
async def test_bu(dut):
    """Test for adding 2 random numbers multiple times"""
    clock = Clock(dut.clk, 10, units="ps")
    cocotb.fork(clock.start())

    # dut.height <= 0b101
    # dut.height <= 0b000
    dut.w_input <= 0b0001100
    # dut.img <= [0b1011110, 0b1000000,0b1010010,0b0001110,0b1011111,0b1001111,0b1001010]
    #packed array
    dut.img <= 0b1011110100000010100100001110101111110011111001010
    dut.opcode <= 0b00000
    await RST(dut)
    
    # await ClockCycles(dut.clk, 1)
    dut.w_en <= 1 
    dut.opcode <= 0b00001
    await ClockCycles(dut.clk, 8)

    dut.w_en <= 0
    dut.opcode <= 0b00000
    await RisingEdge(dut.clk)

    dut.opcode <= 0b10000
    await RisingEdge(dut.clk)
    
    # seelect LUTS    
    dut.opcode <= 0b10010 #opcode= 1;
    await RisingEdge(dut.clk)

    popcount = dut.popcnt_add.value
    binpc = popcount.binstr   
    print("Popcount {} bin{}".format(popcount, binpc))

    dut.opcode <= 0b10100 #opcode= 2;
    await RisingEdge(dut.clk)

    popcount = dut.popcnt_add.value
    binpc = popcount.binstr   
    print("Popcount {} bin{}".format(popcount, binpc))

    dut.opcode <= 0b10110 #opcode= 3;
    await RisingEdge(dut.clk)

    popcount = dut.popcnt_add.value
    binpc = popcount.binstr   
    print("Popcount {} bin{}".format(popcount, binpc))

    dut.opcode <= 0b11000 #opcode= 4;
    await RisingEdge(dut.clk)

    popcount = dut.popcnt_add.value
    binpc = popcount.binstr   
    print("Popcount {} bin{}".format(popcount, binpc))

    dut.opcode <= 0b11010 #opcode= 5;
    await RisingEdge(dut.clk)

    popcount = dut.popcnt_add.value
    binpc = popcount.binstr   
    print("Popcount {} bin{}".format(popcount, binpc))

    dut.opcode <= 0b11100 #opcode= 6;
    await RisingEdge(dut.clk)

    popcount = dut.popcnt_add.value
    binpc = popcount.binstr   
    print("Popcount {} bin{}".format(popcount, binpc))

    dut.opcode <= 0b11110 #opcode= 7;
    await RisingEdge(dut.clk)

    popcount = dut.popcnt_add.value
    binpc = popcount.binstr   
    print("Popcount {} bin{}".format(popcount, binpc))
    
    dut.opcode <= 0b00000 #opcode= 7;

    await ClockCycles(dut.clk, 5)
      
    # for i in range(50):
    #     popcount = dut.popcnt_add.value
    #     binpc = popcount.binstr   
    #     print("Popcount {} bin{}".format(popcount, binpc))
    #     await RisingEdge(dut.clk)
