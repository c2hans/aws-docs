---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantCapacityReservationSummary.html
---

# ProductionVariantCapacityReservationSummary
<a name="API_ProductionVariantCapacityReservationSummary"></a>

Details about an ML capacity reservation.

## Contents
<a name="API_ProductionVariantCapacityReservationSummary_Contents"></a>

 ** AvailableInstanceCount **   <a name="sagemaker-Type-ProductionVariantCapacityReservationSummary-AvailableInstanceCount"></a>
The number of instances that are currently available in the ML capacity reservation.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** CapacityReservationPreference **   <a name="sagemaker-Type-ProductionVariantCapacityReservationSummary-CapacityReservationPreference"></a>
The option that you chose for the capacity reservation. SageMaker AI supports the following options:
capacity-reservations-only
SageMaker AI launches instances only into an ML capacity reservation. If no capacity is available, the instances fail to launch.
Type: String
Valid Values: `capacity-reservations-only`
Required: No

 ** Ec2CapacityReservations **   <a name="sagemaker-Type-ProductionVariantCapacityReservationSummary-Ec2CapacityReservations"></a>
The EC2 capacity reservations that are shared to this ML capacity reservation, if any.
Type: Array of [Ec2CapacityReservation](API_Ec2CapacityReservation.md) objects
Required: No

 ** MlReservationArn **   <a name="sagemaker-Type-ProductionVariantCapacityReservationSummary-MlReservationArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the ML capacity reservation that SageMaker AI applies when it deploys the endpoint.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 258.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z0-9\-]{1,14}/.*`
Required: No

 ** TotalInstanceCount **   <a name="sagemaker-Type-ProductionVariantCapacityReservationSummary-TotalInstanceCount"></a>
The number of instances that you allocated to the ML capacity reservation.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** UsedByCurrentEndpoint **   <a name="sagemaker-Type-ProductionVariantCapacityReservationSummary-UsedByCurrentEndpoint"></a>
The number of instances from the ML capacity reservation that are being used by the endpoint.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ProductionVariantCapacityReservationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProductionVariantCapacityReservationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProductionVariantCapacityReservationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProductionVariantCapacityReservationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
