---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_StartPosition.html
---

# StartPosition
<a name="API_connect-participant_StartPosition"></a>

A filtering option for where to start. For example, if you sent 100 messages, start with message 50.

## Contents
<a name="API_connect-participant_StartPosition_Contents"></a>

 ** AbsoluteTime **   <a name="connect-Type-connect-participant_StartPosition-AbsoluteTime"></a>
The time in ISO format where to start.
It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Id **   <a name="connect-Type-connect-participant_StartPosition-Id"></a>
The ID of the message or event where to start.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** MostRecent **   <a name="connect-Type-connect-participant_StartPosition-MostRecent"></a>
The start position of the most recent message where you want to start.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## See Also
<a name="API_connect-participant_StartPosition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/StartPosition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/StartPosition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/StartPosition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
