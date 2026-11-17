---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-cloudconnector-gcpconfigurationtargets.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::CloudConnector GcpConfigurationTargets
<a name="aws-properties-ssm-cloudconnector-gcpconfigurationtargets"></a>

<a name="aws-properties-ssm-cloudconnector-gcpconfigurationtargets-description"></a>The `GcpConfigurationTargets` property type specifies Property description not available. for an [AWS::SSM::CloudConnector](aws-resource-ssm-cloudconnector.md).

## Syntax
<a name="aws-properties-ssm-cloudconnector-gcpconfigurationtargets-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-cloudconnector-gcpconfigurationtargets-syntax.json"></a>

```
{
  "[Projects](#cfn-ssm-cloudconnector-gcpconfigurationtargets-projects)" : {{[ GcpProject, ... ]}}
}
```

### YAML
<a name="aws-properties-ssm-cloudconnector-gcpconfigurationtargets-syntax.yaml"></a>

```
  [Projects](#cfn-ssm-cloudconnector-gcpconfigurationtargets-projects): {{
    - GcpProject}}
```

## Properties
<a name="aws-properties-ssm-cloudconnector-gcpconfigurationtargets-properties"></a>

`Projects`  <a name="cfn-ssm-cloudconnector-gcpconfigurationtargets-projects"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [GcpProject](aws-properties-ssm-cloudconnector-gcpproject.md)
*Minimum*: `1`
*Maximum*: `75`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
