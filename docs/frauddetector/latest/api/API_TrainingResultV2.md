---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_TrainingResultV2.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# TrainingResultV2
<a name="API_TrainingResultV2"></a>

 The training result details.

## Contents
<a name="API_TrainingResultV2_Contents"></a>

 ** aggregatedVariablesImportanceMetrics **   <a name="FraudDetector-Type-TrainingResultV2-aggregatedVariablesImportanceMetrics"></a>
 The variable importance metrics of the aggregated variables.
Account Takeover Insights (ATI) model uses event variables from the login data you provide to continuously calculate a set of variables (aggregated variables) based on historical events. For example, your ATI model might calculate the number of times an user has logged in using the same IP address. In this case, event variables used to derive the aggregated variables are `IP address` and `user`.
Type: [AggregatedVariablesImportanceMetrics](API_AggregatedVariablesImportanceMetrics.md) object
Required: No

 ** dataValidationMetrics **   <a name="FraudDetector-Type-TrainingResultV2-dataValidationMetrics"></a>
The model training data validation metrics.
Type: [DataValidationMetrics](API_DataValidationMetrics.md) object
Required: No

 ** trainingMetricsV2 **   <a name="FraudDetector-Type-TrainingResultV2-trainingMetricsV2"></a>
 The training metric details.
Type: [TrainingMetricsV2](API_TrainingMetricsV2.md) object
Required: No

 ** variableImportanceMetrics **   <a name="FraudDetector-Type-TrainingResultV2-variableImportanceMetrics"></a>
The variable importance metrics details.
Type: [VariableImportanceMetrics](API_VariableImportanceMetrics.md) object
Required: No

## See Also
<a name="API_TrainingResultV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/TrainingResultV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/TrainingResultV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/TrainingResultV2)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
