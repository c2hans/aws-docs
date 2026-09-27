---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_SqsParameters.html
---

# SqsParameters
<a name="API_SqsParameters"></a>

SQS invocation parameters for subscribers. Values are forwarded to the SQS SendMessageBatch API. All scalar values accept a literal or a JSONata expression (e.g. "{% $events.Data.groupId %}").

## Contents
<a name="API_SqsParameters_Contents"></a>

 ** DelaySeconds **   <a name="eventbridgev2-Type-SqsParameters-DelaySeconds"></a>
Delay in seconds before the message becomes visible, standard queues only. Accepts JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** MessageAttributes **   <a name="eventbridgev2-Type-SqsParameters-MessageAttributes"></a>
Custom message attributes (name/type/value).
Type: String to [SqsMessageAttributeValue](API_SqsMessageAttributeValue.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** MessageDeduplicationId **   <a name="eventbridgev2-Type-SqsParameters-MessageDeduplicationId"></a>
Message deduplication ID for FIFO queues. Accepts JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** MessageGroupId **   <a name="eventbridgev2-Type-SqsParameters-MessageGroupId"></a>
Message group ID for FIFO queues. Accepts JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** MessageSystemAttributes **   <a name="eventbridgev2-Type-SqsParameters-MessageSystemAttributes"></a>
System message attributes (e.g., AWSTraceHeader).
Type: String to [SqsMessageAttributeValue](API_SqsMessageAttributeValue.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

## See Also
<a name="API_SqsParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/SqsParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/SqsParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/SqsParameters)
