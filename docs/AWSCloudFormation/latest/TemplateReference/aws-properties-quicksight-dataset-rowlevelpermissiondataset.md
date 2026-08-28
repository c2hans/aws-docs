---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-rowlevelpermissiondataset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet RowLevelPermissionDataSet
<a name="aws-properties-quicksight-dataset-rowlevelpermissiondataset"></a>

Information about a dataset that contains permissions for row-level security (RLS). The permissions dataset maps fields to users or groups. For more information, see [Using Row-Level Security (RLS) to Restrict Access to a Dataset](https://docs.aws.amazon.com/quicksight/latest/user/restrict-access-to-a-data-set-using-row-level-security.html) in the *Quick Sight User Guide*.

The option to deny permissions by setting `PermissionPolicy` to `DENY_ACCESS` is not supported for new RLS datasets.

## Syntax
<a name="aws-properties-quicksight-dataset-rowlevelpermissiondataset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-rowlevelpermissiondataset-syntax.json"></a>

```
{
  "[Arn](#cfn-quicksight-dataset-rowlevelpermissiondataset-arn)" : {{String}},
  "[FormatVersion](#cfn-quicksight-dataset-rowlevelpermissiondataset-formatversion)" : {{String}},
  "[Namespace](#cfn-quicksight-dataset-rowlevelpermissiondataset-namespace)" : {{String}},
  "[PermissionPolicy](#cfn-quicksight-dataset-rowlevelpermissiondataset-permissionpolicy)" : {{String}},
  "[Status](#cfn-quicksight-dataset-rowlevelpermissiondataset-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-rowlevelpermissiondataset-syntax.yaml"></a>

```
  [Arn](#cfn-quicksight-dataset-rowlevelpermissiondataset-arn): {{String}}
  [FormatVersion](#cfn-quicksight-dataset-rowlevelpermissiondataset-formatversion): {{String}}
  [Namespace](#cfn-quicksight-dataset-rowlevelpermissiondataset-namespace): {{String}}
  [PermissionPolicy](#cfn-quicksight-dataset-rowlevelpermissiondataset-permissionpolicy): {{String}}
  [Status](#cfn-quicksight-dataset-rowlevelpermissiondataset-status): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-rowlevelpermissiondataset-properties"></a>

`Arn`  <a name="cfn-quicksight-dataset-rowlevelpermissiondataset-arn"></a>
The Amazon Resource Name (ARN) of the dataset that contains permissions for RLS.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FormatVersion`  <a name="cfn-quicksight-dataset-rowlevelpermissiondataset-formatversion"></a>
The user or group rules associated with the dataset that contains permissions for RLS.
By default, `FormatVersion` is `VERSION_1`. When `FormatVersion` is `VERSION_1`, `UserName` and `GroupName` are required. When `FormatVersion` is `VERSION_2`, `UserARN` and `GroupARN` are required, and `Namespace` must not exist.
*Required*: No
*Type*: String
*Allowed values*: `VERSION_1 | VERSION_2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-quicksight-dataset-rowlevelpermissiondataset-namespace"></a>
The namespace associated with the dataset that contains permissions for RLS.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9._-]*$`
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PermissionPolicy`  <a name="cfn-quicksight-dataset-rowlevelpermissiondataset-permissionpolicy"></a>
The type of permissions to use when interpreting the permissions for RLS. `DENY_ACCESS` is included for backward compatibility only.
*Required*: Yes
*Type*: String
*Allowed values*: `GRANT_ACCESS | DENY_ACCESS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-quicksight-dataset-rowlevelpermissiondataset-status"></a>
The status of the row-level security permission dataset. If enabled, the status is `ENABLED`. If disabled, the status is `DISABLED`.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
