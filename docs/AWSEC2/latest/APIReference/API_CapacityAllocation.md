---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityAllocation.html
---

# CapacityAllocation
<a name="API_CapacityAllocation"></a>

Information about instance capacity usage for a Capacity Reservation.

## Contents
<a name="API_CapacityAllocation_Contents"></a>

 ** AllocationMetadataList.N **
Additional metadata associated with the capacity allocation. Each entry contains a key-value pair providing context about the allocation.
Type: Array of [CapacityAllocationMetadataEntry](API_CapacityAllocationMetadataEntry.md) objects
Required: No

 ** allocationType **
The usage type. `used` indicates that the instance capacity is in use by instances that are running in the Capacity Reservation.
Type: String
Valid Values: `used | cancelling`
Required: No

 ** count **
The amount of instance capacity associated with the usage. For example a value of `4` indicates that instance capacity for 4 instances is currently in use.
Type: Integer
Required: No

## See Also
<a name="API_CapacityAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityAllocation)
