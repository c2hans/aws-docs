---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cur-reportdefinition-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CUR::ReportDefinition Tag
<a name="aws-properties-cur-reportdefinition-tag"></a>

Describes a tag. A tag is a key-value pair. You can add up to 50 tags to a report definition.

## Syntax
<a name="aws-properties-cur-reportdefinition-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cur-reportdefinition-tag-syntax.json"></a>

```
{
  "[Key](#cfn-cur-reportdefinition-tag-key)" : {{String}},
  "[Value](#cfn-cur-reportdefinition-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-cur-reportdefinition-tag-syntax.yaml"></a>

```
  [Key](#cfn-cur-reportdefinition-tag-key): {{String}}
  [Value](#cfn-cur-reportdefinition-tag-value): {{String}}
```

## Properties
<a name="aws-properties-cur-reportdefinition-tag-properties"></a>

`Key`  <a name="cfn-cur-reportdefinition-tag-key"></a>
The key of the tag. Tag keys are case sensitive. Each report definition can only have up to one tag with the same key. If you try to add an existing tag with the same key, the existing tag value will be updated to the new value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-cur-reportdefinition-tag-value"></a>
The value of the tag. Tag values are case-sensitive. This can be an empty string.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
