#!/usr/bin/perl -w

use strict;

# the $sp flag indicates we are in a spoken file
my $sp = 0;

my $langcode;
my $word;
my $pos;
my $lemma;

while (<>) {

  chomp;
  
  # skip lines beginning with "<" (tags), but get information on text type
  if (/^</) {
    if (/type=\"([a-z]{2})_sp/) {
      $langcode = $1;
      $sp = 1;
    }
    elsif (/type=\"([a-z]{2})_wr_/) {
      $langcode = $1;
      $sp = 0;
    }

    print;
    print "\n";
  }

  else {
    
    if ($langcode eq "pl") {
      ($word,$pos,undef,$lemma) = split "[\t ]+",$_;
    }

    if ($langcode eq "fr") {
      ($word,$pos,undef,$lemma,undef,undef) = split "[\t ]+",$_;
    }


    elsif ($langcode ne /pl/) {
      ($word,$pos,$lemma) = split "[\t ]+",$_;
    }  

    $lemma =~s/<unknown>/UNKNOWN/;
    $lemma =~s/-[a-z]$//;

    # EPTIC HACKs!! (the interpreting files, the -o swith must have been activated)
    
    #transform tag of three dots into "PAUSE"
    
    if ($sp && $word eq "\.\.\."){
      $pos = "EPAUSE";
    }


    # if a word ends in a "-" assign pos-tag DYSF (for: "DYSFluency")
    # and assign word form as lemma

    if ($sp && $word =~ /PIPPERO$/){
      $word =~ s/(.+)PIPPERO/$1-/;
      $pos = "DYSF";
      $lemma = $word;
    }

    if ($sp && $word =~ /[Ee]hm/){
      $pos = "FPAUSE";
      $lemma = "ehm";
    }

    if ($sp && $word =~ /#/){
      $pos = "UNCLEAR";
      $lemma = "#";
    }

    # other manual corrections of tagging, based on inspection of output. Not sure these are still relevant, since we now perform tagging with NoSke tagger

    if ($langcode eq "fr" && $word =~ /(Conseil|Commissaire)/){
      $pos = "NOM";
      $lemma = $word;
    }
    
    if ($langcode eq "it" && $word =~ /(Presidente|Commissario|Consiglio|Commissione)/){
      $pos = "NOUN";
      $lemma = $word;
    }

    if ($langcode eq "it" && $word =~ /(Stat(i|o))/){
      $pos = "NOUN";
      $lemma = "stato";
    }

    if ($langcode eq "it" && $word =~ /^[Nn]è$/){
      $word =~ s/è/é/g;
      $pos = "CON";
      $lemma = "né";
    }
    
    if ($langcode eq "en" && $word =~ /cannot/){
      $pos = "MD";
      $lemma = "can";
    }
    
    print "$word\t$pos\t$lemma\n";
  }

}


