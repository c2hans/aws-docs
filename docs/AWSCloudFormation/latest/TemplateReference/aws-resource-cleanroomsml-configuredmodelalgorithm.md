---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cleanroomsml-configuredmodelalgorithm.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithm
<a name="aws-resource-cleanroomsml-configuredmodelalgorithm"></a>

Creates a configured model algorithm using a container image stored in an ECR repository.

## Syntax
<a name="aws-resource-cleanroomsml-configuredmodelalgorithm-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cleanroomsml-configuredmodelalgorithm-syntax.json"></a>

```
{
  "Type" : "AWS::CleanRoomsML::ConfiguredModelAlgorithm",
  "Properties" : {
      "[Description](#cfn-cleanroomsml-configuredmodelalgorithm-description)" : {{String}},
      "[InferenceContainerConfig](#cfn-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig)" : {{InferenceContainerConfig}},
      "[KmsKeyArn](#cfn-cleanroomsml-configuredmodelalgorithm-kmskeyarn)" : {{String}},
      "[Name](#cfn-cleanroomsml-configuredmodelalgorithm-name)" : {{String}},
      "[RoleArn](#cfn-cleanroomsml-configuredmodelalgorithm-rolearn)" : {{String}},
      "[Tags](#cfn-cleanroomsml-configuredmodelalgorithm-tags)" : {{[ Tag, ... ]}},
      "[TrainingContainerConfig](#cfn-cleanroomsml-configuredmodelalgorithm-trainingcontainerconfig)" : {{ContainerConfig}}
    }
}
```

### YAML
<a name="aws-resource-cleanroomsml-configuredmodelalgorithm-syntax.yaml"></a>

```
Type: AWS::CleanRoomsML::ConfiguredModelAlgorithm
Properties:
  [Description](#cfn-cleanroomsml-configuredmodelalgorithm-description): {{String}}
  [InferenceContainerConfig](#cfn-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig): {{
    InferenceContainerConfig}}
  [KmsKeyArn](#cfn-cleanroomsml-configuredmodelalgorithm-kmskeyarn): {{String}}
  [Name](#cfn-cleanroomsml-configuredmodelalgorithm-name): {{String}}
  [RoleArn](#cfn-cleanroomsml-configuredmodelalgorithm-rolearn): {{String}}
  [Tags](#cfn-cleanroomsml-configuredmodelalgorithm-tags): {{
    - Tag}}
  [TrainingContainerConfig](#cfn-cleanroomsml-configuredmodelalgorithm-trainingcontainerconfig): {{
    ContainerConfig}}
```

## Properties
<a name="aws-resource-cleanroomsml-configuredmodelalgorithm-properties"></a>

`Description`  <a name="cfn-cleanroomsml-configuredmodelalgorithm-description"></a>
The description of the configured model algorithm.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*$`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InferenceContainerConfig`  <a name="cfn-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig"></a>
Provides configuration information for the inference container that is used when you run an inference job on a configured model algorithm.
*Required*: No
*Type*: [InferenceContainerConfig](aws-properties-cleanroomsml-configuredmodelalgorithm-inferencecontainerconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyArn`  <a name="cfn-cleanroomsml-configuredmodelalgorithm-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the configured ML model algorithm and associated data.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[-a-z]*:kms:[-a-z0-9]+:[0-9]{12}:key/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cleanroomsml-configuredmodelalgorithm-name"></a>
The name of the configured model algorithm.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-cleanroomsml-configuredmodelalgorithm-rolearn"></a>
The Amazon Resource Name (ARN) of the role that is used to access the repository.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z]*:iam::[0-9]{12}:role/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cleanroomsml-configuredmodelalgorithm-tags"></a>
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
*Type*: Array of [Tag](aws-properties-cleanroomsml-configuredmodelalgorithm-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrainingContainerConfig`  <a name="cfn-cleanroomsml-configuredmodelalgorithm-trainingcontainerconfig"></a>
Provides configuration information for the training container, including entrypoints and arguments.
*Required*: No
*Type*: [ContainerConfig](aws-properties-cleanroomsml-configuredmodelalgorithm-containerconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cleanroomsml-configuredmodelalgorithm-return-values"></a>

### Ref
<a name="aws-resource-cleanroomsml-configuredmodelalgorithm-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource ARN. For example:

 `{ "Ref": "myConfiguredModelAlgorithm" }`

For the Clean Rooms ML configured model algorithm, `Ref` returns the ARN of the configured model algorithm.

Example: `arn:aws:cleanrooms-ml:us-east-1:123456789012:configured-model-algorithm/a1b2c3d4e5f6`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cleanroomsml-configuredmodelalgorithm-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cleanroomsml-configuredmodelalgorithm-return-values-fn--getatt-fn--getatt"></a>

`ConfiguredModelAlgorithmArn`  <a name="ConfiguredModelAlgorithmArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the configured model algorithm.

## Examples
<a name="aws-resource-cleanroomsml-configuredmodelalgorithm--examples"></a>

### Create a configured model algorithm
<a name="aws-resource-cleanroomsml-configuredmodelalgorithm--examples--Create_a_configured_model_algorithm"></a>

The following example creates a configured model algorithm with training and inference container configurations.

#### JSON
<a name="aws-resource-cleanroomsml-configuredmodelalgorithm--examples--Create_a_configured_model_algorithm--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyConfiguredModelAlgorithm": {
      "Type": "AWS::CleanRoomsML::ConfiguredModelAlgorithm",
      "Properties": {
        "Name": "MyMLAlgorithm",
        "Description": "A configured model algorithm for collaborative ML",
        "RoleArn": "arn:aws:iam::123456789012:role/CleanRoomsMLServiceRole",
        "TrainingContainerConfig": {
          "ImageUri": "123456789012.dkr.ecr.us-east-1.amazonaws.com/my-training-image:latest",
          "MetricDefinitions": [
            {
              "Name": "loss",
              "Regex": "Loss: ([0-9\\\\.]+)"
            }
          ]
        },
        "InferenceContainerConfig": {
          "ImageUri": "123456789012.dkr.ecr.us-east-1.amazonaws.com/my-inference-image:latest"
        },
        "Tags": [
          {
            "Key": "Environment",
            "Value": "Production"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cleanroomsml-configuredmodelalgorithm--examples--Create_a_configured_model_algorithm--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyConfiguredModelAlgorithm:
    Type: AWS::CleanRoomsML::ConfiguredModelAlgorithm
    Properties:
      Name: MyMLAlgorithm
      Description: A configured model algorithm for collaborative ML
      RoleArn: arn:aws:iam::123456789012:role/CleanRoomsMLServiceRole
      TrainingContainerConfig:
        ImageUri: 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-training-image:latest
        MetricDefinitions:
          - Name: loss
            Regex: 'Loss: ([0-9\.]+)'
      InferenceContainerConfig:
        ImageUri: 123456789012.dkr.ecr.us-east-1.amazonaws.com/my-inference-image:latest
      Tags:
        - Key: Environment
          Value: Production
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
