Nelle path nei registry c'è sempre EPTIC3

1. Rinominare i file in intertext_alignments con intertext2noske_cambiato.py (generalmente il secondo elemento nel nome file dovrebbe essere quello che va prima ma ci sono un paio di casi in cui è l'opposto)

es. python3.6 intertext2noske_cambiato.py '/var/lib/manatee/registry/eptic_sl_sp_tt' '/var/lib/manatee/registry/eptic_fr_sp_tt' 'eptic_fr_sp_tt.eptic_sl_sp_tt.xml'

2. Applicare fixgaps.py a tutti i file (ho messo uno script in python rename_and_fixgaps.py che lo fa su tutti i .txt di output)

gli url dei video so sbagliati

alignments.xlsx contiene alignments anche di cose non pubblicate tipo l'ungherese+


workflow was different. i used aeneas and other things to recover missing parts of corpus... not the same as the future problems