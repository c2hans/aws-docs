---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DisplayData.html
---

# DisplayData
<a name="API_DisplayData"></a>

A structure that describes how the portal represents an application provider.

## Contents
<a name="API_DisplayData_Contents"></a>

 ** Description **   <a name="singlesignon-Type-DisplayData-Description"></a>
The description of the application provider that appears in the portal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** DisplayName **   <a name="singlesignon-Type-DisplayData-DisplayName"></a>
The name of the application provider that appears in the portal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** IconUrl **   <a name="singlesignon-Type-DisplayData-IconUrl"></a>
A URL that points to an icon that represents the application provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Pattern: `(http|https):\/\/.*`
Required: No

## See Also
<a name="API_DisplayData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/DisplayData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/DisplayData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/DisplayData)
