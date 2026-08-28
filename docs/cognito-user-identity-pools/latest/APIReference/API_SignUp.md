---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SignUp.html
---

# SignUp
<a name="API_SignUp"></a>

Registers a user with an app client and requests a user name, password, and user attributes in the user pool.

**Note**
Amazon Cognito doesn't evaluate AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can't use IAM credentials to authorize requests, and you can't grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html).

**Note**
This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with [Amazon Pinpoint](https://console.aws.amazon.com/pinpoint/home/). Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.
If you have never used SMS text messages with Amazon Cognito or any other AWS service, Amazon Simple Notification Service might place your account in the SMS sandbox. In * [sandbox mode](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) *, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see [ SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) in the *Amazon Cognito Developer Guide*.

You might receive a `LimitExceeded` exception in response to this request if you have exceeded a rate quota for email or SMS messages, and if your user pool automatically verifies email addresses or phone numbers. When you get this exception in the response, the user is successfully created and is in an `UNCONFIRMED` state.

You can send a new code with the [ResendConfirmationCode](API_ResendConfirmationCode.md) request, or confirm the user as an administrator with an [AdminConfirmSignUp](API_AdminConfirmSignUp.md) request.

## Request Syntax
<a name="API_SignUp_RequestSyntax"></a>

```
{
   "AnalyticsMetadata": {
      "AnalyticsEndpointId": "{{string}}"
   },
   "ClientId": "{{string}}",
   "ClientMetadata": {
      "{{string}}" : "{{string}}"
   },
   "Password": "{{string}}",
   "SecretHash": "{{string}}",
   "UserAttributes": [
      {
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "UserContextData": {
      "EncodedData": "{{string}}",
      "IpAddress": "{{string}}"
   },
   "Username": "{{string}}",
   "ValidationData": [
      {
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_SignUp_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AnalyticsMetadata](#API_SignUp_RequestSyntax) **   <a name="CognitoUserPools-SignUp-request-AnalyticsMetadata"></a>
Information that supports analytics outcomes with Amazon Pinpoint, including the user's endpoint ID. The endpoint ID is a destination for Amazon Pinpoint push notifications, for example a device identifier, email address, or phone number.
Type: [AnalyticsMetadataType](API_AnalyticsMetadataType.md) object
Required: No

 ** [ClientId](#API_SignUp_RequestSyntax) **   <a name="CognitoUserPools-SignUp-request-ClientId"></a>
The ID of the app client where the user wants to sign up.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: Yes

 ** [ClientMetadata](#API_SignUp_RequestSyntax) **   <a name="CognitoUserPools-SignUp-request-ClientMetadata"></a>
A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers. You create custom workflows by assigning AWS Lambda functions to user pool triggers.
When Amazon Cognito invokes any of these functions, it passes a JSON payload, which the function receives as input. This payload contains a `clientMetadata` attribute that provides the data that you assigned to the ClientMetadata parameter in your request. In your function code, you can process the `clientMetadata` value to enhance your workflow for your specific needs.
To review the Lambda trigger types that Amazon Cognito invokes at runtime with API requests, see [ Connecting API actions to Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-working-with-lambda-triggers.html#lambda-triggers-by-event) in the *Amazon Cognito Developer Guide*.
When you use the `ClientMetadata` parameter, note that Amazon Cognito won't do the following:
+ Store the `ClientMetadata` value. This data is available only to AWS Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration doesn't include triggers, the `ClientMetadata` parameter serves no purpose.
+ Validate the `ClientMetadata` value.
+ Encrypt the `ClientMetadata` value. Don't send sensitive information in this parameter.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 131072.
Value Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** [Password](#API_SignUp_RequestSyntax) **   <a name="CognitoUserPools-SignUp-request-Password"></a>
The user's proposed password. The password must comply with the [password requirements](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users-passwords.html) of your user pool.
Users can sign up without a password when your user pool supports passwordless sign-in with email or SMS OTPs. To create a user with no password, omit this parameter or submit a blank value. You can only create a passwordless user when passwordless sign-in is available.
For more information about passwordless options, see [SignInPolicyType](API_SignInPolicyType.md), a property of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md).
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\S]+`
Required: No

 ** [SecretHash](#API_SignUp_RequestSyntax) **   <a name="CognitoUserPools-SignUp-request-SecretHash"></a>
A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message. For more information about `SecretHash`, see [Computing secret hash values](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#cognito-user-pools-computing-secret-hash).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=/]+`
Required: No

 ** [UserAttributes](#API_SignUp_RequestSyntax) **   <a name="CognitoUserPools-SignUp-request-UserAttributes"></a>
An array of name-value pairs representing user attributes.
For custom attributes, include a `custom:` prefix in the attribute name, for example `custom:department`.
Type: Array of [AttributeType](API_AttributeType.md) objects
Required: No

 ** [UserContextData](#API_SignUp_RequestSyntax) **   <a name="CognitoUserPools-SignUp-request-UserContextData"></a>
Contextual data about your user session like the device fingerprint, IP address, or location. Amazon Cognito threat protection evaluates the risk of an authentication event based on the context that your app generates and passes to Amazon Cognito when it makes API requests.
For more information, see [Collecting data for threat protection in applications](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-viewing-threat-protection-app.html).
Type: [UserContextDataType](API_UserContextDataType.md) object
Required: No

 ** [Username](#API_SignUp_RequestSyntax) **   <a name="CognitoUserPools-SignUp-request-Username"></a>
The username of the user that you want to sign up. The value of this parameter is typically a username, but can be any alias attribute in your user pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** [ValidationData](#API_SignUp_RequestSyntax) **   <a name="CognitoUserPools-SignUp-request-ValidationData"></a>
Temporary user attributes that contribute to the outcomes of your pre sign-up Lambda trigger. This set of key-value pairs are for custom validation of information that you collect from your users but don't need to retain.
Your Lambda function can analyze this additional data and act on it. Your function can automatically confirm and verify select users or perform external API operations like logging user attributes and validation data to Amazon CloudWatch Logs.
For more information about the pre sign-up Lambda trigger, see [Pre sign-up Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html).
Type: Array of [AttributeType](API_AttributeType.md) objects
Required: No

## Response Syntax
<a name="API_SignUp_ResponseSyntax"></a>

```
{
   "CodeDeliveryDetails": {
      "AttributeName": "string",
      "DeliveryMedium": "string",
      "Destination": "string"
   },
   "Session": "string",
   "UserConfirmed": boolean,
   "UserSub": "string"
}
```

## Response Elements
<a name="API_SignUp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CodeDeliveryDetails](#API_SignUp_ResponseSyntax) **   <a name="CognitoUserPools-SignUp-response-CodeDeliveryDetails"></a>
In user pools that automatically verify and confirm new users, Amazon Cognito sends users a message with a code or link that confirms ownership of the phone number or email address that they entered. The `CodeDeliveryDetails` object is information about the delivery destination for that link or code.
Collect this code from the user and submit it in a [ConfirmSignUp](API_ConfirmSignUp.md) request.
Type: [CodeDeliveryDetailsType](API_CodeDeliveryDetailsType.md) object

 ** [Session](#API_SignUp_ResponseSyntax) **   <a name="CognitoUserPools-SignUp-response-Session"></a>
A session Id that you can pass to `ConfirmSignUp` when you want to immediately sign in your user with the `USER_AUTH` flow after they complete sign-up.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [UserConfirmed](#API_SignUp_ResponseSyntax) **   <a name="CognitoUserPools-SignUp-response-UserConfirmed"></a>
Indicates whether the user was automatically confirmed. You can auto-confirm users with a [pre sign-up Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html).
Type: Boolean

 ** [UserSub](#API_SignUp_ResponseSyntax) **   <a name="CognitoUserPools-SignUp-response-UserSub"></a>
The unique identifier of the new user, for example `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.

## Errors
<a name="API_SignUp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CodeDeliveryFailureException **
This exception is thrown when a verification code fails to deliver successfully.
 ** message **
The message sent when a verification code fails to deliver successfully.
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

 ** InvalidEmailRoleAccessPolicyException **
This exception is thrown when Amazon Cognito isn't allowed to use your email identity. HTTP status code: 400.
 ** message **
The message returned when you have an unverified email address or the identity policy isn't set on an email address that Amazon Cognito can access.
HTTP Status Code: 400

 ** InvalidLambdaResponseException **
This exception is thrown when Amazon Cognito encounters an invalid AWS Lambda response.
 ** message **
The message returned when Amazon Cognito throws an invalid AWS Lambda response exception.
HTTP Status Code: 400

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** InvalidPasswordException **
This exception is thrown when Amazon Cognito encounters an invalid password.
 ** message **
The message returned when Amazon Cognito throws an invalid user password exception.
HTTP Status Code: 400

 ** InvalidSmsRoleAccessPolicyException **
This exception is returned when the role provided for SMS configuration doesn't have permission to publish using Amazon SNS.
 ** message **
The message returned when the invalid SMS role access policy exception is thrown.
HTTP Status Code: 400

 ** InvalidSmsRoleTrustRelationshipException **
This exception is thrown when the trust relationship is not valid for the role provided for SMS configuration. This can happen if you don't trust `cognito-idp.amazonaws.com` or the external ID provided in the role does not match what is provided in the SMS configuration for the user pool.
 ** message **
The message returned when the role trust relationship for the SMS message is not valid.
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

 ** UnexpectedLambdaException **
This exception is thrown when Amazon Cognito encounters an unexpected exception with AWS Lambda.
 ** message **
The message returned when Amazon Cognito returns an unexpected Lambda exception.
HTTP Status Code: 400

 ** UserLambdaValidationException **
This exception is thrown when the Amazon Cognito service encounters a user validation exception with the AWS Lambda service.
 ** message **
The message returned when the Amazon Cognito service returns a user validation exception with the Lambda service.
HTTP Status Code: 400

 ** UsernameExistsException **
This exception is thrown when Amazon Cognito encounters a user name that already exists in the user pool.
 ** message **
The message returned when Amazon Cognito throws a user name exists exception.
HTTP Status Code: 400

## Examples
<a name="API_SignUp_Examples"></a>

### Example
<a name="API_SignUp_Example_1"></a>

A sign-up request for the user `mary_major`.

#### Sample Request
<a name="API_SignUp_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.SignUp
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "ClientId": "1example23456789",
    "Username": "mary_major",
    "Password": "<Password>",
    "SecretHash": "<Secret hash>",
    "UserAttributes": [
        {
            "Name": "name",
            "Value": "Mary"
        },
        {
            "Name": "email",
            "Value": "mary_major@example.com"
        },
        {
            "Name": "phone_number",
            "Value": "+12065551212"
        }
    ]
}
```

#### Sample Response
<a name="API_SignUp_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive

{
	"CodeDeliveryDetails": {
		"AttributeName": "email",
		"DeliveryMedium": "EMAIL",
		"Destination": "m***@e***"
	},
	"UserConfirmed": false,
	"UserSub": "44284a5f-66af-4888-b582-fccc213c51fd"
}
```

## See Also
<a name="API_SignUp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/SignUp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/SignUp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/SignUp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/SignUp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/SignUp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/SignUp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/SignUp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/SignUp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/SignUp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/SignUp)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
