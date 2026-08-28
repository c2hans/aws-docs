---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-vcpucountrangerequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider VCpuCountRangeRequest
<a name="aws-properties-ecs-capacityprovider-vcpucountrangerequest"></a>

The minimum and maximum number of vCPUs for instance type selection. This allows you to specify a range of vCPU counts that meet your workload requirements.

## Syntax
<a name="aws-properties-ecs-capacityprovider-vcpucountrangerequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-vcpucountrangerequest-syntax.json"></a>

```
{
  "[Max](#cfn-ecs-capacityprovider-vcpucountrangerequest-max)" : {{Integer}},
  "[Min](#cfn-ecs-capacityprovider-vcpucountrangerequest-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-vcpucountrangerequest-syntax.yaml"></a>

```
  [Max](#cfn-ecs-capacityprovider-vcpucountrangerequest-max): {{Integer}}
  [Min](#cfn-ecs-capacityprovider-vcpucountrangerequest-min): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-vcpucountrangerequest-properties"></a>

`Max`  <a name="cfn-ecs-capacityprovider-vcpucountrangerequest-max"></a>
The maximum number of vCPUs. Instance types with more vCPUs than this value are excluded from selection.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-ecs-capacityprovider-vcpucountrangerequest-min"></a>
The minimum number of vCPUs. Instance types with fewer vCPUs than this value are excluded from selection.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
