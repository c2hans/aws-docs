---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_OptionConfiguration.html
---

# OptionConfiguration
<a name="API_OptionConfiguration"></a>

A list of all available options for an option group.

## Contents
<a name="API_OptionConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** OptionName **
The configuration of options to include in a group.
Type: String
Required: Yes

 ** DBSecurityGroupMemberships.DBSecurityGroupName.N **
A list of DB security groups used for this option.
Type: Array of strings
Required: No

 ** OptionSettings.OptionSetting.N **
The option settings to include in an option group.
Type: Array of [OptionSetting](API_OptionSetting.md) objects
Required: No

 ** OptionVersion **
The version for the option.
Type: String
Required: No

 ** Port **
The optional port for the option.
Type: Integer
Required: No

 ** VpcSecurityGroupMemberships.VpcSecurityGroupId.N **
A list of VPC security group names used for this option.
Type: Array of strings
Required: No

## See Also
<a name="API_OptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/OptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/OptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/OptionConfiguration)
