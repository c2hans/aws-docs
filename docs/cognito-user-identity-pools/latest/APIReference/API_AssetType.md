---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AssetType.html
---

# AssetType
<a name="API_AssetType"></a>

An image file from a managed login branding style in a user pool.

This data type is a request parameter of [CreateManagedLoginBranding](API_CreateManagedLoginBranding.md) and [UpdateManagedLoginBranding](API_UpdateManagedLoginBranding.md), and a response parameter of [DescribeManagedLoginBranding](API_DescribeManagedLoginBranding.md).

## Contents
<a name="API_AssetType_Contents"></a>

 ** Category **   <a name="CognitoUserPools-Type-AssetType-Category"></a>
The category that the image corresponds to in your managed login configuration. Managed login has asset categories for different types of logos, backgrounds, and icons.
Type: String
Valid Values: `FAVICON_ICO | FAVICON_SVG | EMAIL_GRAPHIC | SMS_GRAPHIC | AUTH_APP_GRAPHIC | PASSWORD_GRAPHIC | PASSKEY_GRAPHIC | PAGE_HEADER_LOGO | PAGE_HEADER_BACKGROUND | PAGE_FOOTER_LOGO | PAGE_FOOTER_BACKGROUND | PAGE_BACKGROUND | FORM_BACKGROUND | FORM_LOGO | IDP_BUTTON_ICON`
Required: Yes

 ** ColorMode **   <a name="CognitoUserPools-Type-AssetType-ColorMode"></a>
The display-mode target of the asset: light, dark, or browser-adaptive. For example, Amazon Cognito displays a dark-mode image only when the browser or application is in dark mode, but displays a browser-adaptive file in all contexts.
Type: String
Valid Values: `LIGHT | DARK | DYNAMIC`
Required: Yes

 ** Extension **   <a name="CognitoUserPools-Type-AssetType-Extension"></a>
The file type of the image file.
Type: String
Valid Values: `ICO | JPEG | PNG | SVG | WEBP`
Required: Yes

 ** Bytes **   <a name="CognitoUserPools-Type-AssetType-Bytes"></a>
The image file, in Base64-encoded binary.
Type: Base64-encoded binary data object
Length Constraints: Maximum length of 1000000.
Required: No

 ** ResourceId **   <a name="CognitoUserPools-Type-AssetType-ResourceId"></a>
The ID of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `^[\w\- ]+$`
Required: No

## See Also
<a name="API_AssetType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AssetType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AssetType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AssetType)
