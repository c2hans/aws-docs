---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application Tag
<a name="aws-properties-kinesisanalyticsv2-application-tag"></a>

A key-value pair (the value is optional) that you can define and assign to Amazon resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see [Using Tagging](https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html).

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-tag-syntax.json"></a>

```
{
  "[Key](#cfn-kinesisanalyticsv2-application-tag-key)" : {{String}},
  "[Value](#cfn-kinesisanalyticsv2-application-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-tag-syntax.yaml"></a>

```
  [Key](#cfn-kinesisanalyticsv2-application-tag-key): {{String}}
  [Value](#cfn-kinesisanalyticsv2-application-tag-value): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-tag-properties"></a>

`Key`  <a name="cfn-kinesisanalyticsv2-application-tag-key"></a>
The key of the key-value tag.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-kinesisanalyticsv2-application-tag-value"></a>
The value of the key-value tag. The value is optional.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
