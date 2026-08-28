---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_Entity.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# Entity
<a name="API_Entity"></a>

The entity details.

## Contents
<a name="API_Entity_Contents"></a>

 ** entityId **   <a name="FraudDetector-Type-Entity-entityId"></a>
The entity ID. If you do not know the `entityId`, you can pass `unknown`, which is areserved string literal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[0-9A-Za-z_.@+-]+$`
Required: Yes

 ** entityType **   <a name="FraudDetector-Type-Entity-entityType"></a>
The entity type.
Type: String
Required: Yes

## See Also
<a name="API_Entity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/Entity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/Entity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/Entity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
