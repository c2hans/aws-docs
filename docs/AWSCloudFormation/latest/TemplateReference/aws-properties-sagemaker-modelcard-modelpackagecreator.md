---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-modelpackagecreator.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard ModelPackageCreator
<a name="aws-properties-sagemaker-modelcard-modelpackagecreator"></a>

Information about the user who created the model package.

## Syntax
<a name="aws-properties-sagemaker-modelcard-modelpackagecreator-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-modelpackagecreator-syntax.json"></a>

```
{
  "[UserProfileName](#cfn-sagemaker-modelcard-modelpackagecreator-userprofilename)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-modelpackagecreator-syntax.yaml"></a>

```
  [UserProfileName](#cfn-sagemaker-modelcard-modelpackagecreator-userprofilename): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-modelpackagecreator-properties"></a>

`UserProfileName`  <a name="cfn-sagemaker-modelcard-modelpackagecreator-userprofilename"></a>
The user profile name of the model package creator.
*Required*: No
*Type*: String
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
