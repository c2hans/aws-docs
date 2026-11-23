---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CapacityReservationHyperPodClustersAssociation.html
---

# CapacityReservationHyperPodClustersAssociation

The association between the SageMaker AI HyperPod clusters in your account and a SageMaker Capacity Reservation.

## Contents
<a name="API_CapacityReservationHyperPodClustersAssociation_Contents"></a>

 ** AssociatedTime **   <a name="sagemaker-Type-CapacityReservationHyperPodClustersAssociation-AssociatedTime"></a>
The time when SageMaker AI started the current association. This time resets when you add the association again after it was removed or after it failed.
Type: Timestamp
Required: Yes

 ** Status **   <a name="sagemaker-Type-CapacityReservationHyperPodClustersAssociation-Status"></a>
The status of the association. Valid values:
Pending
SageMaker AI is adding or removing the association.
Active
The resources are associated with the SageMaker Capacity Reservation and can use its instances.
Inactive
The resources are not associated with the SageMaker Capacity Reservation.
Type: String
Valid Values: `Pending | Active | Inactive`
Required: Yes

 ** FailureReason **   <a name="sagemaker-Type-CapacityReservationHyperPodClustersAssociation-FailureReason"></a>
The reason that the most recent attempt to add or remove the association failed. This value is returned only when the most recent attempt failed. After a failure to add the association, the status is `Inactive`. After a failure to remove the association, the status is `Active`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_CapacityReservationHyperPodClustersAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CapacityReservationHyperPodClustersAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CapacityReservationHyperPodClustersAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CapacityReservationHyperPodClustersAssociation)
