---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-fpgaimage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::FpgaImage
<a name="aws-resource-ec2-fpgaimage"></a>

Describes an Amazon FPGA image (AFI).

## Syntax
<a name="aws-resource-ec2-fpgaimage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-fpgaimage-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::FpgaImage",
  "Properties" : {
      "[Description](#cfn-ec2-fpgaimage-description)" : {{String}},
      "[InputStorageLocation](#cfn-ec2-fpgaimage-inputstoragelocation)" : {{StorageLocation}},
      "[LogsStorageLocation](#cfn-ec2-fpgaimage-logsstoragelocation)" : {{StorageLocation}},
      "[Name](#cfn-ec2-fpgaimage-name)" : {{String}},
      "[Tags](#cfn-ec2-fpgaimage-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-fpgaimage-syntax.yaml"></a>

```
Type: AWS::EC2::FpgaImage
Properties:
  [Description](#cfn-ec2-fpgaimage-description): {{String}}
  [InputStorageLocation](#cfn-ec2-fpgaimage-inputstoragelocation): {{
    StorageLocation}}
  [LogsStorageLocation](#cfn-ec2-fpgaimage-logsstoragelocation): {{
    StorageLocation}}
  [Name](#cfn-ec2-fpgaimage-name): {{String}}
  [Tags](#cfn-ec2-fpgaimage-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-fpgaimage-properties"></a>

`Description`  <a name="cfn-ec2-fpgaimage-description"></a>
The description of the AFI.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputStorageLocation`  <a name="cfn-ec2-fpgaimage-inputstoragelocation"></a>
Describes a storage location in Amazon S3.
*Required*: No
*Type*: [StorageLocation](aws-properties-ec2-fpgaimage-storagelocation.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogsStorageLocation`  <a name="cfn-ec2-fpgaimage-logsstoragelocation"></a>
Describes a storage location in Amazon S3.
*Required*: No
*Type*: [StorageLocation](aws-properties-ec2-fpgaimage-storagelocation.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-ec2-fpgaimage-name"></a>
The name of the AFI.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-fpgaimage-tags"></a>
Any tags assigned to the AFI.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-fpgaimage-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-fpgaimage-return-values"></a>

### Ref
<a name="aws-resource-ec2-fpgaimage-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-fpgaimage-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-fpgaimage-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreateTime`  <a name="CreateTime-fn::getatt"></a>
The date and time the AFI was created.

`DataRetentionSupport`  <a name="DataRetentionSupport-fn::getatt"></a>
Indicates whether data retention support is enabled for the AFI.

`FpgaImageGlobalId`  <a name="FpgaImageGlobalId-fn::getatt"></a>
The global FPGA image identifier (AGFI ID).

`FpgaImageId`  <a name="FpgaImageId-fn::getatt"></a>
The FPGA image identifier (AFI ID).

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
The ID of the AWS account that owns the AFI.

`Public`  <a name="Public-fn::getatt"></a>
Indicates whether the AFI is public.

`State`  <a name="State-fn::getatt"></a>
Information about the state of the AFI.

`UpdateTime`  <a name="UpdateTime-fn::getatt"></a>
The time of the most recent update to the AFI.
