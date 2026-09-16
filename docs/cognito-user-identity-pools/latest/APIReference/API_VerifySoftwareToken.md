---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_VerifySoftwareToken.html
---

# VerifySoftwareToken
<a name="API_VerifySoftwareToken"></a>

Registers the current user's time-based one-time password (TOTP) authenticator with a code generated in their authenticator app from a private key that's supplied by your user pool. Marks the user's software token MFA status as "verified" if successful. The request takes an access token or a session string, but not both.

**Note**
Amazon Cognito doesn't evaluate AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can't use IAM credentials to authorize requests, and you can't grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html).

## Request Syntax
<a name="API_VerifySoftwareToken_RequestSyntax"></a>

```
{
   "AccessToken": "{{string}}",
   "FriendlyDeviceName": "{{string}}",
   "Session": "{{string}}",
   "UserCode": "{{string}}"
}
```

## Request Parameters
<a name="API_VerifySoftwareToken_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessToken](#API_VerifySoftwareToken_RequestSyntax) **   <a name="CognitoUserPools-VerifySoftwareToken-request-AccessToken"></a>
A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for `aws.cognito.signin.user.admin`.
Type: String
Pattern: `[A-Za-z0-9-_=.]+`
Required: No

 ** [FriendlyDeviceName](#API_VerifySoftwareToken_RequestSyntax) **   <a name="CognitoUserPools-VerifySoftwareToken-request-FriendlyDeviceName"></a>
A friendly name for the device that's running the TOTP authenticator.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** [Session](#API_VerifySoftwareToken_RequestSyntax) **   <a name="CognitoUserPools-VerifySoftwareToken-request-Session"></a>
The session ID from an `AssociateSoftwareToken` request.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [UserCode](#API_VerifySoftwareToken_RequestSyntax) **   <a name="CognitoUserPools-VerifySoftwareToken-request-UserCode"></a>
A TOTP that the user generated in their configured authenticator app.
Type: String
Length Constraints: Fixed length of 6.
Pattern: `[0-9]+`
Required: Yes

## Response Syntax
<a name="API_VerifySoftwareToken_ResponseSyntax"></a>

```
{
   "Session": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_VerifySoftwareToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Session](#API_VerifySoftwareToken_ResponseSyntax) **   <a name="CognitoUserPools-VerifySoftwareToken-response-Session"></a>
This session ID satisfies an `MFA_SETUP` challenge. Supply the session ID in your challenge response.
Operations that can return an `MFA_SETUP` challenge include [InitiateAuth](API_InitiateAuth.md), [AdminInitiateAuth](API_AdminInitiateAuth.md), [RespondToAuthChallenge](API_RespondToAuthChallenge.md), and [AdminRespondToAuthChallenge](API_AdminRespondToAuthChallenge.md).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [Status](#API_VerifySoftwareToken_ResponseSyntax) **   <a name="CognitoUserPools-VerifySoftwareToken-response-Status"></a>
Amazon Cognito can accept or reject the code that you provide. This response parameter indicates the success of TOTP verification. Some reasons that this operation might return an error are clock skew on the user's device and excessive retries.
Type: String
Valid Values: `SUCCESS | ERROR`

## Errors
<a name="API_VerifySoftwareToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CodeMismatchException **
This exception is thrown if the provided code doesn't match what the server was expecting.
 ** message **
The message provided when the code mismatch exception is thrown.
HTTP Status Code: 400

 ** EnableSoftwareTokenMFAException **
This exception is thrown when there is a code mismatch and the service fails to configure the software token TOTP multi-factor authentication (MFA).
HTTP Status Code: 400

 ** ForbiddenException **
This exception is thrown when AWS WAF doesn't allow your request based on a web ACL that's associated with your user pool.
 ** message **
The message returned when AWS WAF doesn't allow your request based on a web ACL that's associated with your user pool.
HTTP Status Code: 400

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

 ** InvalidUserPoolConfigurationException **
This exception is thrown when the user pool configuration is not valid.
 ** message **
The message returned when the user pool configuration is not valid.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** OperationNotEnabledException **
This exception is thrown when an operation is not available in the current region or for the current user pool configuration. This can occur when attempting to perform operations that are not supported in secondary replica regions.
HTTP Status Code: 400

 ** PasswordResetRequiredException **
This exception is thrown when a password reset is required.
 ** message **
The message returned when a password reset is required.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when the Amazon Cognito service can't find the requested resource.
 ** message **
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** SoftwareTokenMFANotFoundException **
This exception is thrown when the software token time-based one-time password (TOTP) multi-factor authentication (MFA) isn't activated for the user pool.
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
<a name="API_VerifySoftwareToken_Examples"></a>

### Example
<a name="API_VerifySoftwareToken_Example_1"></a>

The following example request activates TOTP MFA for the current user.

#### Sample Request
<a name="API_VerifySoftwareToken_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.VerifySoftwareToken
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "AccessToken": "eyJra456defEXAMPLE",
   "FriendlyDeviceName": "MyAuthenticatorApp",
   "UserCode": "123456"
}
```

#### Sample Response
<a name="API_VerifySoftwareToken_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
	"Status": "SUCCESS"
}
```

## See Also
<a name="API_VerifySoftwareToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/VerifySoftwareToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/VerifySoftwareToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/VerifySoftwareToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/VerifySoftwareToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/VerifySoftwareToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/VerifySoftwareToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/VerifySoftwareToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/VerifySoftwareToken)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/VerifySoftwareToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/VerifySoftwareToken)
