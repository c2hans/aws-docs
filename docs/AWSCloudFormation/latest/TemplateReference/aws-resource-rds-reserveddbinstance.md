---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-reserveddbinstance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::ReservedDBInstance
<a name="aws-resource-rds-reserveddbinstance"></a>

This data type is used as a response element in the `DescribeReservedDBInstances` and `PurchaseReservedDBInstancesOffering` actions.

## Syntax
<a name="aws-resource-rds-reserveddbinstance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rds-reserveddbinstance-syntax.json"></a>

```
{
  "Type" : "AWS::RDS::ReservedDBInstance",
  "Properties" : {
      "[DBInstanceCount](#cfn-rds-reserveddbinstance-dbinstancecount)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-rds-reserveddbinstance-syntax.yaml"></a>

```
Type: AWS::RDS::ReservedDBInstance
Properties:
  [DBInstanceCount](#cfn-rds-reserveddbinstance-dbinstancecount): {{Integer}}
```

## Properties
<a name="aws-resource-rds-reserveddbinstance-properties"></a>

`DBInstanceCount`  <a name="cfn-rds-reserveddbinstance-dbinstancecount"></a>
The number of reserved DB instances.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-rds-reserveddbinstance-return-values"></a>

### Ref
<a name="aws-resource-rds-reserveddbinstance-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-rds-reserveddbinstance-return-values-fn--getatt"></a>

####
<a name="aws-resource-rds-reserveddbinstance-return-values-fn--getatt-fn--getatt"></a>

`CurrencyCode`  <a name="CurrencyCode-fn::getatt"></a>
The currency code for the reserved DB instance.

`DBInstanceClass`  <a name="DBInstanceClass-fn::getatt"></a>
The DB instance class for the reserved DB instance.

`Duration`  <a name="Duration-fn::getatt"></a>
The duration of the reservation in seconds.

`FixedPrice`  <a name="FixedPrice-fn::getatt"></a>
The fixed price charged for this reserved DB instance.

`MultiAZ`  <a name="MultiAZ-fn::getatt"></a>
Indicates whether the reservation applies to Multi-AZ deployments.

`OfferingType`  <a name="OfferingType-fn::getatt"></a>
The offering type of this reserved DB instance.

`ProductDescription`  <a name="ProductDescription-fn::getatt"></a>
The description of the reserved DB instance.

`RecurringCharges`  <a name="RecurringCharges-fn::getatt"></a>
The recurring price charged to run this reserved DB instance.

`ReservedDBInstanceArn`  <a name="ReservedDBInstanceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the reserved DB instance.

`ReservedDBInstanceId`  <a name="ReservedDBInstanceId-fn::getatt"></a>
The unique identifier for the reservation.

`ReservedDBInstancesOfferingId`  <a name="ReservedDBInstancesOfferingId-fn::getatt"></a>
The offering identifier.

`StartTime`  <a name="StartTime-fn::getatt"></a>
The time the reservation started.

`State`  <a name="State-fn::getatt"></a>
The state of the reserved DB instance.

`Tags`  <a name="Tags-fn::getatt"></a>
Property description not available.

`UsagePrice`  <a name="UsagePrice-fn::getatt"></a>
The hourly price charged for this reserved DB instance.
