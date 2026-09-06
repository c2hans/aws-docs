---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ReservedDBInstance.html
---

# ReservedDBInstance
<a name="API_ReservedDBInstance"></a>

This data type is used as a response element in the `DescribeReservedDBInstances` and `PurchaseReservedDBInstancesOffering` actions.

## Contents
<a name="API_ReservedDBInstance_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CurrencyCode **
The currency code for the reserved DB instance.
Type: String
Required: No

 ** DBInstanceClass **
The DB instance class for the reserved DB instance.
Type: String
Required: No

 ** DBInstanceCount **
The number of reserved DB instances.
Type: Integer
Required: No

 ** Duration **
The duration of the reservation in seconds.
Type: Integer
Required: No

 ** FixedPrice **
The fixed price charged for this reserved DB instance.
Type: Double
Required: No

 ** LeaseId **
The unique identifier for the lease associated with the reserved DB instance.
 AWS Support might request the lease ID for an issue related to a reserved DB instance.
Type: String
Required: No

 ** MultiAZ **
Indicates whether the reservation applies to Multi-AZ deployments.
Type: Boolean
Required: No

 ** OfferingType **
The offering type of this reserved DB instance.
Type: String
Required: No

 ** ProductDescription **
The description of the reserved DB instance.
Type: String
Required: No

 ** RecurringCharges.RecurringCharge.N **
The recurring price charged to run this reserved DB instance.
Type: Array of [RecurringCharge](API_RecurringCharge.md) objects
Required: No

 ** ReservedDBInstanceArn **
The Amazon Resource Name (ARN) for the reserved DB instance.
Type: String
Required: No

 ** ReservedDBInstanceId **
The unique identifier for the reservation.
Type: String
Required: No

 ** ReservedDBInstancesOfferingId **
The offering identifier.
Type: String
Required: No

 ** StartTime **
The time the reservation started.
Type: Timestamp
Required: No

 ** State **
The state of the reserved DB instance.
Type: String
Required: No

 ** UsagePrice **
The hourly price charged for this reserved DB instance.
Type: Double
Required: No

## See Also
<a name="API_ReservedDBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ReservedDBInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ReservedDBInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ReservedDBInstance)
