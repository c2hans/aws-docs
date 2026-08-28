---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_ReservedNode.html
---

# ReservedNode
<a name="API_ReservedNode"></a>

Describes a reserved node. You can call the [DescribeReservedNodeOfferings](API_DescribeReservedNodeOfferings.md) API to obtain the available reserved node offerings.

## Contents
<a name="API_ReservedNode_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CurrencyCode **
The currency code for the reserved cluster.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Duration **
The duration of the node reservation in seconds.
Type: Integer
Required: No

 ** FixedPrice **
The fixed cost Amazon Redshift charges you for this reserved node.
Type: Double
Required: No

 ** NodeCount **
The number of reserved compute nodes.
Type: Integer
Required: No

 ** NodeType **
The node type of the reserved node.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** OfferingType **
The anticipated utilization of the reserved node, as defined in the reserved node offering.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** RecurringCharges.RecurringCharge.N **
The recurring charges for the reserved node.
Type: Array of [RecurringCharge](API_RecurringCharge.md) objects
Required: No

 ** ReservedNodeId **
The unique identifier for the reservation.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ReservedNodeOfferingId **
The identifier for the reserved node offering.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ReservedNodeOfferingType **

Type: String
Valid Values: `Regular | Upgradable`
Required: No

 ** StartTime **
The time the reservation started. You purchase a reserved node offering for a duration. This is the start time of that duration.
Type: Timestamp
Required: No

 ** State **
The state of the reserved compute node.
Possible Values:
+ pending-payment-This reserved node has recently been purchased, and the sale has been approved, but payment has not yet been confirmed.
+ active-This reserved node is owned by the caller and is available for use.
+ payment-failed-Payment failed for the purchase attempt.
+ retired-The reserved node is no longer available.
+ exchanging-The owner is exchanging the reserved node for another reserved node.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** UsagePrice **
The hourly rate Amazon Redshift charges you for this reserved node.
Type: Double
Required: No

## See Also
<a name="API_ReservedNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ReservedNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ReservedNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ReservedNode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
