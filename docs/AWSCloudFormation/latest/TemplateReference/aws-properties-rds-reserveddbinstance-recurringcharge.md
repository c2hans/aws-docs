---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-reserveddbinstance-recurringcharge.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::ReservedDBInstance RecurringCharge
<a name="aws-properties-rds-reserveddbinstance-recurringcharge"></a>

This data type is used as a response element in the `DescribeReservedDBInstances` and `DescribeReservedDBInstancesOfferings` actions.

## Syntax
<a name="aws-properties-rds-reserveddbinstance-recurringcharge-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rds-reserveddbinstance-recurringcharge-syntax.json"></a>

```
{
  "[RecurringChargeAmount](#cfn-rds-reserveddbinstance-recurringcharge-recurringchargeamount)" : {{Number}},
  "[RecurringChargeFrequency](#cfn-rds-reserveddbinstance-recurringcharge-recurringchargefrequency)" : {{String}}
}
```

### YAML
<a name="aws-properties-rds-reserveddbinstance-recurringcharge-syntax.yaml"></a>

```
  [RecurringChargeAmount](#cfn-rds-reserveddbinstance-recurringcharge-recurringchargeamount): {{Number}}
  [RecurringChargeFrequency](#cfn-rds-reserveddbinstance-recurringcharge-recurringchargefrequency): {{String}}
```

## Properties
<a name="aws-properties-rds-reserveddbinstance-recurringcharge-properties"></a>

`RecurringChargeAmount`  <a name="cfn-rds-reserveddbinstance-recurringcharge-recurringchargeamount"></a>
The amount of the recurring charge.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecurringChargeFrequency`  <a name="cfn-rds-reserveddbinstance-recurringcharge-recurringchargefrequency"></a>
The frequency of the recurring charge.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
