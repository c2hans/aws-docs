---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelpackage-validationspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelPackage ValidationSpecification
<a name="aws-properties-sagemaker-modelpackage-validationspecification"></a>

Specifies batch transform jobs that SageMaker runs to validate your model package.

## Syntax
<a name="aws-properties-sagemaker-modelpackage-validationspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelpackage-validationspecification-syntax.json"></a>

```
{
  "[ValidationProfiles](#cfn-sagemaker-modelpackage-validationspecification-validationprofiles)" : {{[ ValidationProfile, ... ]}},
  "[ValidationRole](#cfn-sagemaker-modelpackage-validationspecification-validationrole)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelpackage-validationspecification-syntax.yaml"></a>

```
  [ValidationProfiles](#cfn-sagemaker-modelpackage-validationspecification-validationprofiles): {{
    - ValidationProfile}}
  [ValidationRole](#cfn-sagemaker-modelpackage-validationspecification-validationrole): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelpackage-validationspecification-properties"></a>

`ValidationProfiles`  <a name="cfn-sagemaker-modelpackage-validationspecification-validationprofiles"></a>
An array of `ModelPackageValidationProfile` objects, each of which specifies a batch transform job that SageMaker runs to validate your model package.
*Required*: Yes
*Type*: Array of [ValidationProfile](aws-properties-sagemaker-modelpackage-validationprofile.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ValidationRole`  <a name="cfn-sagemaker-modelpackage-validationspecification-validationrole"></a>
The IAM roles to be used for the validation of the model package.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
