---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/ug/creating-automation-rules-with-cloudformation.html
---

# Creating automation rules with CloudFormation
<a name="creating-automation-rules-with-cloudformation"></a>

AWS Compute Optimizer integrates with AWS CloudFormation, enabling you to define and deploy automation rules with infrastructure-as-code. You can create a template that describes the automation rules you want, and CloudFormation provisions and configures those rules for you. When you use CloudFormation, you can reuse your template to set up your automation rules consistently and repeatedly across multiple AWS accounts.

## Compute Optimizer and CloudFormation templates
<a name="cfn-automation-rules-templates"></a>

To provision and configure automation rules, you must understand how [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) work. Templates are text files in JSON or YAML format. These templates describe the resources that you want to provision in your CloudFormation stacks.

If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

You can create CloudFormation templates for the following types of automation rules:
+ Account rules that apply recommended actions only to your account
+ Organization rules that centrally apply recommended actions across member accounts

For more information, including examples of JSON and YAML templates for automation rules, see [AWS::ComputeOptimizer::AutomationRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.html) in the *AWS CloudFormation User Guide*.

## Learn more about CloudFormation
<a name="cfn-automation-rules-learn-more"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [AWS CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
