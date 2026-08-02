---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_EntityType.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# EntityType
<a name="API_EntityType"></a>

The entity type details.

## Contents
<a name="API_EntityType_Contents"></a>

 ** arn **   <a name="FraudDetector-Type-EntityType-arn"></a>
The entity type ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`
Required: No

 ** createdTime **   <a name="FraudDetector-Type-EntityType-createdTime"></a>
Timestamp of when the entity type was created.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** description **   <a name="FraudDetector-Type-EntityType-description"></a>
The entity type description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** lastUpdatedTime **   <a name="FraudDetector-Type-EntityType-lastUpdatedTime"></a>
Timestamp of when the entity type was last updated.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** name **   <a name="FraudDetector-Type-EntityType-name"></a>
The entity type name.
Type: String
Required: No

## See Also
<a name="API_EntityType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/EntityType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/EntityType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/EntityType)
