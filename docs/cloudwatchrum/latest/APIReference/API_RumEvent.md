---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_RumEvent.html
---

# RumEvent
<a name="API_RumEvent"></a>

A structure that contains the information for one performance event that RUM collects from a user session with your application.

## Contents
<a name="API_RumEvent_Contents"></a>

 ** details **   <a name="cloudwatchrum-Type-RumEvent-details"></a>
A string containing details about the event.
Type: String
Required: Yes

 ** id **   <a name="cloudwatchrum-Type-RumEvent-id"></a>
A unique ID for this event.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: Yes

 ** timestamp **   <a name="cloudwatchrum-Type-RumEvent-timestamp"></a>
The exact time that this event occurred.
Type: Timestamp
Required: Yes

 ** type **   <a name="cloudwatchrum-Type-RumEvent-type"></a>
The JSON schema that denotes the type of event this is, such as a page load or a new session.
Type: String
Required: Yes

 ** metadata **   <a name="cloudwatchrum-Type-RumEvent-metadata"></a>
Metadata about this event, which contains a JSON serialization of the identity of the user for this session. The user information comes from information such as the HTTP user-agent request header and document interface.
Type: String
Required: No

## See Also
<a name="API_RumEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/RumEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/RumEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/RumEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch RUM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchrum` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
