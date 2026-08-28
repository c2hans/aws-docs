---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CardValue.html
---

# CardValue
<a name="API_qapps_CardValue"></a>

The value or result associated with a card in a Amazon Q App session.

## Contents
<a name="API_qapps_CardValue_Contents"></a>

 ** cardId **   <a name="qbusiness-Type-qapps_CardValue-cardId"></a>
The unique identifier of the card.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** value **   <a name="qbusiness-Type-qapps_CardValue-value"></a>
The value or result associated with the card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40000.
Required: Yes

 ** submissionMutation **   <a name="qbusiness-Type-qapps_CardValue-submissionMutation"></a>
The structure that describes how the current form card value is mutated. Only applies for form cards when multiple responses are allowed.
Type: [SubmissionMutation](API_qapps_SubmissionMutation.md) object
Required: No

## See Also
<a name="API_qapps_CardValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/CardValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/CardValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/CardValue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
