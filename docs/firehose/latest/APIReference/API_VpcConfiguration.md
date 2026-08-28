---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_VpcConfiguration.html
---

# VpcConfiguration
<a name="API_VpcConfiguration"></a>

The details of the VPC of the Amazon OpenSearch or Amazon OpenSearch Serverless destination.

## Contents
<a name="API_VpcConfiguration_Contents"></a>

 ** RoleARN **   <a name="Firehose-Type-VpcConfiguration-RoleARN"></a>
The ARN of the IAM role that you want the Firehose stream to use to create endpoints in the destination VPC. You can use your existing Firehose delivery role or you can specify a new role. In either case, make sure that the role trusts the Firehose service principal and that it grants the following permissions:
+  `ec2:DescribeVpcs`
+  `ec2:DescribeVpcAttribute`
+  `ec2:DescribeSubnets`
+  `ec2:DescribeSecurityGroups`
+  `ec2:DescribeNetworkInterfaces`
+  `ec2:CreateNetworkInterface`
+  `ec2:CreateNetworkInterfacePermission`
+  `ec2:DeleteNetworkInterface`
When you specify subnets for delivering data to the destination in a private VPC, make sure you have enough number of free IP addresses in chosen subnets. If there is no available free IP address in a specified subnet, Firehose cannot create or add ENIs for the data delivery in the private VPC, and the delivery will be degraded or fail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** SecurityGroupIds **   <a name="Firehose-Type-VpcConfiguration-SecurityGroupIds"></a>
The IDs of the security groups that you want Firehose to use when it creates ENIs in the VPC of the Amazon OpenSearch Service destination. You can use the same security group that the Amazon OpenSearch Service domain uses or different ones. If you specify different security groups here, ensure that they allow outbound HTTPS traffic to the Amazon OpenSearch Service domain's security group. Also ensure that the Amazon OpenSearch Service domain's security group allows HTTPS traffic from the security groups specified here. If you use the same security group for both your delivery stream and the Amazon OpenSearch Service domain, make sure the security group inbound rule allows HTTPS traffic. For more information about security group rules, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules) in the Amazon VPC documentation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^\S+$`
Required: Yes

 ** SubnetIds **   <a name="Firehose-Type-VpcConfiguration-SubnetIds"></a>
The IDs of the subnets that you want Firehose to use to create ENIs in the VPC of the Amazon OpenSearch Service destination. Make sure that the routing tables and inbound and outbound rules allow traffic to flow from the subnets whose IDs are specified here to the subnets that have the destination Amazon OpenSearch Service endpoints. Firehose creates at least one ENI in each of the subnets that are specified here. Do not delete or modify these ENIs.
The number of ENIs that Firehose creates in the subnets specified here scales up and down automatically based on throughput. To enable Firehose to scale up the number of ENIs to match throughput, ensure that you have sufficient quota. To help you calculate the quota you need, assume that Firehose can create up to three ENIs for this Firehose stream for each of the subnets specified here. For more information about ENI quota, see [Network Interfaces ](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-enis) in the Amazon VPC Quotas topic.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^\S+$`
Required: Yes

## See Also
<a name="API_VpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/VpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/VpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/VpcConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
