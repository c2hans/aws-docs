---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_ModelInputConfiguration.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# ModelInputConfiguration
<a name="API_ModelInputConfiguration"></a>

The Amazon SageMaker model input configuration.

## Contents
<a name="API_ModelInputConfiguration_Contents"></a>

 ** useEventVariables **   <a name="FraudDetector-Type-ModelInputConfiguration-useEventVariables"></a>
The event variables.
Type: Boolean
Required: Yes

 ** csvInputTemplate **   <a name="FraudDetector-Type-ModelInputConfiguration-csvInputTemplate"></a>
 Template for constructing the CSV input-data sent to SageMaker. At event-evaluation, the placeholders for variable-names in the template will be replaced with the variable values before being sent to SageMaker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

 ** eventTypeName **   <a name="FraudDetector-Type-ModelInputConfiguration-eventTypeName"></a>
The event type name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** format **   <a name="FraudDetector-Type-ModelInputConfiguration-format"></a>
 The format of the model input configuration. The format differs depending on if it is passed through to SageMaker or constructed by Amazon Fraud Detector.
Type: String
Valid Values: `TEXT_CSV | APPLICATION_JSON`
Required: No

 ** jsonInputTemplate **   <a name="FraudDetector-Type-ModelInputConfiguration-jsonInputTemplate"></a>
 Template for constructing the JSON input-data sent to SageMaker. At event-evaluation, the placeholders for variable names in the template will be replaced with the variable values before being sent to SageMaker.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

## See Also
<a name="API_ModelInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/ModelInputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/ModelInputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/ModelInputConfiguration)
