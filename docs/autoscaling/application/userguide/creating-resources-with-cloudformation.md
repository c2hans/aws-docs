---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/creating-resources-with-cloudformation.html
---

# Configure Application Auto Scaling resources using AWS CloudFormation
<a name="creating-resources-with-cloudformation"></a>

Application Auto Scaling is integrated with AWS CloudFormation, a service that helps you to model and set up your AWS resources so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes all the AWS resources that you want, and CloudFormation provisions and configures those resources for you.

When you use CloudFormation, you can reuse your template to set up your Application Auto Scaling resources consistently and repeatedly. Describe your resources once, and then provision the same resources over and over in multiple AWS accounts and Regions.

## Application Auto Scaling and CloudFormation templates
<a name="working-with-templates"></a>

To provision and configure resources for Application Auto Scaling and related services, you must understand [CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). Templates are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. If you're unfamiliar with JSON or YAML, you can use CloudFormation Designer to help you get started with CloudFormation templates. For more information, see [What is CloudFormation Designer?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html) in the *AWS CloudFormation User Guide*.

When you create a stack template for Application Auto Scaling resources, you must provide the following:
+ A namespace for the target service (for example, **`appstream`**). See the [AWS::ApplicationAutoScaling::ScalableTarget](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html) reference to obtain service namespaces.
+ A scalable dimension associated with the target resource (for example, **`appstream:fleet:DesiredCapacity`**). See the [AWS::ApplicationAutoScaling::ScalableTarget](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html) reference to obtain scalable dimensions.
+ A resource ID for the target resource (for example, **`fleet/sample-fleet`**). See the [AWS::ApplicationAutoScaling::ScalableTarget](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html) reference for information about the syntax and examples of specific resource IDs.
+ A service-linked role for the target resource (for example, **`arn:aws:iam::012345678910:role/aws-service-role/appstream.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_AppStreamFleet`**). See the [Service-linked role ARN reference](application-auto-scaling-service-linked-roles.md#specify-service-linked-role) table to obtain role ARNs.

To learn more about Application Auto Scaling resources, see the [Application Auto Scaling](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApplicationAutoScaling.html) reference in the *AWS CloudFormation User Guide*.

## Example template snippets
<a name="example-templates"></a>

You can find example snippets to include in CloudFormation templates in the following sections of the *AWS CloudFormation User Guide*:
+ For examples of scaling policies and scheduled actions, see [Configure Application Auto Scaling resources with AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-application-auto-scaling.html).
+ For more examples of scaling policies, see [AWS::ApplicationAutoScaling::ScalingPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html).

## Learn more about CloudFormation
<a name="learn-more-cloudformation"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [CloudFormation API Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/Welcome.html)
+ [AWS CloudFormation Command Line Interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
