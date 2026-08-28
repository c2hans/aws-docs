---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-ephemeralstorage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition EphemeralStorage
<a name="aws-properties-batch-jobdefinition-ephemeralstorage"></a>

The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on AWS Fargate.

## Syntax
<a name="aws-properties-batch-jobdefinition-ephemeralstorage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-ephemeralstorage-syntax.json"></a>

```
{
  "[SizeInGiB](#cfn-batch-jobdefinition-ephemeralstorage-sizeingib)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-ephemeralstorage-syntax.yaml"></a>

```
  [SizeInGiB](#cfn-batch-jobdefinition-ephemeralstorage-sizeingib): {{Integer}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-ephemeralstorage-properties"></a>

`SizeInGiB`  <a name="cfn-batch-jobdefinition-ephemeralstorage-sizeingib"></a>
The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is `21` GiB and the maximum supported value is `200` GiB.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
