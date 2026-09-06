---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-command.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Command
<a name="aws-resource-iot-command"></a>

<a name="aws-resource-iot-command-description"></a>The `AWS::IoT::Command` resource Property description not available. for IoT.

## Syntax
<a name="aws-resource-iot-command-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iot-command-syntax.json"></a>

```
{
  "Type" : "AWS::IoT::Command",
  "Properties" : {
      "[CommandId](#cfn-iot-command-commandid)" : {{String}},
      "[CreatedAt](#cfn-iot-command-createdat)" : {{String}},
      "[Deprecated](#cfn-iot-command-deprecated)" : {{Boolean}},
      "[Description](#cfn-iot-command-description)" : {{String}},
      "[DisplayName](#cfn-iot-command-displayname)" : {{String}},
      "[LastUpdatedAt](#cfn-iot-command-lastupdatedat)" : {{String}},
      "[MandatoryParameters](#cfn-iot-command-mandatoryparameters)" : {{[ CommandParameter, ... ]}},
      "[Namespace](#cfn-iot-command-namespace)" : {{String}},
      "[Payload](#cfn-iot-command-payload)" : {{CommandPayload}},
      "[PayloadTemplate](#cfn-iot-command-payloadtemplate)" : {{String}},
      "[PendingDeletion](#cfn-iot-command-pendingdeletion)" : {{Boolean}},
      "[Preprocessor](#cfn-iot-command-preprocessor)" : {{CommandPreprocessor}},
      "[RoleArn](#cfn-iot-command-rolearn)" : {{String}},
      "[Tags](#cfn-iot-command-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iot-command-syntax.yaml"></a>

```
Type: AWS::IoT::Command
Properties:
  [CommandId](#cfn-iot-command-commandid): {{String}}
  [CreatedAt](#cfn-iot-command-createdat): {{String}}
  [Deprecated](#cfn-iot-command-deprecated): {{Boolean}}
  [Description](#cfn-iot-command-description): {{String}}
  [DisplayName](#cfn-iot-command-displayname): {{String}}
  [LastUpdatedAt](#cfn-iot-command-lastupdatedat): {{String}}
  [MandatoryParameters](#cfn-iot-command-mandatoryparameters): {{
    - CommandParameter}}
  [Namespace](#cfn-iot-command-namespace): {{String}}
  [Payload](#cfn-iot-command-payload): {{
    CommandPayload}}
  [PayloadTemplate](#cfn-iot-command-payloadtemplate): {{String}}
  [PendingDeletion](#cfn-iot-command-pendingdeletion): {{Boolean}}
  [Preprocessor](#cfn-iot-command-preprocessor): {{
    CommandPreprocessor}}
  [RoleArn](#cfn-iot-command-rolearn): {{String}}
  [Tags](#cfn-iot-command-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iot-command-properties"></a>

`CommandId`  <a name="cfn-iot-command-commandid"></a>
The unique identifier of the command.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CreatedAt`  <a name="cfn-iot-command-createdat"></a>
The timestamp, when the command was created.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Deprecated`  <a name="cfn-iot-command-deprecated"></a>
Indicates whether the command has been deprecated.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-iot-command-description"></a>
The description of the command parameter.
*Required*: No
*Type*: String
*Maximum*: `2028`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-iot-command-displayname"></a>
The display name of the command.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LastUpdatedAt`  <a name="cfn-iot-command-lastupdatedat"></a>
The timestamp, when the command was last updated.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MandatoryParameters`  <a name="cfn-iot-command-mandatoryparameters"></a>
Property description not available.
*Required*: No
*Type*: Array of [CommandParameter](aws-properties-iot-command-commandparameter.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-iot-command-namespace"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `AWS-IoT | AWS-IoT-FleetWise`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Payload`  <a name="cfn-iot-command-payload"></a>
Property description not available.
*Required*: No
*Type*: [CommandPayload](aws-properties-iot-command-commandpayload.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PayloadTemplate`  <a name="cfn-iot-command-payloadtemplate"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `32768`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PendingDeletion`  <a name="cfn-iot-command-pendingdeletion"></a>
Indicates whether the command is pending deletion.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Preprocessor`  <a name="cfn-iot-command-preprocessor"></a>
Property description not available.
*Required*: No
*Type*: [CommandPreprocessor](aws-properties-iot-command-commandpreprocessor.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-iot-command-rolearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2028`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iot-command-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-iot-command-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iot-command-return-values"></a>

### Ref
<a name="aws-resource-iot-command-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-iot-command-return-values-fn--getatt"></a>

####
<a name="aws-resource-iot-command-return-values-fn--getatt-fn--getatt"></a>

`CommandArn`  <a name="CommandArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the command.
