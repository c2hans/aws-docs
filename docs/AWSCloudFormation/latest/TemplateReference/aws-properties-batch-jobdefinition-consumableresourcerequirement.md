---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-consumableresourcerequirement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition ConsumableResourceRequirement
<a name="aws-properties-batch-jobdefinition-consumableresourcerequirement"></a>

Information about a consumable resource required to run a job.

## Syntax
<a name="aws-properties-batch-jobdefinition-consumableresourcerequirement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-consumableresourcerequirement-syntax.json"></a>

```
{
  "[ConsumableResource](#cfn-batch-jobdefinition-consumableresourcerequirement-consumableresource)" : {{String}},
  "[Quantity](#cfn-batch-jobdefinition-consumableresourcerequirement-quantity)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-consumableresourcerequirement-syntax.yaml"></a>

```
  [ConsumableResource](#cfn-batch-jobdefinition-consumableresourcerequirement-consumableresource): {{String}}
  [Quantity](#cfn-batch-jobdefinition-consumableresourcerequirement-quantity): {{Integer}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-consumableresourcerequirement-properties"></a>

`ConsumableResource`  <a name="cfn-batch-jobdefinition-consumableresourcerequirement-consumableresource"></a>
The name or ARN of the consumable resource.
*Required*: Yes
*Type*: String
*Pattern*: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Quantity`  <a name="cfn-batch-jobdefinition-consumableresourcerequirement-quantity"></a>
The quantity of the consumable resource that is needed.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
