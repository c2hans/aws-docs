---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_Detector.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# Detector
<a name="API_Detector"></a>

The detector.

## Contents
<a name="API_Detector_Contents"></a>

 ** arn **   <a name="FraudDetector-Type-Detector-arn"></a>
The detector ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`
Required: No

 ** createdTime **   <a name="FraudDetector-Type-Detector-createdTime"></a>
Timestamp of when the detector was created.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** description **   <a name="FraudDetector-Type-Detector-description"></a>
The detector description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** detectorId **   <a name="FraudDetector-Type-Detector-detectorId"></a>
The detector ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** eventTypeName **   <a name="FraudDetector-Type-Detector-eventTypeName"></a>
The name of the event type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** lastUpdatedTime **   <a name="FraudDetector-Type-Detector-lastUpdatedTime"></a>
Timestamp of when the detector was last updated.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

## See Also
<a name="API_Detector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/Detector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/Detector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/Detector)
