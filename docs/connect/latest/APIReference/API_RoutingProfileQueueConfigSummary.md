---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfileQueueConfigSummary.html
---

# RoutingProfileQueueConfigSummary
<a name="API_RoutingProfileQueueConfigSummary"></a>

Contains summary information about a routing profile queue.

## Contents
<a name="API_RoutingProfileQueueConfigSummary_Contents"></a>

 ** Channel **   <a name="connect-Type-RoutingProfileQueueConfigSummary-Channel"></a>
The channels this queue supports.
Type: String
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: Yes

 ** Delay **   <a name="connect-Type-RoutingProfileQueueConfigSummary-Delay"></a>
The delay, in seconds, that a contact should be in the queue before they are routed to an available agent. For more information, see [Queues: priority and delay](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html) in the *Connect Customer Administrator Guide*.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 9999.
Required: Yes

 ** Priority **   <a name="connect-Type-RoutingProfileQueueConfigSummary-Priority"></a>
The order in which contacts are to be handled for the queue. For more information, see [Queues: priority and delay](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 99.
Required: Yes

 ** QueueArn **   <a name="connect-Type-RoutingProfileQueueConfigSummary-QueueArn"></a>
The Amazon Resource Name (ARN) of the queue.
Type: String
Required: Yes

 ** QueueId **   <a name="connect-Type-RoutingProfileQueueConfigSummary-QueueId"></a>
The identifier for the queue.
Type: String
Required: Yes

 ** QueueName **   <a name="connect-Type-RoutingProfileQueueConfigSummary-QueueName"></a>
The name of the queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_RoutingProfileQueueConfigSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RoutingProfileQueueConfigSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RoutingProfileQueueConfigSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RoutingProfileQueueConfigSummary)
