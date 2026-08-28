---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-ephemeralstorage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskDefinition EphemeralStorage
<a name="aws-properties-ecs-taskdefinition-ephemeralstorage"></a>

The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on AWS Fargate. For more information, see [Using data volumes in tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html) in the *Amazon ECS Developer Guide;*.

**Note**
For tasks using the Fargate launch type, the task requires the following platforms:
Linux platform version `1.4.0` or later.
Windows platform version `1.0.0` or later.

## Syntax
<a name="aws-properties-ecs-taskdefinition-ephemeralstorage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskdefinition-ephemeralstorage-syntax.json"></a>

```
{
  "[SizeInGiB](#cfn-ecs-taskdefinition-ephemeralstorage-sizeingib)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ecs-taskdefinition-ephemeralstorage-syntax.yaml"></a>

```
  [SizeInGiB](#cfn-ecs-taskdefinition-ephemeralstorage-sizeingib): {{Integer}}
```

## Properties
<a name="aws-properties-ecs-taskdefinition-ephemeralstorage-properties"></a>

`SizeInGiB`  <a name="cfn-ecs-taskdefinition-ephemeralstorage-sizeingib"></a>
The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is `21` GiB and the maximum supported value is `200` GiB.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
