---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationAcknowledgementSummary.html
---

# EvaluationAcknowledgementSummary
<a name="API_EvaluationAcknowledgementSummary"></a>

Summary information about an evaluation acknowledgement.

## Contents
<a name="API_EvaluationAcknowledgementSummary_Contents"></a>

 ** AcknowledgedBy **   <a name="connect-Type-EvaluationAcknowledgementSummary-AcknowledgedBy"></a>
The agent who acknowledged the evaluation.
Type: String
Required: No

 ** AcknowledgedTime **   <a name="connect-Type-EvaluationAcknowledgementSummary-AcknowledgedTime"></a>
The time when an agent acknowledged the evaluation.
Type: Timestamp
Required: No

 ** AcknowledgerComment **   <a name="connect-Type-EvaluationAcknowledgementSummary-AcknowledgerComment"></a>
A comment from the agent when they confirmed they acknowledged the evaluation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Required: No

## See Also
<a name="API_EvaluationAcknowledgementSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationAcknowledgementSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationAcknowledgementSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationAcknowledgementSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
