---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-backup-tieringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::TieringConfiguration
<a name="aws-resource-backup-tieringconfiguration"></a>

This contains metadata about a tiering configuration.

## Syntax
<a name="aws-resource-backup-tieringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-backup-tieringconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::Backup::TieringConfiguration",
  "Properties" : {
      "[BackupVaultName](#cfn-backup-tieringconfiguration-backupvaultname)" : {{String}},
      "[ResourceSelection](#cfn-backup-tieringconfiguration-resourceselection)" : {{[ ResourceSelection, ... ]}},
      "[TieringConfigurationName](#cfn-backup-tieringconfiguration-tieringconfigurationname)" : {{String}},
      "[TieringConfigurationTags](#cfn-backup-tieringconfiguration-tieringconfigurationtags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-backup-tieringconfiguration-syntax.yaml"></a>

```
Type: AWS::Backup::TieringConfiguration
Properties:
  [BackupVaultName](#cfn-backup-tieringconfiguration-backupvaultname): {{String}}
  [ResourceSelection](#cfn-backup-tieringconfiguration-resourceselection): {{
    - ResourceSelection}}
  [TieringConfigurationName](#cfn-backup-tieringconfiguration-tieringconfigurationname): {{String}}
  [TieringConfigurationTags](#cfn-backup-tieringconfiguration-tieringconfigurationtags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-backup-tieringconfiguration-properties"></a>

`BackupVaultName`  <a name="cfn-backup-tieringconfiguration-backupvaultname"></a>
The name of the backup vault where the tiering configuration applies. Use `*` to apply to all backup vaults.
*Required*: Yes
*Type*: String
*Pattern*: `^(\*|[a-zA-Z0-9\-\_]{2,50})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceSelection`  <a name="cfn-backup-tieringconfiguration-resourceselection"></a>
An array of resource selection objects that specify which resources are included in the tiering configuration and their tiering settings.
*Required*: Yes
*Type*: [Array](aws-properties-backup-tieringconfiguration-resourceselection.md) of [ResourceSelection](aws-properties-backup-tieringconfiguration-resourceselection.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TieringConfigurationName`  <a name="cfn-backup-tieringconfiguration-tieringconfigurationname"></a>
The unique name of the tiering configuration. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_]{1,200}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TieringConfigurationTags`  <a name="cfn-backup-tieringconfiguration-tieringconfigurationtags"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^.{1,128}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-backup-tieringconfiguration-return-values"></a>

### Ref
<a name="aws-resource-backup-tieringconfiguration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-backup-tieringconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-backup-tieringconfiguration-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The date and time a tiering configuration was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The date and time a tiering configuration was updated, in Unix format and Coordinated Universal Time (UTC). The value of `LastUpdatedTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.

`TieringConfigurationArn`  <a name="TieringConfigurationArn-fn::getatt"></a>
An Amazon Resource Name (ARN) that uniquely identifies the tiering configuration.
