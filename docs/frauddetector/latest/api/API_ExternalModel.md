---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_ExternalModel.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# ExternalModel
<a name="API_ExternalModel"></a>

The Amazon SageMaker model.

## Contents
<a name="API_ExternalModel_Contents"></a>

 ** arn **   <a name="FraudDetector-Type-ExternalModel-arn"></a>
The model ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`
Required: No

 ** createdTime **   <a name="FraudDetector-Type-ExternalModel-createdTime"></a>
Timestamp of when the model was last created.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** inputConfiguration **   <a name="FraudDetector-Type-ExternalModel-inputConfiguration"></a>
The input configuration.
Type: [ModelInputConfiguration](API_ModelInputConfiguration.md) object
Required: No

 ** invokeModelEndpointRoleArn **   <a name="FraudDetector-Type-ExternalModel-invokeModelEndpointRoleArn"></a>
The role used to invoke the model.
Type: String
Required: No

 ** lastUpdatedTime **   <a name="FraudDetector-Type-ExternalModel-lastUpdatedTime"></a>
Timestamp of when the model was last updated.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** modelEndpoint **   <a name="FraudDetector-Type-ExternalModel-modelEndpoint"></a>
The Amazon SageMaker model endpoints.
Type: String
Required: No

 ** modelEndpointStatus **   <a name="FraudDetector-Type-ExternalModel-modelEndpointStatus"></a>
The Amazon Fraud Detector status for the external model endpoint
Type: String
Valid Values: `ASSOCIATED | DISSOCIATED`
Required: No

 ** modelSource **   <a name="FraudDetector-Type-ExternalModel-modelSource"></a>
The source of the model.
Type: String
Valid Values: `SAGEMAKER`
Required: No

 ** outputConfiguration **   <a name="FraudDetector-Type-ExternalModel-outputConfiguration"></a>
The output configuration.
Type: [ModelOutputConfiguration](API_ModelOutputConfiguration.md) object
Required: No

## See Also
<a name="API_ExternalModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/ExternalModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/ExternalModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/ExternalModel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
