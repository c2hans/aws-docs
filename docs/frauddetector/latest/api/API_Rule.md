---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_Rule.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# Rule
<a name="API_Rule"></a>

A rule.

## Contents
<a name="API_Rule_Contents"></a>

 ** detectorId **   <a name="FraudDetector-Type-Rule-detectorId"></a>
The detector for which the rule is associated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** ruleId **   <a name="FraudDetector-Type-Rule-ruleId"></a>
The rule ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: Yes

 ** ruleVersion **   <a name="FraudDetector-Type-Rule-ruleVersion"></a>
The rule version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^([1-9][0-9]*)$`
Required: Yes

## See Also
<a name="API_Rule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/Rule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/Rule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/Rule)
