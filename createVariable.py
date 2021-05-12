import json

outputname = "varsFile.json"

dict = {}
varlist0 = ["Mass"]
varlist = []

for var in varlist0:
    for j in range(0,5):
        varlist.append(var+"%sj"%j)

varlist.append("MassAllj") #for comparison check with original Mass variable

print(varlist)

for var in varlist:
    dict[var] = {}
    nj = var.replace("j","").replace("Mass","")
    if var == "MassAllj":
        nj = "All"
    dict[var]["units"] = '[GeV]'
    dict[var]["_binning"] = [100.] + [200.+50.*i for i in range(5)] + [500.,600.,800.,1000.]
    dict[var]["prettyVars"] = 'm_{4\\ell}' + " with %s jets"%nj
    dict[var]["responseClassNames"] = 'testJet'
    
with open(outputname,'w') as output_file:
  json.dump(dict,output_file,indent=4)
