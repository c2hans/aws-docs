---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-imageversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ImageVersion
<a name="aws-resource-sagemaker-imageversion"></a>

Creates a version of the SageMaker image specified by `ImageName`. The version represents the Amazon Container Registry (ECR) container image specified by `BaseImage`.

**Note**
You can use the `DependsOn` attribute to specify that the creation of a specific resource follows another. You can use it for the following use cases. For more information, see [`DependsOn` attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html).
1. `DependsOn` can be used to establish a parent/child relationship between `ImageVersion` and `Image` where the `ImageVersion``DependsOn`the `Image`.
2. `DependsOn` can be used to establish order among `ImageVersion`s within the same `Image` namespace. For example, if ImageVersionB `DependsOn` ImageVersionA and both share the same parent `Image`, then ImageVersionA is version N and ImageVersionB is N\+1.

## Syntax
<a name="aws-resource-sagemaker-imageversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-imageversion-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::ImageVersion",
  "Properties" : {
      "[Alias](#cfn-sagemaker-imageversion-alias)" : {{String}},
      "[Aliases](#cfn-sagemaker-imageversion-aliases)" : {{[ String, ... ]}},
      "[BaseImage](#cfn-sagemaker-imageversion-baseimage)" : {{String}},
      "[Horovod](#cfn-sagemaker-imageversion-horovod)" : {{Boolean}},
      "[ImageName](#cfn-sagemaker-imageversion-imagename)" : {{String}},
      "[JobType](#cfn-sagemaker-imageversion-jobtype)" : {{String}},
      "[MLFramework](#cfn-sagemaker-imageversion-mlframework)" : {{String}},
      "[Processor](#cfn-sagemaker-imageversion-processor)" : {{String}},
      "[ProgrammingLang](#cfn-sagemaker-imageversion-programminglang)" : {{String}},
      "[ReleaseNotes](#cfn-sagemaker-imageversion-releasenotes)" : {{String}},
      "[VendorGuidance](#cfn-sagemaker-imageversion-vendorguidance)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-imageversion-syntax.yaml"></a>

```
Type: AWS::SageMaker::ImageVersion
Properties:
  [Alias](#cfn-sagemaker-imageversion-alias): {{String}}
  [Aliases](#cfn-sagemaker-imageversion-aliases): {{
    - String}}
  [BaseImage](#cfn-sagemaker-imageversion-baseimage): {{String}}
  [Horovod](#cfn-sagemaker-imageversion-horovod): {{Boolean}}
  [ImageName](#cfn-sagemaker-imageversion-imagename): {{String}}
  [JobType](#cfn-sagemaker-imageversion-jobtype): {{String}}
  [MLFramework](#cfn-sagemaker-imageversion-mlframework): {{String}}
  [Processor](#cfn-sagemaker-imageversion-processor): {{String}}
  [ProgrammingLang](#cfn-sagemaker-imageversion-programminglang): {{String}}
  [ReleaseNotes](#cfn-sagemaker-imageversion-releasenotes): {{String}}
  [VendorGuidance](#cfn-sagemaker-imageversion-vendorguidance): {{String}}
```

## Properties
<a name="aws-resource-sagemaker-imageversion-properties"></a>

`Alias`  <a name="cfn-sagemaker-imageversion-alias"></a>
The alias for the image version.
*Required*: No
*Type*: String
*Pattern*: `(?!^[.-])^([a-zA-Z0-9-_.]+)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Aliases`  <a name="cfn-sagemaker-imageversion-aliases"></a>
A list of aliases for the image version.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BaseImage`  <a name="cfn-sagemaker-imageversion-baseimage"></a>
The container image that the SageMaker image version is based on.
*Required*: Yes
*Type*: String
*Pattern*: `.+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Horovod`  <a name="cfn-sagemaker-imageversion-horovod"></a>
Indicates whether the image version supports Horovod distributed training framework.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageName`  <a name="cfn-sagemaker-imageversion-imagename"></a>
The name of the parent image.
*Length Constraints*: Minimum length of 1. Maximum length of 63.
*Pattern*: `^[a-zA-Z0-9]([-.]?[a-zA-Z0-9]){0,62}$`
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9]([-.]?[A-Za-z0-9])*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobType`  <a name="cfn-sagemaker-imageversion-jobtype"></a>
The job type that the image version supports (for example, TRAINING or INFERENCE).
*Required*: No
*Type*: String
*Allowed values*: `TRAINING | INFERENCE | NOTEBOOK_KERNEL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MLFramework`  <a name="cfn-sagemaker-imageversion-mlframework"></a>
The machine learning framework that the image version supports.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z]+ ?\d+\.\d+(\.\d+)?$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Processor`  <a name="cfn-sagemaker-imageversion-processor"></a>
The processor architecture that the image version supports (for example, CPU or GPU).
*Required*: No
*Type*: String
*Allowed values*: `CPU | GPU`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProgrammingLang`  <a name="cfn-sagemaker-imageversion-programminglang"></a>
The programming language that the image version supports.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z]+ ?\d+\.\d+(\.\d+)?$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReleaseNotes`  <a name="cfn-sagemaker-imageversion-releasenotes"></a>
Release notes for the image version.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VendorGuidance`  <a name="cfn-sagemaker-imageversion-vendorguidance"></a>
Vendor guidance for the image version, such as stability or deprecation status.
*Required*: No
*Type*: String
*Allowed values*: `NOT_PROVIDED | STABLE | TO_BE_ARCHIVED | ARCHIVED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-imageversion-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-imageversion-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ImageVersionArn.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sagemaker-imageversion-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-imageversion-return-values-fn--getatt-fn--getatt"></a>

`ContainerImage`  <a name="ContainerImage-fn::getatt"></a>
The URI of the container image version referenced by ImageVersion.

`ImageArn`  <a name="ImageArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the parent Image.

`ImageVersionArn`  <a name="ImageVersionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the image version.
*Type*: String
*Length Constraints*: Maximum length of 256.
*Pattern*: `^arn:aws(-[\w]+)*:sagemaker:.+:[0-9]{12}:image-version/[a-z0-9]([-.]?[a-z0-9])*/[0-9]+$`

`Version`  <a name="Version-fn::getatt"></a>
The version of the image.
