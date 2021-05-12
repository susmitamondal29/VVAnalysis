#variables="pt mass zpt leppt dphiz1z2 drz1z2"
#variables="dphiz1z2"
variables="MassAllj Mass0j Mass1j Mass2j Mass3j Mass4j"
for var in $variables;do
  echo $var
  ./Utilities/scripts/plotUnfolded.py -a ZZ4l2017 -s LooseLeptons -l 41.5 -f ZZ4l2017 -vr ${var} --test --makeTotals --scaleymin 0.5 --scaleymax 1.0 --unfoldDir /afs/cern.ch/user/h/hehe/www/ZZFullRun2/PlottingResults/ZZ4l2017/ZZSelectionsTightLeps/ANPlots/ZZ4l2017/FinalDiffDist_16Apr2020/
  #--plotResponse
done
