---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_ModelOutputConfiguration.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# ModelOutputConfiguration
<a name="API_ModelOutputConfiguration"></a>

Provides the Amazon Sagemaker model output configuration.

## Contents
<a name="API_ModelOutputConfiguration_Contents"></a>

 ** format **   <a name="FraudDetector-Type-ModelOutputConfiguration-format"></a>
The format of the model output configuration.
Type: String
Valid Values: `TEXT_CSV | APPLICATION_JSONLINES`
Required: Yes

 ** csvIndexToVariableMap **   <a name="FraudDetector-Type-ModelOutputConfiguration-csvIndexToVariableMap"></a>
A map of CSV index values in the SageMaker response to the Amazon Fraud Detector variables.
Type: String to string map
Required: No

 ** jsonKeyToVariableMap **   <a name="FraudDetector-Type-ModelOutputConfiguration-jsonKeyToVariableMap"></a>
A map of JSON keys in response from SageMaker to the Amazon Fraud Detector variables.
Type: String to string map
Required: No

## See Also
<a name="API_ModelOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/ModelOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/ModelOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/ModelOutputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
