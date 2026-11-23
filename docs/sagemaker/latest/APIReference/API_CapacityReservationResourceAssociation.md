---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CapacityReservationResourceAssociation.html
---

# CapacityReservationResourceAssociation

An association between one type of resource in your account and a SageMaker Capacity Reservation. Each item contains exactly one member.

## Contents
<a name="API_CapacityReservationResourceAssociation_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Endpoints **   <a name="sagemaker-Type-CapacityReservationResourceAssociation-Endpoints"></a>
The association between the SageMaker AI endpoints in your account and the SageMaker Capacity Reservation, through one ML capacity reservation. The response includes one item for each ML capacity reservation.
Type: [CapacityReservationEndpointsAssociation](API_CapacityReservationEndpointsAssociation.md) object
Required: No

 ** HyperPodClusters **   <a name="sagemaker-Type-CapacityReservationResourceAssociation-HyperPodClusters"></a>
The association between the SageMaker AI HyperPod clusters in your account and the SageMaker Capacity Reservation. The association applies to all HyperPod clusters in your account.
Type: [CapacityReservationHyperPodClustersAssociation](API_CapacityReservationHyperPodClustersAssociation.md) object
Required: No

## See Also
<a name="API_CapacityReservationResourceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CapacityReservationResourceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CapacityReservationResourceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CapacityReservationResourceAssociation)
