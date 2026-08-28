---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJobVPCConnectionOverrideParameters.html
---

# AssetBundleImportJobVPCConnectionOverrideParameters
<a name="API_AssetBundleImportJobVPCConnectionOverrideParameters"></a>

The override parameters for a single VPC connection that is imported.

## Contents
<a name="API_AssetBundleImportJobVPCConnectionOverrideParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** VPCConnectionId **   <a name="QS-Type-AssetBundleImportJobVPCConnectionOverrideParameters-VPCConnectionId"></a>
The ID of the VPC Connection to apply overrides to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** DnsResolvers **   <a name="QS-Type-AssetBundleImportJobVPCConnectionOverrideParameters-DnsResolvers"></a>
An optional override of DNS resolvers to be used by the VPC connection.
Type: Array of strings
Array Members: Maximum number of 15 items.
Length Constraints: Minimum length of 7. Maximum length of 15.
Required: No

 ** Name **   <a name="QS-Type-AssetBundleImportJobVPCConnectionOverrideParameters-Name"></a>
A new name for the VPC connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** RoleArn **   <a name="QS-Type-AssetBundleImportJobVPCConnectionOverrideParameters-RoleArn"></a>
An optional override of the role ARN to be used by the VPC connection.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** SecurityGroupIds **   <a name="QS-Type-AssetBundleImportJobVPCConnectionOverrideParameters-SecurityGroupIds"></a>
A new security group ID for the VPC connection you are importing. This field is required if you are importing the VPC connection from another AWS account or Region.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^sg-[0-9a-z]*$`
Required: No

 ** SubnetIds **   <a name="QS-Type-AssetBundleImportJobVPCConnectionOverrideParameters-SubnetIds"></a>
A list of new subnet IDs for the VPC connection you are importing. This field is required if you are importing the VPC connection from another AWS account or Region.
Type: Array of strings
Array Members: Minimum number of 2 items. Maximum number of 15 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^subnet-[0-9a-z]*$`
Required: No

## See Also
<a name="API_AssetBundleImportJobVPCConnectionOverrideParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportJobVPCConnectionOverrideParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportJobVPCConnectionOverrideParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportJobVPCConnectionOverrideParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
