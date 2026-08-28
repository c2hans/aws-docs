---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Option.html
---

# Option
<a name="API_Option"></a>

The details of an option.

## Contents
<a name="API_Option_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DBSecurityGroupMemberships.DBSecurityGroup.N **
If the option requires access to a port, then this DB security group allows access to the port.
Type: Array of [DBSecurityGroupMembership](API_DBSecurityGroupMembership.md) objects
Required: No

 ** OptionDescription **
The description of the option.
Type: String
Required: No

 ** OptionName **
The name of the option.
Type: String
Required: No

 ** OptionSettings.OptionSetting.N **
The option settings for this option.
Type: Array of [OptionSetting](API_OptionSetting.md) objects
Required: No

 ** OptionVersion **
The version of the option.
Type: String
Required: No

 ** Permanent **
Indicates whether this option is permanent.
Type: Boolean
Required: No

 ** Persistent **
Indicates whether this option is persistent.
Type: Boolean
Required: No

 ** Port **
If required, the port configured for this option to use.
Type: Integer
Required: No

 ** VpcSecurityGroupMemberships.VpcSecurityGroupMembership.N **
If the option requires access to a port, then this VPC security group allows access to the port.
Type: Array of [VpcSecurityGroupMembership](API_VpcSecurityGroupMembership.md) objects
Required: No

## See Also
<a name="API_Option_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/Option)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/Option)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/Option)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
