"""
 RAM block
"""
import random

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, ReadOnly
from cocotb.result import TestFailure, ReturnValue

@cocotb.coroutine
def write_ram(dut, address, value):
    yield RisingEdge(dut.clk)              # Synchronise to the read clock
    dut.we = 1
    dut.addr_w = address
    dut.data_i = value
    yield RisingEdge(dut.clk)              # Wait 1 clock cycle
    dut.we  = 0                        # Disable write

@cocotb.coroutine
def read_ram(dut, address):
    yield RisingEdge(dut.clk)               # Synchronise to the read clock
    dut.addr_r = address                   # Drive the value onto the signal
    yield RisingEdge(dut.clk)               # Wait for 1 clock cycle
    yield ReadOnly()                             # Wait until all events have executed for this timestep
    raise ReturnValue(int(dut.data_o.value))  # Read back the value


@cocotb.test()
def test_ram(dut):
    """Try writing values into the RAM and reading back"""
    RAM = {}
    
    # Read the parameters back from the DUT to set up our model
    width = dut.DWIDTH.value
    depth = 2**dut.AWIDTH.value
    dut.log.info("Found %d entry RAM by %d bits wide" % (depth, width))

    clock = Clock(dut.clk, 20, units="us")
    # Set up independent read/write clocks
    cocotb.fork(clock.start())
    
    dut.log.info("Writing in random values")
    for i in range(depth):
        RAM[i] = int(random.getrandbits(width))
        yield write_ram(dut, i, RAM[i])

    dut.log.info("Reading back values and checking")
    for i in range(depth):
        value = yield read_ram(dut, i)
        if value != RAM[i]:
            dut.log.error("RAM[%d] expected %d but got %d" % (i, RAM[i], dut.data_read.value.value))
            raise TestFailure("RAM contents incorrect")
    dut.log.info("RAM contents OK")