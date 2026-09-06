---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_ModelVersionDetail.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# ModelVersionDetail
<a name="API_ModelVersionDetail"></a>

The details of the model version.

## Contents
<a name="API_ModelVersionDetail_Contents"></a>

 ** arn **   <a name="FraudDetector-Type-ModelVersionDetail-arn"></a>
The model version ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`
Required: No

 ** createdTime **   <a name="FraudDetector-Type-ModelVersionDetail-createdTime"></a>
The timestamp when the model was created.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** externalEventsDetail **   <a name="FraudDetector-Type-ModelVersionDetail-externalEventsDetail"></a>
The external events data details. This will be populated if the `trainingDataSource` for the model version is specified as `EXTERNAL_EVENTS`.
Type: [ExternalEventsDetail](API_ExternalEventsDetail.md) object
Required: No

 ** ingestedEventsDetail **   <a name="FraudDetector-Type-ModelVersionDetail-ingestedEventsDetail"></a>
The ingested events data details. This will be populated if the `trainingDataSource` for the model version is specified as `INGESTED_EVENTS`.
Type: [IngestedEventsDetail](API_IngestedEventsDetail.md) object
Required: No

 ** lastUpdatedTime **   <a name="FraudDetector-Type-ModelVersionDetail-lastUpdatedTime"></a>
The timestamp when the model was last updated.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** modelId **   <a name="FraudDetector-Type-ModelVersionDetail-modelId"></a>
The model ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_]+$`
Required: No

 ** modelType **   <a name="FraudDetector-Type-ModelVersionDetail-modelType"></a>
The model type.
Type: String
Valid Values: `ONLINE_FRAUD_INSIGHTS | TRANSACTION_FRAUD_INSIGHTS | ACCOUNT_TAKEOVER_INSIGHTS`
Required: No

 ** modelVersionNumber **   <a name="FraudDetector-Type-ModelVersionDetail-modelVersionNumber"></a>
The model version number.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 7.
Pattern: `^[1-9][0-9]{0,3}\.[0-9]{1,2}$`
Required: No

 ** status **   <a name="FraudDetector-Type-ModelVersionDetail-status"></a>
The status of the model version.
Type: String
Required: No

 ** trainingDataSchema **   <a name="FraudDetector-Type-ModelVersionDetail-trainingDataSchema"></a>
The training data schema.
Type: [TrainingDataSchema](API_TrainingDataSchema.md) object
Required: No

 ** trainingDataSource **   <a name="FraudDetector-Type-ModelVersionDetail-trainingDataSource"></a>
The model version training data source.
Type: String
Valid Values: `EXTERNAL_EVENTS | INGESTED_EVENTS`
Required: No

 ** trainingResult **   <a name="FraudDetector-Type-ModelVersionDetail-trainingResult"></a>
The training results.
Type: [TrainingResult](API_TrainingResult.md) object
Required: No

 ** trainingResultV2 **   <a name="FraudDetector-Type-ModelVersionDetail-trainingResultV2"></a>
 The training result details. The details include the relative importance of the variables.
Type: [TrainingResultV2](API_TrainingResultV2.md) object
Required: No

## See Also
<a name="API_ModelVersionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/ModelVersionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/ModelVersionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/ModelVersionDetail)
