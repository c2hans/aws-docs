---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_EvaluatedRule.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# EvaluatedRule
<a name="API_EvaluatedRule"></a>

 The details of the rule used for evaluating variable values.

## Contents
<a name="API_EvaluatedRule_Contents"></a>

 ** evaluated **   <a name="FraudDetector-Type-EvaluatedRule-evaluated"></a>
 Indicates whether the rule was evaluated.
Type: Boolean
Required: No

 ** expression **   <a name="FraudDetector-Type-EvaluatedRule-expression"></a>
 The rule expression.
Type: String
Required: No

 ** expressionWithValues **   <a name="FraudDetector-Type-EvaluatedRule-expressionWithValues"></a>
 The rule expression value.
Type: String
Required: No

 ** matched **   <a name="FraudDetector-Type-EvaluatedRule-matched"></a>
 Indicates whether the rule matched.
Type: Boolean
Required: No

 ** outcomes **   <a name="FraudDetector-Type-EvaluatedRule-outcomes"></a>
 The rule outcome.
Type: Array of strings
Required: No

 ** ruleId **   <a name="FraudDetector-Type-EvaluatedRule-ruleId"></a>
 The rule ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** ruleVersion **   <a name="FraudDetector-Type-EvaluatedRule-ruleVersion"></a>
 The rule version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^([1-9][0-9]*)$`
Required: No

## See Also
<a name="API_EvaluatedRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/EvaluatedRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/EvaluatedRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/EvaluatedRule)
