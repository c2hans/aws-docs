---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_VpcConfig.html
---

# VpcConfig
<a name="API_VpcConfig"></a>

Amazon Virtual Private Cloud configuration details associated with your Lambda function.

## Contents
<a name="API_VpcConfig_Contents"></a>

 ** securityGroups **   <a name="guardduty-Type-VpcConfig-securityGroups"></a>
The identifier of the security group attached to the Lambda function.
Type: Array of [SecurityGroup](API_SecurityGroup.md) objects
Required: No

 ** subnetIds **   <a name="guardduty-Type-VpcConfig-subnetIds"></a>
The identifiers of the subnets that are associated with your Lambda function.
Type: Array of strings
Required: No

 ** vpcId **   <a name="guardduty-Type-VpcConfig-vpcId"></a>
The identifier of the Amazon Virtual Private Cloud.
Type: String
Required: No

## See Also
<a name="API_VpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/VpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/VpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/VpcConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
