---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-devicefleet.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::DeviceFleet
<a name="aws-resource-sagemaker-devicefleet"></a>

The `AWS::SageMaker::DeviceFleet` resource is an Amazon SageMaker resource type that allows you to create a DeviceFleet that manages your SageMaker Edge Manager Devices. You must register your devices against the `DeviceFleet` separately.

## Syntax
<a name="aws-resource-sagemaker-devicefleet-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-devicefleet-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::DeviceFleet",
  "Properties" : {
      "[Description](#cfn-sagemaker-devicefleet-description)" : {{String}},
      "[DeviceFleetName](#cfn-sagemaker-devicefleet-devicefleetname)" : {{String}},
      "[OutputConfig](#cfn-sagemaker-devicefleet-outputconfig)" : {{EdgeOutputConfig}},
      "[RoleArn](#cfn-sagemaker-devicefleet-rolearn)" : {{String}},
      "[Tags](#cfn-sagemaker-devicefleet-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-devicefleet-syntax.yaml"></a>

```
Type: AWS::SageMaker::DeviceFleet
Properties:
  [Description](#cfn-sagemaker-devicefleet-description): {{String}}
  [DeviceFleetName](#cfn-sagemaker-devicefleet-devicefleetname): {{String}}
  [OutputConfig](#cfn-sagemaker-devicefleet-outputconfig): {{
    EdgeOutputConfig}}
  [RoleArn](#cfn-sagemaker-devicefleet-rolearn): {{String}}
  [Tags](#cfn-sagemaker-devicefleet-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-devicefleet-properties"></a>

`Description`  <a name="cfn-sagemaker-devicefleet-description"></a>
A description of the fleet.
*Required*: No
*Type*: String
*Pattern*: `[\S\s]+`
*Minimum*: `0`
*Maximum*: `800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceFleetName`  <a name="cfn-sagemaker-devicefleet-devicefleetname"></a>
Name of the device fleet.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*_*[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputConfig`  <a name="cfn-sagemaker-devicefleet-outputconfig"></a>
The output configuration for storing sample data collected by the fleet.
*Required*: Yes
*Type*: [EdgeOutputConfig](aws-properties-sagemaker-devicefleet-edgeoutputconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-sagemaker-devicefleet-rolearn"></a>
The Amazon Resource Name (ARN) that has access to AWS Internet of Things (IoT).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-devicefleet-tags"></a>
An array of key-value pairs that contain metadata to help you categorize and organize your device fleets. Each tag consists of a key and a value, both of which you define.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-devicefleet-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-devicefleet-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-devicefleet-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the DeviceFleetName.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).
