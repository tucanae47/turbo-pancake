`default_nettype none
`timescale 1ns/1ns

module sram
	#(
	parameter DWIDTH = 32,
	parameter AWIDTH = 8
	)
	(
	input          				clk,
	input          				we,
	output reg 	[DWIDTH-1:0]	data_o,
	input  		[DWIDTH-1:0]	data_i,
	input  		[AWIDTH-1:0]	addr
	);

reg [DWIDTH-1:0] ram [0:(2**AWIDTH)-1];

always @(posedge clk)
begin
	if(we)	ram[addr] <= data_i;
	data_o 	<= ram[addr];

end

endmodule



  


