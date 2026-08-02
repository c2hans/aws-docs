---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iottwinmaker-componenttype-error.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::ComponentType Error
<a name="aws-properties-iottwinmaker-componenttype-error"></a>

The component type error.

## Syntax
<a name="aws-properties-iottwinmaker-componenttype-error-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iottwinmaker-componenttype-error-syntax.json"></a>

```
{
  "[Code](#cfn-iottwinmaker-componenttype-error-code)" : {{String}},
  "[Message](#cfn-iottwinmaker-componenttype-error-message)" : {{String}}
}
```

### YAML
<a name="aws-properties-iottwinmaker-componenttype-error-syntax.yaml"></a>

```
  [Code](#cfn-iottwinmaker-componenttype-error-code): {{String}}
  [Message](#cfn-iottwinmaker-componenttype-error-message): {{String}}
```

## Properties
<a name="aws-properties-iottwinmaker-componenttype-error-properties"></a>

`Code`  <a name="cfn-iottwinmaker-componenttype-error-code"></a>
The component type error code.
*Required*: No
*Type*: String
*Allowed values*: `VALIDATION_ERROR | INTERNAL_FAILURE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Message`  <a name="cfn-iottwinmaker-componenttype-error-message"></a>
The component type error message.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
