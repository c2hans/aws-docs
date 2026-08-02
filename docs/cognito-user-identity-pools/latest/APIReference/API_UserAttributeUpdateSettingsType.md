---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserAttributeUpdateSettingsType.html
---

# UserAttributeUpdateSettingsType
<a name="API_UserAttributeUpdateSettingsType"></a>

The settings for updates to user attributes. These settings include the property `AttributesRequireVerificationBeforeUpdate`, a user-pool setting that tells Amazon Cognito how to handle changes to the value of your users' email address and phone number attributes. For more information, see [ Verifying updates to email addresses and phone numbers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html#user-pool-settings-verifications-verify-attribute-updates).

This data type is a request and response parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_UserAttributeUpdateSettingsType_Contents"></a>

 ** AttributesRequireVerificationBeforeUpdate **   <a name="CognitoUserPools-Type-UserAttributeUpdateSettingsType-AttributesRequireVerificationBeforeUpdate"></a>
Requires that your user verifies their email address, phone number, or both before Amazon Cognito updates the value of that attribute. When you update a user attribute that has this option activated, Amazon Cognito sends a verification message to the new phone number or email address. Amazon Cognito doesn’t change the value of the attribute until your user responds to the verification message and confirms the new value.
You can verify an updated email address or phone number with a [VerifyUserAttribute](API_VerifyUserAttribute.md) API request. You can also call the [AdminUpdateUserAttributes](API_AdminUpdateUserAttributes.md) API and set `email_verified` or `phone_number_verified` to true.
When `AttributesRequireVerificationBeforeUpdate` is false, your user pool doesn't require that your users verify attribute changes before Amazon Cognito updates them. In a user pool where `AttributesRequireVerificationBeforeUpdate` is false, API operations that change attribute values can immediately update a user’s `email` or `phone_number` attribute.
Type: Array of strings
Valid Values: `phone_number | email`
Required: No

## See Also
<a name="API_UserAttributeUpdateSettingsType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UserAttributeUpdateSettingsType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UserAttributeUpdateSettingsType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UserAttributeUpdateSettingsType)
