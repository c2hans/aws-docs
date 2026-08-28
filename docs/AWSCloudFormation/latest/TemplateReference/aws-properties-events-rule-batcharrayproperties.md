---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-rule-batcharrayproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Rule BatchArrayProperties
<a name="aws-properties-events-rule-batcharrayproperties"></a>

The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an AWS Batch job.

## Syntax
<a name="aws-properties-events-rule-batcharrayproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-rule-batcharrayproperties-syntax.json"></a>

```
{
  "[Size](#cfn-events-rule-batcharrayproperties-size)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-events-rule-batcharrayproperties-syntax.yaml"></a>

```
  [Size](#cfn-events-rule-batcharrayproperties-size): {{Integer}}
```

## Properties
<a name="aws-properties-events-rule-batcharrayproperties-properties"></a>

`Size`  <a name="cfn-events-rule-batcharrayproperties-size"></a>
The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-events-rule-batcharrayproperties--examples"></a>

### Set the BatchArrayProperties property
<a name="aws-properties-events-rule-batcharrayproperties--examples--Set_the_BatchArrayProperties_property"></a>

The following example sets the `BatchArrayProperties` property to 950.

#### JSON
<a name="aws-properties-events-rule-batcharrayproperties--examples--Set_the_BatchArrayProperties_property--json"></a>

```
"ArrayProperties": {
  "Size": 950
}
```

#### YAML
<a name="aws-properties-events-rule-batcharrayproperties--examples--Set_the_BatchArrayProperties_property--yaml"></a>

```
ArrayProperties:
  Size: 950
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
