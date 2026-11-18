---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetOnDemandScanStatus.html
---

# GetOnDemandScanStatus
<a name="API_GetOnDemandScanStatus"></a>

Retrieves the status of a specific on-demand scan for a resource.

## Request Syntax
<a name="API_GetOnDemandScanStatus_RequestSyntax"></a>

```
POST /ondemand/scan/status HTTP/1.1
Content-type: application/json

{
   "resourceId": "{{string}}",
   "resourceType": "{{string}}",
   "scanId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetOnDemandScanStatus_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetOnDemandScanStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceId](#API_GetOnDemandScanStatus_RequestSyntax) **   <a name="inspector2-GetOnDemandScanStatus-request-resourceId"></a>
The ID of the resource whose on-demand scan status is being requested.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1024.
Pattern: `.*(^arn:.*:ecr:.*:\d{12}:repository\/[a-zA-Z0-9._\/-]+(\/sha256:[a-z0-9]{64})?$)|(^i-([a-z0-9]{8}|[a-z0-9]{17}|\\*)$|(^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$)|(^arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration\/[a-f0-9-]{36}\/project-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$))|(^\/subscriptions\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\/resourcegroups\/[a-z0-9_\-\.()]+\/providers\/(microsoft\.compute\/virtualmachines\/[a-z0-9_\-]+|microsoft\.web\/sites\/[a-z0-9_\-]+|microsoft\.containerregistry\/registries\/[a-z0-9_\-]+(\/repositories\/[a-z0-9_\-\/]+\/images?\/sha256:[a-f0-9]{64})?)$).*`
Required: Yes

 ** [resourceType](#API_GetOnDemandScanStatus_RequestSyntax) **   <a name="inspector2-GetOnDemandScanStatus-request-resourceType"></a>
The type of the resource whose on-demand scan status is being requested.
Type: String
Valid Values: `AMI`
Required: Yes

 ** [scanId](#API_GetOnDemandScanStatus_RequestSyntax) **   <a name="inspector2-GetOnDemandScanStatus-request-scanId"></a>
The unique identifier of the on-demand scan whose status is being requested.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_GetOnDemandScanStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "completedAt": "string",
   "resourceId": "string",
   "resourceType": "string",
   "scanId": "string",
   "scanStatus": "string",
   "scanStatusReason": "string",
   "startedAt": "string"
}
```

## Response Elements
<a name="API_GetOnDemandScanStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [completedAt](#API_GetOnDemandScanStatus_ResponseSyntax) **   <a name="inspector2-GetOnDemandScanStatus-response-completedAt"></a>
The date and time, in ISO 8601 format, when the on-demand scan completed. This field is absent if the scan has not completed.
Type: Timestamp

 ** [resourceId](#API_GetOnDemandScanStatus_ResponseSyntax) **   <a name="inspector2-GetOnDemandScanStatus-response-resourceId"></a>
The ID of the resource that was scanned.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1024.
Pattern: `.*(^arn:.*:ecr:.*:\d{12}:repository\/[a-zA-Z0-9._\/-]+(\/sha256:[a-z0-9]{64})?$)|(^i-([a-z0-9]{8}|[a-z0-9]{17}|\\*)$|(^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$)|(^arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration\/[a-f0-9-]{36}\/project-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$))|(^\/subscriptions\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\/resourcegroups\/[a-z0-9_\-\.()]+\/providers\/(microsoft\.compute\/virtualmachines\/[a-z0-9_\-]+|microsoft\.web\/sites\/[a-z0-9_\-]+|microsoft\.containerregistry\/registries\/[a-z0-9_\-]+(\/repositories\/[a-z0-9_\-\/]+\/images?\/sha256:[a-f0-9]{64})?)$).*`

 ** [resourceType](#API_GetOnDemandScanStatus_ResponseSyntax) **   <a name="inspector2-GetOnDemandScanStatus-response-resourceType"></a>
The type of the resource that was scanned.
Type: String
Valid Values: `AMI`

 ** [scanId](#API_GetOnDemandScanStatus_ResponseSyntax) **   <a name="inspector2-GetOnDemandScanStatus-response-scanId"></a>
The unique identifier of the on-demand scan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [scanStatus](#API_GetOnDemandScanStatus_ResponseSyntax) **   <a name="inspector2-GetOnDemandScanStatus-response-scanStatus"></a>
The current status of the on-demand scan.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED`

 ** [scanStatusReason](#API_GetOnDemandScanStatus_ResponseSyntax) **   <a name="inspector2-GetOnDemandScanStatus-response-scanStatusReason"></a>
The reason associated with the current on-demand scan status.
Type: String
Valid Values: `ACCESS_DENIED | INTERNAL_ERROR | STORAGE_LIMIT_EXCEEDED | EXTRACTION_COLLECTION_TIME_LIMIT_EXCEEDED | UNSUPPORTED_OS | RESOURCE_TERMINATED`

 ** [startedAt](#API_GetOnDemandScanStatus_ResponseSyntax) **   <a name="inspector2-GetOnDemandScanStatus-response-startedAt"></a>
The date and time, in ISO 8601 format, when the on-demand scan started.
Type: Timestamp

## Errors
<a name="API_GetOnDemandScanStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access an invalid resource. Make sure the resource is specified correctly.
HTTP Status Code: 404

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
<a name="API_GetOnDemandScanStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/GetOnDemandScanStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/GetOnDemandScanStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GetOnDemandScanStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/GetOnDemandScanStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GetOnDemandScanStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/GetOnDemandScanStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/GetOnDemandScanStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/GetOnDemandScanStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/GetOnDemandScanStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GetOnDemandScanStatus)
