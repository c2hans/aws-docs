---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-rstudioserverproappsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain RStudioServerProAppSettings
<a name="aws-properties-sagemaker-domain-rstudioserverproappsettings"></a>

A collection of settings that configure user interaction with the `RStudioServerPro` app.

## Syntax
<a name="aws-properties-sagemaker-domain-rstudioserverproappsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-rstudioserverproappsettings-syntax.json"></a>

```
{
  "[AccessStatus](#cfn-sagemaker-domain-rstudioserverproappsettings-accessstatus)" : {{String}},
  "[UserGroup](#cfn-sagemaker-domain-rstudioserverproappsettings-usergroup)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-rstudioserverproappsettings-syntax.yaml"></a>

```
  [AccessStatus](#cfn-sagemaker-domain-rstudioserverproappsettings-accessstatus): {{String}}
  [UserGroup](#cfn-sagemaker-domain-rstudioserverproappsettings-usergroup): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-domain-rstudioserverproappsettings-properties"></a>

`AccessStatus`  <a name="cfn-sagemaker-domain-rstudioserverproappsettings-accessstatus"></a>
Indicates whether the current user has access to the `RStudioServerPro` app.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserGroup`  <a name="cfn-sagemaker-domain-rstudioserverproappsettings-usergroup"></a>
The level of permissions that the user has within the `RStudioServerPro` app. This value defaults to `User`. The `Admin` value allows the user access to the RStudio Administrative Dashboard.
*Required*: No
*Type*: String
*Allowed values*: `R_STUDIO_ADMIN | R_STUDIO_USER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
