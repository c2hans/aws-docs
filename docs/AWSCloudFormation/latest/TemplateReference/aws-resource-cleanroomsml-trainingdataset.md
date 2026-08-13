---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cleanroomsml-trainingdataset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::TrainingDataset
<a name="aws-resource-cleanroomsml-trainingdataset"></a>

Defines the information necessary to create a training dataset. In Clean Rooms ML, the `TrainingDataset` is metadata that points to a Glue table, which is read only during `AudienceModel` creation.

## Syntax
<a name="aws-resource-cleanroomsml-trainingdataset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cleanroomsml-trainingdataset-syntax.json"></a>

```
{
  "Type" : "AWS::CleanRoomsML::TrainingDataset",
  "Properties" : {
      "[Description](#cfn-cleanroomsml-trainingdataset-description)" : {{String}},
      "[Name](#cfn-cleanroomsml-trainingdataset-name)" : {{String}},
      "[RoleArn](#cfn-cleanroomsml-trainingdataset-rolearn)" : {{String}},
      "[Tags](#cfn-cleanroomsml-trainingdataset-tags)" : {{[ Tag, ... ]}},
      "[TrainingData](#cfn-cleanroomsml-trainingdataset-trainingdata)" : {{[ Dataset, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cleanroomsml-trainingdataset-syntax.yaml"></a>

```
Type: AWS::CleanRoomsML::TrainingDataset
Properties:
  [Description](#cfn-cleanroomsml-trainingdataset-description): {{String}}
  [Name](#cfn-cleanroomsml-trainingdataset-name): {{String}}
  [RoleArn](#cfn-cleanroomsml-trainingdataset-rolearn): {{String}}
  [Tags](#cfn-cleanroomsml-trainingdataset-tags): {{
    - Tag}}
  [TrainingData](#cfn-cleanroomsml-trainingdataset-trainingdata): {{
    - Dataset}}
```

## Properties
<a name="aws-resource-cleanroomsml-trainingdataset-properties"></a>

`Description`  <a name="cfn-cleanroomsml-trainingdataset-description"></a>
The description of the training dataset.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*$`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cleanroomsml-trainingdataset-name"></a>
The name of the training dataset.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-cleanroomsml-trainingdataset-rolearn"></a>
The ARN of the IAM role that Clean Rooms ML can assume to read the data referred to in the `dataSource` field of each dataset.
Passing a role across accounts is not allowed. If you pass a role that isn't in your account, you get an `AccessDeniedException` error.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z]*:iam::[0-9]{12}:role/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cleanroomsml-trainingdataset-tags"></a>
The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50.
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8.
+ Maximum value length - 256 Unicode characters in UTF-8.
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for keys as it is reserved. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has `aws` as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of `aws` do not count against your tags per resource limit.
*Required*: No
*Type*: Array of [Tag](aws-properties-cleanroomsml-trainingdataset-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrainingData`  <a name="cfn-cleanroomsml-trainingdataset-trainingdata"></a>
An array of information that lists the Dataset objects, which specifies the dataset type and details on its location and schema. You must provide a role that has read access to these tables.
*Required*: Yes
*Type*: Array of [Dataset](aws-properties-cleanroomsml-trainingdataset-dataset.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cleanroomsml-trainingdataset-return-values"></a>

### Ref
<a name="aws-resource-cleanroomsml-trainingdataset-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource ARN. For example:

 `{ "Ref": "myTrainingDataset" }`

For the Clean Rooms ML training dataset, `Ref` returns the ARN of the training dataset.

Example: `arn:aws:cleanrooms-ml:ap-northeast-1:891377082322:training-dataset/fR8doOMxlv5q5HD5qB0f68`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cleanroomsml-trainingdataset-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cleanroomsml-trainingdataset-return-values-fn--getatt-fn--getatt"></a>

`Status`  <a name="Status-fn::getatt"></a>
The status of the training dataset.

`TrainingDatasetArn`  <a name="TrainingDatasetArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the training dataset.
