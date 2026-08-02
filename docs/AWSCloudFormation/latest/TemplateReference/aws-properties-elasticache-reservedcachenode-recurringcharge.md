---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-reservedcachenode-recurringcharge.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::ReservedCacheNode RecurringCharge
<a name="aws-properties-elasticache-reservedcachenode-recurringcharge"></a>

Contains the specific price and frequency of a recurring charges for a reserved cache node, or for a reserved cache node offering.

## Syntax
<a name="aws-properties-elasticache-reservedcachenode-recurringcharge-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-reservedcachenode-recurringcharge-syntax.json"></a>

```
{
  "[RecurringChargeAmount](#cfn-elasticache-reservedcachenode-recurringcharge-recurringchargeamount)" : {{Number}},
  "[RecurringChargeFrequency](#cfn-elasticache-reservedcachenode-recurringcharge-recurringchargefrequency)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticache-reservedcachenode-recurringcharge-syntax.yaml"></a>

```
  [RecurringChargeAmount](#cfn-elasticache-reservedcachenode-recurringcharge-recurringchargeamount): {{Number}}
  [RecurringChargeFrequency](#cfn-elasticache-reservedcachenode-recurringcharge-recurringchargefrequency): {{String}}
```

## Properties
<a name="aws-properties-elasticache-reservedcachenode-recurringcharge-properties"></a>

`RecurringChargeAmount`  <a name="cfn-elasticache-reservedcachenode-recurringcharge-recurringchargeamount"></a>
The monetary amount of the recurring charge.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecurringChargeFrequency`  <a name="cfn-elasticache-reservedcachenode-recurringcharge-recurringchargefrequency"></a>
The frequency of the recurring charge.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
