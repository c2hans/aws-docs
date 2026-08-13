---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-mitigationaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::MitigationAction
<a name="aws-resource-iot-mitigationaction"></a>

Defines an action that can be applied to audit findings by using StartAuditMitigationActionsTask. For API reference, see [CreateMitigationAction](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateMitigationAction.html) and for general information, see [Mitigation actions](https://docs.aws.amazon.com/iot/latest/developerguide/dd-mitigation-actions.html).

## Syntax
<a name="aws-resource-iot-mitigationaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iot-mitigationaction-syntax.json"></a>

```
{
  "Type" : "AWS::IoT::MitigationAction",
  "Properties" : {
      "[ActionName](#cfn-iot-mitigationaction-actionname)" : {{String}},
      "[ActionParams](#cfn-iot-mitigationaction-actionparams)" : {{ActionParams}},
      "[RoleArn](#cfn-iot-mitigationaction-rolearn)" : {{String}},
      "[Tags](#cfn-iot-mitigationaction-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iot-mitigationaction-syntax.yaml"></a>

```
Type: AWS::IoT::MitigationAction
Properties:
  [ActionName](#cfn-iot-mitigationaction-actionname): {{String}}
  [ActionParams](#cfn-iot-mitigationaction-actionparams): {{
    ActionParams}}
  [RoleArn](#cfn-iot-mitigationaction-rolearn): {{String}}
  [Tags](#cfn-iot-mitigationaction-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iot-mitigationaction-properties"></a>

`ActionName`  <a name="cfn-iot-mitigationaction-actionname"></a>
The friendly name of the mitigation action.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9:_-]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ActionParams`  <a name="cfn-iot-mitigationaction-actionparams"></a>
The set of parameters for this mitigation action. The parameters vary, depending on the kind of action you apply.
*Required*: Yes
*Type*: [ActionParams](aws-properties-iot-mitigationaction-actionparams.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iot-mitigationaction-rolearn"></a>
The IAM role ARN used to apply this mitigation action.
*Required*: Yes
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iot-mitigationaction-tags"></a>
Metadata that can be used to manage the mitigation action.
*Required*: No
*Type*: Array of [Tag](aws-properties-iot-mitigationaction-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iot-mitigationaction-return-values"></a>

### Ref
<a name="aws-resource-iot-mitigationaction-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the mitigation action name.

### Fn::GetAtt
<a name="aws-resource-iot-mitigationaction-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iot-mitigationaction-return-values-fn--getatt-fn--getatt"></a>

`MitigationActionArn`  <a name="MitigationActionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the mitigation action.

`MitigationActionId`  <a name="MitigationActionId-fn::getatt"></a>
The ID of the mitigation action.

## Examples
<a name="aws-resource-iot-mitigationaction--examples"></a>

###
<a name="aws-resource-iot-mitigationaction--examples--"></a>

#### JSON
<a name="aws-resource-iot-mitigationaction--examples----json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Amazon Web Services IoT MitigationAction Sample Template",
  "Resources": {
    "PublishToSnsMitigationAction": {
      "Type": "AWS::IoT::MitigationAction",
      "Properties": {
        "ActionName": "PublishToSns",
        "RoleArn": "arn:aws:us-east-1:123456789012:iam:role/RoleForIoTMitigationActions",
        "ActionParams": {
          "PublishFindingToSnsParams": {
            "TopicArn": "arn:aws:sns:us-east-1:123456789012:IoTFindingNotifications"
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-iot-mitigationaction--examples----yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Description: Amazon Web Services IoT MitigationAction Sample Template
Resources:
  PublishToSnsMitigationAction:
    Type: AWS::IoT::MitigationAction
    Properties:
      ActionName: PublishToSns
      RoleArn: arn:aws:us-east-1:123456789012:iam:role/RoleForIoTMitigationActions
      ActionParams:
        PublishFindingToSnsParams:
          TopicArn: arn:aws:sns:us-east-1:123456789012:IoTFindingNotifications
```
