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
