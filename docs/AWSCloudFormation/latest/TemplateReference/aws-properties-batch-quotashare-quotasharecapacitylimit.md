---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-quotashare-quotasharecapacitylimit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::QuotaShare QuotaShareCapacityLimit
<a name="aws-properties-batch-quotashare-quotasharecapacitylimit"></a>

Defines the capacity limit for a quota share, or the type and maximum quantity of a particular resource that can be allocated to jobs in the quota share without borrowing.

## Syntax
<a name="aws-properties-batch-quotashare-quotasharecapacitylimit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-quotashare-quotasharecapacitylimit-syntax.json"></a>

```
{
  "[CapacityUnit](#cfn-batch-quotashare-quotasharecapacitylimit-capacityunit)" : {{String}},
  "[MaxCapacity](#cfn-batch-quotashare-quotasharecapacitylimit-maxcapacity)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-batch-quotashare-quotasharecapacitylimit-syntax.yaml"></a>

```
  [CapacityUnit](#cfn-batch-quotashare-quotasharecapacitylimit-capacityunit): {{String}}
  [MaxCapacity](#cfn-batch-quotashare-quotasharecapacitylimit-maxcapacity): {{Integer}}
```

## Properties
<a name="aws-properties-batch-quotashare-quotasharecapacitylimit-properties"></a>

`CapacityUnit`  <a name="cfn-batch-quotashare-quotasharecapacitylimit-capacityunit"></a>
The unit of compute capacity for the capacityLimit. For example, `ml.m5.large`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxCapacity`  <a name="cfn-batch-quotashare-quotasharecapacitylimit-maxcapacity"></a>
The maximum capacity available for the quota share. This value represents the maximum quantity of a resource that can be allocated to jobs in the quota share without borrowing.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
