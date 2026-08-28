---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_InsightFeedback.html
---

# InsightFeedback
<a name="API_InsightFeedback"></a>

 Information about insight feedback received from a customer.

## Contents
<a name="API_InsightFeedback_Contents"></a>

 ** Feedback **   <a name="DevOpsGuru-Type-InsightFeedback-Feedback"></a>
 The feedback provided by the customer.
Type: String
Valid Values: `VALID_COLLECTION | RECOMMENDATION_USEFUL | ALERT_TOO_SENSITIVE | DATA_NOISY_ANOMALY | DATA_INCORRECT`
Required: No

 ** Id **   <a name="DevOpsGuru-Type-InsightFeedback-Id"></a>
 The insight feedback ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w-]*$`
Required: No

## See Also
<a name="API_InsightFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/InsightFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/InsightFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/InsightFeedback)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
