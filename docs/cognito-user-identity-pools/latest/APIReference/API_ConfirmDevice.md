---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ConfirmDevice.html
---

# ConfirmDevice
<a name="API_ConfirmDevice"></a>

Confirms a device that a user wants to remember. A remembered device is a "Remember me on this device" option for user pools that perform authentication with the device key of a trusted device in the back end, instead of a user-provided MFA code. For more information about device authentication, see [Working with user devices in your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html).

Authorize this action with a signed-in user's access token. It must include the scope `aws.cognito.signin.user.admin`.

**Note**
Amazon Cognito doesn't evaluate AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you can't use IAM credentials to authorize requests, and you can't grant IAM permissions in policies. For more information about authorization models in Amazon Cognito, see [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html).

## Request Syntax
<a name="API_ConfirmDevice_RequestSyntax"></a>

```
{
   "AccessToken": "{{string}}",
   "DeviceKey": "{{string}}",
   "DeviceName": "{{string}}",
   "DeviceSecretVerifierConfig": {
      "PasswordVerifier": "{{string}}",
      "Salt": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ConfirmDevice_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessToken](#API_ConfirmDevice_RequestSyntax) **   <a name="CognitoUserPools-ConfirmDevice-request-AccessToken"></a>
A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for `aws.cognito.signin.user.admin`.
Type: String
Pattern: `[A-Za-z0-9-_=.]+`
Required: Yes

 ** [DeviceKey](#API_ConfirmDevice_RequestSyntax) **   <a name="CognitoUserPools-ConfirmDevice-request-DeviceKey"></a>
The unique identifier, or device key, of the device that you want to update the status for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-f-]+`
Required: Yes

 ** [DeviceName](#API_ConfirmDevice_RequestSyntax) **   <a name="CognitoUserPools-ConfirmDevice-request-DeviceName"></a>
A friendly name for the device, for example `MyMobilePhone`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [DeviceSecretVerifierConfig](#API_ConfirmDevice_RequestSyntax) **   <a name="CognitoUserPools-ConfirmDevice-request-DeviceSecretVerifierConfig"></a>
The configuration of the device secret verifier.
Type: [DeviceSecretVerifierConfigType](API_DeviceSecretVerifierConfigType.md) object
Required: No

## Response Syntax
<a name="API_ConfirmDevice_ResponseSyntax"></a>

```
{
   "UserConfirmationNecessary": boolean
}
```

## Response Elements
<a name="API_ConfirmDevice_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UserConfirmationNecessary](#API_ConfirmDevice_ResponseSyntax) **   <a name="CognitoUserPools-ConfirmDevice-response-UserConfirmationNecessary"></a>
When `true`, your user must confirm that they want to remember the device. Prompt the user for an answer.
You must then make an [UpdateDeviceStatus](API_UpdateDeviceStatus.md) request that sets the device to `remembered` or `not_remembered`.
When `false`, immediately sets the device as remembered and eligible for device authentication.
You can configure your user pool to always remember devices, in which case this response is `false`, or to allow users to opt in, in which case this response is `true`. Configure this option under *Device tracking* in the *Sign-in* menu of your user pool.
You can also configure this option with the `DeviceConfiguration` parameter of a [CreateUserPool](API_CreateUserPool.md) or [UpdateUserPool](API_UpdateUserPool.md) request.
Type: Boolean

## Errors
<a name="API_ConfirmDevice_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DeviceKeyExistsException **
This exception is thrown when a user attempts to confirm a device with a device key that already exists.
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

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

 ** UsernameExistsException **
This exception is thrown when Amazon Cognito encounters a user name that already exists in the user pool.
 ** message **
The message returned when Amazon Cognito throws a user name exists exception.
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
<a name="API_ConfirmDevice_Examples"></a>

### Example
<a name="API_ConfirmDevice_Example_1"></a>

The following example request confirms a device for the user with the access token "eyJra456defEXAMPLE". In the user pool in this example, the user must confirm that they want to remember the device with a new [UpdateDeviceStatus](API_UpdateDeviceStatus.md) request that sets `DeviceRememberedStatus` to `true` for the device with key `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.

#### Sample Request
<a name="API_ConfirmDevice_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.ConfirmDevice
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "AccessToken": "eyJra456defEXAMPLE",
   "DeviceKey": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
   "DeviceName": "MyMobileDevice",
   "DeviceSecretVerifierConfig": {
      "PasswordVerifier": "[calculated verifier string]",
      "Salt": "[salt]"
   }
}
```

#### Sample Response
<a name="API_ConfirmDevice_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
   "UserConfirmationNecessary": true
}
```

## See Also
<a name="API_ConfirmDevice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/ConfirmDevice)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/ConfirmDevice)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ConfirmDevice)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/ConfirmDevice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ConfirmDevice)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/ConfirmDevice)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/ConfirmDevice)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/ConfirmDevice)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/ConfirmDevice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ConfirmDevice)
