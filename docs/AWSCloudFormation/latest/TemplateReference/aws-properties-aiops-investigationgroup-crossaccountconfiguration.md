---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-aiops-investigationgroup-crossaccountconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AIOps::InvestigationGroup CrossAccountConfiguration
<a name="aws-properties-aiops-investigationgroup-crossaccountconfiguration"></a>

This structure contains information about the cross-account configuration in the account.

## Syntax
<a name="aws-properties-aiops-investigationgroup-crossaccountconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-aiops-investigationgroup-crossaccountconfiguration-syntax.json"></a>

```
{
  "[SourceRoleArn](#cfn-aiops-investigationgroup-crossaccountconfiguration-sourcerolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-aiops-investigationgroup-crossaccountconfiguration-syntax.yaml"></a>

```
  [SourceRoleArn](#cfn-aiops-investigationgroup-crossaccountconfiguration-sourcerolearn): {{String}}
```

## Properties
<a name="aws-properties-aiops-investigationgroup-crossaccountconfiguration-properties"></a>

`SourceRoleArn`  <a name="cfn-aiops-investigationgroup-crossaccountconfiguration-sourcerolearn"></a>
The ARN of an existing role which will be used to do investigations on your behalf.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
