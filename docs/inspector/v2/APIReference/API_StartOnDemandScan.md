---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_StartOnDemandScan.html
---

# StartOnDemandScan
<a name="API_StartOnDemandScan"></a>

Starts an on-demand scan of the specified resource, such as an Amazon Machine Image (AMI).

## Request Syntax
<a name="API_StartOnDemandScan_RequestSyntax"></a>

```
POST /ondemand/scan HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "resourceId": "{{string}}",
   "resourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartOnDemandScan_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartOnDemandScan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartOnDemandScan_RequestSyntax) **   <a name="inspector2-StartOnDemandScan-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: No

 ** [resourceId](#API_StartOnDemandScan_RequestSyntax) **   <a name="inspector2-StartOnDemandScan-request-resourceId"></a>
The ID of the resource to scan on demand.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1024.
Pattern: `.*(^arn:.*:ecr:.*:\d{12}:repository\/[a-zA-Z0-9._\/-]+(\/sha256:[a-z0-9]{64})?$)|(^i-([a-z0-9]{8}|[a-z0-9]{17}|\\*)$|(^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$)|(^arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration\/[a-f0-9-]{36}\/project-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$))|(^\/subscriptions\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\/resourcegroups\/[a-z0-9_\-\.()]+\/providers\/(microsoft\.compute\/virtualmachines\/[a-z0-9_\-]+|microsoft\.web\/sites\/[a-z0-9_\-]+|microsoft\.containerregistry\/registries\/[a-z0-9_\-]+(\/repositories\/[a-z0-9_\-\/]+\/images?\/sha256:[a-f0-9]{64})?)$).*`
Required: Yes

 ** [resourceType](#API_StartOnDemandScan_RequestSyntax) **   <a name="inspector2-StartOnDemandScan-request-resourceType"></a>
The type of the resource to scan on demand.
Type: String
Valid Values: `AMI`
Required: Yes

## Response Syntax
<a name="API_StartOnDemandScan_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "scanId": "string"
}
```

## Response Elements
<a name="API_StartOnDemandScan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [scanId](#API_StartOnDemandScan_ResponseSyntax) **   <a name="inspector2-StartOnDemandScan-response-scanId"></a>
The unique identifier assigned to the on-demand scan that was started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

## Errors
<a name="API_StartOnDemandScan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** ConflictException **
A conflict occurred. This exception occurs when the same resource is being modified by concurrent requests.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_StartOnDemandScan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/StartOnDemandScan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/StartOnDemandScan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/StartOnDemandScan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/StartOnDemandScan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/StartOnDemandScan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/StartOnDemandScan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/StartOnDemandScan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/StartOnDemandScan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/StartOnDemandScan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/StartOnDemandScan)
