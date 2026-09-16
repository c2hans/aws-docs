---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_CreateIdentitySource.html
---

# CreateIdentitySource
<a name="API_CreateIdentitySource"></a>

Creates a new identity source. For more information, see [Identity Source](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html) in the *Multi-party approval User Guide*.

## Request Syntax
<a name="API_CreateIdentitySource_RequestSyntax"></a>

```
POST /identity-sources HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "IdentitySourceParameters": {
      "IamIdentityCenter": {
         "InstanceArn": "{{string}}",
         "Region": "{{string}}"
      }
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateIdentitySource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateIdentitySource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateIdentitySource_RequestSyntax) **   <a name="mpa-CreateIdentitySource-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS populates this field.
 **What is idempotency?**
When you make a mutating API request, the request typically returns a result before the operation's asynchronous workflows have completed. Operations might also time out or encounter other server issues before they complete, even though the request has already returned a result. This could make it difficult to determine whether the request succeeded or not, and could lead to multiple retries to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation is completed multiple times. This means that you might create more resources than you intended.
 *Idempotency* ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [IdentitySourceParameters](#API_CreateIdentitySource_RequestSyntax) **   <a name="mpa-CreateIdentitySource-request-IdentitySourceParameters"></a>
A ` IdentitySourceParameters` object. Contains details for the resource that provides identities to the identity source. For example, an IAM Identity Center instance.
Type: [IdentitySourceParameters](API_IdentitySourceParameters.md) object
Required: Yes

 ** [Tags](#API_CreateIdentitySource_RequestSyntax) **   <a name="mpa-CreateIdentitySource-request-Tags"></a>
Tag you want to attach to the identity source.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateIdentitySource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": "string",
   "IdentitySourceArn": "string",
   "IdentitySourceType": "string"
}
```

## Response Elements
<a name="API_CreateIdentitySource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_CreateIdentitySource_ResponseSyntax) **   <a name="mpa-CreateIdentitySource-response-CreationTime"></a>
Timestamp when the identity source was created.
Type: Timestamp

 ** [IdentitySourceArn](#API_CreateIdentitySource_ResponseSyntax) **   <a name="mpa-CreateIdentitySource-response-IdentitySourceArn"></a>
Amazon Resource Name (ARN) for the identity source that was created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [IdentitySourceType](#API_CreateIdentitySource_ResponseSyntax) **   <a name="mpa-CreateIdentitySource-response-IdentitySourceType"></a>
The type of resource that provided identities to the identity source. For example, an IAM Identity Center instance.
Type: String
Valid Values: `IAM_IDENTITY_CENTER`

## Errors
<a name="API_CreateIdentitySource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You do not have sufficient access to perform this action. Check your permissions, and try again.
 ** Message **
Message for the `AccessDeniedException` error.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error. Try your request again. If the problem persists, contact AWS Support.
 ** Message **
Message for the `InternalServerException` error.
HTTP Status Code: 500

 [ServiceQuotaExceededException](API_ServiceQuotaExceededException.md)
The request exceeds the service quota for your account. Request a quota increase or reduce your request size.
 ** Message **
Message for the `ServiceQuotaExceededException` error.
HTTP Status Code: 402

 [ThrottlingException](API_ThrottlingException.md)
The request was denied due to request throttling.
 ** Message **
Message for the `ThrottlingException` error.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
The input fails to satisfy the constraints specified by an AWS service.
 ** Message **
Message for the `ValidationException` error.
HTTP Status Code: 400

## See Also
<a name="API_CreateIdentitySource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mpa-2022-07-26/CreateIdentitySource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mpa-2022-07-26/CreateIdentitySource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/CreateIdentitySource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mpa-2022-07-26/CreateIdentitySource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/CreateIdentitySource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mpa-2022-07-26/CreateIdentitySource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mpa-2022-07-26/CreateIdentitySource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mpa-2022-07-26/CreateIdentitySource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mpa-2022-07-26/CreateIdentitySource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/CreateIdentitySource)
