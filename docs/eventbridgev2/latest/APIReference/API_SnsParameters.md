---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_SnsParameters.html
---

# SnsParameters
<a name="API_SnsParameters"></a>

SNS invocation parameters for subscribers. Values are forwarded to the SNS PublishBatch API. All scalar values accept a literal or a JSONata expression (e.g. "{% $events.Data.groupId %}").

## Contents
<a name="API_SnsParameters_Contents"></a>

 ** MessageAttributes **   <a name="eventbridgev2-Type-SnsParameters-MessageAttributes"></a>
Custom message attributes for SNS filtering.
Type: String to [SnsMessageAttributeValue](API_SnsMessageAttributeValue.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** MessageDeduplicationId **   <a name="eventbridgev2-Type-SnsParameters-MessageDeduplicationId"></a>
Message deduplication ID for FIFO topics. Accepts JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** MessageGroupId **   <a name="eventbridgev2-Type-SnsParameters-MessageGroupId"></a>
Message group ID for FIFO topics. Accepts JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** MessageStructure **   <a name="eventbridgev2-Type-SnsParameters-MessageStructure"></a>
Per-protocol message formatting mode, forwarded to SNS Publish unchanged. Accepts JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** Subject **   <a name="eventbridgev2-Type-SnsParameters-Subject"></a>
Subject line for email protocol subscriptions. Accepts JSONata expression.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

## See Also
<a name="API_SnsParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/SnsParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/SnsParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/SnsParameters)
