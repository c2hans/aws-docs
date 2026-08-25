---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-backup-restoretestingplan-restoretestingrecoverypointselection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::RestoreTestingPlan RestoreTestingRecoveryPointSelection
<a name="aws-properties-backup-restoretestingplan-restoretestingrecoverypointselection"></a>

`RecoveryPointSelection` has five parameters (three required and two optional). The values you specify determine which recovery point is included in the restore test. You must indicate with `Algorithm` if you want the latest recovery point within your `SelectionWindowDays` or if you want a random recovery point, and you must indicate through `IncludeVaults` from which vaults the recovery points can be chosen.

`Algorithm` (*required*) Valid values: "`LATEST_WITHIN_WINDOW`" or "`RANDOM_WITHIN_WINDOW`".

`Recovery point types` (*required*) Valid values: "`SNAPSHOT`" and/or "`CONTINUOUS`". Include `SNAPSHOT` to restore only snapshot recovery points; include `CONTINUOUS` to restore continuous recovery points (point in time restore / PITR); use both to restore either a snapshot or a continuous recovery point. The recovery point will be determined by the value for `Algorithm`.

`IncludeVaults` (*required*). You must include one or more backup vaults. Use the wildcard ["\*"] or specific ARNs.

`SelectionWindowDays` (*optional*) Value must be an integer (in days) from 1 to 365. If not included, the value defaults to `30`.

`ExcludeVaults` (*optional*). You can choose to input one or more specific backup vault ARNs to exclude those vaults' contents from restore eligibility. Or, you can include a list of selectors. If this parameter and its value are not included, it defaults to empty list.

## Syntax
<a name="aws-properties-backup-restoretestingplan-restoretestingrecoverypointselection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-backup-restoretestingplan-restoretestingrecoverypointselection-syntax.json"></a>

```
{
  "[Algorithm](#cfn-backup-restoretestingplan-restoretestingrecoverypointselection-algorithm)" : {{String}},
  "[ExcludeVaults](#cfn-backup-restoretestingplan-restoretestingrecoverypointselection-excludevaults)" : {{[ String, ... ]}},
  "[IncludeVaults](#cfn-backup-restoretestingplan-restoretestingrecoverypointselection-includevaults)" : {{[ String, ... ]}},
  "[RecoveryPointTypes](#cfn-backup-restoretestingplan-restoretestingrecoverypointselection-recoverypointtypes)" : {{[ String, ... ]}},
  "[SelectionWindowDays](#cfn-backup-restoretestingplan-restoretestingrecoverypointselection-selectionwindowdays)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-backup-restoretestingplan-restoretestingrecoverypointselection-syntax.yaml"></a>

```
  [Algorithm](#cfn-backup-restoretestingplan-restoretestingrecoverypointselection-algorithm): {{String}}
  [ExcludeVaults](#cfn-backup-restoretestingplan-restoretestingrecoverypointselection-excludevaults): {{
    - String}}
  [IncludeVaults](#cfn-backup-restoretestingplan-restoretestingrecoverypointselection-includevaults): {{
    - String}}
  [RecoveryPointTypes](#cfn-backup-restoretestingplan-restoretestingrecoverypointselection-recoverypointtypes): {{
    - String}}
  [SelectionWindowDays](#cfn-backup-restoretestingplan-restoretestingrecoverypointselection-selectionwindowdays): {{Integer}}
```

## Properties
<a name="aws-properties-backup-restoretestingplan-restoretestingrecoverypointselection-properties"></a>

`Algorithm`  <a name="cfn-backup-restoretestingplan-restoretestingrecoverypointselection-algorithm"></a>
Acceptable values include "LATEST\_WITHIN\_WINDOW" or "RANDOM\_WITHIN\_WINDOW"
*Required*: Yes
*Type*: String
*Allowed values*: `LATEST_WITHIN_WINDOW | RANDOM_WITHIN_WINDOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludeVaults`  <a name="cfn-backup-restoretestingplan-restoretestingrecoverypointselection-excludevaults"></a>
Accepted values include specific ARNs or list of selectors. Defaults to empty list if not listed.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeVaults`  <a name="cfn-backup-restoretestingplan-restoretestingrecoverypointselection-includevaults"></a>
Accepted values include wildcard ["\*"] or by specific ARNs or ARN wilcard replacement ["arn:aws:backup:us-west-2:123456789012:backup-vault:asdf", ...] ["arn:aws:backup:\*:\*:backup-vault:asdf-\*", ...]
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecoveryPointTypes`  <a name="cfn-backup-restoretestingplan-restoretestingrecoverypointselection-recoverypointtypes"></a>
These are the types of recovery points.
Include `SNAPSHOT` to restore only snapshot recovery points; include `CONTINUOUS` to restore continuous recovery points (point in time restore / PITR); use both to restore either a snapshot or a continuous recovery point. The recovery point will be determined by the value for `Algorithm`.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectionWindowDays`  <a name="cfn-backup-restoretestingplan-restoretestingrecoverypointselection-selectionwindowdays"></a>
Accepted values are integers from 1 to 365. If not included, the value defaults to 30. The selection window is calculated from the actual job execution time, not the plan's scheduled start time.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
