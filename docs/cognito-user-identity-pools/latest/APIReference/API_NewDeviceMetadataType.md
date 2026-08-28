---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_NewDeviceMetadataType.html
---

# NewDeviceMetadataType
<a name="API_NewDeviceMetadataType"></a>

Information that your user pool responds with in `AuthenticationResult`when you configure it to remember devices and a user signs in with an unrecognized device. Amazon Cognito presents a new device key that you can use to set up [device authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html) in a "Remember me on this device" authentication model.

This data type is a response parameter of authentication operations like [InitiateAuth](API_InitiateAuth.md), [AdminInitiateAuth](API_AdminInitiateAuth.md), [RespondToAuthChallenge](API_RespondToAuthChallenge.md), and [AdminRespondToAuthChallenge](API_AdminRespondToAuthChallenge.md).

## Contents
<a name="API_NewDeviceMetadataType_Contents"></a>

 ** DeviceGroupKey **   <a name="CognitoUserPools-Type-NewDeviceMetadataType-DeviceGroupKey"></a>
The device group key, an identifier used in generating the `DEVICE_PASSWORD_VERIFIER` for device SRP authentication.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** DeviceKey **   <a name="CognitoUserPools-Type-NewDeviceMetadataType-DeviceKey"></a>
The device key, an identifier used in generating the `DEVICE_PASSWORD_VERIFIER` for device SRP authentication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-f-]+`
Required: No

## See Also
<a name="API_NewDeviceMetadataType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/NewDeviceMetadataType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/NewDeviceMetadataType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/NewDeviceMetadataType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
