---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-comprehend-flywheeldataset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::FlywheelDataset
<a name="aws-resource-comprehend-flywheeldataset"></a>

<a name="aws-resource-comprehend-flywheeldataset-description"></a>The `AWS::Comprehend::FlywheelDataset` resource Property description not available. for Comprehend.

## Syntax
<a name="aws-resource-comprehend-flywheeldataset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-comprehend-flywheeldataset-syntax.json"></a>

```
{
  "Type" : "AWS::Comprehend::FlywheelDataset",
  "Properties" : {
      "[DatasetName](#cfn-comprehend-flywheeldataset-datasetname)" : {{String}},
      "[DatasetType](#cfn-comprehend-flywheeldataset-datasettype)" : {{String}},
      "[Description](#cfn-comprehend-flywheeldataset-description)" : {{String}},
      "[FlywheelArn](#cfn-comprehend-flywheeldataset-flywheelarn)" : {{String}},
      "[Tags](#cfn-comprehend-flywheeldataset-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-comprehend-flywheeldataset-syntax.yaml"></a>

```
Type: AWS::Comprehend::FlywheelDataset
Properties:
  [DatasetName](#cfn-comprehend-flywheeldataset-datasetname): {{String}}
  [DatasetType](#cfn-comprehend-flywheeldataset-datasettype): {{String}}
  [Description](#cfn-comprehend-flywheeldataset-description): {{String}}
  [FlywheelArn](#cfn-comprehend-flywheeldataset-flywheelarn): {{String}}
  [Tags](#cfn-comprehend-flywheeldataset-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-comprehend-flywheeldataset-properties"></a>

`DatasetName`  <a name="cfn-comprehend-flywheeldataset-datasetname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatasetType`  <a name="cfn-comprehend-flywheeldataset-datasettype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `TRAIN | TEST`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-comprehend-flywheeldataset-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FlywheelArn`  <a name="cfn-comprehend-flywheeldataset-flywheelarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-comprehend-flywheeldataset-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-comprehend-flywheeldataset-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-comprehend-flywheeldataset-return-values"></a>

### Ref
<a name="aws-resource-comprehend-flywheeldataset-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-comprehend-flywheeldataset-return-values-fn--getatt"></a>

####
<a name="aws-resource-comprehend-flywheeldataset-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Property description not available.

`DatasetArn`  <a name="DatasetArn-fn::getatt"></a>
Property description not available.

`DatasetS3Uri`  <a name="DatasetS3Uri-fn::getatt"></a>
Property description not available.

`NumberOfDocuments`  <a name="NumberOfDocuments-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.
