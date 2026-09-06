---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iottwinmaker-componenttype-compositecomponenttype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::ComponentType CompositeComponentType
<a name="aws-properties-iottwinmaker-componenttype-compositecomponenttype"></a>

Specifies the ID of the composite component type.

## Syntax
<a name="aws-properties-iottwinmaker-componenttype-compositecomponenttype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iottwinmaker-componenttype-compositecomponenttype-syntax.json"></a>

```
{
  "[ComponentTypeId](#cfn-iottwinmaker-componenttype-compositecomponenttype-componenttypeid)" : {{String}}
}
```

### YAML
<a name="aws-properties-iottwinmaker-componenttype-compositecomponenttype-syntax.yaml"></a>

```
  [ComponentTypeId](#cfn-iottwinmaker-componenttype-compositecomponenttype-componenttypeid): {{String}}
```

## Properties
<a name="aws-properties-iottwinmaker-componenttype-compositecomponenttype-properties"></a>

`ComponentTypeId`  <a name="cfn-iottwinmaker-componenttype-compositecomponenttype-componenttypeid"></a>
The ID of the component type.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z_\.\-0-9:]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
