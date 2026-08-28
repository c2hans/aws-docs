---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-volume-userandgroupquotas.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::Volume UserAndGroupQuotas
<a name="aws-properties-fsx-volume-userandgroupquotas"></a>

Configures how much storage users and groups can use on the volume.

## Syntax
<a name="aws-properties-fsx-volume-userandgroupquotas-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-volume-userandgroupquotas-syntax.json"></a>

```
{
  "[Id](#cfn-fsx-volume-userandgroupquotas-id)" : {{Integer}},
  "[StorageCapacityQuotaGiB](#cfn-fsx-volume-userandgroupquotas-storagecapacityquotagib)" : {{Integer}},
  "[Type](#cfn-fsx-volume-userandgroupquotas-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-volume-userandgroupquotas-syntax.yaml"></a>

```
  [Id](#cfn-fsx-volume-userandgroupquotas-id): {{Integer}}
  [StorageCapacityQuotaGiB](#cfn-fsx-volume-userandgroupquotas-storagecapacityquotagib): {{Integer}}
  [Type](#cfn-fsx-volume-userandgroupquotas-type): {{String}}
```

## Properties
<a name="aws-properties-fsx-volume-userandgroupquotas-properties"></a>

`Id`  <a name="cfn-fsx-volume-userandgroupquotas-id"></a>
The ID of the user or group that the quota applies to.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageCapacityQuotaGiB`  <a name="cfn-fsx-volume-userandgroupquotas-storagecapacityquotagib"></a>
The user or group's storage quota, in gibibytes (GiB).
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-fsx-volume-userandgroupquotas-type"></a>
Specifies whether the quota applies to a user or group.
*Required*: Yes
*Type*: String
*Allowed values*: `USER | GROUP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
