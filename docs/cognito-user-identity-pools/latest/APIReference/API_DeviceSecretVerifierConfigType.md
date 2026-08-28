---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeviceSecretVerifierConfigType.html
---

# DeviceSecretVerifierConfigType
<a name="API_DeviceSecretVerifierConfigType"></a>

A Secure Remote Password (SRP) value that your application generates when you register a user's device. For more information, see [Getting a device key](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html#user-pools-remembered-devices-getting-a-device-key).

This data type is a request parameter of [ConfirmDevice](API_ConfirmDevice.md).

## Contents
<a name="API_DeviceSecretVerifierConfigType_Contents"></a>

 ** PasswordVerifier **   <a name="CognitoUserPools-Type-DeviceSecretVerifierConfigType-PasswordVerifier"></a>
A password verifier for a user's device. Used in SRP authentication.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** Salt **   <a name="CognitoUserPools-Type-DeviceSecretVerifierConfigType-Salt"></a>
The salt that you want to use in SRP authentication with the user's device.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

## See Also
<a name="API_DeviceSecretVerifierConfigType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/DeviceSecretVerifierConfigType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/DeviceSecretVerifierConfigType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/DeviceSecretVerifierConfigType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
