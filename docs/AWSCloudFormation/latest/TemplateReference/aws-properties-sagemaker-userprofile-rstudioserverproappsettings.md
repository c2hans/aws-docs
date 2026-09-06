---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-userprofile-rstudioserverproappsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::UserProfile RStudioServerProAppSettings
<a name="aws-properties-sagemaker-userprofile-rstudioserverproappsettings"></a>

A collection of settings that configure user interaction with the `RStudioServerPro` app.

## Syntax
<a name="aws-properties-sagemaker-userprofile-rstudioserverproappsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-userprofile-rstudioserverproappsettings-syntax.json"></a>

```
{
  "[AccessStatus](#cfn-sagemaker-userprofile-rstudioserverproappsettings-accessstatus)" : {{String}},
  "[UserGroup](#cfn-sagemaker-userprofile-rstudioserverproappsettings-usergroup)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-userprofile-rstudioserverproappsettings-syntax.yaml"></a>

```
  [AccessStatus](#cfn-sagemaker-userprofile-rstudioserverproappsettings-accessstatus): {{String}}
  [UserGroup](#cfn-sagemaker-userprofile-rstudioserverproappsettings-usergroup): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-userprofile-rstudioserverproappsettings-properties"></a>

`AccessStatus`  <a name="cfn-sagemaker-userprofile-rstudioserverproappsettings-accessstatus"></a>
Indicates whether the current user has access to the `RStudioServerPro` app.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserGroup`  <a name="cfn-sagemaker-userprofile-rstudioserverproappsettings-usergroup"></a>
The level of permissions that the user has within the `RStudioServerPro` app. This value defaults to `User`. The `Admin` value allows the user access to the RStudio Administrative Dashboard.
*Required*: No
*Type*: String
*Allowed values*: `R_STUDIO_ADMIN | R_STUDIO_USER`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
