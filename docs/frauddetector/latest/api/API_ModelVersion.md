---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_ModelVersion.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# ModelVersion
<a name="API_ModelVersion"></a>

The model version.

## Contents
<a name="API_ModelVersion_Contents"></a>

 ** modelId **   <a name="FraudDetector-Type-ModelVersion-modelId"></a>
The model ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_]+$`
Required: Yes

 ** modelType **   <a name="FraudDetector-Type-ModelVersion-modelType"></a>
The model type.
Type: String
Valid Values: `ONLINE_FRAUD_INSIGHTS | TRANSACTION_FRAUD_INSIGHTS | ACCOUNT_TAKEOVER_INSIGHTS`
Required: Yes

 ** modelVersionNumber **   <a name="FraudDetector-Type-ModelVersion-modelVersionNumber"></a>
The model version number.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 7.
Pattern: `^[1-9][0-9]{0,3}\.[0-9]{1,2}$`
Required: Yes

 ** arn **   <a name="FraudDetector-Type-ModelVersion-arn"></a>
The model version ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`
Required: No

## See Also
<a name="API_ModelVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/ModelVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/ModelVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/ModelVersion)
