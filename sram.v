`timescale 1ns / 1ps
module sram
	#(
	parameter DWIDTH = 24,
	parameter AWIDTH = 6
	)
	(
	input          				clk,
	input          				we,
	output reg 	[DWIDTH-1:0]	data_o,
	input  		[DWIDTH-1:0]	data_i,
	input  		[AWIDTH-1:0]	addr_w,
	input  		[AWIDTH-1:0]	addr_r
	);

reg [DWIDTH-1:0] ram [0:(2**AWIDTH)-1];

always @(posedge clk)
begin
	if(we)	ram[addr_w] <= data_i;
	data_o 	<= ram[addr_r];

end

`ifdef COCOTB_SIM
    `ifndef SCANNED
    `define SCANNED
    initial begin
        $dumpfile ("wave.vcd");
        $dumpvars (0, sram);
        #1;
    end
    `endif
    `endif

endmodule



  


