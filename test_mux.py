# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

import random

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, FallingEdge, ClockCycles
from cocotb.binary import BinaryValue
from cocotb.triggers import Timer


@cocotb.test()
async def test_mux(dut):
    """ Eric Mux Bin Bhl """
    # parallel_load = np.random.randint(0, 2**10, size=1,
                                #  dtype=np.int32)
    # print("parallel_load = {}".format(parallel_load))
    # dut.words_in <= BinaryValue("1110001110")
    dut.words_in <= BinaryValue("1100111000111100")

    print("1100111000111100")
    dut.selector <= 0

    await Timer(2, units='ns')
    # sel = np.dtype('int32').type(1)
    # print("selector  = {}".format(sel)f
    for i in range(1,18):

        select = format(i, f'0{2}b')
        # print(i, select)
        dut.selector <= i
        # dut.selector <= BinaryValue(selector)
        observed = dut.word_out.value.binstr
        selector = dut.selector.value.integer
        print("observed = {}, selector = {}".format(observed[1:], selector))
        await Timer(2, units='ns')
  