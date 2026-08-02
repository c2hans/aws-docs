---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReservedInstancesListing.html
---

# ReservedInstancesListing
<a name="API_ReservedInstancesListing"></a>

Describes a Reserved Instance listing.

## Contents
<a name="API_ReservedInstancesListing_Contents"></a>

 ** clientToken **
A unique, case-sensitive key supplied by the client to ensure that the request is idempotent. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 ** createDate **
The time the listing was created.
Type: Timestamp
Required: No

 ** InstanceCounts.N **
The number of instances in this state.
Type: Array of [InstanceCount](API_InstanceCount.md) objects
Required: No

 ** PriceSchedules.N **
The price of the Reserved Instance listing.
Type: Array of [PriceSchedule](API_PriceSchedule.md) objects
Required: No

 ** reservedInstancesId **
The ID of the Reserved Instance.
Type: String
Required: No

 ** reservedInstancesListingId **
The ID of the Reserved Instance listing.
Type: String
Required: No

 ** status **
The status of the Reserved Instance listing.
Type: String
Valid Values: `active | pending | cancelled | closed`
Required: No

 ** statusMessage **
The reason for the current status of the Reserved Instance listing. The response can be blank.
Type: String
Required: No

 ** TagSet.N **
Any tags assigned to the resource.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** updateDate **
The last modified timestamp of the listing.
Type: Timestamp
Required: No

## See Also
<a name="API_ReservedInstancesListing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReservedInstancesListing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReservedInstancesListing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReservedInstancesListing)
