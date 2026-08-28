---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-batcharrayproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe BatchArrayProperties
<a name="aws-properties-pipes-pipe-batcharrayproperties"></a>

The array properties for the submitted job, such as the size of the array. The array size can be between 2 and 10,000. If you specify array properties for a job, it becomes an array job. This parameter is used only if the target is an AWS Batch job.

## Syntax
<a name="aws-properties-pipes-pipe-batcharrayproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-batcharrayproperties-syntax.json"></a>

```
{
  "[Size](#cfn-pipes-pipe-batcharrayproperties-size)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-batcharrayproperties-syntax.yaml"></a>

```
  [Size](#cfn-pipes-pipe-batcharrayproperties-size): {{Integer}}
```

## Properties
<a name="aws-properties-pipes-pipe-batcharrayproperties-properties"></a>

`Size`  <a name="cfn-pipes-pipe-batcharrayproperties-size"></a>
The size of the array, if this is an array batch job.
*Required*: No
*Type*: Integer
*Minimum*: `2`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
