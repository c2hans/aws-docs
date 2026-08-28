---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-comprehend-flywheel-entityrecognitionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::Flywheel EntityRecognitionConfig
<a name="aws-properties-comprehend-flywheel-entityrecognitionconfig"></a>

Configuration required for an entity recognition model.

## Syntax
<a name="aws-properties-comprehend-flywheel-entityrecognitionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-comprehend-flywheel-entityrecognitionconfig-syntax.json"></a>

```
{
  "[EntityTypes](#cfn-comprehend-flywheel-entityrecognitionconfig-entitytypes)" : {{[ EntityTypesListItem, ... ]}}
}
```

### YAML
<a name="aws-properties-comprehend-flywheel-entityrecognitionconfig-syntax.yaml"></a>

```
  [EntityTypes](#cfn-comprehend-flywheel-entityrecognitionconfig-entitytypes): {{
    - EntityTypesListItem}}
```

## Properties
<a name="aws-properties-comprehend-flywheel-entityrecognitionconfig-properties"></a>

`EntityTypes`  <a name="cfn-comprehend-flywheel-entityrecognitionconfig-entitytypes"></a>
Up to 25 entity types that the model is trained to recognize.
*Required*: No
*Type*: Array of [EntityTypesListItem](aws-properties-comprehend-flywheel-entitytypeslistitem.md)
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
