---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_TrainingResult.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# TrainingResult
<a name="API_TrainingResult"></a>

The training result details.

## Contents
<a name="API_TrainingResult_Contents"></a>

 ** dataValidationMetrics **   <a name="FraudDetector-Type-TrainingResult-dataValidationMetrics"></a>
The validation metrics.
Type: [DataValidationMetrics](API_DataValidationMetrics.md) object
Required: No

 ** trainingMetrics **   <a name="FraudDetector-Type-TrainingResult-trainingMetrics"></a>
The training metric details.
Type: [TrainingMetrics](API_TrainingMetrics.md) object
Required: No

 ** variableImportanceMetrics **   <a name="FraudDetector-Type-TrainingResult-variableImportanceMetrics"></a>
The variable importance metrics.
Type: [VariableImportanceMetrics](API_VariableImportanceMetrics.md) object
Required: No

## See Also
<a name="API_TrainingResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/TrainingResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/TrainingResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/TrainingResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
