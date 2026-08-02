---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityBlock.html
---

# CapacityBlock
<a name="API_CapacityBlock"></a>

Reserve powerful GPU instances on a future date to support your short duration machine learning (ML) workloads. Instances that run inside a Capacity Block are automatically placed close together inside [Amazon EC2 UltraClusters](http://aws.amazon.com/ec2/ultraclusters/), for low-latency, petabit-scale, non-blocking networking.

You can also reserve Amazon EC2 UltraServers. UltraServers connect multiple EC2 instances using a low-latency, high-bandwidth accelerator interconnect (NeuronLink). They are built to tackle very large-scale AI/ML workloads that require significant processing power. For more information, see Amazon EC2 UltraServers.

## Contents
<a name="API_CapacityBlock_Contents"></a>

 ** availabilityZone **
The Availability Zone of the Capacity Block.
Type: String
Required: No

 ** availabilityZoneId **
The Availability Zone ID of the Capacity Block.
Type: String
Required: No

 ** capacityBlockId **
The ID of the Capacity Block.
Type: String
Required: No

 ** CapacityReservationIdSet.N **
The ID of the Capacity Reservation.
Type: Array of strings
Required: No

 ** createDate **
The date and time at which the Capacity Block was created.
Type: Timestamp
Required: No

 ** endDate **
The date and time at which the Capacity Block expires. When a Capacity Block expires, all instances in the Capacity Block are terminated.
Type: Timestamp
Required: No

 ** startDate **
The date and time at which the Capacity Block was started.
Type: Timestamp
Required: No

 ** state **
The state of the Capacity Block.
Type: String
Valid Values: `active | expired | unavailable | cancelled | failed | scheduled | payment-pending | payment-failed`
Required: No

 ** TagSet.N **
The tags assigned to the Capacity Block.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** ultraserverType **
The EC2 UltraServer type of the Capacity Block.
Type: String
Required: No

## See Also
<a name="API_CapacityBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityBlock)
