---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_WorkforceVpcConfigResponse.html
---

# WorkforceVpcConfigResponse
<a name="API_WorkforceVpcConfigResponse"></a>

A VpcConfig object that specifies the VPC that you want your workforce to connect to.

## Contents
<a name="API_WorkforceVpcConfigResponse_Contents"></a>

 ** SecurityGroupIds **   <a name="sagemaker-Type-WorkforceVpcConfigResponse-SecurityGroupIds"></a>
The VPC security group IDs, in the form sg-xxxxxxxx. The security groups must be for the same VPC as specified in the subnet.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `sg-[0-9a-z]*`
Required: Yes

 ** Subnets **   <a name="sagemaker-Type-WorkforceVpcConfigResponse-Subnets"></a>
The ID of the subnets in the VPC that you want to connect.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `subnet-[0-9a-z]*`
Required: Yes

 ** VpcId **   <a name="sagemaker-Type-WorkforceVpcConfigResponse-VpcId"></a>
The ID of the VPC that the workforce uses for communication.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `vpc-[0-9a-z]*`
Required: Yes

 ** VpcEndpointId **   <a name="sagemaker-Type-WorkforceVpcConfigResponse-VpcEndpointId"></a>
The IDs for the VPC service endpoints of your VPC workforce when it is created and updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `vpce-[0-9a-z]*`
Required: No

## See Also
<a name="API_WorkforceVpcConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/WorkforceVpcConfigResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/WorkforceVpcConfigResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/WorkforceVpcConfigResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
