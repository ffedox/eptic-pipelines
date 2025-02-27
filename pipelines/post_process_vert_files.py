import sys
import re

def main():
    """Simple script to fix PIPPERO tokens in .vert files and apply additional tagging corrections."""
    if len(sys.argv) < 2:
        print("Usage: python fix_pippero.py <input_file> [output_file]", file=sys.stderr)
        return 1
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        with open(input_file, 'r', encoding='utf-8') as in_f:
            out_f = open(output_file, 'w', encoding='utf-8') if output_file else sys.stdout
            
            langcode = None
            pippero_count = 0
            
            for line in in_f:
                if line.startswith("<"):
                    match = re.search(r'type="([a-z]{2})_', line)
                    if match:
                        langcode = match.group(1)
                    out_f.write(line)
                else:
                    parts = line.strip().split('\t')
                    if len(parts) < 1:
                        out_f.write(line)
                        continue
                    
                    word = parts[0]
                    new_word = word
                    pos = parts[1] if len(parts) > 1 else ""
                    lemma = parts[2] if len(parts) > 2 else ""
                    
                    # Process word
                    if 'PIPPERO' in word:
                        new_word = re.sub(r'(.+)PIPPERO', r'\1-', word)
                        pos = "DYSF"
                        lemma = new_word
                        pippero_count += 1
                    
                    # Apply replacements regardless of sp condition
                    if word.strip() == "..." and pos == "Punct":
                        pos = "EPAUSE"
                    elif re.fullmatch(r'[Ee]hm', word.strip()):
                        pos = "FPAUSE"
                        lemma = "ehm"
                    elif word.strip() == "#" and pos == "NON-TWOL":
                        pos = "UNCLEAR"
                        lemma = "#"
                    
                    # Language-specific tagging corrections
                    if langcode == "fr" and re.search(r'\b(Conseil|Commissaire)\b', word):
                        pos = "NOM"
                        lemma = word
                    elif langcode == "it" and re.search(r'\b(Presidente|Commissario|Consiglio|Commissione)\b', word):
                        pos = "NOUN"
                        lemma = word
                    elif langcode == "it" and re.search(r'\bStat(i|o)\b', word):
                        pos = "NOUN"
                        lemma = "stato"
                    elif langcode == "it" and re.fullmatch(r'[Nn]è', word):
                        new_word = word.replace("è", "é")
                        pos = "CON"
                        lemma = "né"
                    elif langcode == "en" and word == "cannot":
                        pos = "MD"
                        lemma = "can"
                    
                    new_line = "\t".join(filter(None, [new_word, pos, lemma])) + "\n"
                    out_f.write(new_line)
            
            if output_file:
                out_f.close()
            
            print(f"Replaced {pippero_count} PIPPERO tokens", file=sys.stderr)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
