---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_CreateCollector.html
---

# CreateCollector
<a name="API_CreateCollector"></a>

Creates the Collector for the caller's account. Provisions an AWS Config service-linked recorder using the caller's federated access session and begins recording infrastructure changes.

## Request Syntax
<a name="API_CreateCollector_RequestSyntax"></a>

```
POST /collectors HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "k8ClusterRole": {
      "externalId": "{{string}}",
      "roleArn": "{{string}}"
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateCollector_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCollector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateCollector_RequestSyntax) **   <a name="continuum-CreateCollector-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[!-~]{1,128}`
Required: No

 ** [k8ClusterRole](#API_CreateCollector_RequestSyntax) **   <a name="continuum-CreateCollector-request-k8ClusterRole"></a>
The kubernetes Cluster Role.
Type: [KubernetesClusterRoleConfiguration](API_KubernetesClusterRoleConfiguration.md) object
Required: No

 ** [type](#API_CreateCollector_RequestSyntax) **   <a name="continuum-CreateCollector-request-type"></a>
The type.
Type: String
Valid Values: `AWS_COLLECTOR`
Required: No

## Response Syntax
<a name="API_CreateCollector_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "collectorArn": "string",
   "collectorId": "string",
   "createdAt": "string",
   "status": "string",
   "type": "string"
}
```

## Response Elements
<a name="API_CreateCollector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [collectorArn](#API_CreateCollector_ResponseSyntax) **   <a name="continuum-CreateCollector-response-collectorArn"></a>
The Amazon Resource Name (ARN) of the collector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:collectors/[a-z0-9]+`

 ** [collectorId](#API_CreateCollector_ResponseSyntax) **   <a name="continuum-CreateCollector-response-collectorId"></a>
The identifier of the collector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`

 ** [createdAt](#API_CreateCollector_ResponseSyntax) **   <a name="continuum-CreateCollector-response-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp

 ** [status](#API_CreateCollector_ResponseSyntax) **   <a name="continuum-CreateCollector-response-status"></a>
The current status of the resource.
Type: String
Valid Values: `ACTIVE | PENDING_DELETION`

 ** [type](#API_CreateCollector_ResponseSyntax) **   <a name="continuum-CreateCollector-response-type"></a>
The type.
Type: String
Valid Values: `AWS_COLLECTOR`

## Errors
<a name="API_CreateCollector_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would exceed a service quota. Review your quota and request an increase if needed.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_CreateCollector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/CreateCollector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/CreateCollector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/CreateCollector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/CreateCollector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/CreateCollector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/CreateCollector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/CreateCollector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/CreateCollector)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/CreateCollector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/CreateCollector)
