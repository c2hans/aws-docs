---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminCreateUser.html
---

# AdminCreateUser
<a name="API_AdminCreateUser"></a>

Creates a new user in the specified user pool.

If `MessageAction` isn't set, the default is to send a welcome message via email or phone (SMS).

This message is based on a template that you configured in your call to create or update a user pool. This template includes your custom sign-up instructions and placeholders for user name and temporary password.

Alternatively, you can call `AdminCreateUser` with `SUPPRESS` for the `MessageAction` parameter, and Amazon Cognito won't send any email.

In either case, if the user has a password, they will be in the `FORCE_CHANGE_PASSWORD` state until they sign in and set their password. Your invitation message template must have the `{####}` password placeholder if your users have passwords. If your template doesn't have this placeholder, Amazon Cognito doesn't deliver the invitation message. In this case, you must update your message template and resend the password with a new `AdminCreateUser` request with a `MessageAction` value of `RESEND`.

**Note**
This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with [Amazon Pinpoint](https://console.aws.amazon.com/pinpoint/home/). Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.
If you have never used SMS text messages with Amazon Cognito or any other AWS service, Amazon Simple Notification Service might place your account in the SMS sandbox. In * [sandbox mode](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) *, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see [ SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) in the *Amazon Cognito Developer Guide*.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_AdminCreateUser_RequestSyntax"></a>

```
{
   "ClientMetadata": {
      "{{string}}" : "{{string}}"
   },
   "DesiredDeliveryMediums": [ "{{string}}" ],
   "ForceAliasCreation": {{boolean}},
   "MessageAction": "{{string}}",
   "TemporaryPassword": "{{string}}",
   "UserAttributes": [
      {
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Username": "{{string}}",
   "UserPoolId": "{{string}}",
   "ValidationData": [
      {
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_AdminCreateUser_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientMetadata](#API_AdminCreateUser_RequestSyntax) **   <a name="CognitoUserPools-AdminCreateUser-request-ClientMetadata"></a>
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

 ** [DesiredDeliveryMediums](#API_AdminCreateUser_RequestSyntax) **   <a name="CognitoUserPools-AdminCreateUser-request-DesiredDeliveryMediums"></a>
Specify `EMAIL` if email will be used to send the welcome message. Specify `SMS` if the phone number will be used. The default value is `SMS`. You can specify more than one value.
Type: Array of strings
Valid Values: `SMS | EMAIL`
Required: No

 ** [ForceAliasCreation](#API_AdminCreateUser_RequestSyntax) **   <a name="CognitoUserPools-AdminCreateUser-request-ForceAliasCreation"></a>
This parameter is used only if the `phone_number_verified` or `email_verified` attribute is set to `True`. Otherwise, it is ignored.
If this parameter is set to `True` and the phone number or email address specified in the `UserAttributes` parameter already exists as an alias with a different user, this request migrates the alias from the previous user to the newly-created user. The previous user will no longer be able to log in using that alias.
If this parameter is set to `False`, the API throws an `AliasExistsException` error if the alias already exists. The default value is `False`.
Type: Boolean
Required: No

 ** [MessageAction](#API_AdminCreateUser_RequestSyntax) **   <a name="CognitoUserPools-AdminCreateUser-request-MessageAction"></a>
Set to `RESEND` to resend the invitation message to a user that already exists, and to reset the temporary-password duration with a new temporary password. Set to `SUPPRESS` to suppress sending the message. You can specify only one value.
Type: String
Valid Values: `RESEND | SUPPRESS`
Required: No

 ** [TemporaryPassword](#API_AdminCreateUser_RequestSyntax) **   <a name="CognitoUserPools-AdminCreateUser-request-TemporaryPassword"></a>
The user's temporary password. This password must conform to the password policy that you specified when you created the user pool.
The exception to the requirement for a password is when your user pool supports passwordless sign-in with email or SMS OTPs. To create a user with no password, omit this parameter or submit a blank value. You can only create a passwordless user when passwordless sign-in is available.
For enabling passwordless factors, see [CreateUserPool:Policies](API_CreateUserPool.md#CognitoUserPools-CreateUserPool-request-Policies) and [UpdateUserPool:Policies](API_UpdateUserPool.md#CognitoUserPools-UpdateUserPool-request-Policies).
The temporary password is valid only once. To complete the Admin Create User flow, the user must enter the temporary password in the sign-in page, along with a new password to be used in all future sign-ins.
If you don't specify a value, Amazon Cognito generates one for you unless you have passwordless options active for your user pool.
The temporary password can only be used until the user account expiration limit that you set for your user pool. To reset the account after that time limit, you must call `AdminCreateUser` again and specify `RESEND` for the `MessageAction` parameter.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\S]+`
Required: No

 ** [UserAttributes](#API_AdminCreateUser_RequestSyntax) **   <a name="CognitoUserPools-AdminCreateUser-request-UserAttributes"></a>
An array of name-value pairs that contain user attributes and attribute values to be set for the user to be created. You can create a user without specifying any attributes other than `Username`. However, any attributes that you specify as required (when creating a user pool or in the **Attributes** tab of the console) either you should supply (in your call to `AdminCreateUser`) or the user should supply (when they sign up in response to your welcome message).
For custom attributes, you must prepend the `custom:` prefix to the attribute name.
To send a message inviting the user to sign up, you must specify the user's email address or phone number. You can do this in your call to AdminCreateUser or in the **Users** tab of the Amazon Cognito console for managing your user pools.
You must also provide an email address or phone number when you expect the user to do passwordless sign-in with an email or SMS OTP. These attributes must be provided when passwordless options are the only available, or when you don't submit a `TemporaryPassword`.
In your `AdminCreateUser` request, you can set the `email_verified` and `phone_number_verified` attributes to `true`. The following conditions apply:
email
The email address where you want the user to receive their confirmation code and username. You must provide a value for `email` when you want to set `email_verified` to `true`, or if you set `EMAIL` in the `DesiredDeliveryMediums` parameter.
phone\_number
The phone number where you want the user to receive their confirmation code and username. You must provide a value for `phone_number` when you want to set `phone_number_verified` to `true`, or if you set `SMS` in the `DesiredDeliveryMediums` parameter.
You can also set attributes verified with [AdminUpdateUserAttributes](API_AdminUpdateUserAttributes.md).
Type: Array of [AttributeType](API_AttributeType.md) objects
Required: No

 ** [Username](#API_AdminCreateUser_RequestSyntax) **   <a name="CognitoUserPools-AdminCreateUser-request-Username"></a>
The value that you want to set as the username sign-in attribute. The following conditions apply to the username parameter.
+ The username can't be a duplicate of another username in the same user pool.
+ You can't change the value of a username after you create it.
+ You can only provide a value if usernames are a valid sign-in attribute for your user pool. If your user pool only supports phone numbers or email addresses as sign-in attributes, Amazon Cognito automatically generates a username value. For more information, see [Customizing sign-in attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#user-pool-settings-aliases).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** [UserPoolId](#API_AdminCreateUser_RequestSyntax) **   <a name="CognitoUserPools-AdminCreateUser-request-UserPoolId"></a>
The ID of the user pool where you want to create a user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

 ** [ValidationData](#API_AdminCreateUser_RequestSyntax) **   <a name="CognitoUserPools-AdminCreateUser-request-ValidationData"></a>
Temporary user attributes that contribute to the outcomes of your pre sign-up Lambda trigger. This set of key-value pairs are for custom validation of information that you collect from your users but don't need to retain.
Your Lambda function can analyze this additional data and act on it. Your function can automatically confirm and verify select users or perform external API operations like logging user attributes and validation data to Amazon CloudWatch Logs.
For more information about the pre sign-up Lambda trigger, see [Pre sign-up Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html).
Type: Array of [AttributeType](API_AttributeType.md) objects
Required: No

## Response Syntax
<a name="API_AdminCreateUser_ResponseSyntax"></a>

```
{
   "User": {
      "Attributes": [
         {
            "Name": "string",
            "Value": "string"
         }
      ],
      "Enabled": boolean,
      "MFAOptions": [
         {
            "AttributeName": "string",
            "DeliveryMedium": "string"
         }
      ],
      "UserCreateDate": number,
      "UserLastModifiedDate": number,
      "Username": "string",
      "UserStatus": "string"
   }
}
```

## Response Elements
<a name="API_AdminCreateUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [User](#API_AdminCreateUser_ResponseSyntax) **   <a name="CognitoUserPools-AdminCreateUser-response-User"></a>
The new user's profile details.
Type: [UserType](API_UserType.md) object

## Errors
<a name="API_AdminCreateUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CodeDeliveryFailureException **
This exception is thrown when a verification code fails to deliver successfully.
 ** message **
The message sent when a verification code fails to deliver successfully.
HTTP Status Code: 400

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

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

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** OperationNotEnabledException **
This exception is thrown when an operation is not available in the current region or for the current user pool configuration. This can occur when attempting to perform operations that are not supported in secondary replica regions.
HTTP Status Code: 400

 ** PreconditionNotMetException **
This exception is thrown when a precondition is not met.
 ** message **
The message returned when a precondition is not met.
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

 ** UnsupportedUserStateException **
The request failed because the user is in an unsupported state.
 ** message **
The message returned when the user is in an unsupported state.
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

 ** UserNotFoundException **
This exception is thrown when a user isn't found.
 ** message **
The message returned when a user isn't found.
HTTP Status Code: 400

## Examples
<a name="API_AdminCreateUser_Examples"></a>

### Example
<a name="API_AdminCreateUser_Example_1"></a>

An AdminCreateUser request for for a test user named John.

#### Sample Request
<a name="API_AdminCreateUser_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminCreateUser
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "UserPoolId": "us-east-1_EXAMPLE",
    "Username": "testuser",
    "DesiredDeliveryMediums": [
        "SMS"
    ],
    "MessageAction": "SUPPRESS",
    "TemporaryPassword": "This-is-my-test-99!",
    "UserAttributes": [
        {
            "Name": "name",
            "Value": "John"
        },
        {
            "Name": "phone_number",
            "Value": "+12065551212"
        },
        {
            "Name": "email",
            "Value": "testuser@example.com"
        }
    ]
}
```

#### Sample Response
<a name="API_AdminCreateUser_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive

{
      "User": {
        "Attributes": [
          {
            "Name": "sub",
            "Value": "d16b4aa8-8633-4abd-93b3-5062a8e1b5f8"
          },
          {
            "Name": "name",
            "Value": "John"
          },
          {
            "Name": "phone_number",
            "Value": "+12065551212"
          },
          {
            "Name": "email",
            "Value": "testuser@example.com"
          }
        ],
        "Enabled": true,
        "UserCreateDate": 1689980857.949,
        "UserLastModifiedDate": 1689980857.949,
        "UserStatus": "FORCE_CHANGE_PASSWORD",
        "Username": "testuser"
      }
}
```

## See Also
<a name="API_AdminCreateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AdminCreateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AdminCreateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AdminCreateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AdminCreateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AdminCreateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AdminCreateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AdminCreateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AdminCreateUser)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AdminCreateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AdminCreateUser)
