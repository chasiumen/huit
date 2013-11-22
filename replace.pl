#!/usr/bin/perl

use strict;
use warnings;

#set variabels
my $file = $ARGV[0];
my $pattern ="view";
my $replace ="download"; 

#check number of arguments
if (@ARGV != 1)
{
	die "Usage: ./replace.pl INPUT_FILE";
}

#MAIN
else
{	
	#opne file from arguments
	open(my $IN, "<$file") or die "Couldn't open $file";
	
	while(my $line = <$IN>)
	{
	
	#print $line
	$line =~ s/$pattern/$replace/g;
	print $line
	}

}

