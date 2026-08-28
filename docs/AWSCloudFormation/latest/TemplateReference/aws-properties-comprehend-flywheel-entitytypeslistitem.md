---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-comprehend-flywheel-entitytypeslistitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::Flywheel EntityTypesListItem
<a name="aws-properties-comprehend-flywheel-entitytypeslistitem"></a>

An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.

## Syntax
<a name="aws-properties-comprehend-flywheel-entitytypeslistitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-comprehend-flywheel-entitytypeslistitem-syntax.json"></a>

```
{
  "[Type](#cfn-comprehend-flywheel-entitytypeslistitem-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-comprehend-flywheel-entitytypeslistitem-syntax.yaml"></a>

```
  [Type](#cfn-comprehend-flywheel-entitytypeslistitem-type): {{String}}
```

## Properties
<a name="aws-properties-comprehend-flywheel-entitytypeslistitem-properties"></a>

`Type`  <a name="cfn-comprehend-flywheel-entitytypeslistitem-type"></a>
An entity type within a labeled training dataset that Amazon Comprehend uses to train a custom entity recognizer.
Entity types must not contain the following invalid characters: \\n (line break), \\\\n (escaped line break, \\r (carriage return), \\\\r (escaped carriage return), \\t (tab), \\\\t (escaped tab), and , (comma).
*Required*: Yes
*Type*: String
*Pattern*: `^(?![^\n\r\t,]*\\n|\\r|\\t)[^\n\r\t,]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
