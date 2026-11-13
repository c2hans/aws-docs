---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InvestigationAccountAnalysis.html
---

# InvestigationAccountAnalysis
<a name="API_InvestigationAccountAnalysis"></a>

Contains an analysis of the findings in an account. Either `Trend` or `Baseline` is set, depending on the `AnalysisType` of the record.

## Contents
<a name="API_InvestigationAccountAnalysis_Contents"></a>

 ** baseline **   <a name="guardduty-Type-InvestigationAccountAnalysis-baseline"></a>
A comparison of findings against normal behavior. Set when `AnalysisType` is `BASELINE`.
Type: [Baseline](API_Baseline.md) object
Required: No

 ** trend **   <a name="guardduty-Type-InvestigationAccountAnalysis-trend"></a>
The trend of findings over time. Set when `AnalysisType` is `TREND`.
Type: [Trend](API_Trend.md) object
Required: No

## See Also
<a name="API_InvestigationAccountAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InvestigationAccountAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InvestigationAccountAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InvestigationAccountAnalysis)
