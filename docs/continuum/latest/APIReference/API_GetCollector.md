---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_GetCollector.html
---

# GetCollector
<a name="API_GetCollector"></a>

Retrieves the current state of the Collector for the caller's account.

## Request Syntax
<a name="API_GetCollector_RequestSyntax"></a>

```
GET /collectors/{{collectorId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCollector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [collectorId](#API_GetCollector_RequestSyntax) **   <a name="continuum-GetCollector-request-uri-collectorId"></a>
The identifier of the collector.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_GetCollector_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCollector_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "collectorArn": "string",
   "collectorId": "string",
   "configRecorderArn": "string",
   "createdAt": "string",
   "k8ClusterRole": "string",
   "status": "string",
   "type": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetCollector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collectorArn](#API_GetCollector_ResponseSyntax) **   <a name="continuum-GetCollector-response-collectorArn"></a>
The Amazon Resource Name (ARN) of the collector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:collectors/[a-z0-9]+`

 ** [collectorId](#API_GetCollector_ResponseSyntax) **   <a name="continuum-GetCollector-response-collectorId"></a>
The identifier of the collector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [configRecorderArn](#API_GetCollector_ResponseSyntax) **   <a name="continuum-GetCollector-response-configRecorderArn"></a>
The Amazon Resource Name (ARN) of the config Recorder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:config:[a-z0-9-]+:[0-9]{12}:config(uration)?-recorder/[a-zA-Z0-9_/-]+`

 ** [createdAt](#API_GetCollector_ResponseSyntax) **   <a name="continuum-GetCollector-response-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp

 ** [k8ClusterRole](#API_GetCollector_ResponseSyntax) **   <a name="continuum-GetCollector-response-k8ClusterRole"></a>
The Amazon Resource Name (ARN) of the kubernetes Cluster Role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@/-]+`

 ** [status](#API_GetCollector_ResponseSyntax) **   <a name="continuum-GetCollector-response-status"></a>
The current status of the resource.
Type: String
Valid Values: `ACTIVE | PENDING_DELETION`

 ** [type](#API_GetCollector_ResponseSyntax) **   <a name="continuum-GetCollector-response-type"></a>
The type.
Type: String
Valid Values: `AWS_COLLECTOR`

 ** [updatedAt](#API_GetCollector_ResponseSyntax) **   <a name="continuum-GetCollector-response-updatedAt"></a>
The timestamp when the resource was last updated.
Type: Timestamp

## Errors
<a name="API_GetCollector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_GetCollector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/GetCollector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/GetCollector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/GetCollector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/GetCollector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/GetCollector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/GetCollector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/GetCollector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/GetCollector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/GetCollector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/GetCollector)
