---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-dockersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain DockerSettings
<a name="aws-properties-sagemaker-domain-dockersettings"></a>

A collection of settings that configure the domain's Docker interaction.

## Syntax
<a name="aws-properties-sagemaker-domain-dockersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-dockersettings-syntax.json"></a>

```
{
  "[EnableDockerAccess](#cfn-sagemaker-domain-dockersettings-enabledockeraccess)" : {{String}},
  "[VpcOnlyTrustedAccounts](#cfn-sagemaker-domain-dockersettings-vpconlytrustedaccounts)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-dockersettings-syntax.yaml"></a>

```
  [EnableDockerAccess](#cfn-sagemaker-domain-dockersettings-enabledockeraccess): {{String}}
  [VpcOnlyTrustedAccounts](#cfn-sagemaker-domain-dockersettings-vpconlytrustedaccounts): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-domain-dockersettings-properties"></a>

`EnableDockerAccess`  <a name="cfn-sagemaker-domain-dockersettings-enabledockeraccess"></a>
Indicates whether the domain can access Docker.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcOnlyTrustedAccounts`  <a name="cfn-sagemaker-domain-dockersettings-vpconlytrustedaccounts"></a>
The list of AWS accounts that are trusted when the domain is created in VPC-only mode.
*Required*: No
*Type*: Array of String
*Minimum*: `12 | 0`
*Maximum*: `12 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
