---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html
---

# ReplicateInstance
<a name="API_ReplicateInstance"></a>

Replicates an Connect Customer instance in the specified AWS Region and copies configuration information for Connect Customer resources across AWS Regions.

For more information about replicating an Connect Customer instance, see [Create a replica of your existing Connect Customer instance](https://docs.aws.amazon.com/connect/latest/adminguide/create-replica-connect-instance.html) in the *Connect Customer Administrator Guide*.

## Request Syntax
<a name="API_ReplicateInstance_RequestSyntax"></a>

```
POST /instance/{{InstanceId}}/replicate HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "ReplicaAlias": "{{string}}",
   "ReplicaRegion": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ReplicateInstance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ReplicateInstance_RequestSyntax) **   <a name="connect-ReplicateInstance-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance. You can provide the `InstanceId`, or the entire ARN.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

## Request Body
<a name="API_ReplicateInstance_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_ReplicateInstance_RequestSyntax) **   <a name="connect-ReplicateInstance-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [ReplicaAlias](#API_ReplicateInstance_RequestSyntax) **   <a name="connect-ReplicateInstance-request-ReplicaAlias"></a>
The alias for the replicated instance. The `ReplicaAlias` must be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 45.
Pattern: `^(?!d-)([\da-zA-Z]+)([-]*[\da-zA-Z])*$`
Required: Yes

 ** [ReplicaRegion](#API_ReplicateInstance_RequestSyntax) **   <a name="connect-ReplicateInstance-request-ReplicaRegion"></a>
The AWS Region where to replicate the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 31.
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: Yes

## Response Syntax
<a name="API_ReplicateInstance_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Id": "string"
}
```

## Response Elements
<a name="API_ReplicateInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_ReplicateInstance_ResponseSyntax) **   <a name="connect-ReplicateInstance-response-Arn"></a>
The Amazon Resource Name (ARN) of the replicated instance.
Type: String

 ** [Id](#API_ReplicateInstance_ResponseSyntax) **   <a name="connect-ReplicateInstance-response-Id"></a>
The identifier of the replicated instance. You can find the `instanceId` in the ARN of the instance. The replicated instance has the same identifier as the instance it was replicated from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

## Errors
<a name="API_ReplicateInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceConflictException **
A resource already has that name.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ResourceNotReadyException **
The resource is not ready.
HTTP Status Code: 409

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ReplicateInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ReplicateInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ReplicateInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ReplicateInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ReplicateInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ReplicateInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ReplicateInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ReplicateInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ReplicateInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ReplicateInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ReplicateInstance)
