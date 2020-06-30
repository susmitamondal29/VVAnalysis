#ifndef ZZSelector_h
#define ZZSelector_h

#include <vector>
#include "Analysis/VVAnalysis/interface/ZZSelectorBase.h"
#include <TH3.h>

class ZZSelector : public ZZSelectorBase {
public :
    bool applyFullSelection_ = true;
    bool isaTGC_ = false;
    bool doaTGC_ = false;

    std::vector<float>* scaleWeights = NULL;
    std::vector<float>* pdfWeights = NULL;
    std::vector<float> lheWeights;
    unsigned int weight_info_;


    float dEtajj;
    float dEtajj_jesUp;
    float dEtajj_jesDown;
    float dEtajj_jerUp;
    float dEtajj_jerDown;
    float dRjj;
    float dRjj_jesUp;
    float dRjj_jesDown;
    float dRjj_jerUp;
    float dRjj_jerDown;
    float zep3l;
    float zep3l_jesUp;
    float zep3l_jesDown;
    float zep3l_jerUp;
    float zep3l_jerDown;
    Float_t mjj;
    Float_t zeppenfeld;
    std::vector<float>* jetEta = NULL;
    std::vector<float>* jetEta_jesUp = NULL;
    std::vector<float>* jetEta_jesDown = NULL;
    std::vector<float>* jetEta_jerUp = NULL;
    std::vector<float>* jetEta_jerDown = NULL;
    std::vector<float>* jetPhi = NULL;
    std::vector<float>* jetPhi_jesUp = NULL;
    std::vector<float>* jetPhi_jesDown = NULL;
    std::vector<float>* jetPhi_jerUp = NULL;
    std::vector<float>* jetPhi_jerDown = NULL;
    std::vector<float>* jetPt = NULL;
    std::vector<float>* jetPt_jesUp = NULL;
    std::vector<float>* jetPt_jesDown = NULL;
    std::vector<float>* jetPt_jerUp = NULL;
    std::vector<float>* jetPt_jerDown = NULL;
    std::vector<float>* jetCSVv2 = NULL;
    UInt_t nvtx;
    Float_t Mass;
    Float_t Pt;
    float dPhiZZ; //DeltaPhi between Z1 and Z2
    TBranch* b_nvtx;
    TBranch* b_Mass;
    TBranch* b_Pt;
    TBranch* b_jetPt;
    TBranch* b_jetPhi;
    TBranch* b_jetEta;
    TBranch* b_mjj;
    TBranch* b_zeppenfeld;
    //TBranch* b_evt;
    float cosTheta_1; 
    float cosTheta_2;
    float cosTheta_3;
    float cosTheta_4;
    int cen_count = 0;
    float count = 0;
    int zzcutcount = 0;
    int mjjcutcount = 0;
    int masscutcount = 0;
    //ULong64_t evt;
    FILE * ggZZFile;
    bool ggZZfirst = true;

    // Readers to access the data (delete the ones you do not need).
    virtual void    Init(TTree *tree) override;
    virtual void    SetupNewDirectory() override;

    ClassDefOverride(ZZSelector,0);

protected:
    virtual void    SetBranchesUWVV() override;
    void LoadBranchesUWVV(Long64_t entry, std::pair<Systematic, std::string> variation) override;
    void FillHistograms(Long64_t entry, std::pair<Systematic, std::string> variation) override;
    void ApplyScaleFactors();
    bool PassesZZSelection(bool nonPrompt);
    bool PassesZZjjSelection();
    bool MassSelection();
    bool PassesHZZSelection();
    bool PassesEtaSelection();
    unsigned int GetLheWeightInfo();
    void SetVariables(Long64_t entry);
    //bool DuplicatedEvent();
    bool TightZZLeptons();
    bool ZZSelection();
    bool Z4lSelection();
    bool ZSelection();
    bool HZZSIPSelection();
    //bool SmartCut();
    bool HZZLowMass();
    bool HZZMediumMass();
    bool TestMuons();
    void GetPolarizationAngle();
    void ShiftEfficiencies(Systematic variation);
};

#endif

