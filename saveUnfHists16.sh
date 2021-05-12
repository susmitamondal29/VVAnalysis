#variables="pt mass zpt leppt dphiz1z2 drz1z2"
variables="MassAllj Mass0j Mass1j Mass2j Mass3j Mass4j"
#variables="dphiz1z2"
for var in $variables;do
  echo $var
  ./Utilities/scripts/saveUnfolded.py -a ZZ4l2016 -s LooseLeptons -l 35.9 -f ZZ4l2016 -sf data/scaleFactorsZZ4l2016.root -ls 2016fWUnc_full -vr ${var} --test --makeTotals --noNorm
  #--plotResponse
done
