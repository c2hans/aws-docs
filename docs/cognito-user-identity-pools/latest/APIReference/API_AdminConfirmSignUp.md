---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminConfirmSignUp.html
---

# AdminConfirmSignUp
<a name="API_AdminConfirmSignUp"></a>

Confirms user sign-up as an administrator.

Unlike [ConfirmSignUp](API_ConfirmSignUp.md), your IAM credentials authorize this operation to confirm user accounts. No confirmation code is required.

This request sets a user account active in a user pool that [requires confirmation of new user accounts](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#signing-up-users-in-your-app-and-confirming-them-as-admin) before they can sign in. You can configure your user pool to not send confirmation codes to new users and instead confirm them with this API operation on the back end.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

To configure your user pool to require administrative confirmation of users, set `AllowAdminCreateUserOnly` to `true` in a `CreateUserPool` or `UpdateUserPool` request.

## Request Syntax
<a name="API_AdminConfirmSignUp_RequestSyntax"></a>

```
{
   "ClientMetadata": {
      "{{string}}" : "{{string}}"
   },
   "Username": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_AdminConfirmSignUp_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientMetadata](#API_AdminConfirmSignUp_RequestSyntax) **   <a name="CognitoUserPools-AdminConfirmSignUp-request-ClientMetadata"></a>
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

 ** [Username](#API_AdminConfirmSignUp_RequestSyntax) **   <a name="CognitoUserPools-AdminConfirmSignUp-request-Username"></a>
The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If `username` isn't an alias attribute in your user pool, this value must be the `sub` of a local user or the username of a user from a third-party IdP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** [UserPoolId](#API_AdminConfirmSignUp_RequestSyntax) **   <a name="CognitoUserPools-AdminConfirmSignUp-request-UserPoolId"></a>
The ID of the user pool where you want to confirm a user's sign-up request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Elements
<a name="API_AdminConfirmSignUp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AdminConfirmSignUp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** TooManyFailedAttemptsException **
This exception is thrown when the user has made too many failed attempts for a given action, such as sign-in.
 ** message **
The message returned when Amazon Cognito returns a `TooManyFailedAttempts` exception.
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
<a name="API_AdminConfirmSignUp_Examples"></a>

### Example
<a name="API_AdminConfirmSignUp_Example_1"></a>

The following example operation confirms sign-up for the user "testuser." Note that because this is an administrative API operation, no confirmation code is required.

#### Sample Request
<a name="API_AdminConfirmSignUp_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminConfirmSignUp
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
  "UserPoolId": "us-west-2_EXAMPLE",
  "Username": "testuser"
}
```

#### Sample Response
<a name="API_AdminConfirmSignUp_Example_1_Response"></a>

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
<a name="API_AdminConfirmSignUp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AdminConfirmSignUp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AdminConfirmSignUp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AdminConfirmSignUp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AdminConfirmSignUp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AdminConfirmSignUp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AdminConfirmSignUp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AdminConfirmSignUp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AdminConfirmSignUp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AdminConfirmSignUp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AdminConfirmSignUp)
