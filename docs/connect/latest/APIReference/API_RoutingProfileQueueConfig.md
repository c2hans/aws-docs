---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfileQueueConfig.html
---

# RoutingProfileQueueConfig
<a name="API_RoutingProfileQueueConfig"></a>

Contains information about the queue and channel for which priority and delay can be set.

## Contents
<a name="API_RoutingProfileQueueConfig_Contents"></a>

 ** Delay **   <a name="connect-Type-RoutingProfileQueueConfig-Delay"></a>
The delay, in seconds, a contact should be in the queue before they are routed to an available agent. For more information, see [Queues: priority and delay](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html) in the *Connect Customer Administrator Guide*.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 9999.
Required: Yes

 ** Priority **   <a name="connect-Type-RoutingProfileQueueConfig-Priority"></a>
The order in which contacts are to be handled for the queue. For more information, see [Queues: priority and delay](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 99.
Required: Yes

 ** QueueReference **   <a name="connect-Type-RoutingProfileQueueConfig-QueueReference"></a>
Contains information about a queue resource.
Type: [RoutingProfileQueueReference](API_RoutingProfileQueueReference.md) object
Required: Yes

## See Also
<a name="API_RoutingProfileQueueConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RoutingProfileQueueConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RoutingProfileQueueConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RoutingProfileQueueConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
