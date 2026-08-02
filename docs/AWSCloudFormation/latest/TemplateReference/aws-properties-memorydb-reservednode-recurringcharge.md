---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-memorydb-reservednode-recurringcharge.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MemoryDB::ReservedNode RecurringCharge
<a name="aws-properties-memorydb-reservednode-recurringcharge"></a>

The recurring charge to run this reserved node.

## Syntax
<a name="aws-properties-memorydb-reservednode-recurringcharge-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-memorydb-reservednode-recurringcharge-syntax.json"></a>

```
{
  "[RecurringChargeAmount](#cfn-memorydb-reservednode-recurringcharge-recurringchargeamount)" : {{Number}},
  "[RecurringChargeFrequency](#cfn-memorydb-reservednode-recurringcharge-recurringchargefrequency)" : {{String}}
}
```

### YAML
<a name="aws-properties-memorydb-reservednode-recurringcharge-syntax.yaml"></a>

```
  [RecurringChargeAmount](#cfn-memorydb-reservednode-recurringcharge-recurringchargeamount): {{Number}}
  [RecurringChargeFrequency](#cfn-memorydb-reservednode-recurringcharge-recurringchargefrequency): {{String}}
```

## Properties
<a name="aws-properties-memorydb-reservednode-recurringcharge-properties"></a>

`RecurringChargeAmount`  <a name="cfn-memorydb-reservednode-recurringcharge-recurringchargeamount"></a>
The amount of the recurring charge to run this reserved node.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecurringChargeFrequency`  <a name="cfn-memorydb-reservednode-recurringcharge-recurringchargefrequency"></a>
The frequency of the recurring price charged to run this reserved node.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
