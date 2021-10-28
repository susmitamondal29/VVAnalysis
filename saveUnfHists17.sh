#variables="pt mass zpt leppt dphiz1z2 drz1z2"
variables="nJets mjj dEtajj jetPt[0] jetPt[1] absjetEta[0] absjetEta[1] MassAllj Mass0j Mass1j Mass2j Mass3j Mass4j" 
for var in $variables;do
  echo $var
  ./Utilities/scripts/saveUnfolded.py -a ZZ4l2017 -s LooseLeptons -l 41.5 -f ZZ4l2017 -sf data/scaleFactorsZZ4l2017.root -ls 2017fWUnc_full -vr ${var} --test --makeTotals --noNorm 
  #--plotResponse
done

echo "Job done!================"