---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_VpcLatticeConfiguration.html
---

# VpcLatticeConfiguration
<a name="API_VpcLatticeConfiguration"></a>

The VPC Lattice configuration for your service that holds the information for the target group(s) Amazon ECS tasks will be registered to.

## Contents
<a name="API_VpcLatticeConfiguration_Contents"></a>

 ** portName **   <a name="ECS-Type-VpcLatticeConfiguration-portName"></a>
The name of the port mapping to register in the VPC Lattice target group. This is the name of the `portMapping` you defined in your task definition.
Type: String
Required: Yes

 ** roleArn **   <a name="ECS-Type-VpcLatticeConfiguration-roleArn"></a>
The ARN of the IAM role to associate with this VPC Lattice configuration. This is the Amazon ECS infrastructure IAM role that is used to manage your VPC Lattice infrastructure.
Type: String
Required: Yes

 ** targetGroupArn **   <a name="ECS-Type-VpcLatticeConfiguration-targetGroupArn"></a>
The full Amazon Resource Name (ARN) of the target group or groups associated with the VPC Lattice configuration that the Amazon ECS tasks will be registered to.
Type: String
Required: Yes

## See Also
<a name="API_VpcLatticeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/VpcLatticeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/VpcLatticeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/VpcLatticeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
