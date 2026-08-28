---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateSecurityKey.html
---

# AssociateSecurityKey
<a name="API_AssociateSecurityKey"></a>

This API is in preview release for Connect Customer and is subject to change.

Associates a security key to the instance.

## Request Syntax
<a name="API_AssociateSecurityKey_RequestSyntax"></a>

```
PUT /instance/{{InstanceId}}/security-key HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Key": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateSecurityKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_AssociateSecurityKey_RequestSyntax) **   <a name="connect-AssociateSecurityKey-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_AssociateSecurityKey_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_AssociateSecurityKey_RequestSyntax) **   <a name="connect-AssociateSecurityKey-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Key](#API_AssociateSecurityKey_RequestSyntax) **   <a name="connect-AssociateSecurityKey-request-Key"></a>
A valid security key in PEM format as a String.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_AssociateSecurityKey_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AssociationId": "string"
}
```

## Response Elements
<a name="API_AssociateSecurityKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociationId](#API_AssociateSecurityKey_ResponseSyntax) **   <a name="connect-AssociateSecurityKey-response-AssociationId"></a>
The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

## Errors
<a name="API_AssociateSecurityKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

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

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_AssociateSecurityKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/AssociateSecurityKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/AssociateSecurityKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AssociateSecurityKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/AssociateSecurityKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AssociateSecurityKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/AssociateSecurityKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/AssociateSecurityKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/AssociateSecurityKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/AssociateSecurityKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AssociateSecurityKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
