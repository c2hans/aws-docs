---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_OptionGroupOptionSetting.html
---

# OptionGroupOptionSetting
<a name="API_OptionGroupOptionSetting"></a>

Option group option settings are used to display settings available for each option with their default values and other information. These values are used with the DescribeOptionGroupOptions action.

## Contents
<a name="API_OptionGroupOptionSetting_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AllowedValues **
Indicates the acceptable values for the option group option.
Type: String
Required: No

 ** ApplyType **
The DB engine specific parameter type for the option group option.
Type: String
Required: No

 ** DefaultValue **
The default value for the option group option.
Type: String
Required: No

 ** IsModifiable **
Indicates whether this option group option can be changed from the default value.
Type: Boolean
Required: No

 ** IsRequired **
Indicates whether a value must be specified for this option setting of the option group option.
Type: Boolean
Required: No

 ** MinimumEngineVersionPerAllowedValue.MinimumEngineVersionPerAllowedValue.N **
The minimum DB engine version required for the corresponding allowed value for this option setting.
Type: Array of [MinimumEngineVersionPerAllowedValue](API_MinimumEngineVersionPerAllowedValue.md) objects
Required: No

 ** SettingDescription **
The description of the option group option.
Type: String
Required: No

 ** SettingName **
The name of the option group option.
Type: String
Required: No

## See Also
<a name="API_OptionGroupOptionSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/OptionGroupOptionSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/OptionGroupOptionSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/OptionGroupOptionSetting)
