# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0
# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles, with_timeout, ReadOnly
import random
from cocotb.binary import BinaryValue

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

async def bit_count(i):
    return bin(i).count('1')

@cocotb.test()
async def test_top(dut):
    """Test reading data from RAM"""
    clock = Clock(dut.clk, 10, units="us")
    cocotb.fork(clock.start())
    # ram_data = 0b10111101000000101001000011101011111100111110010101100011 
    # ram_addr = 0

    # dut.c_rst <= 0;
    # await write_ram(dut, ram_addr, ram_data)
    # await read_ram(dut, ram_addr)

    # dut.opcode <= 0b00000
    # dut.data_high = 0b101111010000001010010000 
    packed_input_h = int(0)
    gen_vals_single = []
    for i in range(4):
        bin_val_h = int(random.getrandbits(7))
        gen_vals_single.append(bin_val_h)
        packed_input_h = packed_input_h | bin_val_h
        print(bin(packed_input_h), bin(bin_val_h))
        if i < 3:
            packed_input_h = packed_input_h << 7 
    print(bin(packed_input_h))
    
    packed_input_l = int(0)
    for i in range(4):
        bin_val_l = int(random.getrandbits(7))
        gen_vals_single.append(bin_val_l)
        packed_input_l = packed_input_l | bin_val_l
        print(bin(packed_input_l), bin(bin_val_l))
        if i < 3:
            packed_input_l = packed_input_l << 7 
    print(bin(packed_input_l))
    

    w = int(gen_vals_single[7])
    img = gen_vals_single[3] 
    print("w: {} , img: {}".format(bin(w), bin(img)))
    xnor_value = ~( img ^ w)

    pc = await bit_count(xnor_value)

    print(bin(w), w, [ bin(x) for x in gen_vals_single])
    print("\n\n XNOR: {}, BIN: {} ---- POPCOUNT: {} BIN: {}".format(xnor_value ,bin(xnor_value), pc, bin(pc)))


    dut.data_high = BinaryValue(packed_input_h)
    dut.data_low = BinaryValue(packed_input_l)
    val_input = dut.data_high.value
    # bin_str_val = val_input.binstr  
    # print("----->> {} bin{}".format(val_input, bin_str_val))
    # dut.data_high = 0b11101011111100111110010101100011 
    # dut.data_low = 0b11101011111100111110010101100011 
    # dut.data_low = 0b0 
    await RST(dut)
    
    # await ClockCycles(dut.clk, 1)
    dut.w_en <= 1 
    dut.c_rst <= 1
    # dut.opcode <= 0b00001
    await ClockCycles(dut.clk, 8)

    dut.w_en <= 0
    await RisingEdge(dut.clk)

      
