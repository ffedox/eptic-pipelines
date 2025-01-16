Proviamo con 2 corpora:

# Registry

/storage/manatee/vert/EPTIC.V3/eptic_de_sp_tt.vert
/storage/manatee/vert/EPTIC.V3/eptic_de_wr_tt.vert

# Registry

/storage/manatee/registry/de_sp_tt  ? Però questo sovrascriverebbe
/storage/manatee/registry/de_wr_tt  ?

compilecorp

# Allineamenti da convertire

Io mi ero fatta una cartella /storage/manatee/utils

Contenente gli script tipo intertext2noske_cambiato, fixgaps.py (quelli in NoSkE_scripts)

E con una cartella /aligns, dentro /aligns mettevo gli .XML. In questo caso mettiamo:

/storage/manatee/utils/aligns/eptic_de_sp_tt.eptic_de_wr_tt.xml

Poi dentro /aligns facevo:

python3.6 intertext2noske_cambiato.py '/storage/manatee/registry/eptic_de_wr_tt' '/storage/manatee/registry/eptic_de_sp_tt' 'eptic_de_sp_tt.eptic_de_wr_tt.xml'

E infine usavo rename_and_fixgaps.py per applicare fixgaps.py a tutti gli allineamenti di NoSke (.txt)

python3.6 rename_and_fixgaps.py

Poi mettevo gli allineamenti .txt NoSke-compliant in /storage/manatee/aligndef_files/EPTIC.V3/

A questo punto si potrebbe compilare un paio di volte per vedere se è tutto a posto




fixgaps.py < > 

no recompile

metti eptic3_sl_wr_tt a tutti i file e correggi i registry