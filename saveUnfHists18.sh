#variables="pt mass zpt leppt dphiz1z2 drz1z2"
#variables="leppt"
variables="MassAllj Mass0j Mass1j Mass2j Mass3j Mass4j"
for var in $variables;do
  echo $var
  ./Utilities/scripts/saveUnfolded.py -a ZZ4l2018 -s LooseLeptons -l 59.7 -f ZZ4l2018 -sf data/scaleFactorsZZ4l2018.root -ls 2018fWUnc_full -vr ${var} --test --makeTotals --noNorm
  #--plotResponse
  #--makeTotals --plotResponse
done
