module m_counter #(parameter M = 5,           // count from 0 to M-1
                       parameter N = 3)
                      (input  clk,
                       input  reset,
                       output  complete_tick,
                       output [N-1:0] count);
    
    reg[N-1:0] count_reg;
    wire[N-1:0] count_next;
    
    always @(posedge clk, posedge reset)
    begin
        if (reset == 1)
            count_reg <= 0;
        else
            count_reg <= count_next;
    end
    
    // set count_next to 0 when maximum count is reached i.e. (M-1)
    // otherwise increase the count
    assign count_next = (count_reg == M-1) ? 0 : count_reg + 1 ;
    
    //Generate 'tick' on each maximum count
    assign complete_tick = (count_reg == M-1) ? 1 : 0;
    
    assign count = count_reg; // assign count to output port
    
    // ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  = 
    // Simulation Only Waveform Dump (.vcd export)
    // ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  ==  = 
    `ifdef COCOTB_SIM
    `ifndef SCANNED
    `define SCANNED
    initial begin
        $dumpfile ("wave.vcd");
        $dumpvars (0, m_counter);
        #1;
    end
    `endif
    `endif
    
endmodule
