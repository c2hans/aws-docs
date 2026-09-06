---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-datasource-athenaparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSource AthenaParameters
<a name="aws-properties-quicksight-datasource-athenaparameters"></a>

Parameters for Amazon Athena.

## Syntax
<a name="aws-properties-quicksight-datasource-athenaparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-datasource-athenaparameters-syntax.json"></a>

```
{
  "[IdentityCenterConfiguration](#cfn-quicksight-datasource-athenaparameters-identitycenterconfiguration)" : {{IdentityCenterConfiguration}},
  "[RoleArn](#cfn-quicksight-datasource-athenaparameters-rolearn)" : {{String}},
  "[WorkGroup](#cfn-quicksight-datasource-athenaparameters-workgroup)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-datasource-athenaparameters-syntax.yaml"></a>

```
  [IdentityCenterConfiguration](#cfn-quicksight-datasource-athenaparameters-identitycenterconfiguration): {{
    IdentityCenterConfiguration}}
  [RoleArn](#cfn-quicksight-datasource-athenaparameters-rolearn): {{String}}
  [WorkGroup](#cfn-quicksight-datasource-athenaparameters-workgroup): {{String}}
```

## Properties
<a name="aws-properties-quicksight-datasource-athenaparameters-properties"></a>

`IdentityCenterConfiguration`  <a name="cfn-quicksight-datasource-athenaparameters-identitycenterconfiguration"></a>
An optional parameter that configures IAM Identity Center authentication to grant Quick Sight access to your workgroup.
This parameter can only be specified if your Quick Sight account is configured with IAM Identity Center.
*Required*: No
*Type*: [IdentityCenterConfiguration](aws-properties-quicksight-datasource-identitycenterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-quicksight-datasource-athenaparameters-rolearn"></a>
Use the `RoleArn` structure to override an account-wide role for a specific Athena data source. For example, say an account administrator has turned off all Athena access with an account-wide role. The administrator can then use `RoleArn` to bypass the account-wide role and allow Athena access for the single Athena data source that is specified in the structure, even if the account-wide role forbidding Athena access is still active.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkGroup`  <a name="cfn-quicksight-datasource-athenaparameters-workgroup"></a>
The workgroup that Amazon Athena uses.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
