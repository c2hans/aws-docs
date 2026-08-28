---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_MembershipMLPaymentConfig.html
---

# MembershipMLPaymentConfig
<a name="API_MembershipMLPaymentConfig"></a>

An object representing the collaboration member's machine learning payment responsibilities set by the collaboration creator.

## Contents
<a name="API_MembershipMLPaymentConfig_Contents"></a>

 ** modelInference **   <a name="API-Type-MembershipMLPaymentConfig-modelInference"></a>
The payment responsibilities accepted by the member for model inference.
Type: [MembershipModelInferencePaymentConfig](API_MembershipModelInferencePaymentConfig.md) object
Required: No

 ** modelTraining **   <a name="API-Type-MembershipMLPaymentConfig-modelTraining"></a>
The payment responsibilities accepted by the member for model training.
Type: [MembershipModelTrainingPaymentConfig](API_MembershipModelTrainingPaymentConfig.md) object
Required: No

 ** syntheticDataGeneration **   <a name="API-Type-MembershipMLPaymentConfig-syntheticDataGeneration"></a>
The payment configuration for synthetic data generation for this machine learning membership.
Type: [MembershipSyntheticDataGenerationPaymentConfig](API_MembershipSyntheticDataGenerationPaymentConfig.md) object
Required: No

## See Also
<a name="API_MembershipMLPaymentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/MembershipMLPaymentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/MembershipMLPaymentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/MembershipMLPaymentConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
