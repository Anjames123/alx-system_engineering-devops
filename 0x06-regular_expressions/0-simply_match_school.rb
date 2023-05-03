#!/usr/bin/env ruby

regex = /School/
input_string = ARGV[0]

if input_string =~ regex
  puts "Match found: #{input_string.match(regex)}"
else
  puts "No match found."
end
