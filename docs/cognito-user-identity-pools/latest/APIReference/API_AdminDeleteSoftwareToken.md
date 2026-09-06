---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminDeleteSoftwareToken.html
---

# AdminDeleteSoftwareToken
<a name="API_AdminDeleteSoftwareToken"></a>

Deletes a user's registered time-based one-time password (TOTP) multi-factor authentication (MFA) factor, also known as a software token. After this operation, the user can no longer sign in with TOTP MFA, and can register a new TOTP factor with `AssociateSoftwareToken`. Use this operation when a user loses access to their TOTP-generating device, for example, a lost or reset phone, and needs to register a new one.

Removes the user's software token registration and any preference for TOTP MFA. It doesn't deactivate the other MFA factors that the user has registered. To change which of a user's factors are active or preferred, use [AdminSetUserMFAPreference](API_AdminSetUserMFAPreference.md).

After you delete a user's software token, their next sign-in depends on your user pool MFA configuration and the factors that remain. When your user pool requires MFA and the user has no other factor available, Amazon Cognito returns an `MFA_SETUP` challenge at the next sign-in. The user must then register a new MFA factor. When the user has another factor available, such as SMS or email message MFA, sign-in falls back to that factor. For more information, see [TOTP software token MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa-totp.html).

If your user still has access to their TOTP-generating device, you don't need to delete their software token to replace it. Amazon Cognito disassociates the existing software token when your user verifies a new token in a [VerifySoftwareToken](API_VerifySoftwareToken.md) request. Use this operation when the user can't sign in to complete that flow.

Returns a `ResourceNotFoundException` when the user has no software token registration to delete.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_AdminDeleteSoftwareToken_RequestSyntax"></a>

```
{
   "Username": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_AdminDeleteSoftwareToken_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Username](#API_AdminDeleteSoftwareToken_RequestSyntax) **   <a name="CognitoUserPools-AdminDeleteSoftwareToken-request-Username"></a>
The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If `username` isn't an alias attribute in your user pool, this value must be the `sub` of a local user or the username of a user from a third-party IdP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** [UserPoolId](#API_AdminDeleteSoftwareToken_RequestSyntax) **   <a name="CognitoUserPools-AdminDeleteSoftwareToken-request-UserPoolId"></a>
The ID of the user pool where you want to delete the user's software token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Elements
<a name="API_AdminDeleteSoftwareToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AdminDeleteSoftwareToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** OperationNotEnabledException **
This exception is thrown when an operation is not available in the current region or for the current user pool configuration. This can occur when attempting to perform operations that are not supported in secondary replica regions.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when the Amazon Cognito service can't find the requested resource.
 ** message **
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

 ** UserNotConfirmedException **
This exception is thrown when a user isn't confirmed successfully.
 ** message **
The message returned when a user isn't confirmed successfully.
HTTP Status Code: 400

 ** UserNotFoundException **
This exception is thrown when a user isn't found.
 ** message **
The message returned when a user isn't found.
HTTP Status Code: 400

## Examples
<a name="API_AdminDeleteSoftwareToken_Examples"></a>

### Example
<a name="API_AdminDeleteSoftwareToken_Example_1"></a>

The following example request deletes the software token of the user "testuser." After this request, "testuser" no longer has TOTP MFA activated and can register a new TOTP factor.

#### Sample Request
<a name="API_AdminDeleteSoftwareToken_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminDeleteSoftwareToken
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
  "UserPoolId": "us-west-2_EXAMPLE",
  "Username": "testuser"
}
```

#### Sample Response
<a name="API_AdminDeleteSoftwareToken_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{}
```

## See Also
<a name="API_AdminDeleteSoftwareToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AdminDeleteSoftwareToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AdminDeleteSoftwareToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AdminDeleteSoftwareToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AdminDeleteSoftwareToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AdminDeleteSoftwareToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AdminDeleteSoftwareToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AdminDeleteSoftwareToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AdminDeleteSoftwareToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AdminDeleteSoftwareToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AdminDeleteSoftwareToken)
