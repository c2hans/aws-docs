---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProductionVariantCapacityReservationConfig.html
---

# ProductionVariantCapacityReservationConfig
<a name="API_ProductionVariantCapacityReservationConfig"></a>

Settings for the capacity reservation for the compute instances that SageMaker AI reserves for an endpoint.

## Contents
<a name="API_ProductionVariantCapacityReservationConfig_Contents"></a>

 ** CapacityReservationPreference **   <a name="sagemaker-Type-ProductionVariantCapacityReservationConfig-CapacityReservationPreference"></a>
Options that you can choose for the capacity reservation. SageMaker AI supports the following options:
capacity-reservations-only
SageMaker AI launches instances only into an ML capacity reservation. If no capacity is available, the instances fail to launch.
Type: String
Valid Values: `capacity-reservations-only`
Required: No

 ** MlReservationArn **   <a name="sagemaker-Type-ProductionVariantCapacityReservationConfig-MlReservationArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the ML capacity reservation that SageMaker AI applies when it deploys the endpoint.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 258.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z0-9\-]{1,14}/.*`
Required: No

## See Also
<a name="API_ProductionVariantCapacityReservationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProductionVariantCapacityReservationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProductionVariantCapacityReservationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProductionVariantCapacityReservationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
