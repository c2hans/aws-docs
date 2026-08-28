---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-ecssettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment EcsSettings
<a name="aws-properties-batch-computeenvironment-ecssettings"></a>

The Amazon ECS settings for a compute environment, including the CloudWatch Container Insights mode. Use this structure with `CreateComputeEnvironment` and `UpdateComputeEnvironment`.

## Syntax
<a name="aws-properties-batch-computeenvironment-ecssettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-ecssettings-syntax.json"></a>

```
{
  "[ContainerInsights](#cfn-batch-computeenvironment-ecssettings-containerinsights)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-ecssettings-syntax.yaml"></a>

```
  [ContainerInsights](#cfn-batch-computeenvironment-ecssettings-containerinsights): {{String}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-ecssettings-properties"></a>

`ContainerInsights`  <a name="cfn-batch-computeenvironment-ecssettings-containerinsights"></a>
Specifies the CloudWatch Container Insights mode for the compute environment. Valid values are:
ENABLED
Turns on standard Container Insights, which collects CPU, memory, disk, and network utilization metrics for the compute environment.
ENHANCED
Turns on enhanced Container Insights, which collects the standard metrics along with additional per-task observability metrics.
DISABLED
Turns off Container Insights for the compute environment.
If you don't specify a value, the default is `DISABLED`. For more information, see [Container Insights](https://docs.aws.amazon.com/batch/latest/userguide/cloudwatch-container-insights.html) in the *AWS Batch User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | ENHANCED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
