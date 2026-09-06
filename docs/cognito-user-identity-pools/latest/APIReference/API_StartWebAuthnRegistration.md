---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_StartWebAuthnRegistration.html
---

# StartWebAuthnRegistration
<a name="API_StartWebAuthnRegistration"></a>

Requests credential creation options from your user pool for the currently signed-in user. Returns information about the user pool, the user profile, and authentication requirements. Users must provide this information in their request to enroll your application with their passkey provider.

After users present this data and register with their passkey provider, return the response to your user pool in a [CompleteWebAuthnRegistration](API_CompleteWebAuthnRegistration.md) API request.

Authorize this action with a signed-in user's access token. It must include the scope `aws.cognito.signin.user.admin`.

## Request Syntax
<a name="API_StartWebAuthnRegistration_RequestSyntax"></a>

```
{
   "AccessToken": "{{string}}"
}
```

## Request Parameters
<a name="API_StartWebAuthnRegistration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessToken](#API_StartWebAuthnRegistration_RequestSyntax) **   <a name="CognitoUserPools-StartWebAuthnRegistration-request-AccessToken"></a>
A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for `aws.cognito.signin.user.admin`.
Type: String
Pattern: `[A-Za-z0-9-_=.]+`
Required: Yes

## Response Syntax
<a name="API_StartWebAuthnRegistration_ResponseSyntax"></a>

```
{
   "CredentialCreationOptions": JSON value
}
```

## Response Elements
<a name="API_StartWebAuthnRegistration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CredentialCreationOptions](#API_StartWebAuthnRegistration_ResponseSyntax) **   <a name="CognitoUserPools-StartWebAuthnRegistration-response-CredentialCreationOptions"></a>
The information that a user can provide in their request to register with their passkey provider.
Type: JSON value

## Errors
<a name="API_StartWebAuthnRegistration_Errors"></a>

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

 ** WebAuthnConfigurationMissingException **
This exception is thrown when a user pool doesn't have a configured relying party id or a user pool domain.
HTTP Status Code: 400

 ** WebAuthnNotEnabledException **
This exception is thrown when the passkey feature isn't enabled for the user pool.
HTTP Status Code: 400

## Examples
<a name="API_StartWebAuthnRegistration_Examples"></a>

### Example
<a name="API_StartWebAuthnRegistration_Example_1"></a>

The following example request gets passkey registration options for the current user.

#### Sample Request
<a name="API_StartWebAuthnRegistration_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.StartWebAuthnRegistration
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
    "AccessToken":"eyJra456defEXAMPLE"
}
```

#### Sample Response
<a name="API_StartWebAuthnRegistration_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
    "CredentialCreationOptions": {
        "authenticatorSelection": {
            "requireResidentKey": true,
            "residentKey": "required",
            "userVerification": "preferred"
        },
        "challenge": "wxvbDicyqQqvF2EXAMPLE",
        "excludeCredentials": [
            {
                "id": "8LApgk4-lNUFHbhm2w6Und7-uxcc8coJGsPxiogvHoItc64xWQc3r4CEXAMPLE",
                "type": "public-key"
            }
        ],
        "pubKeyCredParams": [
            {
                "alg": -7,
                "type": "public-key"
            },
            {
                "alg": -257,
                "type": "public-key"
            }
        ],
        "rp": {
            "id": "auth.example.com",
            "name": "auth.example.com"
        },
        "timeout": 60000,
        "user": {
            "displayName": "testuser",
            "id": "ZWFhZDAyMTktMjExNy00MzlmLThkNDYtNGRiMjBlNEXAMPLE",
            "name": "testuser"
        }
    }
}
```

## See Also
<a name="API_StartWebAuthnRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/StartWebAuthnRegistration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/StartWebAuthnRegistration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/StartWebAuthnRegistration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/StartWebAuthnRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/StartWebAuthnRegistration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/StartWebAuthnRegistration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/StartWebAuthnRegistration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/StartWebAuthnRegistration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/StartWebAuthnRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/StartWebAuthnRegistration)
