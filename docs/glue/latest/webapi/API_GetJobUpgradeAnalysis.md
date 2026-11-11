---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetJobUpgradeAnalysis.html
---

# GetJobUpgradeAnalysis
<a name="API_GetJobUpgradeAnalysis"></a>

Retrieves the current status and results of an upgrade analysis.

## Request Syntax
<a name="API_GetJobUpgradeAnalysis_RequestSyntax"></a>

```
{
   "analysisId": "{{string}}",
   "jobName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetJobUpgradeAnalysis_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [analysisId](#API_GetJobUpgradeAnalysis_RequestSyntax) **   <a name="Glue-GetJobUpgradeAnalysis-request-analysisId"></a>
The unique identifier of the upgrade analysis to retrieve.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `ja-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [jobName](#API_GetJobUpgradeAnalysis_RequestSyntax) **   <a name="Glue-GetJobUpgradeAnalysis-request-jobName"></a>
The name of the job associated with the analysis.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetJobUpgradeAnalysis_ResponseSyntax"></a>

```
{
   "analysisId": "string",
   "analysisType": "string",
   "autoUpgradeEligibilitySummary": "string",
   "autoUpgradeEvaluationSummary": "string",
   "errorMessage": "string",
   "jobName": "string",
   "sourceVersion": "string",
   "status": "string",
   "targetVersion": "string"
}
```

## Response Elements
<a name="API_GetJobUpgradeAnalysis_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analysisId](#API_GetJobUpgradeAnalysis_ResponseSyntax) **   <a name="Glue-GetJobUpgradeAnalysis-response-analysisId"></a>
The unique identifier of the upgrade analysis.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `ja-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [analysisType](#API_GetJobUpgradeAnalysis_ResponseSyntax) **   <a name="Glue-GetJobUpgradeAnalysis-response-analysisType"></a>
The type of upgrade analysis. For auto-upgrade jobs, this value is `AUTO_UPGRADE`.
Type: String
Valid Values: `AUTO_UPGRADE`

 ** [autoUpgradeEligibilitySummary](#API_GetJobUpgradeAnalysis_ResponseSyntax) **   <a name="Glue-GetJobUpgradeAnalysis-response-autoUpgradeEligibilitySummary"></a>
The Amazon S3 URI of the consent report summarizing upgrade assessment findings. Populated when the analysis reaches `WAITING_FOR_CONSENT` and remains available in all subsequent states.
Type: String

 ** [autoUpgradeEvaluationSummary](#API_GetJobUpgradeAnalysis_ResponseSyntax) **   <a name="Glue-GetJobUpgradeAnalysis-response-autoUpgradeEvaluationSummary"></a>
The Amazon S3 URI of the terminal-state evaluation summary, available once the analysis reaches a terminal status (`SUCCEEDED` or `FAILED`).
Type: String

 ** [errorMessage](#API_GetJobUpgradeAnalysis_ResponseSyntax) **   <a name="Glue-GetJobUpgradeAnalysis-response-errorMessage"></a>
The reason the analysis did not complete.
Type: String

 ** [jobName](#API_GetJobUpgradeAnalysis_ResponseSyntax) **   <a name="Glue-GetJobUpgradeAnalysis-response-jobName"></a>
The name of the job associated with this analysis.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [sourceVersion](#API_GetJobUpgradeAnalysis_ResponseSyntax) **   <a name="Glue-GetJobUpgradeAnalysis-response-sourceVersion"></a>
The AWS Glue version the job was running before the upgrade, for example `4.0`.
Type: String

 ** [status](#API_GetJobUpgradeAnalysis_ResponseSyntax) **   <a name="Glue-GetJobUpgradeAnalysis-response-status"></a>
The current status of the analysis.
Type: String
Valid Values: `OBSERVING | WAITING_FOR_CONSENT | UPGRADING | SUCCEEDED | FAILED | TIMEOUT | STOPPED`

 ** [targetVersion](#API_GetJobUpgradeAnalysis_ResponseSyntax) **   <a name="Glue-GetJobUpgradeAnalysis-response-targetVersion"></a>
The AWS Glue version the job will be upgraded to, for example `6.0`.
Type: String

## Errors
<a name="API_GetJobUpgradeAnalysis_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationNotSupportedException **
The operation is not available in the region.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetJobUpgradeAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetJobUpgradeAnalysis)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetJobUpgradeAnalysis)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetJobUpgradeAnalysis)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetJobUpgradeAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetJobUpgradeAnalysis)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetJobUpgradeAnalysis)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetJobUpgradeAnalysis)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetJobUpgradeAnalysis)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetJobUpgradeAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetJobUpgradeAnalysis)
