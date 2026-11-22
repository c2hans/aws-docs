---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-cloudconnector-gcpproject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::CloudConnector GcpProject

<a name="aws-properties-ssm-cloudconnector-gcpproject-description"></a>The `GcpProject` property type specifies Property description not available. for an [AWS::SSM::CloudConnector](aws-resource-ssm-cloudconnector.md).

## Syntax
<a name="aws-properties-ssm-cloudconnector-gcpproject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-cloudconnector-gcpproject-syntax.json"></a>

```json
{
  "[ProjectDisplayName](#cfn-ssm-cloudconnector-gcpproject-projectdisplayname)" : {{String}},
  "[ProjectId](#cfn-ssm-cloudconnector-gcpproject-projectid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssm-cloudconnector-gcpproject-syntax.yaml"></a>

```yaml
  [ProjectDisplayName](#cfn-ssm-cloudconnector-gcpproject-projectdisplayname): {{String}}
  [ProjectId](#cfn-ssm-cloudconnector-gcpproject-projectid): {{String}}
```

## Properties
<a name="aws-properties-ssm-cloudconnector-gcpproject-properties"></a>

`ProjectDisplayName`  <a name="cfn-ssm-cloudconnector-gcpproject-projectdisplayname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}\p{P}\p{M}]*)$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProjectId`  <a name="cfn-ssm-cloudconnector-gcpproject-projectid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9-]{4,28}[a-z0-9]$`
*Minimum*: `6`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
