---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GetAccountUsage.html
---

# GetAccountUsage
<a name="API_GetAccountUsage"></a>

Retrieves monthly account usage metrics and limits for the AWS account.

## Request Syntax
<a name="API_GetAccountUsage_RequestSyntax"></a>

```
GET /usage/account HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccountUsage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAccountUsage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccountUsage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "monthlyAccountEvaluationHours": {
      "limit": number,
      "usage": number
   },
   "monthlyAccountInvestigationHours": {
      "limit": number,
      "usage": number
   },
   "monthlyAccountOnDemandHours": {
      "limit": number,
      "usage": number
   },
   "monthlyAccountSystemLearningHours": {
      "limit": number,
      "usage": number
   },
   "usagePeriodEndTime": "string",
   "usagePeriodStartTime": "string"
}
```

## Response Elements
<a name="API_GetAccountUsage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [monthlyAccountEvaluationHours](#API_GetAccountUsage_ResponseSyntax) **   <a name="devopsagent-GetAccountUsage-response-monthlyAccountEvaluationHours"></a>
Monthly evaluation hours usage and limit for an account
Type: [UsageMetric](API_UsageMetric.md) object

 ** [monthlyAccountInvestigationHours](#API_GetAccountUsage_ResponseSyntax) **   <a name="devopsagent-GetAccountUsage-response-monthlyAccountInvestigationHours"></a>
Monthly investigation hours usage and limit for an account
Type: [UsageMetric](API_UsageMetric.md) object

 ** [monthlyAccountOnDemandHours](#API_GetAccountUsage_ResponseSyntax) **   <a name="devopsagent-GetAccountUsage-response-monthlyAccountOnDemandHours"></a>
Monthly on-demand hours usage and limit for an account
Type: [UsageMetric](API_UsageMetric.md) object

 ** [monthlyAccountSystemLearningHours](#API_GetAccountUsage_ResponseSyntax) **   <a name="devopsagent-GetAccountUsage-response-monthlyAccountSystemLearningHours"></a>
Monthly system learning hours usage and limit for an account
Type: [UsageMetric](API_UsageMetric.md) object

 ** [usagePeriodEndTime](#API_GetAccountUsage_ResponseSyntax) **   <a name="devopsagent-GetAccountUsage-response-usagePeriodEndTime"></a>
The end time of the usage tracking period
Type: Timestamp

 ** [usagePeriodStartTime](#API_GetAccountUsage_ResponseSyntax) **   <a name="devopsagent-GetAccountUsage-response-usagePeriodStartTime"></a>
The start time of the usage tracking period
Type: Timestamp

## Errors
<a name="API_GetAccountUsage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the requested resource is denied due to insufficient permissions.
 ** message **
Detailed error message describing why access was denied.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** message **
Detailed error message describing the conflict.
HTTP Status Code: 409

 ** ContentSizeExceededException **
This exception is thrown when the content size exceeds the allowed limit.
HTTP Status Code: 413

 ** InternalServerException **
This exception is thrown when an unexpected error occurs in the processing of a request.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more parameters provided in the request are invalid.
 ** message **
Detailed error message describing which parameter is invalid and why.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** message **
Detailed error message describing which resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would exceed the service quota limit.
 ** message **
Detailed error message describing which quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled due to too many requests. Please slow down and try again.
 ** message **
Detailed error message describing the throttling condition.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered while validating the input. A member can appear in this list more than once if it failed to satisfy multiple constraints.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_GetAccountUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/GetAccountUsage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/GetAccountUsage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/GetAccountUsage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/GetAccountUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/GetAccountUsage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/GetAccountUsage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/GetAccountUsage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/GetAccountUsage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/GetAccountUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/GetAccountUsage)
