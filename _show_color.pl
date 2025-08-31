#!/usr/bin/perl
# Arguments: HEX_COLORS...
#
# Display given hex colors. Supported formats: `0xRGB`, `0xRRGGBB`.

foreach $a (@ARGV) {
    print (("\e[48:2::".join(":", unpack("C*", pack("H*", $a))) . "m \e[49m") x 8 . "\n");
}
