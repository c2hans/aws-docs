---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_StartCommitmentPurchaseAnalysis.html
---

# StartCommitmentPurchaseAnalysis
<a name="API_StartCommitmentPurchaseAnalysis"></a>

Specifies the parameters of a planned commitment purchase and starts the generation of the analysis. This enables you to estimate the cost, coverage, and utilization impact of your planned commitment purchases.

## Request Syntax
<a name="API_StartCommitmentPurchaseAnalysis_RequestSyntax"></a>

```
{
   "CommitmentPurchaseAnalysisConfiguration": {
      "SavingsPlansPurchaseAnalysisConfiguration": {
         "AccountId": "{{string}}",
         "AccountScope": "{{string}}",
         "AnalysisType": "{{string}}",
         "LookBackTimePeriod": {
            "End": "{{string}}",
            "Start": "{{string}}"
         },
         "SavingsPlansTargetCoverage": {{number}},
         "SavingsPlansToAdd": [
            {
               "InstanceFamily": "{{string}}",
               "OfferingId": "{{string}}",
               "PaymentOption": "{{string}}",
               "Region": "{{string}}",
               "SavingsPlansCommitment": {{number}},
               "SavingsPlansType": "{{string}}",
               "TermInYears": "{{string}}"
            }
         ],
         "SavingsPlansToExclude": [ "{{string}}" ]
      }
   }
}
```

## Request Parameters
<a name="API_StartCommitmentPurchaseAnalysis_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CommitmentPurchaseAnalysisConfiguration](#API_StartCommitmentPurchaseAnalysis_RequestSyntax) **   <a name="awscostmanagement-StartCommitmentPurchaseAnalysis-request-CommitmentPurchaseAnalysisConfiguration"></a>
The configuration for the commitment purchase analysis.
Type: [CommitmentPurchaseAnalysisConfiguration](API_CommitmentPurchaseAnalysisConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_StartCommitmentPurchaseAnalysis_ResponseSyntax"></a>

```
{
   "AnalysisId": "string",
   "AnalysisStartedTime": "string",
   "EstimatedCompletionTime": "string"
}
```

## Response Elements
<a name="API_StartCommitmentPurchaseAnalysis_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AnalysisId](#API_StartCommitmentPurchaseAnalysis_ResponseSyntax) **   <a name="awscostmanagement-StartCommitmentPurchaseAnalysis-response-AnalysisId"></a>
The analysis ID that's associated with the commitment purchase analysis.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[\S\s]{8}-[\S\s]{4}-[\S\s]{4}-[\S\s]{4}-[\S\s]{12}$`

 ** [AnalysisStartedTime](#API_StartCommitmentPurchaseAnalysis_ResponseSyntax) **   <a name="awscostmanagement-StartCommitmentPurchaseAnalysis-response-AnalysisStartedTime"></a>
The start time of the analysis.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`

 ** [EstimatedCompletionTime](#API_StartCommitmentPurchaseAnalysis_ResponseSyntax) **   <a name="awscostmanagement-StartCommitmentPurchaseAnalysis-response-EstimatedCompletionTime"></a>
The estimated time for when the analysis will complete.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`

## Errors
<a name="API_StartCommitmentPurchaseAnalysis_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DataUnavailableException **
The requested data is unavailable.
HTTP Status Code: 400

 ** GenerationExistsException **
A request to generate a recommendation or analysis is already in progress.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
 You've reached the limit on the number of resources you can create, or exceeded the size of an individual resource.
HTTP Status Code: 400

## See Also
<a name="API_StartCommitmentPurchaseAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/StartCommitmentPurchaseAnalysis)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/StartCommitmentPurchaseAnalysis)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/StartCommitmentPurchaseAnalysis)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/StartCommitmentPurchaseAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/StartCommitmentPurchaseAnalysis)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/StartCommitmentPurchaseAnalysis)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/StartCommitmentPurchaseAnalysis)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/StartCommitmentPurchaseAnalysis)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/StartCommitmentPurchaseAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/StartCommitmentPurchaseAnalysis)
