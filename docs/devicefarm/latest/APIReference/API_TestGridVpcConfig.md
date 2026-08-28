---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_TestGridVpcConfig.html
---

# TestGridVpcConfig
<a name="API_TestGridVpcConfig"></a>

The VPC security groups and subnets that are attached to a project.

## Contents
<a name="API_TestGridVpcConfig_Contents"></a>

 ** securityGroupIds **   <a name="devicefarm-Type-TestGridVpcConfig-securityGroupIds"></a>
A list of VPC security group IDs in your Amazon VPC.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.*\S.*`
Required: Yes

 ** subnetIds **   <a name="devicefarm-Type-TestGridVpcConfig-subnetIds"></a>
A list of VPC subnet IDs in your Amazon VPC.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.*\S.*`
Required: Yes

 ** vpcId **   <a name="devicefarm-Type-TestGridVpcConfig-vpcId"></a>
The ID of the Amazon VPC.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_TestGridVpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/TestGridVpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/TestGridVpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/TestGridVpcConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
