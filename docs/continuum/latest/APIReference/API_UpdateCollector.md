---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_UpdateCollector.html
---

# UpdateCollector
<a name="API_UpdateCollector"></a>

Updates the customer-controlled mutable properties of a Collector. Only the name and Kubernetes cluster IAM role can be changed.

## Request Syntax
<a name="API_UpdateCollector_RequestSyntax"></a>

```
PATCH /collectors/{{collectorId}} HTTP/1.1
Content-type: application/json

{
   "k8ClusterRole": { ... },
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateCollector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [collectorId](#API_UpdateCollector_RequestSyntax) **   <a name="continuum-UpdateCollector-request-uri-collectorId"></a>
The identifier of the collector.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateCollector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [k8ClusterRole](#API_UpdateCollector_RequestSyntax) **   <a name="continuum-UpdateCollector-request-k8ClusterRole"></a>
The kubernetes Cluster Role.
Type: [KubernetesClusterRoleUpdate](API_KubernetesClusterRoleUpdate.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [name](#API_UpdateCollector_RequestSyntax) **   <a name="continuum-UpdateCollector-request-name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## Response Syntax
<a name="API_UpdateCollector_ResponseSyntax"></a>

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
<a name="API_UpdateCollector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collectorArn](#API_UpdateCollector_ResponseSyntax) **   <a name="continuum-UpdateCollector-response-collectorArn"></a>
The Amazon Resource Name (ARN) of the collector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:collectors/[a-z0-9]+`

 ** [collectorId](#API_UpdateCollector_ResponseSyntax) **   <a name="continuum-UpdateCollector-response-collectorId"></a>
The identifier of the collector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [configRecorderArn](#API_UpdateCollector_ResponseSyntax) **   <a name="continuum-UpdateCollector-response-configRecorderArn"></a>
The Amazon Resource Name (ARN) of the config Recorder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:config:[a-z0-9-]+:[0-9]{12}:config(uration)?-recorder/[a-zA-Z0-9_/-]+`

 ** [createdAt](#API_UpdateCollector_ResponseSyntax) **   <a name="continuum-UpdateCollector-response-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp

 ** [k8ClusterRole](#API_UpdateCollector_ResponseSyntax) **   <a name="continuum-UpdateCollector-response-k8ClusterRole"></a>
The Amazon Resource Name (ARN) of the kubernetes Cluster Role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@/-]+`

 ** [status](#API_UpdateCollector_ResponseSyntax) **   <a name="continuum-UpdateCollector-response-status"></a>
The current status of the resource.
Type: String
Valid Values: `ACTIVE | PENDING_DELETION`

 ** [type](#API_UpdateCollector_ResponseSyntax) **   <a name="continuum-UpdateCollector-response-type"></a>
The type.
Type: String
Valid Values: `AWS_COLLECTOR`

 ** [updatedAt](#API_UpdateCollector_ResponseSyntax) **   <a name="continuum-UpdateCollector-response-updatedAt"></a>
The timestamp when the resource was last updated.
Type: Timestamp

## Errors
<a name="API_UpdateCollector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource.
HTTP Status Code: 409

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
<a name="API_UpdateCollector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/UpdateCollector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/UpdateCollector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/UpdateCollector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/UpdateCollector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/UpdateCollector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/UpdateCollector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/UpdateCollector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/UpdateCollector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/UpdateCollector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/UpdateCollector)
