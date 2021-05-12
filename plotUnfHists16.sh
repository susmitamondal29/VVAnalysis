#variables="pt mass zpt leppt dphiz1z2 drz1z2"
variables="MassAllj Mass0j Mass1j Mass2j Mass3j Mass4j"
#variables="dphiz1z2"
for var in $variables;do
  echo $var
  ./Utilities/scripts/plotUnfolded.py -a ZZ4l2016 -s TightLeptonsWGen -l 35.9 -f ZZ4l2016 -vr ${var} --test --makeTotals --scaleymin 0.5 --scaleymax 1.0 --unfoldDir /afs/cern.ch/user/h/hehe/www/ZZFullRun2/PlottingResults/ZZ4l2016/ZZSelectionsTightLeps/ANPlots/ZZ4l2016/FinalDiffDist_16Apr2020/
  #--plotResponse
done
