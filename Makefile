# ==============================================================================
# simulation settings
# ==============================================================================
SIM			    ?= icarus			# simulator (icarus, verilator, ...)
TOPLEVEL_LANG   ?= verilog			# hdl (verilog, vhdl)

# ==============================================================================
# source files
# ==============================================================================
# VERILOG_SOURCES += ./*.v
VERILOG_SOURCES += ./mux_bin_bhl.v

# ==============================================================================
# modules
# ==============================================================================
# module	 = test_serin_parout 			# python cocotb tests
# toplevel = serin_parout	        		# top level rtl module


# MODULE	 = test_m_counter 			# python cocotb tests
# TOPLEVEL = m_counter		# top level rtl module


MODULE	 = test_mux 			# python cocotb tests
TOPLEVEL = mux_bin_bhl		# top level rtl module

# ==============================================================================
# cocotb magic
# ==============================================================================
include $(shell cocotb-config --makefiles)/Makefile.sim

# ==============================================================================
# supplemental commands
# ==============================================================================
clean::
	rm -f results.xml
	rm -f *.vcd
	rm -rf __pycache__/

wave:
	gtkwave *.vcd -a *.gtkw
