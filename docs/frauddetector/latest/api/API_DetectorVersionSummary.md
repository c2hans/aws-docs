---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_DetectorVersionSummary.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# DetectorVersionSummary
<a name="API_DetectorVersionSummary"></a>

The summary of the detector version.

## Contents
<a name="API_DetectorVersionSummary_Contents"></a>

 ** description **   <a name="FraudDetector-Type-DetectorVersionSummary-description"></a>
The detector version description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** detectorVersionId **   <a name="FraudDetector-Type-DetectorVersionSummary-detectorVersionId"></a>
The detector version ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^([1-9][0-9]*)$`
Required: No

 ** lastUpdatedTime **   <a name="FraudDetector-Type-DetectorVersionSummary-lastUpdatedTime"></a>
Timestamp of when the detector version was last updated.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** status **   <a name="FraudDetector-Type-DetectorVersionSummary-status"></a>
The detector version status.
Type: String
Valid Values: `DRAFT | ACTIVE | INACTIVE`
Required: No

## See Also
<a name="API_DetectorVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/DetectorVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/DetectorVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/DetectorVersionSummary)
