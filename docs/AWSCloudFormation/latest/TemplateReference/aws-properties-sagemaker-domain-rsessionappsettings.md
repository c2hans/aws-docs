---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-rsessionappsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain RSessionAppSettings
<a name="aws-properties-sagemaker-domain-rsessionappsettings"></a>

A collection of settings that apply to an `RSessionGateway` app.

## Syntax
<a name="aws-properties-sagemaker-domain-rsessionappsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-rsessionappsettings-syntax.json"></a>

```
{
  "[CustomImages](#cfn-sagemaker-domain-rsessionappsettings-customimages)" : {{[ CustomImage, ... ]}},
  "[DefaultResourceSpec](#cfn-sagemaker-domain-rsessionappsettings-defaultresourcespec)" : {{ResourceSpec}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-rsessionappsettings-syntax.yaml"></a>

```
  [CustomImages](#cfn-sagemaker-domain-rsessionappsettings-customimages): {{
    - CustomImage}}
  [DefaultResourceSpec](#cfn-sagemaker-domain-rsessionappsettings-defaultresourcespec): {{
    ResourceSpec}}
```

## Properties
<a name="aws-properties-sagemaker-domain-rsessionappsettings-properties"></a>

`CustomImages`  <a name="cfn-sagemaker-domain-rsessionappsettings-customimages"></a>
A list of custom SageMaker AI images that are configured to run as a RSession app.
*Required*: No
*Type*: Array of [CustomImage](aws-properties-sagemaker-domain-customimage.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultResourceSpec`  <a name="cfn-sagemaker-domain-rsessionappsettings-defaultresourcespec"></a>
Specifies the ARNs of a SageMaker image and SageMaker image version, and the instance type that the version runs on.
*Required*: No
*Type*: [ResourceSpec](aws-properties-sagemaker-domain-resourcespec.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
