---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CardStatus.html
---

# CardStatus
<a name="API_qapps_CardStatus"></a>

The current status and value of a card in an active Amazon Q App session.

## Contents
<a name="API_qapps_CardStatus_Contents"></a>

 ** currentState **   <a name="qbusiness-Type-qapps_CardStatus-currentState"></a>
The current state of the card.
Type: String
Valid Values: `IN_PROGRESS | WAITING | COMPLETED | ERROR`
Required: Yes

 ** currentValue **   <a name="qbusiness-Type-qapps_CardStatus-currentValue"></a>
The current value or result associated with the card.
Type: String
Required: Yes

 ** submissions **   <a name="qbusiness-Type-qapps_CardStatus-submissions"></a>
A list of previous submissions, if the card is a form card.
Type: Array of [Submission](API_qapps_Submission.md) objects
Required: No

## See Also
<a name="API_qapps_CardStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/CardStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/CardStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/CardStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
