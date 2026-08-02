---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-usercontext.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard UserContext
<a name="aws-properties-sagemaker-modelcard-usercontext"></a>

Information about the user who created or modified a SageMaker resource.

## Syntax
<a name="aws-properties-sagemaker-modelcard-usercontext-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-usercontext-syntax.json"></a>

```
{
  "[DomainId](#cfn-sagemaker-modelcard-usercontext-domainid)" : {{String}},
  "[UserProfileArn](#cfn-sagemaker-modelcard-usercontext-userprofilearn)" : {{String}},
  "[UserProfileName](#cfn-sagemaker-modelcard-usercontext-userprofilename)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-usercontext-syntax.yaml"></a>

```
  [DomainId](#cfn-sagemaker-modelcard-usercontext-domainid): {{String}}
  [UserProfileArn](#cfn-sagemaker-modelcard-usercontext-userprofilearn): {{String}}
  [UserProfileName](#cfn-sagemaker-modelcard-usercontext-userprofilename): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-usercontext-properties"></a>

`DomainId`  <a name="cfn-sagemaker-modelcard-usercontext-domainid"></a>
The domain associated with the user.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserProfileArn`  <a name="cfn-sagemaker-modelcard-usercontext-userprofilearn"></a>
The Amazon Resource Name (ARN) of the user's profile.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserProfileName`  <a name="cfn-sagemaker-modelcard-usercontext-userprofilename"></a>
The name of the user's profile.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
