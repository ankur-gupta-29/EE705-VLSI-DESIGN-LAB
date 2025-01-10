====================================
32-bit Counter testing using ILA,VIO
====================================
..
  Objective
  --------- 
  - Vivado project creation.
  - Creating a verilog file or add verilog files.
  - Test the verilog code with ILA,VIO blocks.

Visit the `Pynq-Z2 website <https://www.tulembedded.com/FPGA/ProductsPYNQ-Z2.html>`_ for more information about User Manual,Master XDC,Schematics.
..youtube:: aoMdoZwbjI8
   :width: 640
   :height: 480
..
  .. code-block:: verilog

     module and_gate (
       input a,
       input b,
       output y
    );
       assign y = a & b;
    endmodule

  .. figure:: ./images/xilinx_logo.png
   :alt: Centered Image
   :align: center
   :width: 50%

   This is the caption for the image.

