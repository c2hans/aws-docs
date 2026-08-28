---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ManagedLoginBrandingType.html
---

# ManagedLoginBrandingType
<a name="API_ManagedLoginBrandingType"></a>

A managed login branding style that's assigned to a user pool app client.

This data type is a response parameter of [CreateManagedLoginBranding](API_CreateManagedLoginBranding.md), [UpdateManagedLoginBranding](API_UpdateManagedLoginBranding.md), [DescribeManagedLoginBranding](API_DescribeManagedLoginBranding.md), and [DescribeManagedLoginBrandingByClient](API_DescribeManagedLoginBrandingByClient.md).

## Contents
<a name="API_ManagedLoginBrandingType_Contents"></a>

 ** Assets **   <a name="CognitoUserPools-Type-ManagedLoginBrandingType-Assets"></a>
An array of image files that you want to apply to roles like backgrounds, logos, and icons. Each object must also indicate whether it is for dark mode, light mode, or browser-adaptive mode.
Type: Array of [AssetType](API_AssetType.md) objects
Array Members: Minimum number of 0 items. Maximum number of 40 items.
Required: No

 ** CreationDate **   <a name="CognitoUserPools-Type-ManagedLoginBrandingType-CreationDate"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** LastModifiedDate **   <a name="CognitoUserPools-Type-ManagedLoginBrandingType-LastModifiedDate"></a>
The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** ManagedLoginBrandingId **   <a name="CognitoUserPools-Type-ManagedLoginBrandingType-ManagedLoginBrandingId"></a>
The ID of the managed login branding style.
Type: String
Pattern: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[4][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$`
Required: No

 ** Settings **   <a name="CognitoUserPools-Type-ManagedLoginBrandingType-Settings"></a>
A JSON file, encoded as a `Document` type, with the the settings that you want to apply to your style.
The following components are not currently implemented and reserved for future use:
+  `signUp`
+  `instructions`
+  `sessionTimerDisplay`
+  `languageSelector` (for localization, see [Managed login localization)](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html#managed-login-localization)
Type: JSON value
Required: No

 ** UseCognitoProvidedValues **   <a name="CognitoUserPools-Type-ManagedLoginBrandingType-UseCognitoProvidedValues"></a>
When true, applies the default branding style options. This option reverts to default style options that are managed by Amazon Cognito. You can modify them later in the branding editor.
When you specify `true` for this option, you must also omit values for `Settings` and `Assets` in the request.
Type: Boolean
Required: No

 ** UserPoolId **   <a name="CognitoUserPools-Type-ManagedLoginBrandingType-UserPoolId"></a>
The user pool where the branding style is assigned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: No

## See Also
<a name="API_ManagedLoginBrandingType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ManagedLoginBrandingType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ManagedLoginBrandingType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ManagedLoginBrandingType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
