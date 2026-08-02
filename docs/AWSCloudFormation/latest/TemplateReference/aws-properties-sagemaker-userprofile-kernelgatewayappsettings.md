---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-userprofile-kernelgatewayappsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::UserProfile KernelGatewayAppSettings
<a name="aws-properties-sagemaker-userprofile-kernelgatewayappsettings"></a>

The KernelGateway app settings.

## Syntax
<a name="aws-properties-sagemaker-userprofile-kernelgatewayappsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-userprofile-kernelgatewayappsettings-syntax.json"></a>

```
{
  "[CustomImages](#cfn-sagemaker-userprofile-kernelgatewayappsettings-customimages)" : {{[ CustomImage, ... ]}},
  "[DefaultResourceSpec](#cfn-sagemaker-userprofile-kernelgatewayappsettings-defaultresourcespec)" : {{ResourceSpec}},
  "[LifecycleConfigArns](#cfn-sagemaker-userprofile-kernelgatewayappsettings-lifecycleconfigarns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-userprofile-kernelgatewayappsettings-syntax.yaml"></a>

```
  [CustomImages](#cfn-sagemaker-userprofile-kernelgatewayappsettings-customimages): {{
    - CustomImage}}
  [DefaultResourceSpec](#cfn-sagemaker-userprofile-kernelgatewayappsettings-defaultresourcespec): {{
    ResourceSpec}}
  [LifecycleConfigArns](#cfn-sagemaker-userprofile-kernelgatewayappsettings-lifecycleconfigarns): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-userprofile-kernelgatewayappsettings-properties"></a>

`CustomImages`  <a name="cfn-sagemaker-userprofile-kernelgatewayappsettings-customimages"></a>
A list of custom SageMaker AI images that are configured to run as a KernelGateway app.
The maximum number of custom images are as follows.
+ On a domain level: 200
+ On a space level: 5
+ On a user profile level: 5
*Required*: No
*Type*: Array of [CustomImage](aws-properties-sagemaker-userprofile-customimage.md)
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultResourceSpec`  <a name="cfn-sagemaker-userprofile-kernelgatewayappsettings-defaultresourcespec"></a>
The default instance type and the Amazon Resource Name (ARN) of the default SageMaker AI image used by the KernelGateway app.
The Amazon SageMaker AI Studio UI does not use the default instance type value set here. The default instance type set here is used when Apps are created using the AWS CLI or CloudFormation and the instance type parameter value is not passed.
*Required*: No
*Type*: [ResourceSpec](aws-properties-sagemaker-userprofile-resourcespec.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleConfigArns`  <a name="cfn-sagemaker-userprofile-kernelgatewayappsettings-lifecycleconfigarns"></a>
 The Amazon Resource Name (ARN) of the Lifecycle Configurations attached to the the user profile or domain.
To remove a Lifecycle Config, you must set `LifecycleConfigArns` to an empty list.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
