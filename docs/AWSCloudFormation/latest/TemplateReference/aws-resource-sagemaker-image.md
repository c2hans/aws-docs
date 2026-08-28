---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-image.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Image
<a name="aws-resource-sagemaker-image"></a>

Creates a custom SageMaker AI image. A SageMaker AI image is a set of image versions. Each image version represents a container image stored in Amazon ECR. For more information, see [Bring your own SageMaker AI image](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-byoi.html).

## Syntax
<a name="aws-resource-sagemaker-image-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-image-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::Image",
  "Properties" : {
      "[ImageDescription](#cfn-sagemaker-image-imagedescription)" : {{String}},
      "[ImageDisplayName](#cfn-sagemaker-image-imagedisplayname)" : {{String}},
      "[ImageName](#cfn-sagemaker-image-imagename)" : {{String}},
      "[ImageRoleArn](#cfn-sagemaker-image-imagerolearn)" : {{String}},
      "[Tags](#cfn-sagemaker-image-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-image-syntax.yaml"></a>

```
Type: AWS::SageMaker::Image
Properties:
  [ImageDescription](#cfn-sagemaker-image-imagedescription): {{String}}
  [ImageDisplayName](#cfn-sagemaker-image-imagedisplayname): {{String}}
  [ImageName](#cfn-sagemaker-image-imagename): {{String}}
  [ImageRoleArn](#cfn-sagemaker-image-imagerolearn): {{String}}
  [Tags](#cfn-sagemaker-image-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-image-properties"></a>

`ImageDescription`  <a name="cfn-sagemaker-image-imagedescription"></a>
The description of the image.
*Required*: No
*Type*: String
*Pattern*: `.+`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageDisplayName`  <a name="cfn-sagemaker-image-imagedisplayname"></a>
The display name of the image.
*Length Constraints*: Minimum length of 1. Maximum length of 128.
*Pattern*: `^\S(.*\S)?$`
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9 -_]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageName`  <a name="cfn-sagemaker-image-imagename"></a>
The name of the Image. Must be unique by region in your account.
*Length Constraints*: Minimum length of 1. Maximum length of 63.
*Pattern*: `^[a-zA-Z0-9]([-.]?[a-zA-Z0-9]){0,62}$`
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([-.]?[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImageRoleArn`  <a name="cfn-sagemaker-image-imagerolearn"></a>
The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to perform tasks on your behalf.
*Length Constraints*: Minimum length of 20. Maximum length of 2048.
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[\w]+)*:iam::[0-9]{12}:role/.*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-image-tags"></a>
A list of key-value pairs to apply to this resource.
*Array Members*: Minimum number of 0 items. Maximum number of 50 items.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-image-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-image-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-image-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ImageArn.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sagemaker-image-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-image-return-values-fn--getatt-fn--getatt"></a>

`ImageArn`  <a name="ImageArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the image.
*Type*: String
*Length Constraints*: Maximum length of 256.
*Pattern*: `^arn:aws(-[\w]+)*:sagemaker:.+:[0-9]{12}:image/[a-z0-9]([-.]?[a-z0-9])*$`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
