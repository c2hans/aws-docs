---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/creating-resources-with-cloudformation.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# Creating Amazon WorkSpaces Thin Client resources with AWS CloudFormation
<a name="creating-resources-with-cloudformation"></a>

Amazon WorkSpaces Thin Client is integrated with AWS CloudFormation, a service that helps you model and set up your AWS resources. This way, you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want (such as Environments), and CloudFormation provisions and configures those resources for you.

When you use CloudFormation, you can reuse your template to set up your WorkSpaces Thin Client resources consistently and repeatedly. Describe your resources once, and then provision the same resources repeatedly in multiple AWS accounts and Regions.

## WorkSpaces Thin Client and CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for WorkSpaces Thin Client and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML format. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML formats, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

WorkSpaces Thin Client supports creating Environments in CloudFormation. For more information, including examples of JSON and YAML templates for Environments, see the [Amazon WorkSpaces Thin Client resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WorkSpacesThinClient.html) in the *AWS CloudFormation User Guide*.

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)
