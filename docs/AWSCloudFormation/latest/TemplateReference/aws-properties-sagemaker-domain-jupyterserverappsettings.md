---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-jupyterserverappsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain JupyterServerAppSettings
<a name="aws-properties-sagemaker-domain-jupyterserverappsettings"></a>

The JupyterServer app settings.

## Syntax
<a name="aws-properties-sagemaker-domain-jupyterserverappsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-jupyterserverappsettings-syntax.json"></a>

```
{
  "[DefaultResourceSpec](#cfn-sagemaker-domain-jupyterserverappsettings-defaultresourcespec)" : {{ResourceSpec}},
  "[LifecycleConfigArns](#cfn-sagemaker-domain-jupyterserverappsettings-lifecycleconfigarns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-jupyterserverappsettings-syntax.yaml"></a>

```
  [DefaultResourceSpec](#cfn-sagemaker-domain-jupyterserverappsettings-defaultresourcespec): {{
    ResourceSpec}}
  [LifecycleConfigArns](#cfn-sagemaker-domain-jupyterserverappsettings-lifecycleconfigarns): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-domain-jupyterserverappsettings-properties"></a>

`DefaultResourceSpec`  <a name="cfn-sagemaker-domain-jupyterserverappsettings-defaultresourcespec"></a>
The default instance type and the Amazon Resource Name (ARN) of the default SageMaker image used by the JupyterServer app.
*Required*: No
*Type*: [ResourceSpec](aws-properties-sagemaker-domain-resourcespec.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleConfigArns`  <a name="cfn-sagemaker-domain-jupyterserverappsettings-lifecycleconfigarns"></a>
 The Amazon Resource Name (ARN) of the Lifecycle Configurations attached to the JupyterServerApp. If you use this parameter, the `DefaultResourceSpec` parameter is also required.
To remove a Lifecycle Config, you must set `LifecycleConfigArns` to an empty list.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
