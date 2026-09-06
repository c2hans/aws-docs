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
