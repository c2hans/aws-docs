---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-kernelgatewayappsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain KernelGatewayAppSettings
<a name="aws-properties-sagemaker-domain-kernelgatewayappsettings"></a>

The KernelGateway app settings.

## Syntax
<a name="aws-properties-sagemaker-domain-kernelgatewayappsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-kernelgatewayappsettings-syntax.json"></a>

```
{
  "[CustomImages](#cfn-sagemaker-domain-kernelgatewayappsettings-customimages)" : {{[ CustomImage, ... ]}},
  "[DefaultResourceSpec](#cfn-sagemaker-domain-kernelgatewayappsettings-defaultresourcespec)" : {{ResourceSpec}},
  "[LifecycleConfigArns](#cfn-sagemaker-domain-kernelgatewayappsettings-lifecycleconfigarns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-kernelgatewayappsettings-syntax.yaml"></a>

```
  [CustomImages](#cfn-sagemaker-domain-kernelgatewayappsettings-customimages): {{
    - CustomImage}}
  [DefaultResourceSpec](#cfn-sagemaker-domain-kernelgatewayappsettings-defaultresourcespec): {{
    ResourceSpec}}
  [LifecycleConfigArns](#cfn-sagemaker-domain-kernelgatewayappsettings-lifecycleconfigarns): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-domain-kernelgatewayappsettings-properties"></a>

`CustomImages`  <a name="cfn-sagemaker-domain-kernelgatewayappsettings-customimages"></a>
A list of custom SageMaker AI images that are configured to run as a KernelGateway app.
The maximum number of custom images are as follows.
+ On a domain level: 200
+ On a space level: 5
+ On a user profile level: 5
*Required*: No
*Type*: Array of [CustomImage](aws-properties-sagemaker-domain-customimage.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultResourceSpec`  <a name="cfn-sagemaker-domain-kernelgatewayappsettings-defaultresourcespec"></a>
The default instance type and the Amazon Resource Name (ARN) of the default SageMaker AI image used by the KernelGateway app.
The Amazon SageMaker AI Studio UI does not use the default instance type value set here. The default instance type set here is used when Apps are created using the AWS CLI or CloudFormation and the instance type parameter value is not passed.
*Required*: No
*Type*: [ResourceSpec](aws-properties-sagemaker-domain-resourcespec.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleConfigArns`  <a name="cfn-sagemaker-domain-kernelgatewayappsettings-lifecycleconfigarns"></a>
 The Amazon Resource Name (ARN) of the Lifecycle Configurations attached to the the user profile or domain.
To remove a Lifecycle Config, you must set `LifecycleConfigArns` to an empty list.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
