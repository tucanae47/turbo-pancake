`timescale 1ns / 1ps


module TOP(
    input clk,
    input rst,
    input we,
    input w_en,
    input [7:0] addr_w, 
    input [7:0] addr_r, 
    input [55:0] data_in, 
    input [4:0] opcode, //ins
    output wire signed[6:0] be_out
    );

    wire [55:0] data_out; 
    sram ram
	(
	.clk(clk),
	.we(we),
	.data_o(data_out),
	.data_i(data_in),
	.addr_w(addr_w),
	.addr_r(addr_r)
	);
    
    
    wire [7:0][6:0]img_wgt_in;
    assign img_wgt_in = data_out;

    wire [6:0][6:0]img;
    assign img[0] = img_wgt_in[0];
    assign img[1] = img_wgt_in[1];
    assign img[2] = img_wgt_in[2];
    assign img[3] = img_wgt_in[3];
    assign img[4] = img_wgt_in[4];
    assign img[5] = img_wgt_in[5];
    assign img[6] = img_wgt_in[6];
    
    wire [6:0]wgt_in;//weight data in
    assign wgt_in = img_wgt_in[7];
    //instance
    bin_mult BE0(.clk(clk),
    .rst(rst),
    .opcode(opcode),
    .w_en(w_en),
    .img(img),
    .w_input(wgt_in),
    .popcnt_add(be_out));

    `ifdef COCOTB_SIM
    `ifndef SCANNED
    `define SCANNED
    initial begin
        $dumpfile ("wave.vcd");
        $dumpvars (0, TOP);
        #1;
    end
    `endif
    `endif
endmodule