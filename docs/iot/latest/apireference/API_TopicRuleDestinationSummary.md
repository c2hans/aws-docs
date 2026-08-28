---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_TopicRuleDestinationSummary.html
---

# TopicRuleDestinationSummary
<a name="API_TopicRuleDestinationSummary"></a>

Information about the topic rule destination.

## Contents
<a name="API_TopicRuleDestinationSummary_Contents"></a>

 ** arn **   <a name="iot-Type-TopicRuleDestinationSummary-arn"></a>
The topic rule destination ARN.
Type: String
Required: No

 ** createdAt **   <a name="iot-Type-TopicRuleDestinationSummary-createdAt"></a>
The date and time when the topic rule destination was created.
Type: Timestamp
Required: No

 ** httpUrlSummary **   <a name="iot-Type-TopicRuleDestinationSummary-httpUrlSummary"></a>
Information about the HTTP URL.
Type: [HttpUrlDestinationSummary](API_HttpUrlDestinationSummary.md) object
Required: No

 ** lastUpdatedAt **   <a name="iot-Type-TopicRuleDestinationSummary-lastUpdatedAt"></a>
The date and time when the topic rule destination was last updated.
Type: Timestamp
Required: No

 ** status **   <a name="iot-Type-TopicRuleDestinationSummary-status"></a>
The status of the topic rule destination. Valid values are:
IN\_PROGRESS
A topic rule destination was created but has not been confirmed. You can set `status` to `IN_PROGRESS` by calling `UpdateTopicRuleDestination`. Calling `UpdateTopicRuleDestination` causes a new confirmation challenge to be sent to your confirmation endpoint.
ENABLED
Confirmation was completed, and traffic to this destination is allowed. You can set `status` to `DISABLED` by calling `UpdateTopicRuleDestination`.
DISABLED
Confirmation was completed, and traffic to this destination is not allowed. You can set `status` to `ENABLED` by calling `UpdateTopicRuleDestination`.
ERROR
Confirmation could not be completed, for example if the confirmation timed out. You can call `GetTopicRuleDestination` for details about the error. You can set `status` to `IN_PROGRESS` by calling `UpdateTopicRuleDestination`. Calling `UpdateTopicRuleDestination` causes a new confirmation challenge to be sent to your confirmation endpoint.
Type: String
Valid Values: `ENABLED | IN_PROGRESS | DISABLED | ERROR | DELETING`
Required: No

 ** statusReason **   <a name="iot-Type-TopicRuleDestinationSummary-statusReason"></a>
The reason the topic rule destination is in the current status.
Type: String
Required: No

 ** vpcDestinationSummary **   <a name="iot-Type-TopicRuleDestinationSummary-vpcDestinationSummary"></a>
Information about the virtual private cloud (VPC) connection.
Type: [VpcDestinationSummary](API_VpcDestinationSummary.md) object
Required: No

## See Also
<a name="API_TopicRuleDestinationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/TopicRuleDestinationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/TopicRuleDestinationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/TopicRuleDestinationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
