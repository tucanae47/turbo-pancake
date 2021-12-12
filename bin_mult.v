`timescale 1ns / 1ps

module bin_mult(
    input clk,
    input rst,
    input w_en,
    input c_rst,
    input wire [6:0] [6:0] img ,
    input wire [6:0] w_input,
    output reg signed[6:0] popcnt_add
    );
    // hardcode lookup table to select vectors 
    
    reg [2:0] count = 3'b0;
    reg [6:0][6:0]w;
    always@(posedge clk)begin
        if(rst)begin
            w <= 0;
        end
        else if(w_en)begin
            w <= {w[5:0],w_input};
        end
    end
    
    wire [6:0][6:0] x_out;
    xnor7 xnor0(
    .img(img[0]),
    .w(w[0]),
    .x_out(x_out[0]));
    xnor7 xnor1(
    .img(img[1]),
    .w(w[1]),
    .x_out(x_out[1]));
    xnor7 xnor2(
    .img(img[2]),
    .w(w[2]),
    .x_out(x_out[2]));
    xnor7 xnor3(
    .img(img[3]),
    .w(w[3]),
    .x_out(x_out[3]));
    xnor7 xnor4(
    .img(img[4]),
    .w(w[4]),
    .x_out(x_out[4]));
    xnor7 xnor5(
    .img(img[5]),
    .w(w[5]),
    .x_out(x_out[5]));
    xnor7 xnor6(
    .img(img[6]),
    .w(w[6]),
    .x_out(x_out[6]));
    
    
    
    wire [6:0] lut_in_origin;
    assign lut_in_origin = x_out[count];
    wire [5:0] lut_in;
    assign lut_in = lut_in_origin[5:0];
    
    // lut_selection

    wire[63:0][2:0]lookup_popcnt;
    assign lookup_popcnt={{3'b110},{3'b101},{3'b101},{3'b100},{3'b101},{3'b100},{3'b100},{3'b11},{3'b101},{3'b100},{3'b100},{3'b11},{3'b100},{3'b11},{3'b11},{3'b10},{3'b101},{3'b100},{3'b100},{3'b11},{3'b100},{3'b11},{3'b11},{3'b10},{3'b100},{3'b11},{3'b11},{3'b10},{3'b11},{3'b10},{3'b10},{3'b1},{3'b101},{3'b100},{3'b100},{3'b11},{3'b100},{3'b11},{3'b11},{3'b10},{3'b100},{3'b11},{3'b11},{3'b10},{3'b11},{3'b10},{3'b10},{3'b1},{3'b100},{3'b11},{3'b11},{3'b10},{3'b11},{3'b10},{3'b10},{3'b1},{3'b11},{3'b10},{3'b10},{3'b1},{3'b10},{3'b1},{3'b1},{3'b0}};

    reg signed[4:0] popcnt;
    wire[3:0] intern;

    assign intern = lookup_popcnt[lut_in];
    
    always @(intern) begin
        popcnt = intern;
    end
    
    always @(posedge clk) begin
        if(rst) begin
            count <= 0;
            popcnt_add <= 0;
        end
        else begin
            if(c_rst) begin
                count <= count + 1;
                popcnt_add <= popcnt_add + popcnt;
            end
        end
    end
    // `ifdef COCOTB_SIM
    // `ifndef SCANNED
    // `define SCANNED
    // initial begin
    //     $dumpfile ("wave.vcd");
    //     $dumpvars (0, bin_mult);
    //     #1;
    // end
    // `endif
    // `endif
endmodule
