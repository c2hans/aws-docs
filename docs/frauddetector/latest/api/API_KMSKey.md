---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_KMSKey.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# KMSKey
<a name="API_KMSKey"></a>

The KMS key details.

## Contents
<a name="API_KMSKey_Contents"></a>

 ** kmsEncryptionKeyArn **   <a name="FraudDetector-Type-KMSKey-kmsEncryptionKeyArn"></a>
The encryption key ARN.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 90.
Pattern: `^DEFAULT|arn:[a-zA-Z0-9-]+:kms:[a-zA-Z0-9-]+:\d{12}:key\/\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$`
Required: No

## See Also
<a name="API_KMSKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/KMSKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/KMSKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/KMSKey)
