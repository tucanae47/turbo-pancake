# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0
# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles, with_timeout, ReadOnly
import random


async def  write_ram(dut, address, value):
    await RisingEdge(dut.clk)              # Synchronise to the read clock
    dut.we = 1
    dut.addr_w = address
    dut.data_in = value
    await RisingEdge(dut.clk)              # Wait 1 clock cycle
    dut.we  = 0                        # Disable write

async def read_ram(dut, address):
    await RisingEdge(dut.clk)               # Synchronise to the read clock
    dut.addr_r = address                   # Drive the value onto the signal
    await RisingEdge(dut.clk)               # Wait for 1 clock cycle

async def RST(dut):
    dut.rst  <= 1
    await ClockCycles(dut.clk, 2)
    dut.rst <= 0;
    await ClockCycles(dut.clk, 2)

@cocotb.test()
async def test_top(dut):
    """Test reading data from RAM"""
    clock = Clock(dut.clk, 10, units="ps")
    cocotb.fork(clock.start())
    ram_data = 0b10111101000000101001000011101011111100111110010101100011 
    ram_addr = 0

    dut.c_rst <= 0;
    await write_ram(dut, ram_addr, ram_data)
    await read_ram(dut, ram_addr)

    # dut.opcode <= 0b00000
    await RST(dut)
    
    # await ClockCycles(dut.clk, 1)
    dut.w_en <= 1 
    dut.c_rst <= 1
    # dut.opcode <= 0b00001
    await ClockCycles(dut.clk, 8)

    dut.w_en <= 0
    # dut.opcode <= 0b00000
    await RisingEdge(dut.clk)

    # dut.opcode <= 0b10000
    await RisingEdge(dut.clk)
    
    # seelect LUTS    
    # dut.opcode <= 0b10010 #opcode= 1;
    await RisingEdge(dut.clk)

    popcount = dut.be_out.value
    binpc = popcount.binstr   
    print("Popcount {} bin{}".format(popcount, binpc))

    # dut.opcode <= 0b10100 #opcode= 2;
    await RisingEdge(dut.clk)

    popcount = dut.be_out.value
    binpc = popcount.binstr   
    print("Popcount {} bin{}".format(popcount, binpc))

    # dut.opcode <= 0b10110 #opcode= 3;
    await RisingEdge(dut.clk)

    popcount = dut.be_out.value
    binpc = popcount.binstr   
    print("Popcount {} bin{}".format(popcount, binpc))

    # dut.opcode <= 0b11000 #opcode= 4;
    await RisingEdge(dut.clk)

    popcount = dut.be_out.value
    binpc = popcount.binstr   
    print("Popcount {} bin{}".format(popcount, binpc))

    # dut.opcode <= 0b11010 #opcode= 5;
    await RisingEdge(dut.clk)

    popcount = dut.be_out.value
    binpc = popcount.binstr   
    print("Popcount {} bin{}".format(popcount, binpc))

    # dut.opcode <= 0b11100 #opcode= 6;
    await RisingEdge(dut.clk)

    popcount = dut.be_out.value
    binpc = popcount.binstr   
    print("Popcount {} bin{}".format(popcount, binpc))

    # dut.opcode <= 0b11110 #opcode= 7;
    await RisingEdge(dut.clk)

    popcount = dut.be_out.value
    binpc = popcount.binstr   
    print("Popcount {} bin{}".format(popcount, binpc))
    
    # dut.opcode <= 0b00000 #opcode= 7;

    await ClockCycles(dut.clk, 5)
      
