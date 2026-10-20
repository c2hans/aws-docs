---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-computequota-resourcesharingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ComputeQuota ResourceSharingConfig
<a name="aws-properties-sagemaker-computequota-resourcesharingconfig"></a>

Resource sharing configuration.

## Syntax
<a name="aws-properties-sagemaker-computequota-resourcesharingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-computequota-resourcesharingconfig-syntax.json"></a>

```
{
  "[AbsoluteBorrowLimits](#cfn-sagemaker-computequota-resourcesharingconfig-absoluteborrowlimits)" : {{[ ComputeQuotaResourceConfig, ... ]}},
  "[BorrowLimit](#cfn-sagemaker-computequota-resourcesharingconfig-borrowlimit)" : {{Integer}},
  "[Strategy](#cfn-sagemaker-computequota-resourcesharingconfig-strategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-computequota-resourcesharingconfig-syntax.yaml"></a>

```
  [AbsoluteBorrowLimits](#cfn-sagemaker-computequota-resourcesharingconfig-absoluteborrowlimits): {{
    - ComputeQuotaResourceConfig}}
  [BorrowLimit](#cfn-sagemaker-computequota-resourcesharingconfig-borrowlimit): {{Integer}}
  [Strategy](#cfn-sagemaker-computequota-resourcesharingconfig-strategy): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-computequota-resourcesharingconfig-properties"></a>

`AbsoluteBorrowLimits`  <a name="cfn-sagemaker-computequota-resourcesharingconfig-absoluteborrowlimits"></a>
The absolute limits on compute resources that can be borrowed from idle compute. When specified, these limits define the maximum amount of specific resource types (such as accelerators, vCPU, or memory) that an entity can borrow, regardless of the percentage-based `BorrowLimit`.
*Required*: No
*Type*: Array of [ComputeQuotaResourceConfig](aws-properties-sagemaker-computequota-computequotaresourceconfig.md)
*Minimum*: `0`
*Maximum*: `15`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BorrowLimit`  <a name="cfn-sagemaker-computequota-resourcesharingconfig-borrowlimit"></a>
The limit on how much idle compute can be borrowed.The values can be 1 - 500 percent of idle compute that the team is allowed to borrow.
Default is `50`.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Strategy`  <a name="cfn-sagemaker-computequota-resourcesharingconfig-strategy"></a>
The strategy of how idle compute is shared within the cluster. The following are the options of strategies.
+ `DontLend`: entities do not lend idle compute.
+ `Lend`: entities can lend idle compute to entities that can borrow.
+ `LendandBorrow`: entities can lend idle compute and borrow idle compute from other entities.
Default is `LendandBorrow`.
*Required*: Yes
*Type*: String
*Allowed values*: `Lend | DontLend | LendAndBorrow`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
