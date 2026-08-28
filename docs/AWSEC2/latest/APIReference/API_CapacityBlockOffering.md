---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityBlockOffering.html
---

# CapacityBlockOffering
<a name="API_CapacityBlockOffering"></a>

The recommended Capacity Block that fits your search requirements.

## Contents
<a name="API_CapacityBlockOffering_Contents"></a>

 ** availabilityZone **
The Availability Zone of the Capacity Block offering.
Type: String
Required: No

 ** capacityBlockDurationHours **
The number of hours (in addition to `capacityBlockDurationMinutes`) for the duration of the Capacity Block reservation. For example, if a Capacity Block starts at **04:55** and ends at **11:30**, the hours field would be **6**.
Type: Integer
Required: No

 ** capacityBlockDurationMinutes **
The number of minutes (in addition to `capacityBlockDurationHours`) for the duration of the Capacity Block reservation. For example, if a Capacity Block starts at **08:55** and ends at **11:30**, the minutes field would be **35**.
Type: Integer
Required: No

 ** capacityBlockOfferingId **
The ID of the Capacity Block offering.
Type: String
Required: No

 ** currencyCode **
The currency of the payment for the Capacity Block.
Type: String
Required: No

 ** endDate **
The end date of the Capacity Block offering.
Type: Timestamp
Required: No

 ** instanceCount **
The number of instances in the Capacity Block offering.
Type: Integer
Required: No

 ** instanceType **
The instance type of the Capacity Block offering.
Type: String
Required: No

 ** startDate **
The start date of the Capacity Block offering.
Type: Timestamp
Required: No

 ** tenancy **
The tenancy of the Capacity Block.
Type: String
Valid Values: `default | dedicated`
Required: No

 ** ultraserverCount **
The number of EC2 UltraServers in the offering.
Type: Integer
Required: No

 ** ultraserverType **
The EC2 UltraServer type of the Capacity Block offering.
Type: String
Required: No

 ** upfrontFee **
The total price to be paid up front.
Type: String
Required: No

 ** zoneType **
The type of zone where the Capacity Block offering is available.
Type: String
Required: No

## See Also
<a name="API_CapacityBlockOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityBlockOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityBlockOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityBlockOffering)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
