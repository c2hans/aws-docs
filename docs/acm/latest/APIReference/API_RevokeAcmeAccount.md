---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_RevokeAcmeAccount.html
---

# RevokeAcmeAccount
<a name="API_RevokeAcmeAccount"></a>

Revokes an ACME account, preventing it from requesting or revoking certificates. This operation is irreversible.

## Request Syntax
<a name="API_RevokeAcmeAccount_RequestSyntax"></a>

```
{
   "AccountUrl": "{{string}}",
   "AcmeEndpointArn": "{{string}}"
}
```

## Request Parameters
<a name="API_RevokeAcmeAccount_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AccountUrl](#API_RevokeAcmeAccount_RequestSyntax) **   <a name="ACM-RevokeAcmeAccount-request-AccountUrl"></a>
The URL of the ACME account to revoke.
Type: String
Required: Yes

 ** [AcmeEndpointArn](#API_RevokeAcmeAccount_RequestSyntax) **   <a name="ACM-RevokeAcmeAccount-request-AcmeEndpointArn"></a>
The Amazon Resource Name (ARN) of the ACME endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws[a-z-]*:acm:[a-z0-9-]+:[0-9]{12}:acme-endpoint/[a-zA-Z0-9-]+`
Required: Yes

## Response Elements
<a name="API_RevokeAcmeAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RevokeAcmeAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have access required to perform this action.
HTTP Status Code: 400

 ** ConflictException **
You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified certificate cannot be found in the caller's account or the caller's account cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because it exceeded a quota.
 ** throttlingReasons **
One or more reasons why the request was throttled.
HTTP Status Code: 400

 ** ValidationException **
The supplied input failed to satisfy constraints of an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_RevokeAcmeAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/RevokeAcmeAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/RevokeAcmeAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/RevokeAcmeAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/RevokeAcmeAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/RevokeAcmeAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/RevokeAcmeAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/RevokeAcmeAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/RevokeAcmeAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/RevokeAcmeAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/RevokeAcmeAccount)
