---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_OptionSetting.html
---

# OptionSetting
<a name="API_OptionSetting"></a>

Option settings are the actual settings being applied or configured for that option. It is used when you modify an option group or describe option groups. For example, the NATIVE\_NETWORK\_ENCRYPTION option has a setting called SQLNET.ENCRYPTION\_SERVER that can have several different values.

## Contents
<a name="API_OptionSetting_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AllowedValues **
The allowed values of the option setting.
Type: String
Required: No

 ** ApplyType **
The DB engine specific parameter type.
Type: String
Required: No

 ** DataType **
The data type of the option setting.
Type: String
Required: No

 ** DefaultValue **
The default value of the option setting.
Type: String
Required: No

 ** Description **
The description of the option setting.
Type: String
Required: No

 ** IsCollection **
Indicates whether the option setting is part of a collection.
Type: Boolean
Required: No

 ** IsModifiable **
Indicates whether the option setting can be modified from the default.
Type: Boolean
Required: No

 ** Name **
The name of the option that has settings that you can set.
Type: String
Required: No

 ** Value **
The current value of the option setting.
Type: String
Required: No

## See Also
<a name="API_OptionSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/OptionSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/OptionSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/OptionSetting)
