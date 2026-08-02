---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-backup-legalhold.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::LegalHold
<a name="aws-resource-backup-legalhold"></a>

Creates a legal hold on a recovery point (backup). A legal hold is a restraint on altering or deleting a backup until an authorized user cancels the legal hold. Any actions to delete or disassociate a recovery point will fail with an error if one or more active legal holds are on the recovery point.

## Syntax
<a name="aws-resource-backup-legalhold-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-backup-legalhold-syntax.json"></a>

```
{
  "Type" : "AWS::Backup::LegalHold",
  "Properties" : {
      "[Description](#cfn-backup-legalhold-description)" : {{String}},
      "[RecoveryPointSelection](#cfn-backup-legalhold-recoverypointselection)" : {{RecoveryPointSelection}},
      "[Tags](#cfn-backup-legalhold-tags)" : {{[ TagsItems, ... ]}},
      "[Title](#cfn-backup-legalhold-title)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-backup-legalhold-syntax.yaml"></a>

```
Type: AWS::Backup::LegalHold
Properties:
  [Description](#cfn-backup-legalhold-description): {{String}}
  [RecoveryPointSelection](#cfn-backup-legalhold-recoverypointselection): {{
    RecoveryPointSelection}}
  [Tags](#cfn-backup-legalhold-tags): {{
    - TagsItems}}
  [Title](#cfn-backup-legalhold-title): {{String}}
```

## Properties
<a name="aws-resource-backup-legalhold-properties"></a>

`Description`  <a name="cfn-backup-legalhold-description"></a>
The description of a legal hold.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecoveryPointSelection`  <a name="cfn-backup-legalhold-recoverypointselection"></a>
This specifies criteria to assign a set of resources, such as resource types or backup vaults.
*Required*: Yes
*Type*: [RecoveryPointSelection](aws-properties-backup-legalhold-recoverypointselection.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-backup-legalhold-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-backup-legalhold-tagsitems.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-backup-legalhold-title"></a>
The title of a legal hold.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-backup-legalhold-return-values"></a>

### Ref
<a name="aws-resource-backup-legalhold-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-backup-legalhold-return-values-fn--getatt"></a>

####
<a name="aws-resource-backup-legalhold-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreationDate`  <a name="CreationDate-fn::getatt"></a>
The time when the legal hold was created.

`LegalHoldId`  <a name="LegalHoldId-fn::getatt"></a>
The ID of the legal hold.

`Status`  <a name="Status-fn::getatt"></a>
The status of the legal hold.
