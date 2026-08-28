---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationazureblob-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationAzureBlob Tag
<a name="aws-properties-datasync-locationazureblob-tag"></a>

Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your transfer location.

## Syntax
<a name="aws-properties-datasync-locationazureblob-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationazureblob-tag-syntax.json"></a>

```
{
  "[Key](#cfn-datasync-locationazureblob-tag-key)" : {{String}},
  "[Value](#cfn-datasync-locationazureblob-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-locationazureblob-tag-syntax.yaml"></a>

```
  [Key](#cfn-datasync-locationazureblob-tag-key): {{String}}
  [Value](#cfn-datasync-locationazureblob-tag-value): {{String}}
```

## Properties
<a name="aws-properties-datasync-locationazureblob-tag-properties"></a>

`Key`  <a name="cfn-datasync-locationazureblob-tag-key"></a>
The key for an AWS resource tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s+=._:/-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-datasync-locationazureblob-tag-value"></a>
The value for an AWS resource tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s+=._:@/-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
