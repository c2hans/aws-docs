---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_TestRunEvent.html
---

# TestRunEvent
<a name="API_TestRunEvent"></a>

A single event in a test run's timeline.

## Contents
<a name="API_TestRunEvent_Contents"></a>

 ** eventId **   <a name="ngresiliencehub-Type-TestRunEvent-eventId"></a>
The unique identifier of the event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** eventType **   <a name="ngresiliencehub-Type-TestRunEvent-eventType"></a>
The type of the event, such as action\_started, action\_completed, or rto\_recovery\_detected.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** message **   <a name="ngresiliencehub-Type-TestRunEvent-message"></a>
A human-readable description of what happened.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** timestamp **   <a name="ngresiliencehub-Type-TestRunEvent-timestamp"></a>
The timestamp when the event occurred.
Type: Timestamp
Required: Yes

 ** attributes **   <a name="ngresiliencehub-Type-TestRunEvent-attributes"></a>
Machine-parseable key-value attributes for the event.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_TestRunEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/TestRunEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/TestRunEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/TestRunEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
