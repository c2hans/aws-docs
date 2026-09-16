---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListCommitmentPurchaseAnalyses.html
---

# ListCommitmentPurchaseAnalyses
<a name="API_ListCommitmentPurchaseAnalyses"></a>

Lists the commitment purchase analyses for your account.

## Request Syntax
<a name="API_ListCommitmentPurchaseAnalyses_RequestSyntax"></a>

```
{
   "AnalysisIds": [ "{{string}}" ],
   "AnalysisStatus": "{{string}}",
   "NextPageToken": "{{string}}",
   "PageSize": {{number}}
}
```

## Request Parameters
<a name="API_ListCommitmentPurchaseAnalyses_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AnalysisIds](#API_ListCommitmentPurchaseAnalyses_RequestSyntax) **   <a name="awscostmanagement-ListCommitmentPurchaseAnalyses-request-AnalysisIds"></a>
The analysis IDs associated with the commitment purchase analyses.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 600 items.
Length Constraints: Fixed length of 36.
Pattern: `^[\S\s]{8}-[\S\s]{4}-[\S\s]{4}-[\S\s]{4}-[\S\s]{12}$`
Required: No

 ** [AnalysisStatus](#API_ListCommitmentPurchaseAnalyses_RequestSyntax) **   <a name="awscostmanagement-ListCommitmentPurchaseAnalyses-request-AnalysisStatus"></a>
The status of the analysis.
Type: String
Valid Values: `SUCCEEDED | PROCESSING | FAILED`
Required: No

 ** [NextPageToken](#API_ListCommitmentPurchaseAnalyses_RequestSyntax) **   <a name="awscostmanagement-ListCommitmentPurchaseAnalyses-request-NextPageToken"></a>
The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [PageSize](#API_ListCommitmentPurchaseAnalyses_RequestSyntax) **   <a name="awscostmanagement-ListCommitmentPurchaseAnalyses-request-PageSize"></a>
The number of analyses that you want returned in a single response object.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 600.
Required: No

## Response Syntax
<a name="API_ListCommitmentPurchaseAnalyses_ResponseSyntax"></a>

```
{
   "AnalysisSummaryList": [
      {
         "AnalysisCompletionTime": "string",
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
   ],
   "NextPageToken": "string"
}
```

## Response Elements
<a name="API_ListCommitmentPurchaseAnalyses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AnalysisSummaryList](#API_ListCommitmentPurchaseAnalyses_ResponseSyntax) **   <a name="awscostmanagement-ListCommitmentPurchaseAnalyses-response-AnalysisSummaryList"></a>
The list of analyses.
Type: Array of [AnalysisSummary](API_AnalysisSummary.md) objects

 ** [NextPageToken](#API_ListCommitmentPurchaseAnalyses_ResponseSyntax) **   <a name="awscostmanagement-ListCommitmentPurchaseAnalyses-response-NextPageToken"></a>
The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

## Errors
<a name="API_ListCommitmentPurchaseAnalyses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DataUnavailableException **
The requested data is unavailable.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The pagination token is invalid. Try again without a pagination token.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## See Also
<a name="API_ListCommitmentPurchaseAnalyses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/ListCommitmentPurchaseAnalyses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/ListCommitmentPurchaseAnalyses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ListCommitmentPurchaseAnalyses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/ListCommitmentPurchaseAnalyses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ListCommitmentPurchaseAnalyses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/ListCommitmentPurchaseAnalyses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/ListCommitmentPurchaseAnalyses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/ListCommitmentPurchaseAnalyses)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/ListCommitmentPurchaseAnalyses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ListCommitmentPurchaseAnalyses)
