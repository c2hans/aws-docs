---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_UncertaintyRange.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# UncertaintyRange
<a name="API_UncertaintyRange"></a>

 Range of area under curve (auc) expected from the model. A range greater than 0.1 indicates higher model uncertainity. A range is the difference between upper and lower bound of auc.

## Contents
<a name="API_UncertaintyRange_Contents"></a>

 ** lowerBoundValue **   <a name="FraudDetector-Type-UncertaintyRange-lowerBoundValue"></a>
 The lower bound value of the area under curve (auc).
Type: Float
Required: Yes

 ** upperBoundValue **   <a name="FraudDetector-Type-UncertaintyRange-upperBoundValue"></a>
 The upper bound value of the area under curve (auc).
Type: Float
Required: Yes

## See Also
<a name="API_UncertaintyRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/UncertaintyRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/UncertaintyRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/UncertaintyRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
