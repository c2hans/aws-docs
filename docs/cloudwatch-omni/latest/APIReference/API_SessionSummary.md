---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_SessionSummary.html
---

# SessionSummary
<a name="API_SessionSummary"></a>

Summary information about a query session, including its identifier, name, and activity timestamps.

## Contents
<a name="API_SessionSummary_Contents"></a>

 ** sessionId **   <a name="cloudwatchomni-Type-SessionSummary-sessionId"></a>
The unique ID of the session.
Type: String
Required: Yes

 ** createdAt **   <a name="cloudwatchomni-Type-SessionSummary-createdAt"></a>
The timestamp when the session was created.
Type: Timestamp
Required: No

 ** lastActivityAt **   <a name="cloudwatchomni-Type-SessionSummary-lastActivityAt"></a>
The timestamp of the most recent activity in the session.
Type: Timestamp
Required: No

 ** sessionName **   <a name="cloudwatchomni-Type-SessionSummary-sessionName"></a>
The human-readable name of the session. Names under `/aws/` are reserved for service integrations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `([a-zA-Z0-9_-]+|/aws/[a-zA-Z0-9_-]+(/[a-zA-Z0-9_-]+)?)`
Required: No

## See Also
<a name="API_SessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/SessionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/SessionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/SessionSummary)
