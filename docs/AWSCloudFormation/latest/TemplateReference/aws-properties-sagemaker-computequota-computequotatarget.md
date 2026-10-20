---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-computequota-computequotatarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ComputeQuota ComputeQuotaTarget
<a name="aws-properties-sagemaker-computequota-computequotatarget"></a>

The target entity to allocate compute resources to.

## Syntax
<a name="aws-properties-sagemaker-computequota-computequotatarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-computequota-computequotatarget-syntax.json"></a>

```
{
  "[FairShareWeight](#cfn-sagemaker-computequota-computequotatarget-fairshareweight)" : {{Integer}},
  "[TeamName](#cfn-sagemaker-computequota-computequotatarget-teamname)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-computequota-computequotatarget-syntax.yaml"></a>

```
  [FairShareWeight](#cfn-sagemaker-computequota-computequotatarget-fairshareweight): {{Integer}}
  [TeamName](#cfn-sagemaker-computequota-computequotatarget-teamname): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-computequota-computequotatarget-properties"></a>

`FairShareWeight`  <a name="cfn-sagemaker-computequota-computequotatarget-fairshareweight"></a>
Assigned entity fair-share weight. Idle compute will be shared across entities based on these assigned weights. This weight is only used when `FairShare` is enabled.
A weight of 0 is the lowest priority and 100 is the highest. Weight 0 is the default.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TeamName`  <a name="cfn-sagemaker-computequota-computequotatarget-teamname"></a>
Name of the team to allocate compute resources to.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]([-a-z0-9]*[a-z0-9]){0,39}?$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
