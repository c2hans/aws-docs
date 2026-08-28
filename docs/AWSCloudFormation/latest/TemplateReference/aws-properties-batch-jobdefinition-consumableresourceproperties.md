---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-consumableresourceproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition ConsumableResourceProperties
<a name="aws-properties-batch-jobdefinition-consumableresourceproperties"></a>

Contains a list of consumable resources required by a job.

## Syntax
<a name="aws-properties-batch-jobdefinition-consumableresourceproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-consumableresourceproperties-syntax.json"></a>

```
{
  "[ConsumableResourceList](#cfn-batch-jobdefinition-consumableresourceproperties-consumableresourcelist)" : {{[ ConsumableResourceRequirement, ... ]}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-consumableresourceproperties-syntax.yaml"></a>

```
  [ConsumableResourceList](#cfn-batch-jobdefinition-consumableresourceproperties-consumableresourcelist): {{
    - ConsumableResourceRequirement}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-consumableresourceproperties-properties"></a>

`ConsumableResourceList`  <a name="cfn-batch-jobdefinition-consumableresourceproperties-consumableresourcelist"></a>
The list of consumable resources required by a job.
*Required*: Yes
*Type*: Array of [ConsumableResourceRequirement](aws-properties-batch-jobdefinition-consumableresourcerequirement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
