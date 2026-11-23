---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CapacityReservationResourceUsage.html
---

# CapacityReservationResourceUsage

The instances from a SageMaker Capacity Reservation that one resource type uses in an account.

## Contents
<a name="API_CapacityReservationResourceUsage_Contents"></a>

 ** InUseInstanceCount **   <a name="sagemaker-Type-CapacityReservationResourceUsage-InUseInstanceCount"></a>
The number of instances from the SageMaker Capacity Reservation that are in use.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** ResourceType **   <a name="sagemaker-Type-CapacityReservationResourceUsage-ResourceType"></a>
The type of resource that uses the instances. Valid values:
HyperPodClusters
SageMaker AI HyperPod clusters.
Endpoints
SageMaker AI endpoints.
Type: String
Valid Values: `HyperPodClusters | Endpoints`
Required: Yes

## See Also
<a name="API_CapacityReservationResourceUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CapacityReservationResourceUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CapacityReservationResourceUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CapacityReservationResourceUsage)
