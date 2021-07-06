import json

outputname = "varsFile.json"

dict = {}
#Mass variables===================================================================
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
    if var == "Mass4j":
        nj = ">=4"
    dict[var]["units"] = '[GeV]'
    dict[var]["_binning"] = [100.] + [200.+50.*i for i in range(5)] + [500.,600.,800.,1000.]
    dict[var]["prettyVars"] = 'm_{4\\ell}' + "(%s jets)"%nj
    dict[var]["responseClassNames"] = 'testJet'
#====================================================================================    

#jet variables=======================================================================
var2="nJets"
dict[var2] = {}
dict[var2]["units"] = ''
dict[var2]["_binning"] = [0.0,1.0,2.0,3.0,4.0]
dict[var2]["prettyVars"] = 'N_{jets}'
dict[var2]["responseClassNames"] = 'testJet'

var3="mjj"
dict[var3] = {}
dict[var3]["units"] = '[GeV]'
dict[var3]["_binning"] = [0.,200.,400.,600.,1000.]#[100.+40.*i for i in range(31)]
dict[var3]["prettyVars"] = 'Di-jet Mass'
dict[var3]["responseClassNames"] = 'testJet'

var4="dEtajj"
dict[var4] = {}
dict[var4]["units"] = ''
dict[var4]["_binning"] = [0.,1.2,2.4,3.6,4.7]
dict[var4]["prettyVars"] = '#Delta#eta(j_{1}, j_{2})'
dict[var4]["responseClassNames"] = 'testJet'

for i,var in enumerate(["jetPt[0]","jetPt[1]","absjetEta[0]","absjetEta[1]"]):
    dict[var] = {}
    if "Pt" in var:
        dict[var]["units"] = '[GeV]'
    else:
        dict[var]["units"] = ''
    if i==0:
        dict[var]["_binning"] = [30.,50.,100.,200.,300.,500.]
        dict[var]["prettyVars"] ='p_{T}^{j1}'
    if i==1:
        dict[var]["_binning"] = [30.,50.,100.,170.,300.]
        dict[var]["prettyVars"] ='p_{T}^{j2}'
    if i==2:
        dict[var]["_binning"] = [0.,1.5,2.4,3.2,4.7]
        dict[var]["prettyVars"] = '|#eta_{j1}|'
    if i==3:
        dict[var]["_binning"] = [0.,1.5,3.,4.7]
        dict[var]["prettyVars"] = '|#eta_{j2}|'
    
    dict[var]["responseClassNames"] = 'testJet'    

with open(outputname,'w') as output_file:
  json.dump(dict,output_file,indent=4)
