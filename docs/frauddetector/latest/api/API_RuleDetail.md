---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_RuleDetail.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# RuleDetail
<a name="API_RuleDetail"></a>

The details of the rule.

## Contents
<a name="API_RuleDetail_Contents"></a>

 ** arn **   <a name="FraudDetector-Type-RuleDetail-arn"></a>
The rule ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`
Required: No

 ** createdTime **   <a name="FraudDetector-Type-RuleDetail-createdTime"></a>
The timestamp of when the rule was created.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** description **   <a name="FraudDetector-Type-RuleDetail-description"></a>
The rule description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** detectorId **   <a name="FraudDetector-Type-RuleDetail-detectorId"></a>
The detector for which the rule is associated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** expression **   <a name="FraudDetector-Type-RuleDetail-expression"></a>
The rule expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** language **   <a name="FraudDetector-Type-RuleDetail-language"></a>
The rule language.
Type: String
Valid Values: `DETECTORPL`
Required: No

 ** lastUpdatedTime **   <a name="FraudDetector-Type-RuleDetail-lastUpdatedTime"></a>
Timestamp of the last time the rule was updated.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** outcomes **   <a name="FraudDetector-Type-RuleDetail-outcomes"></a>
The rule outcomes.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

 ** ruleId **   <a name="FraudDetector-Type-RuleDetail-ruleId"></a>
The rule ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** ruleVersion **   <a name="FraudDetector-Type-RuleDetail-ruleVersion"></a>
The rule version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^([1-9][0-9]*)$`
Required: No

## See Also
<a name="API_RuleDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/RuleDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/RuleDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/RuleDetail)
