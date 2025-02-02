#!/usr/bin/perl -w

use strict;

my $subs = shift;
my $corpus = shift;
my %sentsub;
my $sid; # sentence id in sub files
my $csid; # sentence id in corpus files. The two should coincide,
             # but just to be on the safe side...

open SUBS, $subs;

while (<SUBS>) {
  chomp;
  if (/<s id="([0-9\:]+)/) {
    $sid = $1;
    $sentsub{$sid} = $_;
  }
}

close SUBS;


open CORPUS, $corpus;

while (<CORPUS>) {
  
  chomp;
  
  s/<corpus>//;

  if (/^<\/?(text|speaker|st|interpreter)/) { #skip header lines
    print;
    print "\n";
  }

  elsif (/<s id="([0-9\:]+)">/) {
    $csid = $1;
    if ($sentsub{$csid}) {
      s/^ *<s id="([0-9\:]+)">//;
      s/<\/s>/\n<\/s>\n/;
      print "$sentsub{$csid}\n";
      transform($_);
      print;

    }
    elsif (!($sentsub{$csid})) { # for some texts we don't have videos
      s/^ *(<s id="[0-9\:]+")>/$1 video=\"NA\">\n/;
      s/<\/s>/\n<\/s>\n/;
      transform($_);
      print;
    }
  }

}

sub transform {
  s/([a-zA-Z])- /$1PIPPERO /g; #we need to signal disfluencies like this,
  # otherwise tokenization gets wrong

  # the following is a set of transformations to remove transcription features that we still don't know
  # how to index (and may no longer be used. We keep them here to be on the safe side)
  
  s/ ?#ie?# ?/ /g; # no explicit markers of italics (BUT: we want to encode italics in next
                   # version of the corpus) 
    
  s/\/.+?\///g; # tags like these "/ /" (e.g. /preoccupanto/) indicate words that have
                # been transcribed using the correct form, but were pronounced
                # incorrectly. For the moment we discard the incorrect pronunciation

  s/\[.+?\]//g; # tags like these "[ ]" (e.g. [microfono spento]) indicate comments that have
                # been inserted by the person who transcribed the texts. These are eliminated

  s/ \.\.\./\.\.\./g; # delete space before three dots (which mark a pause in the spoken files)

  s/[\{\}]+//g; # remove tags indicating calques/made-up words: in this case we only discard the tag symbol ({}),
                  # but keep the word within the tag

  return($_);
}
