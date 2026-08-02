---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_TopicRuleDestination.html
---

# TopicRuleDestination
<a name="API_TopicRuleDestination"></a>

A topic rule destination.

## Contents
<a name="API_TopicRuleDestination_Contents"></a>

 ** arn **   <a name="iot-Type-TopicRuleDestination-arn"></a>
The topic rule destination URL.
Type: String
Required: No

 ** createdAt **   <a name="iot-Type-TopicRuleDestination-createdAt"></a>
The date and time when the topic rule destination was created.
Type: Timestamp
Required: No

 ** httpUrlProperties **   <a name="iot-Type-TopicRuleDestination-httpUrlProperties"></a>
Properties of the HTTP URL.
Type: [HttpUrlDestinationProperties](API_HttpUrlDestinationProperties.md) object
Required: No

 ** lastUpdatedAt **   <a name="iot-Type-TopicRuleDestination-lastUpdatedAt"></a>
The date and time when the topic rule destination was last updated.
Type: Timestamp
Required: No

 ** status **   <a name="iot-Type-TopicRuleDestination-status"></a>
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

 ** statusReason **   <a name="iot-Type-TopicRuleDestination-statusReason"></a>
Additional details or reason why the topic rule destination is in the current status.
Type: String
Required: No

 ** vpcProperties **   <a name="iot-Type-TopicRuleDestination-vpcProperties"></a>
Properties of the virtual private cloud (VPC) connection.
Type: [VpcDestinationProperties](API_VpcDestinationProperties.md) object
Required: No

## See Also
<a name="API_TopicRuleDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/TopicRuleDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/TopicRuleDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/TopicRuleDestination)
