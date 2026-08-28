---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityBlockStatus.html
---

# CapacityBlockStatus
<a name="API_CapacityBlockStatus"></a>

Describes the availability of capacity for a Capacity Block.

## Contents
<a name="API_CapacityBlockStatus_Contents"></a>

 ** capacityBlockId **
The ID of the Capacity Block.
Type: String
Required: No

 ** CapacityReservationStatusSet.N **
The availability of capacity for the Capacity Block reservations.
Type: Array of [CapacityReservationStatus](API_CapacityReservationStatus.md) objects
Required: No

 ** interconnectStatus **
The status of the high-bandwidth accelerator interconnect. Possible states include:
+  `ok` the accelerator interconnect is healthy.
+  `impaired` - accelerator interconnect communication is impaired.
+  `insufficient-data` - insufficient data to determine accelerator interconnect status.
Type: String
Valid Values: `ok | impaired | insufficient-data`
Required: No

 ** totalAvailableCapacity **
The remaining capacity. Indicates the number of resources that can be launched into the Capacity Block.
Type: Integer
Required: No

 ** totalCapacity **
The combined amount of `Available` and `Unavailable` capacity in the Capacity Block.
Type: Integer
Required: No

 ** totalUnavailableCapacity **
The unavailable capacity. Indicates the instance capacity that is unavailable for use due to a system status check failure.
Type: Integer
Required: No

## See Also
<a name="API_CapacityBlockStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityBlockStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityBlockStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityBlockStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
