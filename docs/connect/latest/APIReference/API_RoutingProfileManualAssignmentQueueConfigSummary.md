---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfileManualAssignmentQueueConfigSummary.html
---

# RoutingProfileManualAssignmentQueueConfigSummary
<a name="API_RoutingProfileManualAssignmentQueueConfigSummary"></a>

Contains summary information about a routing profile manual assignment queue.

## Contents
<a name="API_RoutingProfileManualAssignmentQueueConfigSummary_Contents"></a>

 ** Channel **   <a name="connect-Type-RoutingProfileManualAssignmentQueueConfigSummary-Channel"></a>
The channels this queue supports. Valid Values: CHAT \| TASK \| EMAIL
VOICE is not supported. The information shown below is incorrect. We're working to correct it.
Type: String
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: Yes

 ** QueueArn **   <a name="connect-Type-RoutingProfileManualAssignmentQueueConfigSummary-QueueArn"></a>
The Amazon Resource Name (ARN) of the queue.
Type: String
Required: Yes

 ** QueueId **   <a name="connect-Type-RoutingProfileManualAssignmentQueueConfigSummary-QueueId"></a>
The identifier for the queue.
Type: String
Required: Yes

 ** QueueName **   <a name="connect-Type-RoutingProfileManualAssignmentQueueConfigSummary-QueueName"></a>
The name of the queue.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_RoutingProfileManualAssignmentQueueConfigSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RoutingProfileManualAssignmentQueueConfigSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RoutingProfileManualAssignmentQueueConfigSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RoutingProfileManualAssignmentQueueConfigSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
