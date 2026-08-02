---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-filesystem-userandgroupquotas.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::FileSystem UserAndGroupQuotas
<a name="aws-properties-fsx-filesystem-userandgroupquotas"></a>

Used to configure quotas that define how much storage a user or group can use on an FSx for OpenZFS volume. For more information, see [Volume properties](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-volumes.html#volume-properties) in the FSx for OpenZFS User Guide.

## Syntax
<a name="aws-properties-fsx-filesystem-userandgroupquotas-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-filesystem-userandgroupquotas-syntax.json"></a>

```
{
  "[Id](#cfn-fsx-filesystem-userandgroupquotas-id)" : {{Integer}},
  "[StorageCapacityQuotaGiB](#cfn-fsx-filesystem-userandgroupquotas-storagecapacityquotagib)" : {{Integer}},
  "[Type](#cfn-fsx-filesystem-userandgroupquotas-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-filesystem-userandgroupquotas-syntax.yaml"></a>

```
  [Id](#cfn-fsx-filesystem-userandgroupquotas-id): {{Integer}}
  [StorageCapacityQuotaGiB](#cfn-fsx-filesystem-userandgroupquotas-storagecapacityquotagib): {{Integer}}
  [Type](#cfn-fsx-filesystem-userandgroupquotas-type): {{String}}
```

## Properties
<a name="aws-properties-fsx-filesystem-userandgroupquotas-properties"></a>

`Id`  <a name="cfn-fsx-filesystem-userandgroupquotas-id"></a>
The ID of the user or group that the quota applies to.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageCapacityQuotaGiB`  <a name="cfn-fsx-filesystem-userandgroupquotas-storagecapacityquotagib"></a>
The user or group's storage quota, in gibibytes (GiB).
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-fsx-filesystem-userandgroupquotas-type"></a>
Specifies whether the quota applies to a user or group.
*Required*: No
*Type*: String
*Allowed values*: `USER | GROUP`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
