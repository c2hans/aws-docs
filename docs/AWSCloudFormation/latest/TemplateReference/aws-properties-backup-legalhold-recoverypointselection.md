---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-legalhold-recoverypointselection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::LegalHold RecoveryPointSelection
<a name="aws-properties-backup-legalhold-recoverypointselection"></a>

This specifies criteria to assign a set of resources, such as resource types or backup vaults.

## Syntax
<a name="aws-properties-backup-legalhold-recoverypointselection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-legalhold-recoverypointselection-syntax.json"></a>

```
{
  "[DateRange](#cfn-backup-legalhold-recoverypointselection-daterange)" : {{DateRange}},
  "[ResourceIdentifiers](#cfn-backup-legalhold-recoverypointselection-resourceidentifiers)" : {{[ String, ... ]}},
  "[VaultNames](#cfn-backup-legalhold-recoverypointselection-vaultnames)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-backup-legalhold-recoverypointselection-syntax.yaml"></a>

```
  [DateRange](#cfn-backup-legalhold-recoverypointselection-daterange): {{
    DateRange}}
  [ResourceIdentifiers](#cfn-backup-legalhold-recoverypointselection-resourceidentifiers): {{
    - String}}
  [VaultNames](#cfn-backup-legalhold-recoverypointselection-vaultnames): {{
    - String}}
```

## Properties
<a name="aws-properties-backup-legalhold-recoverypointselection-properties"></a>

`DateRange`  <a name="cfn-backup-legalhold-recoverypointselection-daterange"></a>
Property description not available.
*Required*: No
*Type*: [DateRange](aws-properties-backup-legalhold-daterange.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceIdentifiers`  <a name="cfn-backup-legalhold-recoverypointselection-resourceidentifiers"></a>
These are the resources included in the resource selection (including type of resources and vaults).
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VaultNames`  <a name="cfn-backup-legalhold-recoverypointselection-vaultnames"></a>
These are the names of the vaults in which the selected recovery points are contained.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
