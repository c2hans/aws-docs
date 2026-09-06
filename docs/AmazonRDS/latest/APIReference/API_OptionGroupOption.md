---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_OptionGroupOption.html
---

# OptionGroupOption
<a name="API_OptionGroupOption"></a>

Available option.

## Contents
<a name="API_OptionGroupOption_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CopyableCrossAccount **
Indicates whether the option can be copied across AWS accounts.
Type: Boolean
Required: No

 ** DefaultPort **
If the option requires a port, specifies the default port for the option.
Type: Integer
Required: No

 ** Description **
The description of the option.
Type: String
Required: No

 ** EngineName **
The name of the engine that this option can be applied to.
Type: String
Required: No

 ** MajorEngineVersion **
Indicates the major engine version that the option is available for.
Type: String
Required: No

 ** MinimumRequiredMinorEngineVersion **
The minimum required engine version for the option to be applied.
Type: String
Required: No

 ** Name **
The name of the option.
Type: String
Required: No

 ** OptionGroupOptionSettings.OptionGroupOptionSetting.N **
The option settings that are available (and the default value) for each option in an option group.
Type: Array of [OptionGroupOptionSetting](API_OptionGroupOptionSetting.md) objects
Required: No

 ** OptionGroupOptionVersions.OptionVersion.N **
The versions that are available for the option.
Type: Array of [OptionVersion](API_OptionVersion.md) objects
Required: No

 ** OptionsConflictsWith.OptionConflictName.N **
The options that conflict with this option.
Type: Array of strings
Required: No

 ** OptionsDependedOn.OptionName.N **
The options that are prerequisites for this option.
Type: Array of strings
Required: No

 ** Permanent **
Permanent options can never be removed from an option group. An option group containing a permanent option can't be removed from a DB instance.
Type: Boolean
Required: No

 ** Persistent **
Persistent options can't be removed from an option group while DB instances are associated with the option group. If you disassociate all DB instances from the option group, your can remove the persistent option from the option group.
Type: Boolean
Required: No

 ** PortRequired **
Indicates whether the option requires a port.
Type: Boolean
Required: No

 ** RequiresAutoMinorEngineVersionUpgrade **
If true, you must enable the Auto Minor Version Upgrade setting for your DB instance before you can use this option. You can enable Auto Minor Version Upgrade when you first create your DB instance, or by modifying your DB instance later.
Type: Boolean
Required: No

 ** SupportsOptionVersionDowngrade **
If true, you can change the option to an earlier version of the option. This only applies to options that have different versions available.
Type: Boolean
Required: No

 ** VpcOnly **
If true, you can only use this option with a DB instance that is in a VPC.
Type: Boolean
Required: No

## See Also
<a name="API_OptionGroupOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/OptionGroupOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/OptionGroupOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/OptionGroupOption)
