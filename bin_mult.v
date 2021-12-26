`default_nettype none
`timescale 1ns/1ns
module bin_mult(
    input clk,
    input rst,
    input w_en,
    input c_rst,
    input wire [48:0] img ,
    input wire [48:0] w,
    output reg signed[6:0] popcnt_add
    );

    // wire [6:0] img_unpacked [6:0];
    // assign img_unpacked[0] = img[0];
    // assign img_unpacked[1] = img[1];
    // assign img_unpacked[2] = img[2];
    // assign img_unpacked[3] = img[3];
    // assign img_unpacked[4] = img[4];
    // assign img_unpacked[5] = img[5];
    // assign img_unpacked[6] = img[6];
    // hardcode lookup table to select vectors 
    
    reg [2:0] count = 3'b0;
    // reg [42:0] w;
    // always@(posedge clk)begin
    //     if(rst)begin
    //         w <= 0;
    //     end
    //     else if(w_en)begin
    //         w <= {w[5:0],w_input};
    //     end
    // end
    
    wire [48:0] x_out;
    xnor7 xnor0(
    .img(img[0+:7]),
    .w(w[0+:7]),
    .x_out(x_out[0+:7]));

    xnor7 xnor1(
    .img(img[7+:7]),
    .w(w[7+:7]),
    .x_out(x_out[7+:7]));

    xnor7 xnor2(
    .img(img[14+:7]),
    .w(w[14+:7]),
    .x_out(x_out[14+:7]));

    xnor7 xnor3(
    .img(img[21+:7]),
    .w(w[21+:7]),
  .x_out(x_out[21+:7]));

    xnor7 xnor4(
    .img(img[28+:7]),
    .w(w[28+:7]),
    .x_out(x_out[28+:7]));

    xnor7 xnor5(
    .img(img[35+:7]),
    .w(w[35+:7]),
    .x_out(x_out[35+:7]));

    xnor7 xnor6(
    .img(img[42+:7]),
    .w(w[42+:7]),
    .x_out(x_out[42+:7]));
    
    
    
    wire [6:0] lut_in_origin;
    assign lut_in_origin = x_out[count+:7];
    wire [5:0] lut_in;
    assign lut_in = lut_in_origin[5:0];
    
    // lut_selection

    wire [63:0] lookup_popcnt;
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
    
endmodule
