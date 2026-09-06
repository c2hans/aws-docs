---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_DeleteIdentitySource.html
---

# DeleteIdentitySource
<a name="API_DeleteIdentitySource"></a>

Deletes an identity source. For more information, see [Identity Source](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html) in the *Multi-party approval User Guide*.

## Request Syntax
<a name="API_DeleteIdentitySource_RequestSyntax"></a>

```
DELETE /identity-sources/{{IdentitySourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteIdentitySource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [IdentitySourceArn](#API_DeleteIdentitySource_RequestSyntax) **   <a name="mpa-DeleteIdentitySource-request-uri-IdentitySourceArn"></a>
Amazon Resource Name (ARN) for identity source.
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

## Request Body
<a name="API_DeleteIdentitySource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteIdentitySource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteIdentitySource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteIdentitySource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You do not have sufficient access to perform this action. Check your permissions, and try again.
 ** Message **
Message for the `AccessDeniedException` error.
HTTP Status Code: 403

 [ConflictException](API_ConflictException.md)
The request cannot be completed because it conflicts with the current state of a resource.
 ** Message **
Message for the `ConflictException` error.
HTTP Status Code: 409

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error. Try your request again. If the problem persists, contact AWS Support.
 ** Message **
Message for the `InternalServerException` error.
HTTP Status Code: 500

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
<a name="API_DeleteIdentitySource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mpa-2022-07-26/DeleteIdentitySource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mpa-2022-07-26/DeleteIdentitySource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/DeleteIdentitySource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mpa-2022-07-26/DeleteIdentitySource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/DeleteIdentitySource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mpa-2022-07-26/DeleteIdentitySource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mpa-2022-07-26/DeleteIdentitySource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mpa-2022-07-26/DeleteIdentitySource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mpa-2022-07-26/DeleteIdentitySource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/DeleteIdentitySource)
