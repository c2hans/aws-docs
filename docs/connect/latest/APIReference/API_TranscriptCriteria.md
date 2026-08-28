---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TranscriptCriteria.html
---

# TranscriptCriteria
<a name="API_TranscriptCriteria"></a>

A structure that defines search criteria base on words or phrases, participants in the Contact Lens conversational analytics transcript.

## Contents
<a name="API_TranscriptCriteria_Contents"></a>

 ** MatchType **   <a name="connect-Type-TranscriptCriteria-MatchType"></a>
The match type combining search criteria using multiple search texts in a transcript criteria.
Type: String
Valid Values: `MATCH_ALL | MATCH_ANY | MATCH_EXACT | MATCH_NONE`
Required: Yes

 ** ParticipantRole **   <a name="connect-Type-TranscriptCriteria-ParticipantRole"></a>
The participant role in a transcript
Type: String
Valid Values: `AGENT | CUSTOMER | SYSTEM | CUSTOM_BOT | SUPERVISOR`
Required: Yes

 ** SearchText **   <a name="connect-Type-TranscriptCriteria-SearchText"></a>
The words or phrases used to search within a transcript.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Maximum length of 128.
Required: Yes

## See Also
<a name="API_TranscriptCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TranscriptCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TranscriptCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TranscriptCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
