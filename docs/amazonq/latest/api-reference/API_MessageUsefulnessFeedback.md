---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_MessageUsefulnessFeedback.html
---

# MessageUsefulnessFeedback
<a name="API_MessageUsefulnessFeedback"></a>

End user feedback on an AI-generated web experience chat message usefulness.

## Contents
<a name="API_MessageUsefulnessFeedback_Contents"></a>

 ** submittedAt **   <a name="qbusiness-Type-MessageUsefulnessFeedback-submittedAt"></a>
The timestamp for when the feedback was submitted.
Type: Timestamp
Required: Yes

 ** usefulness **   <a name="qbusiness-Type-MessageUsefulnessFeedback-usefulness"></a>
The usefulness value assigned by an end user to a message.
Type: String
Valid Values: `USEFUL | NOT_USEFUL`
Required: Yes

 ** comment **   <a name="qbusiness-Type-MessageUsefulnessFeedback-comment"></a>
A comment given by an end user on the usefulness of an AI-generated chat message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `\P{C}*`
Required: No

 ** reason **   <a name="qbusiness-Type-MessageUsefulnessFeedback-reason"></a>
The reason for a usefulness rating.
Type: String
Valid Values: `NOT_FACTUALLY_CORRECT | HARMFUL_OR_UNSAFE | INCORRECT_OR_MISSING_SOURCES | NOT_HELPFUL | FACTUALLY_CORRECT | COMPLETE | RELEVANT_SOURCES | HELPFUL | NOT_BASED_ON_DOCUMENTS | NOT_COMPLETE | NOT_CONCISE | OTHER`
Required: No

## See Also
<a name="API_MessageUsefulnessFeedback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/MessageUsefulnessFeedback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/MessageUsefulnessFeedback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/MessageUsefulnessFeedback)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
