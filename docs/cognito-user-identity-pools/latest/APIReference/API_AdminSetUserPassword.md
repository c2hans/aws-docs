---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminSetUserPassword.html
---

# AdminSetUserPassword
<a name="API_AdminSetUserPassword"></a>

Sets the specified user's password in a user pool. This operation administratively sets a temporary or permanent password for a user. With this operation, you can bypass self-service password changes and permit immediate sign-in with the password that you set. To do this, set `Permanent` to `true`.

You can also set a new temporary password in this request, send it to a user, and require them to choose a new password on their next sign-in. To do this, set `Permanent` to `false`.

If the password is temporary, the user's `Status` becomes `FORCE_CHANGE_PASSWORD`. When the user next tries to sign in, the `InitiateAuth` or `AdminInitiateAuth` response includes the `NEW_PASSWORD_REQUIRED` challenge. If the user doesn't sign in before the temporary password expires, they can no longer sign in and you must repeat this operation to set a temporary or permanent password for them.

After the user sets a new password, or if you set a permanent password, their status becomes `Confirmed`.

 `AdminSetUserPassword` can set a password for the user profile that Amazon Cognito creates for third-party federated users. When you set a password, the federated user's status changes from `EXTERNAL_PROVIDER` to `CONFIRMED`. A user in this state can sign in as a federated user, and initiate authentication flows in the API like a linked native user. They can also modify their password and attributes in token-authenticated API requests like `ChangePassword` and `UpdateUserAttributes`. As a best security practice and to keep users in sync with your external IdP, don't set passwords on federated user profiles. To set up a federated user for native sign-in with a linked native user, refer to [Linking federated users to an existing user profile](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html).

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_AdminSetUserPassword_RequestSyntax"></a>

```
{
   "Password": "{{string}}",
   "Permanent": {{boolean}},
   "Username": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_AdminSetUserPassword_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Password](#API_AdminSetUserPassword_RequestSyntax) **   <a name="CognitoUserPools-AdminSetUserPassword-request-Password"></a>
The new temporary or permanent password that you want to set for the user. You can't remove the password for a user who already has a password so that they can only sign in with passwordless methods. In this scenario, you must create a new user without a password.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\S]+`
Required: Yes

 ** [Permanent](#API_AdminSetUserPassword_RequestSyntax) **   <a name="CognitoUserPools-AdminSetUserPassword-request-Permanent"></a>
Set to `true` to set a password that the user can immediately sign in with. Set to `false` to set a temporary password that the user must change on their next sign-in.
Type: Boolean
Required: No

 ** [Username](#API_AdminSetUserPassword_RequestSyntax) **   <a name="CognitoUserPools-AdminSetUserPassword-request-Username"></a>
The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If `username` isn't an alias attribute in your user pool, this value must be the `sub` of a local user or the username of a user from a third-party IdP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** [UserPoolId](#API_AdminSetUserPassword_RequestSyntax) **   <a name="CognitoUserPools-AdminSetUserPassword-request-UserPoolId"></a>
The ID of the user pool where you want to set the user's password.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Elements
<a name="API_AdminSetUserPassword_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AdminSetUserPassword_Errors"></a>

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

 ** InvalidPasswordException **
This exception is thrown when Amazon Cognito encounters an invalid password.
 ** message **
The message returned when Amazon Cognito throws an invalid user password exception.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** OperationNotEnabledException **
This exception is thrown when an operation is not available in the current region or for the current user pool configuration. This can occur when attempting to perform operations that are not supported in secondary replica regions.
HTTP Status Code: 400

 ** PasswordHistoryPolicyViolationException **
The message returned when a user's new password matches a previous password and doesn't comply with the password-history policy.
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

 ** UserNotFoundException **
This exception is thrown when a user isn't found.
 ** message **
The message returned when a user isn't found.
HTTP Status Code: 400

## Examples
<a name="API_AdminSetUserPassword_Examples"></a>

### Example
<a name="API_AdminSetUserPassword_Example_1"></a>

The following example request sets the user "testuser" to have the password "MyExamplePassword1=", and to be able to sign in with that password without a reset.

#### Sample Request
<a name="API_AdminSetUserPassword_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminSetUserPassword
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
  "Password": "MyExamplePassword1=",
  "UserPoolId": "us-west-2_EXAMPLE",
  "Username": "testuser",
  "Permanent": true
}
```

#### Sample Response
<a name="API_AdminSetUserPassword_Example_1_Response"></a>

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
<a name="API_AdminSetUserPassword_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AdminSetUserPassword)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AdminSetUserPassword)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AdminSetUserPassword)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AdminSetUserPassword)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AdminSetUserPassword)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AdminSetUserPassword)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AdminSetUserPassword)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AdminSetUserPassword)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AdminSetUserPassword)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AdminSetUserPassword)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
