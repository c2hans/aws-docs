---
source_url: https://docs.aws.amazon.com/autoscaling/plans/userguide/gs-next-steps.html
---

# Step 6: Next steps
<a name="gs-next-steps"></a>

Now that you have familiarized yourself with scaling plans and some of its features, you may want to try creating your own scaling plan template using CloudFormation.

An CloudFormation template is a JSON or YAML-formatted text file that describes the Amazon Web Services infrastructure needed to run an application or service along with any interconnections among infrastructure components. With CloudFormation, you deploy and manage an associated collection of resources as a *stack*. CloudFormation is available at no additional charge, and you pay only for the AWS resources needed to run your applications. Resources can consist of any AWS resource you define within the template. For more information, see [How CloudFormation works](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-overview.html) in the *AWS CloudFormation User Guide*.

In the *AWS CloudFormation User Guide*, we provide a simple template to get you started. The sample template is available as an example in the [AWS::AutoScalingPlans::ScalingPlan](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html) section of the CloudFormation template reference documentation. The sample template creates a scaling plan for a single Auto Scaling group and enables predictive scaling and dynamic scaling.

For more information, see [Getting started with CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.html) in the *AWS CloudFormation User Guide*.
