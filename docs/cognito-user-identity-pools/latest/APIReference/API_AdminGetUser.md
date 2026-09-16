---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminGetUser.html
---

# AdminGetUser
<a name="API_AdminGetUser"></a>

Given a username, returns details about a user profile in a user pool. You can specify alias attributes in the `Username` request parameter.

This operation contributes to your monthly active user (MAU) count for the purpose of billing.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_AdminGetUser_RequestSyntax"></a>

```
{
   "Username": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_AdminGetUser_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Username](#API_AdminGetUser_RequestSyntax) **   <a name="CognitoUserPools-AdminGetUser-request-Username"></a>
The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If `username` isn't an alias attribute in your user pool, this value must be the `sub` of a local user or the username of a user from a third-party IdP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: Yes

 ** [UserPoolId](#API_AdminGetUser_RequestSyntax) **   <a name="CognitoUserPools-AdminGetUser-request-UserPoolId"></a>
The ID of the user pool where you want to get information about the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## Response Syntax
<a name="API_AdminGetUser_ResponseSyntax"></a>

```
{
   "Enabled": boolean,
   "MFAOptions": [
      {
         "AttributeName": "string",
         "DeliveryMedium": "string"
      }
   ],
   "PreferredMfaSetting": "string",
   "UserAttributes": [
      {
         "Name": "string",
         "Value": "string"
      }
   ],
   "UserCreateDate": number,
   "UserLastModifiedDate": number,
   "UserMFASettingList": [ "string" ],
   "Username": "string",
   "UserStatus": "string"
}
```

## Response Elements
<a name="API_AdminGetUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Enabled](#API_AdminGetUser_ResponseSyntax) **   <a name="CognitoUserPools-AdminGetUser-response-Enabled"></a>
Indicates whether the user is activated for sign-in.
The [AdminDisableUser](API_AdminDisableUser.md) and [AdminEnableUser](API_AdminEnableUser.md) API operations deactivate and activate user sign-in, respectively.
Type: Boolean

 ** [MFAOptions](#API_AdminGetUser_ResponseSyntax) **   <a name="CognitoUserPools-AdminGetUser-response-MFAOptions"></a>
 *This response parameter is no longer supported.* It provides information only about SMS MFA configurations. It doesn't provide information about time-based one-time password (TOTP) software token MFA configurations. To look up information about either type of MFA configuration, use UserMFASettingList instead.
Type: Array of [MFAOptionType](API_MFAOptionType.md) objects

 ** [PreferredMfaSetting](#API_AdminGetUser_ResponseSyntax) **   <a name="CognitoUserPools-AdminGetUser-response-PreferredMfaSetting"></a>
The user's preferred MFA. Users can prefer SMS message, email message, or TOTP MFA.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.

 ** [UserAttributes](#API_AdminGetUser_ResponseSyntax) **   <a name="CognitoUserPools-AdminGetUser-response-UserAttributes"></a>
An array of name-value pairs of user attributes and their values, for example `"email": "testuser@example.com"`.
Type: Array of [AttributeType](API_AttributeType.md) objects

 ** [UserCreateDate](#API_AdminGetUser_ResponseSyntax) **   <a name="CognitoUserPools-AdminGetUser-response-UserCreateDate"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp

 ** [UserLastModifiedDate](#API_AdminGetUser_ResponseSyntax) **   <a name="CognitoUserPools-AdminGetUser-response-UserLastModifiedDate"></a>
The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp

 ** [UserMFASettingList](#API_AdminGetUser_ResponseSyntax) **   <a name="CognitoUserPools-AdminGetUser-response-UserMFASettingList"></a>
The MFA options that are activated for the user. The possible values in this list are `SMS_MFA`, `EMAIL_OTP`, and `SOFTWARE_TOKEN_MFA`.
You can change the MFA preference for users who have more than one available MFA factor with [AdminSetUserMFAPreference](API_AdminSetUserMFAPreference.md) or [SetUserMFAPreference](API_SetUserMFAPreference.md).
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 131072.

 ** [Username](#API_AdminGetUser_ResponseSyntax) **   <a name="CognitoUserPools-AdminGetUser-response-Username"></a>
The username of the user that you requested.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`

 ** [UserStatus](#API_AdminGetUser_ResponseSyntax) **   <a name="CognitoUserPools-AdminGetUser-response-UserStatus"></a>
The user's status. Can be one of the following:
+ UNCONFIRMED - User has been created but not confirmed.
+ CONFIRMED - User has been confirmed.
+ UNKNOWN - User status isn't known.
+ RESET\_REQUIRED - User is confirmed, but the user must request a code and reset their password before they can sign in.
+ FORCE\_CHANGE\_PASSWORD - The user is confirmed and the user can sign in using a temporary password, but on first sign-in, the user must change their password to a new value before doing anything else.
+ EXTERNAL\_PROVIDER - The user signed in with a third-party identity provider.
Type: String
Valid Values: `UNCONFIRMED | CONFIRMED | ARCHIVED | COMPROMISED | UNKNOWN | RESET_REQUIRED | FORCE_CHANGE_PASSWORD | EXTERNAL_PROVIDER`

## Errors
<a name="API_AdminGetUser_Errors"></a>

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

 ** UserNotFoundException **
This exception is thrown when a user isn't found.
 ** message **
The message returned when a user isn't found.
HTTP Status Code: 400

## Examples
<a name="API_AdminGetUser_Examples"></a>

### Example
<a name="API_AdminGetUser_Example_1"></a>

The following example API request gets user details for the user "testuser."

#### Sample Request
<a name="API_AdminGetUser_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.AdminGetUser
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
  "UserPoolId": "us-west-2_EXAMPLE",
  "Username": "testuser"
}
```

#### Sample Response
<a name="API_AdminGetUser_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive

{
    "Enabled": true,
    "UserAttributes": [
        {
            "Name": "sub",
            "Value": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        },
        {
            "Name": "identities",
            "Value": "[{\"userId\":\"a1b2c3d4-5678-90ab-cdef-EXAMPLE22222\",\"providerName\":\"SignInWithApple\",\"providerType\":\"SignInWithApple\",\"issuer\":null,\"primary\":false,\"dateCreated\":1701125599632}]"
        },
        {
            "Name": "email_verified",
            "Value": "true"
        },
        {
            "Name": "custom:deliverables",
            "Value": "project-111222"
        },
        {
            "Name": "name",
            "Value": "John"
        },
        {
            "Name": "phone_number_verified",
            "Value": "true"
        },
        {
            "Name": "phone_number",
            "Value": "+12065551212"
        },
        {
            "Name": "preferred_username",
            "Value": "John Doe"
        },
        {
            "Name": "locale",
            "Value": "EMEA"
        },
        {
            "Name": "email",
            "Value": "testuser@example.com"
        }
    ],
    "UserCreateDate": 1.682955829578E9,
    "UserLastModifiedDate": 1.722380161794E9,
    "UserStatus": "CONFIRMED",
    "Username": "testuser"
}
```

## See Also
<a name="API_AdminGetUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/AdminGetUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/AdminGetUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AdminGetUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/AdminGetUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AdminGetUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/AdminGetUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/AdminGetUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/AdminGetUser)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/AdminGetUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AdminGetUser)
