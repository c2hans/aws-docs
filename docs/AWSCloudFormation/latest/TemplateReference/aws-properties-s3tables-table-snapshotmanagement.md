---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-table-snapshotmanagement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::Table SnapshotManagement
<a name="aws-properties-s3tables-table-snapshotmanagement"></a>

Contains details about the snapshot management settings for an Iceberg table. The oldest snapshot expires when its age exceeds the `maxSnapshotAgeHours` and the total number of snapshots exceeds the value for the minimum number of snapshots to keep `minSnapshotsToKeep`.

## Syntax
<a name="aws-properties-s3tables-table-snapshotmanagement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-table-snapshotmanagement-syntax.json"></a>

```
{
  "[MaxSnapshotAgeHours](#cfn-s3tables-table-snapshotmanagement-maxsnapshotagehours)" : {{Integer}},
  "[MinSnapshotsToKeep](#cfn-s3tables-table-snapshotmanagement-minsnapshotstokeep)" : {{Integer}},
  "[Status](#cfn-s3tables-table-snapshotmanagement-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3tables-table-snapshotmanagement-syntax.yaml"></a>

```
  [MaxSnapshotAgeHours](#cfn-s3tables-table-snapshotmanagement-maxsnapshotagehours): {{Integer}}
  [MinSnapshotsToKeep](#cfn-s3tables-table-snapshotmanagement-minsnapshotstokeep): {{Integer}}
  [Status](#cfn-s3tables-table-snapshotmanagement-status): {{String}}
```

## Properties
<a name="aws-properties-s3tables-table-snapshotmanagement-properties"></a>

`MaxSnapshotAgeHours`  <a name="cfn-s3tables-table-snapshotmanagement-maxsnapshotagehours"></a>
The maximum age of a snapshot before it can be expired.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinSnapshotsToKeep`  <a name="cfn-s3tables-table-snapshotmanagement-minsnapshotstokeep"></a>
The minimum number of snapshots to keep.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-s3tables-table-snapshotmanagement-status"></a>
The status of the maintenance configuration.
*Required*: No
*Type*: String
*Allowed values*: `enabled | disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
