---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCommitmentPurchaseAnalysis.html
---

# GetCommitmentPurchaseAnalysis
<a name="API_GetCommitmentPurchaseAnalysis"></a>

Retrieves a commitment purchase analysis result based on the `AnalysisId`.

## Request Syntax
<a name="API_GetCommitmentPurchaseAnalysis_RequestSyntax"></a>

```
{
   "AnalysisId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCommitmentPurchaseAnalysis_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AnalysisId](#API_GetCommitmentPurchaseAnalysis_RequestSyntax) **   <a name="awscostmanagement-GetCommitmentPurchaseAnalysis-request-AnalysisId"></a>
The analysis ID that's associated with the commitment purchase analysis.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[\S\s]{8}-[\S\s]{4}-[\S\s]{4}-[\S\s]{4}-[\S\s]{12}$`
Required: Yes

## Response Syntax
<a name="API_GetCommitmentPurchaseAnalysis_ResponseSyntax"></a>

```
{
   "AnalysisCompletionTime": "string",
   "AnalysisDetails": {
      "SavingsPlansPurchaseAnalysisDetails": {
         "AdditionalMetadata": "string",
         "CurrencyCode": "string",
         "CurrentAverageCoverage": "string",
         "CurrentAverageHourlyOnDemandSpend": "string",
         "CurrentMaximumHourlyOnDemandSpend": "string",
         "CurrentMinimumHourlyOnDemandSpend": "string",
         "CurrentOnDemandSpend": "string",
         "EstimatedAverageCoverage": "string",
         "EstimatedAverageUtilization": "string",
         "EstimatedCommitmentCost": "string",
         "EstimatedMonthlySavingsAmount": "string",
         "EstimatedOnDemandCost": "string",
         "EstimatedOnDemandCostWithCurrentCommitment": "string",
         "EstimatedROI": "string",
         "EstimatedSavingsAmount": "string",
         "EstimatedSavingsPercentage": "string",
         "ExistingHourlyCommitment": "string",
         "HourlyCommitmentToPurchase": "string",
         "LatestUsageTimestamp": "string",
         "LookbackPeriodInHours": "string",
         "MetricsOverLookbackPeriod": [
            {
               "CurrentCoverage": "string",
               "EstimatedCoverage": "string",
               "EstimatedNewCommitmentUtilization": "string",
               "EstimatedOnDemandCost": "string",
               "StartTime": "string"
            }
         ],
         "UpfrontCost": "string"
      }
   },
   "AnalysisId": "string",
   "AnalysisStartedTime": "string",
   "AnalysisStatus": "string",
   "CommitmentPurchaseAnalysisConfiguration": {
      "SavingsPlansPurchaseAnalysisConfiguration": {
         "AccountId": "string",
         "AccountScope": "string",
         "AnalysisType": "string",
         "LookBackTimePeriod": {
            "End": "string",
            "Start": "string"
         },
         "SavingsPlansTargetCoverage": number,
         "SavingsPlansToAdd": [
            {
               "InstanceFamily": "string",
               "OfferingId": "string",
               "PaymentOption": "string",
               "Region": "string",
               "SavingsPlansCommitment": number,
               "SavingsPlansType": "string",
               "TermInYears": "string"
            }
         ],
         "SavingsPlansToExclude": [ "string" ]
      }
   },
   "ErrorCode": "string",
   "EstimatedCompletionTime": "string"
}
```

## Response Elements
<a name="API_GetCommitmentPurchaseAnalysis_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AnalysisCompletionTime](#API_GetCommitmentPurchaseAnalysis_ResponseSyntax) **   <a name="awscostmanagement-GetCommitmentPurchaseAnalysis-response-AnalysisCompletionTime"></a>
The completion time of the analysis.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`

 ** [AnalysisDetails](#API_GetCommitmentPurchaseAnalysis_ResponseSyntax) **   <a name="awscostmanagement-GetCommitmentPurchaseAnalysis-response-AnalysisDetails"></a>
Details about the analysis.
Type: [AnalysisDetails](API_AnalysisDetails.md) object

 ** [AnalysisId](#API_GetCommitmentPurchaseAnalysis_ResponseSyntax) **   <a name="awscostmanagement-GetCommitmentPurchaseAnalysis-response-AnalysisId"></a>
The analysis ID that's associated with the commitment purchase analysis.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[\S\s]{8}-[\S\s]{4}-[\S\s]{4}-[\S\s]{4}-[\S\s]{12}$`

 ** [AnalysisStartedTime](#API_GetCommitmentPurchaseAnalysis_ResponseSyntax) **   <a name="awscostmanagement-GetCommitmentPurchaseAnalysis-response-AnalysisStartedTime"></a>
The start time of the analysis.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`

 ** [AnalysisStatus](#API_GetCommitmentPurchaseAnalysis_ResponseSyntax) **   <a name="awscostmanagement-GetCommitmentPurchaseAnalysis-response-AnalysisStatus"></a>
The status of the analysis.
Type: String
Valid Values: `SUCCEEDED | PROCESSING | FAILED`

 ** [CommitmentPurchaseAnalysisConfiguration](#API_GetCommitmentPurchaseAnalysis_ResponseSyntax) **   <a name="awscostmanagement-GetCommitmentPurchaseAnalysis-response-CommitmentPurchaseAnalysisConfiguration"></a>
The configuration for the commitment purchase analysis.
Type: [CommitmentPurchaseAnalysisConfiguration](API_CommitmentPurchaseAnalysisConfiguration.md) object

 ** [ErrorCode](#API_GetCommitmentPurchaseAnalysis_ResponseSyntax) **   <a name="awscostmanagement-GetCommitmentPurchaseAnalysis-response-ErrorCode"></a>
The error code used for the analysis.
Type: String
Valid Values: `NO_USAGE_FOUND | INTERNAL_FAILURE | INVALID_SAVINGS_PLANS_TO_ADD | INVALID_SAVINGS_PLANS_TO_EXCLUDE | INVALID_ACCOUNT_ID`

 ** [EstimatedCompletionTime](#API_GetCommitmentPurchaseAnalysis_ResponseSyntax) **   <a name="awscostmanagement-GetCommitmentPurchaseAnalysis-response-EstimatedCompletionTime"></a>
The estimated time for when the analysis will complete.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`

## Errors
<a name="API_GetCommitmentPurchaseAnalysis_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AnalysisNotFoundException **
The requested analysis can't be found.
HTTP Status Code: 400

 ** DataUnavailableException **
The requested data is unavailable.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## See Also
<a name="API_GetCommitmentPurchaseAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/GetCommitmentPurchaseAnalysis)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/GetCommitmentPurchaseAnalysis)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/GetCommitmentPurchaseAnalysis)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/GetCommitmentPurchaseAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/GetCommitmentPurchaseAnalysis)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/GetCommitmentPurchaseAnalysis)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/GetCommitmentPurchaseAnalysis)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/GetCommitmentPurchaseAnalysis)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/GetCommitmentPurchaseAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/GetCommitmentPurchaseAnalysis)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
