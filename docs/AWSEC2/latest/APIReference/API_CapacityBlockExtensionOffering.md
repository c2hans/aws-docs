---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityBlockExtensionOffering.html
---

# CapacityBlockExtensionOffering
<a name="API_CapacityBlockExtensionOffering"></a>

The recommended Capacity Block extension that fits your search requirements.

## Contents
<a name="API_CapacityBlockExtensionOffering_Contents"></a>

 ** availabilityZone **
The Availability Zone of the Capacity Block that will be extended.
Type: String
Required: No

 ** availabilityZoneId **
The Availability Zone ID of the Capacity Block that will be extended.
Type: String
Required: No

 ** capacityBlockExtensionDurationHours **
The amount of time of the Capacity Block extension offering in hours.
Type: Integer
Required: No

 ** capacityBlockExtensionEndDate **
The date and time at which the Capacity Block extension expires. When a Capacity Block expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Block's state changes to `expired` when it reaches its end date
Type: Timestamp
Required: No

 ** capacityBlockExtensionOfferingId **
The ID of the Capacity Block extension offering.
Type: String
Required: No

 ** capacityBlockExtensionStartDate **
The date and time at which the Capacity Block extension will start. This date is also the same as the end date of the Capacity Block that will be extended.
Type: Timestamp
Required: No

 ** currencyCode **
The currency of the payment for the Capacity Block extension offering.
Type: String
Required: No

 ** instanceCount **
The number of instances in the Capacity Block extension offering.
Type: Integer
Required: No

 ** instanceType **
The instance type of the Capacity Block that will be extended.
Type: String
Required: No

 ** startDate **
The start date of the Capacity Block that will be extended.
Type: Timestamp
Required: No

 ** tenancy **
Indicates the tenancy of the Capacity Block extension offering. A Capacity Block can have one of the following tenancy settings:
+  `default` - The Capacity Block is created on hardware that is shared with other AWS accounts.
+  `dedicated` - The Capacity Block is created on single-tenant hardware that is dedicated to a single AWS account.
Type: String
Valid Values: `default | dedicated`
Required: No

 ** upfrontFee **
The total price of the Capacity Block extension offering, to be paid up front.
Type: String
Required: No

 ** zoneType **
The type of zone where the Capacity Block extension offering is available.
Type: String
Required: No

## See Also
<a name="API_CapacityBlockExtensionOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityBlockExtensionOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityBlockExtensionOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityBlockExtensionOffering)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
