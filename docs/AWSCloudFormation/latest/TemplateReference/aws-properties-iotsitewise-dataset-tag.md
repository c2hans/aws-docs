---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-dataset-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Dataset Tag
<a name="aws-properties-iotsitewise-dataset-tag"></a>

Metadata assigned to an AWS IoT SiteWise resource that consists of a key-value pair.

## Syntax
<a name="aws-properties-iotsitewise-dataset-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-dataset-tag-syntax.json"></a>

```
{
  "[Key](#cfn-iotsitewise-dataset-tag-key)" : {{String}},
  "[Value](#cfn-iotsitewise-dataset-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-dataset-tag-syntax.yaml"></a>

```
  [Key](#cfn-iotsitewise-dataset-tag-key): {{String}}
  [Value](#cfn-iotsitewise-dataset-tag-value): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-dataset-tag-properties"></a>

`Key`  <a name="cfn-iotsitewise-dataset-tag-key"></a>
The key or name that identifies the tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iotsitewise-dataset-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
