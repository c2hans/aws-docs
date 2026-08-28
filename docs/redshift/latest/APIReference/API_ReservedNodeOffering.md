---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_ReservedNodeOffering.html
---

# ReservedNodeOffering
<a name="API_ReservedNodeOffering"></a>

Describes a reserved node offering.

## Contents
<a name="API_ReservedNodeOffering_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CurrencyCode **
The currency code for the compute nodes offering.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Duration **
The duration, in seconds, for which the offering will reserve the node.
Type: Integer
Required: No

 ** FixedPrice **
The upfront fixed charge you will pay to purchase the specific reserved node offering.
Type: Double
Required: No

 ** NodeType **
The node type offered by the reserved node offering.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** OfferingType **
The anticipated utilization of the reserved node, as defined in the reserved node offering.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** RecurringCharges.RecurringCharge.N **
The charge to your account regardless of whether you are creating any clusters using the node offering. Recurring charges are only in effect for heavy-utilization reserved nodes.
Type: Array of [RecurringCharge](API_RecurringCharge.md) objects
Required: No

 ** ReservedNodeOfferingId **
The offering identifier.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ReservedNodeOfferingType **

Type: String
Valid Values: `Regular | Upgradable`
Required: No

 ** UsagePrice **
The rate you are charged for each hour the cluster that is using the offering is running.
Type: Double
Required: No

## See Also
<a name="API_ReservedNodeOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ReservedNodeOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ReservedNodeOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ReservedNodeOffering)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
