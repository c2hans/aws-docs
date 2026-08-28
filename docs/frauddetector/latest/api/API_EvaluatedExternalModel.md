---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_EvaluatedExternalModel.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# EvaluatedExternalModel
<a name="API_EvaluatedExternalModel"></a>

 The details of the external (Amazon Sagemaker) model evaluated for generating predictions.

## Contents
<a name="API_EvaluatedExternalModel_Contents"></a>

 ** inputVariables **   <a name="FraudDetector-Type-EvaluatedExternalModel-inputVariables"></a>
 Input variables use for generating predictions.
Type: String to string map
Required: No

 ** modelEndpoint **   <a name="FraudDetector-Type-EvaluatedExternalModel-modelEndpoint"></a>
 The endpoint of the external (Amazon Sagemaker) model.
Type: String
Required: No

 ** outputVariables **   <a name="FraudDetector-Type-EvaluatedExternalModel-outputVariables"></a>
 Output variables.
Type: String to string map
Required: No

 ** useEventVariables **   <a name="FraudDetector-Type-EvaluatedExternalModel-useEventVariables"></a>
 Indicates whether event variables were used to generate predictions.
Type: Boolean
Required: No

## See Also
<a name="API_EvaluatedExternalModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/EvaluatedExternalModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/EvaluatedExternalModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/EvaluatedExternalModel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
