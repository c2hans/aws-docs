---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iottwinmaker-componenttype-status.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::ComponentType Status
<a name="aws-properties-iottwinmaker-componenttype-status"></a>

The component type status.

## Syntax
<a name="aws-properties-iottwinmaker-componenttype-status-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iottwinmaker-componenttype-status-syntax.json"></a>

```
{
  "[Error](#cfn-iottwinmaker-componenttype-status-error)" : {{Error}},
  "[State](#cfn-iottwinmaker-componenttype-status-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-iottwinmaker-componenttype-status-syntax.yaml"></a>

```
  [Error](#cfn-iottwinmaker-componenttype-status-error): {{
    Error}}
  [State](#cfn-iottwinmaker-componenttype-status-state): {{String}}
```

## Properties
<a name="aws-properties-iottwinmaker-componenttype-status-properties"></a>

`Error`  <a name="cfn-iottwinmaker-componenttype-status-error"></a>
The component type error.
*Required*: No
*Type*: [Error](aws-properties-iottwinmaker-componenttype-error.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-iottwinmaker-componenttype-status-state"></a>
The component type status state.
*Required*: No
*Type*: String
*Allowed values*: `CREATING | UPDATING | DELETING | ACTIVE | ERROR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
