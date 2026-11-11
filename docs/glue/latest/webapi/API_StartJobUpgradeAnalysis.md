---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StartJobUpgradeAnalysis.html
---

# StartJobUpgradeAnalysis
<a name="API_StartJobUpgradeAnalysis"></a>

Resumes an analysis that is waiting for upgrade consent.

## Request Syntax
<a name="API_StartJobUpgradeAnalysis_RequestSyntax"></a>

```
{
   "analysisId": "{{string}}",
   "jobName": "{{string}}",
   "upgradeConsent": "{{string}}"
}
```

## Request Parameters
<a name="API_StartJobUpgradeAnalysis_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [analysisId](#API_StartJobUpgradeAnalysis_RequestSyntax) **   <a name="Glue-StartJobUpgradeAnalysis-request-analysisId"></a>
The unique identifier of the upgrade analysis. The analysis must be in `WAITING_FOR_CONSENT` status.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `ja-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [jobName](#API_StartJobUpgradeAnalysis_RequestSyntax) **   <a name="Glue-StartJobUpgradeAnalysis-request-jobName"></a>
The name of the job associated with the analysis to resume.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [upgradeConsent](#API_StartJobUpgradeAnalysis_RequestSyntax) **   <a name="Glue-StartJobUpgradeAnalysis-request-upgradeConsent"></a>
The customer's decision on whether to proceed with the upgrade.
Type: String
Valid Values: `APPROVE | DECLINE`
Required: No

## Response Syntax
<a name="API_StartJobUpgradeAnalysis_ResponseSyntax"></a>

```
{
   "analysisId": "string",
   "jobName": "string"
}
```

## Response Elements
<a name="API_StartJobUpgradeAnalysis_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analysisId](#API_StartJobUpgradeAnalysis_ResponseSyntax) **   <a name="Glue-StartJobUpgradeAnalysis-response-analysisId"></a>
The unique identifier of the upgrade analysis.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `ja-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [jobName](#API_StartJobUpgradeAnalysis_ResponseSyntax) **   <a name="Glue-StartJobUpgradeAnalysis-response-jobName"></a>
The name of the job associated with this analysis.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_StartJobUpgradeAnalysis_Errors"></a>

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

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_StartJobUpgradeAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/StartJobUpgradeAnalysis)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/StartJobUpgradeAnalysis)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StartJobUpgradeAnalysis)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/StartJobUpgradeAnalysis)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StartJobUpgradeAnalysis)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/StartJobUpgradeAnalysis)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/StartJobUpgradeAnalysis)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/StartJobUpgradeAnalysis)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/StartJobUpgradeAnalysis)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StartJobUpgradeAnalysis)
