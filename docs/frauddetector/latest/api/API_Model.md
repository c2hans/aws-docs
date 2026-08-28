---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_Model.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# Model
<a name="API_Model"></a>

The model.

## Contents
<a name="API_Model_Contents"></a>

 ** arn **   <a name="FraudDetector-Type-Model-arn"></a>
The ARN of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`
Required: No

 ** createdTime **   <a name="FraudDetector-Type-Model-createdTime"></a>
Timestamp of when the model was created.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** description **   <a name="FraudDetector-Type-Model-description"></a>
The model description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** eventTypeName **   <a name="FraudDetector-Type-Model-eventTypeName"></a>
The name of the event type.
Type: String
Required: No

 ** lastUpdatedTime **   <a name="FraudDetector-Type-Model-lastUpdatedTime"></a>
Timestamp of last time the model was updated.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** modelId **   <a name="FraudDetector-Type-Model-modelId"></a>
The model ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_]+$`
Required: No

 ** modelType **   <a name="FraudDetector-Type-Model-modelType"></a>
The model type.
Type: String
Valid Values: `ONLINE_FRAUD_INSIGHTS | TRANSACTION_FRAUD_INSIGHTS | ACCOUNT_TAKEOVER_INSIGHTS`
Required: No

## See Also
<a name="API_Model_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/Model)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/Model)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/Model)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
