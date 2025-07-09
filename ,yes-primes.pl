#!/usr/bin/perl
# Print prime numbers forever.

(1 x $_) !~ /^(11+)\1+$/ && print while ++ $_
