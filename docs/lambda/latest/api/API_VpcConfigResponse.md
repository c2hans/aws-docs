---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_VpcConfigResponse.html
---

# VpcConfigResponse
<a name="API_VpcConfigResponse"></a>

The VPC security groups and subnets that are attached to a Lambda function.

## Contents
<a name="API_VpcConfigResponse_Contents"></a>

 ** Ipv6AllowedForDualStack **   <a name="lambda-Type-VpcConfigResponse-Ipv6AllowedForDualStack"></a>
Allows outbound IPv6 traffic on VPC functions that are connected to dual-stack subnets.
Type: Boolean
Required: No

 ** SecurityGroupIds **   <a name="lambda-Type-VpcConfigResponse-SecurityGroupIds"></a>
A list of VPC security group IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** SubnetIds **   <a name="lambda-Type-VpcConfigResponse-SubnetIds"></a>
A list of VPC subnet IDs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 16 items.
Required: No

 ** VpcId **   <a name="lambda-Type-VpcConfigResponse-VpcId"></a>
The ID of the VPC.
Type: String
Required: No

## See Also
<a name="API_VpcConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/VpcConfigResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/VpcConfigResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/VpcConfigResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
