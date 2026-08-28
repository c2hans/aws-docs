---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AssociateSoftwareToken.html
---

# AssociateSoftwareToken
<a name="API_AssociateSoftwareToken"></a>

Begins setup of time-based one-time password (TOTP) multi-factor authentication (MFA) for a user, with a unique private key that Amazon Cognito generates and returns in the API response. You can authorize an `AssociateSoftwareToken` request with either the user's access token, or a session string from a challenge response that you received from Amazon Cognito.

**Note**
Amazon Cognito disassociates an existing software token when you verify the new token in a [VerifySoftwareToken](API_VerifySoftwareToken.md) API request. If you don't verify the software token and your user pool doesn't require MFA, the user can then authenticate with user name and password credentials alone. If your user pool requires TOTP MFA, Amazon Cognito generates an `MFA_SETUP` or `SOFTWARE_TOKEN_SETUP` challenge each time your user signs in. Complete setup with `AssociateSoftwareToken` and `VerifySoftwareToken`.
After you set up software token MFA for your user, Amazon Cognito generates a `SOFTWARE_TOKEN_MFA` challenge when they authenticate. Respond to this challenge with your user's TOTP.

**Note**
Amazon Cognito doesn't evaluate AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can't use IAM credentials to authorize requests, and you can't grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html).

Authorize this action with a signed-in user's access token. It must include the scope `aws.cognito.signin.user.admin`.

## Request Syntax
<a name="API_AssociateSoftwareToken_RequestSyntax"></a>

```
{
   "AccessToken": "{{string}}",
   "Session": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateSoftwareToken_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessToken](#API_AssociateSoftwareToken_RequestSyntax) **   <a name="CognitoUserPools-AssociateSoftwareToken-request-AccessToken"></a>
A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for `aws.cognito.signin.user.admin`.
You can provide either an access token or a session ID in the request.
Type: String
Pattern: `[A-Za-z0-9-_=.]+`
Required: No

 ** [Session](#API_AssociateSoftwareToken_RequestSyntax) **   <a name="CognitoUserPools-AssociateSoftwareToken-request-Session"></a>
The session identifier that maintains the state of authentication requests and challenge responses. In `AssociateSoftwareToken`, this is the session ID from a successful sign-in. You can provide either an access token or a session ID in the request.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_AssociateSoftwareToken_ResponseSyntax"></a>

```
{
   "SecretCode": "string",
   "Session": "string"
}
```

## Response Elements
<a name="API_AssociateSoftwareToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SecretCode](#API_AssociateSoftwareToken_ResponseSyntax) **   <a name="CognitoUserPools-AssociateSoftwareToken-response-SecretCode"></a>
A unique generated shared secret code that is used by the TOTP algorithm to generate a one-time code.
Type: String
Length Constraints: Minimum length of 16.
Pattern: `[A-Za-z0-9]+`

 ** [Session](#API_AssociateSoftwareToken_ResponseSyntax) **   <a name="CognitoUserPools-AssociateSoftwareToken-response-Session"></a>
The session identifier that maintains the state of authentication requests and challenge responses.
This session ID is valid for the next request in this flow, [VerifySoftwareToken](API_VerifySoftwareToken.md).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

## Errors
<a name="API_AssociateSoftwareToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
This exception is thrown if two or more modifications are happening concurrently.
 ** message **
The message provided when the concurrent exception is thrown.
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

 ** SoftwareTokenMFANotFoundException **
This exception is thrown when the software token time-based one-time password (TOTP) multi-factor authentication (MFA) isn't activated for the user pool.
HTTP Status Code: 400

## Examples
<a name="API_AssociateSoftwareToken_Examples"></a>

### Example
<a name="API_AssociateSoftwareToken_Example_1"></a>

The following example request generates a TOTP private key for the user who the access key was issued to.

#### Sample Request
<a name="API_AssociateSoftwareToken_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AssociateSoftwareToken
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
  "AccessToken": "eyJraACCESSEXAMPLE..."
}
```

#### Sample Response
<a name="API_AssociateSoftwareToken_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
	"SecretCode": "PRIVATECODEEXAMPLE..."
}
```

## See Also
<a name="API_AssociateSoftwareToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AssociateSoftwareToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AssociateSoftwareToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AssociateSoftwareToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AssociateSoftwareToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AssociateSoftwareToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AssociateSoftwareToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AssociateSoftwareToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AssociateSoftwareToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AssociateSoftwareToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AssociateSoftwareToken)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
