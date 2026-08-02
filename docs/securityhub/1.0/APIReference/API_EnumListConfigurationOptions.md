---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_EnumListConfigurationOptions.html
---

# EnumListConfigurationOptions
<a name="API_EnumListConfigurationOptions"></a>

 The options for customizing a security control parameter that is a list of enums.

## Contents
<a name="API_EnumListConfigurationOptions_Contents"></a>

 ** AllowedValues **   <a name="securityhub-Type-EnumListConfigurationOptions-AllowedValues"></a>
 The valid values for a control parameter that is a list of enums.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** DefaultValue **   <a name="securityhub-Type-EnumListConfigurationOptions-DefaultValue"></a>
 The Security Hub CSPM default value for a control parameter that is a list of enums.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** MaxItems **   <a name="securityhub-Type-EnumListConfigurationOptions-MaxItems"></a>
 The maximum number of list items that an enum list control parameter can accept.
Type: Integer
Required: No

## See Also
<a name="API_EnumListConfigurationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/EnumListConfigurationOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/EnumListConfigurationOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/EnumListConfigurationOptions)
