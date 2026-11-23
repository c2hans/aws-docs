---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CapacityReservationInstanceUsage.html
---

# CapacityReservationInstanceUsage

The instances from a SageMaker Capacity Reservation that one account uses.

## Contents
<a name="API_CapacityReservationInstanceUsage_Contents"></a>

 ** AccountId **   <a name="sagemaker-Type-CapacityReservationInstanceUsage-AccountId"></a>
The ID of the AWS account that uses the instances.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** InUseInstanceCount **   <a name="sagemaker-Type-CapacityReservationInstanceUsage-InUseInstanceCount"></a>
The number of instances that the account uses, across all resource types.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** ResourcesUsage **   <a name="sagemaker-Type-CapacityReservationInstanceUsage-ResourcesUsage"></a>
The instance usage for each resource type that has instances in use in the account.
Type: Array of [CapacityReservationResourceUsage](API_CapacityReservationResourceUsage.md) objects
Required: Yes

## See Also
<a name="API_CapacityReservationInstanceUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CapacityReservationInstanceUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CapacityReservationInstanceUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CapacityReservationInstanceUsage)
