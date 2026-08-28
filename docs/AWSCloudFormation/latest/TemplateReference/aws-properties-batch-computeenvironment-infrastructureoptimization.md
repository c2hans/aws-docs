---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-infrastructureoptimization.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment InfrastructureOptimization
<a name="aws-properties-batch-computeenvironment-infrastructureoptimization"></a>

The infrastructure optimization configuration for an Amazon ECS Managed Instances capacity provider. Specifies the idle-instance scale-in behavior.

## Syntax
<a name="aws-properties-batch-computeenvironment-infrastructureoptimization-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-infrastructureoptimization-syntax.json"></a>

```
{
  "[ScaleInAfter](#cfn-batch-computeenvironment-infrastructureoptimization-scaleinafter)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-infrastructureoptimization-syntax.yaml"></a>

```
  [ScaleInAfter](#cfn-batch-computeenvironment-infrastructureoptimization-scaleinafter): {{Integer}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-infrastructureoptimization-properties"></a>

`ScaleInAfter`  <a name="cfn-batch-computeenvironment-infrastructureoptimization-scaleinafter"></a>
The number of seconds an instance can remain idle before it is terminated. Valid values are `-1` or `0` to `3600`. Use `-1` as a special value to disable scale-in (instances are never terminated for being idle). If not specified, a default value applies.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
