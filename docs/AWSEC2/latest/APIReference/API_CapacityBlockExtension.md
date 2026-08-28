---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityBlockExtension.html
---

# CapacityBlockExtension
<a name="API_CapacityBlockExtension"></a>

Describes a Capacity Block extension. With an extension, you can extend the duration of time for an existing Capacity Block.

## Contents
<a name="API_CapacityBlockExtension_Contents"></a>

 ** availabilityZone **
The Availability Zone of the Capacity Block extension.
Type: String
Required: No

 ** availabilityZoneId **
The Availability Zone ID of the Capacity Block extension.
Type: String
Required: No

 ** capacityBlockExtensionDurationHours **
The duration of the Capacity Block extension in hours.
Type: Integer
Required: No

 ** capacityBlockExtensionEndDate **
The end date of the Capacity Block extension.
Type: Timestamp
Required: No

 ** capacityBlockExtensionOfferingId **
The ID of the Capacity Block extension offering.
Type: String
Required: No

 ** capacityBlockExtensionPurchaseDate **
The date when the Capacity Block extension was purchased.
Type: Timestamp
Required: No

 ** capacityBlockExtensionStartDate **
The start date of the Capacity Block extension.
Type: Timestamp
Required: No

 ** capacityBlockExtensionStatus **
The status of the Capacity Block extension. A Capacity Block extension can have one of the following statuses:
+  `payment-pending` - The Capacity Block extension payment is processing. If your payment can't be processed within 12 hours, the Capacity Block extension is failed.
+  `payment-failed` - Payment for the Capacity Block extension request was not successful.
+  `payment-succeeded` - Payment for the Capacity Block extension request was successful. You receive an invoice that reflects the one-time upfront payment. In the invoice, you can associate the paid amount with the Capacity Block reservation ID.
Type: String
Valid Values: `payment-pending | payment-failed | payment-succeeded`
Required: No

 ** capacityReservationId **
The reservation ID of the Capacity Block extension.
Type: String
Required: No

 ** currencyCode **
The currency of the payment for the Capacity Block extension.
Type: String
Required: No

 ** instanceCount **
The number of instances in the Capacity Block extension.
Type: Integer
Required: No

 ** instanceType **
The instance type of the Capacity Block extension.
Type: String
Required: No

 ** upfrontFee **
The total price to be paid up front.
Type: String
Required: No

 ** zoneType **
The type of zone where the Capacity Block extension is located.
Type: String
Required: No

## See Also
<a name="API_CapacityBlockExtension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityBlockExtension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityBlockExtension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityBlockExtension)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
