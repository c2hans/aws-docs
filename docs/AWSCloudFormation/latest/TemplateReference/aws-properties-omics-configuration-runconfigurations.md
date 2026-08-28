---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-configuration-runconfigurations.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::Configuration RunConfigurations
<a name="aws-properties-omics-configuration-runconfigurations"></a>

Run-specific configuration settings.

## Syntax
<a name="aws-properties-omics-configuration-runconfigurations-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-configuration-runconfigurations-syntax.json"></a>

```
{
  "[VpcConfig](#cfn-omics-configuration-runconfigurations-vpcconfig)" : {{VpcConfig}}
}
```

### YAML
<a name="aws-properties-omics-configuration-runconfigurations-syntax.yaml"></a>

```
  [VpcConfig](#cfn-omics-configuration-runconfigurations-vpcconfig): {{
    VpcConfig}}
```

## Properties
<a name="aws-properties-omics-configuration-runconfigurations-properties"></a>

`VpcConfig`  <a name="cfn-omics-configuration-runconfigurations-vpcconfig"></a>
VPC configuration for workflow runs.
*Required*: No
*Type*: [VpcConfig](aws-properties-omics-configuration-vpcconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
