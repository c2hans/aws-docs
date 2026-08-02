---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminUpdateUserAttributes.html
---

# AdminUpdateUserAttributes
<a name="API_AdminUpdateUserAttributes"></a>

Updates the specified user's attributes. To delete an attribute from your user, submit the attribute in your API request with a blank value.

For custom attributes, you must add a `custom:` prefix to the attribute name, for example `custom:department`.

This operation can set a user's email address or phone number as verified and permit immediate sign-in in user pools that require verification of these attributes. To do this, set the `email_verified` or `phone_number_verified` attribute to `true`.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

**Note**
This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with [Amazon Pinpoint](https://console.aws.amazon.com/pinpoint/home/). Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.
If you have never used SMS text messages with Amazon Cognito or any other AWS service, Amazon Simple Notification Service might place your account in the SMS sandbox. In * [sandbox mode](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) *, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see [ SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) in the *Amazon Cognito Developer Guide*.

## Request Syntax
<a name="API_AdminUpdateUserAttributes_RequestSyntax"></a>

```
{
   "ClientMetadata": {
      "{{string}}" : "{{string}}"
   },
   "UserAttributes": [
      {
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Username": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_AdminUpdateUserAttributes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientMetadata](#API_AdminUpdateUserAttributes_RequestSyntax) **   <a name="CognitoUserPools-AdminUpdateUserAttributes-request-ClientMetadata"></a>
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

 ** [UserAttributes](#API_AdminUpdateUserAttributes_RequestSyntax) **   <a name="CognitoUserPools-AdminUpdateUserAttributes-request-UserAttributes"></a>
An array of name-value pairs representing user attributes.
For custom attributes, you must prepend the `custom:` prefix to the attribute name.
If your user pool requires verification before Amazon Cognito updates an attribute value that you specify in this request, Amazon Cognito doesn’t immediately update the value of that attribute. After your user receives and responds to a verification message to verify the new value, Amazon Cognito updates the attribute value. Your user can sign in and receive messages with the original attribute value until they verify the new value.
To skip the verification message and update the value of an attribute that requires verification in the same API request, include the `email_verified` or `phone_number_verified` attribute, with a value of `true`. If you set the `email_verified` or `phone_number_verified` value for an `email` or `phone_number` attribute that requires verification to `true`, Amazon Cognito doesn’t send a verification message to your user.
Type: Array of [AttributeType](API_AttributeType.md) objects
Required: Yes

 ** [Username](#API_AdminUpdateUserAttributes_RequestSyntax) **   <a name="CognitoUserPools-AdminUpdateUserAttributes-request-Username"></a>
The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If `username` isn't an alias attribute in your user pool, this value must be the `sub` of a local user or the username of a user from a third-party IdP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** [UserPoolId](#API_AdminUpdateUserAttributes_RequestSyntax) **   <a name="CognitoUserPools-AdminUpdateUserAttributes-request-UserPoolId"></a>
The ID of the user pool where you want to update user attributes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Elements
<a name="API_AdminUpdateUserAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AdminUpdateUserAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AliasExistsException **
This exception is thrown when a user tries to confirm the account with an email address or phone number that has already been supplied as an alias for a different user profile. This exception indicates that an account with this email address or phone already exists in a user pool that you've configured to use email address or phone number as a sign-in alias.
 ** message **
The message that Amazon Cognito sends to the user when the value of an alias attribute is already linked to another user profile.
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

 ** UserNotFoundException **
This exception is thrown when a user isn't found.
 ** message **
The message returned when a user isn't found.
HTTP Status Code: 400

## Examples
<a name="API_AdminUpdateUserAttributes_Examples"></a>

### Example
<a name="API_AdminUpdateUserAttributes_Example_1"></a>

The following example request sets the values of two attributes for "testuser." The request also includes client metadata that the user pool passes on in a ` CustomMessage_UpdateUserAttribute` Lambda trigger event.

#### Sample Request
<a name="API_AdminUpdateUserAttributes_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminUpdateUserAttributes
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
  "UserAttributes": [
      {
          "Name": "custom:deliverables",
          "Value": "project-111222"
      },
      {
          "Name": "name",
          "Value": "John"
      }
  ],
  "UserPoolId": "us-west-2_EXAMPLE",
  "Username": "testuser",
  "ClientMetadata": {
        "MyTestKey": "MyTestValue"
  }
}
```

#### Sample Response
<a name="API_AdminUpdateUserAttributes_Example_1_Response"></a>

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
<a name="API_AdminUpdateUserAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AdminUpdateUserAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AdminUpdateUserAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AdminUpdateUserAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AdminUpdateUserAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AdminUpdateUserAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AdminUpdateUserAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AdminUpdateUserAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AdminUpdateUserAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AdminUpdateUserAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AdminUpdateUserAttributes)
