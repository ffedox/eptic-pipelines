#!/bin/bash

ERROR_LOG="failed_commands.log"
> $ERROR_LOG  

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_sl_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_sl_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_sl_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_wr_tt and eptic_sl_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_fr_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_fr_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_fr_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fi_wr_tt and eptic_fr_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_it_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_it_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_it_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_wr_st and eptic_it_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_pl_wr_st' '/storage/manatee/registry/eptic3_pl_sp_st' 'eptic_pl_sp_st.eptic_pl_wr_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_pl_wr_st' '/storage/manatee/registry/eptic3_pl_sp_st' 'eptic_pl_sp_st.eptic_pl_wr_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_pl_wr_st' '/storage/manatee/registry/eptic3_pl_sp_st' 'eptic_pl_sp_st.eptic_pl_wr_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_pl_sp_st and eptic_pl_wr_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_it' 'eptic_en_sp_tt_from_it.eptic_it_wr_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_it' 'eptic_en_sp_tt_from_it.eptic_it_wr_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_it' 'eptic_en_sp_tt_from_it.eptic_it_wr_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_tt_from_it and eptic_it_wr_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_it_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_it_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_it_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fi_sp_tt and eptic_it_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_it_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_it_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_it_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_sp_tt and eptic_it_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_wr_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_fi_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_wr_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_fi_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_wr_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_fi_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_sp_tt and eptic_fi_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_it' 'eptic_en_wr_tt_from_it.eptic_it_sp_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_it' 'eptic_en_wr_tt_from_it.eptic_it_sp_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_it' 'eptic_en_wr_tt_from_it.eptic_it_sp_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_wr_tt_from_it and eptic_it_sp_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_wr_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_fi_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_wr_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_fi_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_wr_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_fi_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_wr_tt and eptic_fi_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_fr_sp_tt' 'eptic_fr_sp_tt.eptic_sl_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_fr_sp_tt' 'eptic_fr_sp_tt.eptic_sl_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_fr_sp_tt' 'eptic_fr_sp_tt.eptic_sl_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fr_sp_tt and eptic_sl_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_fr_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_fr_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_fr_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fi_wr_tt and eptic_fr_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_tt_from_pl' '/storage/manatee/registry/eptic3_en_sp_tt_from_pl' 'eptic_en_sp_tt_from_pl.eptic_en_wr_tt_from_pl.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_tt_from_pl' '/storage/manatee/registry/eptic3_en_sp_tt_from_pl' 'eptic_en_sp_tt_from_pl.eptic_en_wr_tt_from_pl.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_tt_from_pl' '/storage/manatee/registry/eptic3_en_sp_tt_from_pl' 'eptic_en_sp_tt_from_pl.eptic_en_wr_tt_from_pl.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_tt_from_pl and eptic_en_wr_tt_from_pl"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_sl_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_sl_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_sl_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_st and eptic_sl_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_sl_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_sl_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_sl_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_sp_tt and eptic_sl_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_it_sp_tt' 'eptic_it_sp_tt.eptic_sl_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_it_sp_tt' 'eptic_it_sp_tt.eptic_sl_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_it_sp_tt' 'eptic_it_sp_tt.eptic_sl_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_it_sp_tt and eptic_sl_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_st' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_en_wr_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_st' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_en_wr_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_st' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_en_wr_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_sp_tt and eptic_en_wr_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_sp_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_fi_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_sp_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_fi_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_sp_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_fi_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_sp_tt and eptic_fi_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_fr_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_fr_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_fr_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_sp_tt and eptic_fr_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_pl_wr_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_pl' 'eptic_en_sp_tt_from_pl.eptic_pl_wr_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_pl_wr_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_pl' 'eptic_en_sp_tt_from_pl.eptic_pl_wr_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_pl_wr_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_pl' 'eptic_en_sp_tt_from_pl.eptic_pl_wr_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_tt_from_pl and eptic_pl_wr_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_it_wr_tt' 'eptic_it_wr_tt.eptic_sl_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_it_wr_tt' 'eptic_it_wr_tt.eptic_sl_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_it_wr_tt' 'eptic_it_wr_tt.eptic_sl_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_it_wr_tt and eptic_sl_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_it_wr_tt' 'eptic_it_wr_tt.eptic_sl_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_it_wr_tt' 'eptic_it_wr_tt.eptic_sl_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_it_wr_tt' 'eptic_it_wr_tt.eptic_sl_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_it_wr_tt and eptic_sl_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_sp_st' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_en_sp_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_sp_st' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_en_sp_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_sp_st' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_en_sp_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_wr_tt and eptic_en_sp_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_st' '/storage/manatee/registry/eptic3_fr_sp_st' 'eptic_fr_sp_st.eptic_fr_wr_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_st' '/storage/manatee/registry/eptic3_fr_sp_st' 'eptic_fr_sp_st.eptic_fr_wr_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_st' '/storage/manatee/registry/eptic3_fr_sp_st' 'eptic_fr_sp_st.eptic_fr_wr_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fr_sp_st and eptic_fr_wr_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_fr_wr_tt' 'eptic_fr_wr_tt.eptic_sl_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_fr_wr_tt' 'eptic_fr_wr_tt.eptic_sl_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_fr_wr_tt' 'eptic_fr_wr_tt.eptic_sl_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fr_wr_tt and eptic_sl_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_fr' 'eptic_en_wr_tt_from_fr.eptic_fr_sp_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_fr' 'eptic_en_wr_tt_from_fr.eptic_fr_sp_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_fr' 'eptic_en_wr_tt_from_fr.eptic_fr_sp_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_wr_tt_from_fr and eptic_fr_sp_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_sl_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_sl_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_sl_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_st and eptic_sl_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_it_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_it_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_it_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_st and eptic_it_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_pl_wr_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_pl' 'eptic_en_wr_tt_from_pl.eptic_pl_wr_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_pl_wr_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_pl' 'eptic_en_wr_tt_from_pl.eptic_pl_wr_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_pl_wr_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_pl' 'eptic_en_wr_tt_from_pl.eptic_pl_wr_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_wr_tt_from_pl and eptic_pl_wr_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_it_sp_tt' 'eptic_it_sp_tt.eptic_sl_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_it_sp_tt' 'eptic_it_sp_tt.eptic_sl_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_it_sp_tt' 'eptic_it_sp_tt.eptic_sl_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_it_sp_tt and eptic_sl_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_sl_sp_tt' 'eptic_sl_sp_tt.eptic_sl_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_sl_sp_tt' 'eptic_sl_sp_tt.eptic_sl_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_sl_sp_tt' 'eptic_sl_sp_tt.eptic_sl_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_sl_sp_tt and eptic_sl_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_sl_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_sl_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_sl_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fi_wr_tt and eptic_sl_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_fr' 'eptic_en_wr_tt_from_fr.eptic_fr_wr_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_fr' 'eptic_en_wr_tt_from_fr.eptic_fr_wr_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_fr' 'eptic_en_wr_tt_from_fr.eptic_fr_wr_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_wr_tt_from_fr and eptic_fr_wr_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_it_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_it_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_it_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_sp_tt and eptic_it_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_sl_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_sl_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_sl_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_sp_tt and eptic_sl_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_it_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_it_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_it_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_wr_st and eptic_it_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_sl_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_sl_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_sl_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fi_wr_tt and eptic_sl_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_fr' 'eptic_en_sp_tt_from_fr.eptic_fr_sp_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_fr' 'eptic_en_sp_tt_from_fr.eptic_fr_sp_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_fr' 'eptic_en_sp_tt_from_fr.eptic_fr_sp_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_tt_from_fr and eptic_fr_sp_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_wr_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_fi_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_wr_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_fi_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_wr_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_fi_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_wr_st and eptic_fi_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_fr_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_fr_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_fr_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_wr_tt and eptic_fr_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_fr_wr_tt' 'eptic_fr_wr_tt.eptic_sl_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_fr_wr_tt' 'eptic_fr_wr_tt.eptic_sl_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_fr_wr_tt' 'eptic_fr_wr_tt.eptic_sl_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fr_wr_tt and eptic_sl_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_sp_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_fi_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_sp_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_fi_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_sp_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_fi_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_wr_st and eptic_fi_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_sl_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_sl_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_sl_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_wr_tt and eptic_sl_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_sp_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_fi_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_sp_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_fi_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_sp_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_fi_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_st and eptic_fi_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_fr_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_fr_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_fr_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_wr_tt and eptic_fr_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_st' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_en_wr_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_st' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_en_wr_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_st' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_en_wr_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_wr_tt and eptic_en_wr_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_st' '/storage/manatee/registry/eptic3_it_sp_st' 'eptic_it_sp_st.eptic_it_wr_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_st' '/storage/manatee/registry/eptic3_it_sp_st' 'eptic_it_sp_st.eptic_it_wr_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_st' '/storage/manatee/registry/eptic3_it_sp_st' 'eptic_it_sp_st.eptic_it_wr_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_it_sp_st and eptic_it_wr_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_pl_sp_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_pl' 'eptic_en_sp_tt_from_pl.eptic_pl_sp_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_pl_sp_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_pl' 'eptic_en_sp_tt_from_pl.eptic_pl_sp_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_pl_sp_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_pl' 'eptic_en_sp_tt_from_pl.eptic_pl_sp_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_tt_from_pl and eptic_pl_sp_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_it_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_it_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_it_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fi_wr_tt and eptic_it_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_fr_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_fr_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_fr_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_st and eptic_fr_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_tt_from_it' '/storage/manatee/registry/eptic3_en_sp_tt_from_it' 'eptic_en_sp_tt_from_it.eptic_en_wr_tt_from_it.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_tt_from_it' '/storage/manatee/registry/eptic3_en_sp_tt_from_it' 'eptic_en_sp_tt_from_it.eptic_en_wr_tt_from_it.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_tt_from_it' '/storage/manatee/registry/eptic3_en_sp_tt_from_it' 'eptic_en_sp_tt_from_it.eptic_en_wr_tt_from_it.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_tt_from_it and eptic_en_wr_tt_from_it"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_it' 'eptic_en_sp_tt_from_it.eptic_it_sp_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_it' 'eptic_en_sp_tt_from_it.eptic_it_sp_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_it' 'eptic_en_sp_tt_from_it.eptic_it_sp_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_tt_from_it and eptic_it_sp_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_it' 'eptic_en_wr_tt_from_it.eptic_it_wr_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_it' 'eptic_en_wr_tt_from_it.eptic_it_wr_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_it' 'eptic_en_wr_tt_from_it.eptic_it_wr_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_wr_tt_from_it and eptic_it_wr_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_fr_wr_tt' 'eptic_fr_wr_tt.eptic_it_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_fr_wr_tt' 'eptic_fr_wr_tt.eptic_it_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_fr_wr_tt' 'eptic_fr_wr_tt.eptic_it_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fr_wr_tt and eptic_it_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_pl_sp_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_pl' 'eptic_en_wr_tt_from_pl.eptic_pl_sp_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_pl_sp_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_pl' 'eptic_en_wr_tt_from_pl.eptic_pl_sp_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_pl_sp_st' '/storage/manatee/registry/eptic3_en_wr_tt_from_pl' 'eptic_en_wr_tt_from_pl.eptic_pl_sp_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_wr_tt_from_pl and eptic_pl_sp_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_fr_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_fr_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_fr_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_sp_tt and eptic_fr_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_tt_from_fr' '/storage/manatee/registry/eptic3_en_sp_tt_from_fr' 'eptic_en_sp_tt_from_fr.eptic_en_wr_tt_from_fr.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_tt_from_fr' '/storage/manatee/registry/eptic3_en_sp_tt_from_fr' 'eptic_en_sp_tt_from_fr.eptic_en_wr_tt_from_fr.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_tt_from_fr' '/storage/manatee/registry/eptic3_en_sp_tt_from_fr' 'eptic_en_sp_tt_from_fr.eptic_en_wr_tt_from_fr.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_tt_from_fr and eptic_en_wr_tt_from_fr"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_fr_sp_tt' 'eptic_fr_sp_tt.eptic_it_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_fr_sp_tt' 'eptic_fr_sp_tt.eptic_it_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_fr_sp_tt' 'eptic_fr_sp_tt.eptic_it_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fr_sp_tt and eptic_it_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_it_sp_tt' 'eptic_it_sp_tt.eptic_it_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_it_sp_tt' 'eptic_it_sp_tt.eptic_it_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_it_sp_tt' 'eptic_it_sp_tt.eptic_it_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_it_sp_tt and eptic_it_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_it_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_it_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_it_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_wr_tt and eptic_it_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_fr' 'eptic_en_sp_tt_from_fr.eptic_fr_wr_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_fr' 'eptic_en_sp_tt_from_fr.eptic_fr_wr_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_st' '/storage/manatee/registry/eptic3_en_sp_tt_from_fr' 'eptic_en_sp_tt_from_fr.eptic_fr_wr_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_tt_from_fr and eptic_fr_wr_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_fr_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_fr_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_fr_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_wr_st and eptic_fr_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_sl_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_sl_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_sl_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fi_sp_tt and eptic_sl_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_fr_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_fr_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_fr_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_st and eptic_fr_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_sp_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_fi_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_sp_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_fi_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_sp_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_fi_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_wr_tt and eptic_fi_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_it_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_it_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_de_wr_tt' 'eptic_de_wr_tt.eptic_it_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_wr_tt and eptic_it_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_fr_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_fr_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_fr_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_wr_st and eptic_fr_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_de_wr_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_de_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_de_wr_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_de_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_de_wr_tt' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_de_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_sp_tt and eptic_de_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_wr_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_fi_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_wr_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_fi_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_wr_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_fi_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fi_sp_tt and eptic_fi_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_it_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_it_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_fi_wr_tt' 'eptic_fi_wr_tt.eptic_it_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fi_wr_tt and eptic_it_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_st' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_en_wr_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_st' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_en_wr_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_wr_st' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_en_wr_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_st and eptic_en_wr_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_fr_wr_tt' 'eptic_fr_wr_tt.eptic_it_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_fr_wr_tt' 'eptic_fr_wr_tt.eptic_it_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_sp_tt' '/storage/manatee/registry/eptic3_fr_wr_tt' 'eptic_fr_wr_tt.eptic_it_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fr_wr_tt and eptic_it_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_sl_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_sl_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_sl_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fi_sp_tt and eptic_sl_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_fr_sp_tt' 'eptic_fr_sp_tt.eptic_it_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_fr_sp_tt' 'eptic_fr_sp_tt.eptic_it_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_fr_sp_tt' 'eptic_fr_sp_tt.eptic_it_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fr_sp_tt and eptic_it_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_wr_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_fi_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_wr_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_fi_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fi_wr_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_fi_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_st and eptic_fi_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_fr_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_fr_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_sp_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_fr_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fi_sp_tt and eptic_fr_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_it_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_it_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_it_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fi_sp_tt and eptic_it_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_sl_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_sl_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_sl_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_wr_st and eptic_sl_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_fr_sp_tt' 'eptic_fr_sp_tt.eptic_fr_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_fr_sp_tt' 'eptic_fr_sp_tt.eptic_fr_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_fr_sp_tt' 'eptic_fr_sp_tt.eptic_fr_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fr_sp_tt and eptic_fr_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_sl_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_sl_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_wr_tt' '/storage/manatee/registry/eptic3_en_wr_st' 'eptic_en_wr_st.eptic_sl_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_wr_st and eptic_sl_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_sp_st' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_en_sp_st.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_sp_st' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_en_sp_st.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_en_sp_st' '/storage/manatee/registry/eptic3_de_sp_tt' 'eptic_de_sp_tt.eptic_en_sp_st.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_de_sp_tt and eptic_en_sp_st"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_fr_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_fr_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_fr_wr_tt' '/storage/manatee/registry/eptic3_fi_sp_tt' 'eptic_fi_sp_tt.eptic_fr_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fi_sp_tt and eptic_fr_wr_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_fr_sp_tt' 'eptic_fr_sp_tt.eptic_sl_sp_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_fr_sp_tt' 'eptic_fr_sp_tt.eptic_sl_sp_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_sl_sp_tt' '/storage/manatee/registry/eptic3_fr_sp_tt' 'eptic_fr_sp_tt.eptic_sl_sp_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_fr_sp_tt and eptic_sl_sp_tt"
fi

echo "Running: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_it_wr_tt.xml'"
python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_it_wr_tt.xml'
if [ $? -ne 0 ]; then
    echo "FAILED: python3 intertext2noske_cambiato.py '/storage/manatee/registry/eptic3_it_wr_tt' '/storage/manatee/registry/eptic3_en_sp_st' 'eptic_en_sp_st.eptic_it_wr_tt.xml'" >> $ERROR_LOG
    echo "This couple of corpora failed: eptic_en_sp_st and eptic_it_wr_tt"
fi
