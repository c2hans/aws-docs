---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-computescalingpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment ComputeScalingPolicy
<a name="aws-properties-batch-computeenvironment-computescalingpolicy"></a>

An object that represents a scaling policy for a compute environment.

## Syntax
<a name="aws-properties-batch-computeenvironment-computescalingpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-computescalingpolicy-syntax.json"></a>

```
{
  "[MinScaleDownDelayMinutes](#cfn-batch-computeenvironment-computescalingpolicy-minscaledowndelayminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-computescalingpolicy-syntax.yaml"></a>

```
  [MinScaleDownDelayMinutes](#cfn-batch-computeenvironment-computescalingpolicy-minscaledowndelayminutes): {{Integer}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-computescalingpolicy-properties"></a>

`MinScaleDownDelayMinutes`  <a name="cfn-batch-computeenvironment-computescalingpolicy-minscaledowndelayminutes"></a>
The minimum time (in minutes) that AWS Batch keeps instances running in the compute environment after their jobs complete. For each instance, the delay period begins when the last job finishes. If no new jobs are placed on the instance during this delay, AWS Batch terminates the instance once the delay expires.
Valid Range: Minimum value of 20. Maximum value of 10080. Use 0 to unset and disable the scale down delay.
Idle instances retained during the scale-down delay period are billable at standard EC2 pricing.
The scale down delay does not apply to:
+ Instances being replaced during infrastructure updates
+ Newly launched instances that have not yet run any jobs
+ Spot instances reclaimed due to interruption
*Required*: No
*Type*: Integer
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
