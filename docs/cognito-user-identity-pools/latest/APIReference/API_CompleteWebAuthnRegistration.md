---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CompleteWebAuthnRegistration.html
---

# CompleteWebAuthnRegistration
<a name="API_CompleteWebAuthnRegistration"></a>

Completes registration of a passkey authenticator for the currently signed-in user.

Your application provides data from a successful registration request with the data from the output of a [StartWebAuthnRegistration](API_StartWebAuthnRegistration.md).

Authorize this action with a signed-in user's access token. It must include the scope `aws.cognito.signin.user.admin`.

## Request Syntax
<a name="API_CompleteWebAuthnRegistration_RequestSyntax"></a>

```
{
   "AccessToken": "{{string}}",
   "Credential": {{JSON value}}
}
```

## Request Parameters
<a name="API_CompleteWebAuthnRegistration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessToken](#API_CompleteWebAuthnRegistration_RequestSyntax) **   <a name="CognitoUserPools-CompleteWebAuthnRegistration-request-AccessToken"></a>
A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for `aws.cognito.signin.user.admin`.
Type: String
Pattern: `[A-Za-z0-9-_=.]+`
Required: Yes

 ** [Credential](#API_CompleteWebAuthnRegistration_RequestSyntax) **   <a name="CognitoUserPools-CompleteWebAuthnRegistration-request-Credential"></a>
A [RegistrationResponseJSON](https://www.w3.org/TR/WebAuthn-3/#dictdef-registrationresponsejson) public-key credential response from the user's passkey provider.
Type: JSON value
Required: Yes

## Response Elements
<a name="API_CompleteWebAuthnRegistration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CompleteWebAuthnRegistration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** LimitExceededException **
This exception is thrown when a user exceeds the limit for a requested AWS resource.
 ** message **
The message returned when Amazon Cognito throws a limit exceeded exception.
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

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

 ** WebAuthnChallengeNotFoundException **
This exception is thrown when the challenge from `StartWebAuthn` registration has expired.
HTTP Status Code: 400

 ** WebAuthnClientMismatchException **
This exception is thrown when the access token is for a different client than the one in the original `StartWebAuthnRegistration` request.
HTTP Status Code: 400

 ** WebAuthnCredentialNotSupportedException **
This exception is thrown when a user presents passkey credentials from an unsupported device or provider.
HTTP Status Code: 400

 ** WebAuthnNotEnabledException **
This exception is thrown when the passkey feature isn't enabled for the user pool.
HTTP Status Code: 400

 ** WebAuthnOriginNotAllowedException **
This exception is thrown when the passkey credential's registration origin does not align with the user pool relying party id.
HTTP Status Code: 400

 ** WebAuthnRelyingPartyMismatchException **
This exception is thrown when the given passkey credential is associated with a different relying party ID than the user pool relying party ID.
HTTP Status Code: 400

## Examples
<a name="API_CompleteWebAuthnRegistration_Examples"></a>

### Example
<a name="API_CompleteWebAuthnRegistration_Example_1"></a>

The following example completes passkey registration for the user with access token "eyJra456defEXAMPLE".

#### Sample Request
<a name="API_CompleteWebAuthnRegistration_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.CompleteWebAuthnRegistration
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "AccessToken": "eyJra456defEXAMPLE",
   "Credential": "[RegistrationResponseJSON]"
}
```

## See Also
<a name="API_CompleteWebAuthnRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/CompleteWebAuthnRegistration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/CompleteWebAuthnRegistration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/CompleteWebAuthnRegistration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/CompleteWebAuthnRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/CompleteWebAuthnRegistration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/CompleteWebAuthnRegistration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/CompleteWebAuthnRegistration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/CompleteWebAuthnRegistration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/CompleteWebAuthnRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/CompleteWebAuthnRegistration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
