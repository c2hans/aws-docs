---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BrandDefinition.html
---

# BrandDefinition
<a name="API_BrandDefinition"></a>

The definition of the brand.

## Contents
<a name="API_BrandDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BrandName **   <a name="QS-Type-BrandDefinition-BrandName"></a>
The name of the brand.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[ -ÿ]+`
Required: Yes

 ** ApplicationTheme **   <a name="QS-Type-BrandDefinition-ApplicationTheme"></a>
The application theme of the brand.
Type: [ApplicationTheme](API_ApplicationTheme.md) object
Required: No

 ** Description **   <a name="QS-Type-BrandDefinition-Description"></a>
The description of the brand.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[ -ÿ]+`
Required: No

 ** LogoConfiguration **   <a name="QS-Type-BrandDefinition-LogoConfiguration"></a>
The logo configuration of the brand.
Type: [LogoConfiguration](API_LogoConfiguration.md) object
Required: No

## See Also
<a name="API_BrandDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BrandDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BrandDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BrandDefinition)
