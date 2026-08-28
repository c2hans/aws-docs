---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AICapacityReservationConfig.html
---

# AICapacityReservationConfig
<a name="API_AICapacityReservationConfig"></a>

The capacity reservation configuration for an AI recommendation job.

## Contents
<a name="API_AICapacityReservationConfig_Contents"></a>

 ** CapacityReservationPreference **   <a name="sagemaker-Type-AICapacityReservationConfig-CapacityReservationPreference"></a>
The capacity reservation preference. The only valid value is `capacity-reservations-only`.
Type: String
Valid Values: `capacity-reservations-only`
Required: No

 ** MlReservationArns **   <a name="sagemaker-Type-AICapacityReservationConfig-MlReservationArns"></a>
The list of ML reservation ARNs to use.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z0-9\-]{1,14}/.*`
Required: No

## See Also
<a name="API_AICapacityReservationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AICapacityReservationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AICapacityReservationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AICapacityReservationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
