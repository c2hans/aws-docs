---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ReservedDBInstancesOffering.html
---

# ReservedDBInstancesOffering
<a name="API_ReservedDBInstancesOffering"></a>

This data type is used as a response element in the `DescribeReservedDBInstancesOfferings` action.

## Contents
<a name="API_ReservedDBInstancesOffering_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CurrencyCode **
The currency code for the reserved DB instance offering.
Type: String
Required: No

 ** DBInstanceClass **
The DB instance class for the reserved DB instance.
Type: String
Required: No

 ** Duration **
The duration of the offering in seconds.
Type: Integer
Required: No

 ** FixedPrice **
The fixed price charged for this offering.
Type: Double
Required: No

 ** MultiAZ **
Indicates whether the offering applies to Multi-AZ deployments.
Type: Boolean
Required: No

 ** OfferingType **
The offering type.
Type: String
Required: No

 ** ProductDescription **
The database engine used by the offering.
Type: String
Required: No

 ** RecurringCharges.RecurringCharge.N **
The recurring price charged to run this reserved DB instance.
Type: Array of [RecurringCharge](API_RecurringCharge.md) objects
Required: No

 ** ReservedDBInstancesOfferingId **
The offering identifier.
Type: String
Required: No

 ** UsagePrice **
The hourly price charged for this offering.
Type: Double
Required: No

## See Also
<a name="API_ReservedDBInstancesOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ReservedDBInstancesOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ReservedDBInstancesOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ReservedDBInstancesOffering)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
