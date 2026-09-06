---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-quotashare-quotashareresourcesharingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::QuotaShare QuotaShareResourceSharingConfiguration
<a name="aws-properties-batch-quotashare-quotashareresourcesharingconfiguration"></a>

Specifies whether a quota share reserves, lends, or both lends and borrows idle compute capacity.

## Syntax
<a name="aws-properties-batch-quotashare-quotashareresourcesharingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-quotashare-quotashareresourcesharingconfiguration-syntax.json"></a>

```
{
  "[BorrowLimit](#cfn-batch-quotashare-quotashareresourcesharingconfiguration-borrowlimit)" : {{Integer}},
  "[Strategy](#cfn-batch-quotashare-quotashareresourcesharingconfiguration-strategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-quotashare-quotashareresourcesharingconfiguration-syntax.yaml"></a>

```
  [BorrowLimit](#cfn-batch-quotashare-quotashareresourcesharingconfiguration-borrowlimit): {{Integer}}
  [Strategy](#cfn-batch-quotashare-quotashareresourcesharingconfiguration-strategy): {{String}}
```

## Properties
<a name="aws-properties-batch-quotashare-quotashareresourcesharingconfiguration-properties"></a>

`BorrowLimit`  <a name="cfn-batch-quotashare-quotashareresourcesharingconfiguration-borrowlimit"></a>
The maximum percentage of additional capacity that the quota share can borrow from other shares. `borrowLimit` can only be applied to quota shares with a strategy of `LEND_AND_BORROW`. This value is expressed as a percentage of the quota share's configured [CapacityLimits](https://docs.aws.amazon.com/batch/latest/APIReference/API_QuotaShareCapacityLimit.html).
The `borrowLimit` is applied uniformly across all capacity units. For example, if the `borrowLimit` is 200, the quota share can borrow up to 200% of its configured `maxCapacity` for each capacity unit. The default `borrowLimit` is -1, which indicates unlimited borrowing.
*Required*: No
*Type*: Integer
*Minimum*: `-1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Strategy`  <a name="cfn-batch-quotashare-quotashareresourcesharingconfiguration-strategy"></a>
The resource sharing strategy for the quota share. The `RESERVE` strategy allows a quota share to reserve idle capacity for itself. `LEND` configures the share to lend its idle capacity to another share in need of capacity. The `LEND_AND_BORROW` strategy configures the share to borrow idle capacity from an underutilized share, as well as lend to another share.
*Required*: Yes
*Type*: String
*Allowed values*: `RESERVE | LEND | LEND_AND_BORROW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
