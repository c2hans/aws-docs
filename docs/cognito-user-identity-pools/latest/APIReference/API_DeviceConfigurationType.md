---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeviceConfigurationType.html
---

# DeviceConfigurationType
<a name="API_DeviceConfigurationType"></a>

The device-remembering configuration for a user pool.

A [DescribeUserPool](API_DescribeUserPool.md) request returns a null value for this object when the user pool isn't configured to remember devices. When device remembering is active, you can remember a user's device with a [ConfirmDevice](API_ConfirmDevice.md) API request. Additionally. when the property `DeviceOnlyRememberedOnUserPrompt` is `true`, you must follow `ConfirmDevice` with an [UpdateDeviceStatus](API_UpdateDeviceStatus.md) API request that sets the user's device to `remembered` or `not_remembered`.

To sign in with a remembered device, include `DEVICE_KEY` in the authentication parameters in your user's [InitiateAuth](API_InitiateAuth.md) request. If your app doesn't include a `DEVICE_KEY` parameter, the [InitiateAuth](API_InitiateAuth.md) from Amazon Cognito includes newly-generated `DEVICE_KEY` and `DEVICE_GROUP_KEY` values under `NewDeviceMetadata`. Store these values to use in future device-authentication requests.

**Note**
When you provide a value for any property of `DeviceConfiguration`, you activate the device remembering for the user pool.
This data type is a request and response parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_DeviceConfigurationType_Contents"></a>

 ** ChallengeRequiredOnNewDevice **   <a name="CognitoUserPools-Type-DeviceConfigurationType-ChallengeRequiredOnNewDevice"></a>
When true, a remembered device can sign in with device authentication instead of SMS and time-based one-time password (TOTP) factors for multi-factor authentication (MFA).
Whether or not `ChallengeRequiredOnNewDevice` is true, users who sign in with devices that have not been confirmed or remembered must still provide a second factor in a user pool that requires MFA.
Type: Boolean
Required: No

 ** DeviceOnlyRememberedOnUserPrompt **   <a name="CognitoUserPools-Type-DeviceConfigurationType-DeviceOnlyRememberedOnUserPrompt"></a>
When true, Amazon Cognito doesn't automatically remember a user's device when your app sends a `ConfirmDevice` API request. In your app, create a prompt for your user to choose whether they want to remember their device. Return the user's choice in an `UpdateDeviceStatus` API request.
When `DeviceOnlyRememberedOnUserPrompt` is `false`, Amazon Cognito immediately remembers devices that you register in a `ConfirmDevice` API request.
Type: Boolean
Required: No

## See Also
<a name="API_DeviceConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/DeviceConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/DeviceConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/DeviceConfigurationType)
