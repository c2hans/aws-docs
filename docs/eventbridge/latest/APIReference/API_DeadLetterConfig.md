---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeadLetterConfig.html
---

# DeadLetterConfig
<a name="API_DeadLetterConfig"></a>

Configuration details of the Amazon SQS queue for EventBridge to use as a dead-letter queue (DLQ).

For more information, see [Using dead-letter queues to process undelivered events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-event-delivery.html#eb-rule-dlq) in the *EventBridge User Guide*.

## Contents
<a name="API_DeadLetterConfig_Contents"></a>

 ** Arn **   <a name="eventbridge-Type-DeadLetterConfig-Arn"></a>
The ARN of the SQS queue specified as the target for the dead-letter queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

## See Also
<a name="API_DeadLetterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/DeadLetterConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DeadLetterConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/DeadLetterConfig)
