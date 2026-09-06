---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnalysisSummary.html
---

# AnalysisSummary
<a name="API_AnalysisSummary"></a>

A summary of the analysis.

## Contents
<a name="API_AnalysisSummary_Contents"></a>

 ** AnalysisCompletionTime **   <a name="awscostmanagement-Type-AnalysisSummary-AnalysisCompletionTime"></a>
The completion time of the analysis.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** AnalysisId **   <a name="awscostmanagement-Type-AnalysisSummary-AnalysisId"></a>
The analysis ID that's associated with the commitment purchase analysis.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[\S\s]{8}-[\S\s]{4}-[\S\s]{4}-[\S\s]{4}-[\S\s]{12}$`
Required: No

 ** AnalysisStartedTime **   <a name="awscostmanagement-Type-AnalysisSummary-AnalysisStartedTime"></a>
The start time of the analysis.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

 ** AnalysisStatus **   <a name="awscostmanagement-Type-AnalysisSummary-AnalysisStatus"></a>
The status of the analysis.
Type: String
Valid Values: `SUCCEEDED | PROCESSING | FAILED`
Required: No

 ** CommitmentPurchaseAnalysisConfiguration **   <a name="awscostmanagement-Type-AnalysisSummary-CommitmentPurchaseAnalysisConfiguration"></a>
The configuration for the commitment purchase analysis.
Type: [CommitmentPurchaseAnalysisConfiguration](API_CommitmentPurchaseAnalysisConfiguration.md) object
Required: No

 ** ErrorCode **   <a name="awscostmanagement-Type-AnalysisSummary-ErrorCode"></a>
The error code used for the analysis.
Type: String
Valid Values: `NO_USAGE_FOUND | INTERNAL_FAILURE | INVALID_SAVINGS_PLANS_TO_ADD | INVALID_SAVINGS_PLANS_TO_EXCLUDE | INVALID_ACCOUNT_ID`
Required: No

 ** EstimatedCompletionTime **   <a name="awscostmanagement-Type-AnalysisSummary-EstimatedCompletionTime"></a>
The estimated time for when the analysis will complete.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`
Required: No

## See Also
<a name="API_AnalysisSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/AnalysisSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/AnalysisSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/AnalysisSummary)
