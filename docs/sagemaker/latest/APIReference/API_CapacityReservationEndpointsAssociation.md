---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CapacityReservationEndpointsAssociation.html
---

# CapacityReservationEndpointsAssociation

The association between the SageMaker AI endpoints in your account and a SageMaker Capacity Reservation, through one ML capacity reservation. To use the reserved instances for an endpoint, specify the ML capacity reservation ARN in the `MlReservationArn` field of `ProductionVariantCapacityReservationConfig` when you call `CreateEndpointConfig`.

## Contents
<a name="API_CapacityReservationEndpointsAssociation_Contents"></a>

 ** AssociatedTime **   <a name="sagemaker-Type-CapacityReservationEndpointsAssociation-AssociatedTime"></a>
The time when SageMaker AI started the current association. This time resets when you add the association again after it was removed or after it failed.
Type: Timestamp
Required: Yes

 ** Status **   <a name="sagemaker-Type-CapacityReservationEndpointsAssociation-Status"></a>
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

 ** EndpointSharing **   <a name="sagemaker-Type-CapacityReservationEndpointsAssociation-EndpointSharing"></a>
Whether one endpoint or multiple endpoints can use the ML capacity reservation. Valid values:
SingleEndpoint
Only one endpoint can use the ML capacity reservation.
MultipleEndpoints
Multiple endpoints can use the ML capacity reservation.
Type: String
Valid Values: `SingleEndpoint | MultipleEndpoints`
Required: No

 ** FailureReason **   <a name="sagemaker-Type-CapacityReservationEndpointsAssociation-FailureReason"></a>
The reason that the most recent attempt to add or remove the association failed. This value is returned only when the most recent attempt failed. After a failure to add the association, the status is `Inactive`. After a failure to remove the association, the status is `Active`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** MatchCriteria **   <a name="sagemaker-Type-CapacityReservationEndpointsAssociation-MatchCriteria"></a>
How endpoints in your account match the ML capacity reservation. Valid values:
Open
Endpoints in your account use the ML capacity reservation automatically when their instance type matches. You don't specify the ML capacity reservation ARN when you create the endpoint.
Targeted
An endpoint uses the ML capacity reservation only when you specify its ARN when you create or update the endpoint.
Type: String
Valid Values: `Open | Targeted`
Required: No

 ** MlReservationArn **   <a name="sagemaker-Type-CapacityReservationEndpointsAssociation-MlReservationArn"></a>
The Amazon Resource Name (ARN) of the ML capacity reservation. Specify this ARN in `CreateEndpointConfig` to use the reserved instances for an endpoint. For a new ML capacity reservation, this value is returned when the status is `Active`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 258.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z0-9\-]{1,14}/.*`
Required: No

 ** MlReservationId **   <a name="sagemaker-Type-CapacityReservationEndpointsAssociation-MlReservationId"></a>
The name of the ML capacity reservation. The name is the last part of the ML capacity reservation ARN.
Type: String
Required: No

## See Also
<a name="API_CapacityReservationEndpointsAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CapacityReservationEndpointsAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CapacityReservationEndpointsAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CapacityReservationEndpointsAssociation)
