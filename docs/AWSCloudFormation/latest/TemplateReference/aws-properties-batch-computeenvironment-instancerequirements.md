---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-instancerequirements.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment InstanceRequirements
<a name="aws-properties-batch-computeenvironment-instancerequirements"></a>

The instance type requirements for the Amazon ECS Managed Instances capacity provider. Use this to specify which Amazon EC2 instance types or instance families Amazon ECS can launch.

## Syntax
<a name="aws-properties-batch-computeenvironment-instancerequirements-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-instancerequirements-syntax.json"></a>

```
{
  "[AllowedInstanceTypes](#cfn-batch-computeenvironment-instancerequirements-allowedinstancetypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-instancerequirements-syntax.yaml"></a>

```
  [AllowedInstanceTypes](#cfn-batch-computeenvironment-instancerequirements-allowedinstancetypes): {{
    - String}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-instancerequirements-properties"></a>

`AllowedInstanceTypes`  <a name="cfn-batch-computeenvironment-instancerequirements-allowedinstancetypes"></a>
A list of specific instance types or instance families that Amazon ECS can launch (for example, `m5.large` or `g5`). When specified, only these instance types are used.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
