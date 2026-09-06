---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ConfigurationOptions.html
---

# ConfigurationOptions
<a name="API_ConfigurationOptions"></a>

 The options for customizing a security control parameter.

## Contents
<a name="API_ConfigurationOptions_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Boolean **   <a name="securityhub-Type-ConfigurationOptions-Boolean"></a>
 The options for customizing a security control parameter that is a boolean. For a boolean parameter, the options are `true` and `false`.
Type: [BooleanConfigurationOptions](API_BooleanConfigurationOptions.md) object
Required: No

 ** Double **   <a name="securityhub-Type-ConfigurationOptions-Double"></a>
 The options for customizing a security control parameter that is a double.
Type: [DoubleConfigurationOptions](API_DoubleConfigurationOptions.md) object
Required: No

 ** Enum **   <a name="securityhub-Type-ConfigurationOptions-Enum"></a>
 The options for customizing a security control parameter that is an enum.
Type: [EnumConfigurationOptions](API_EnumConfigurationOptions.md) object
Required: No

 ** EnumList **   <a name="securityhub-Type-ConfigurationOptions-EnumList"></a>
 The options for customizing a security control parameter that is a list of enums.
Type: [EnumListConfigurationOptions](API_EnumListConfigurationOptions.md) object
Required: No

 ** Integer **   <a name="securityhub-Type-ConfigurationOptions-Integer"></a>
 The options for customizing a security control parameter that is an integer.
Type: [IntegerConfigurationOptions](API_IntegerConfigurationOptions.md) object
Required: No

 ** IntegerList **   <a name="securityhub-Type-ConfigurationOptions-IntegerList"></a>
 The options for customizing a security control parameter that is a list of integers.
Type: [IntegerListConfigurationOptions](API_IntegerListConfigurationOptions.md) object
Required: No

 ** String **   <a name="securityhub-Type-ConfigurationOptions-String"></a>
 The options for customizing a security control parameter that is a string data type.
Type: [StringConfigurationOptions](API_StringConfigurationOptions.md) object
Required: No

 ** StringList **   <a name="securityhub-Type-ConfigurationOptions-StringList"></a>
 The options for customizing a security control parameter that is a list of strings.
Type: [StringListConfigurationOptions](API_StringListConfigurationOptions.md) object
Required: No

## See Also
<a name="API_ConfigurationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ConfigurationOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ConfigurationOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ConfigurationOptions)
