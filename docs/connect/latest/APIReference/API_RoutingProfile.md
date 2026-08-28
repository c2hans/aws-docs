---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html
---

# RoutingProfile
<a name="API_RoutingProfile"></a>

Contains information about a routing profile.

## Contents
<a name="API_RoutingProfile_Contents"></a>

 ** AgentAvailabilityTimer **   <a name="connect-Type-RoutingProfile-AgentAvailabilityTimer"></a>
Whether agents with this routing profile will have their routing order calculated based on *time since their last inbound contact* or *longest idle time*.
Type: String
Valid Values: `TIME_SINCE_LAST_ACTIVITY | TIME_SINCE_LAST_INBOUND`
Required: No

 ** AssociatedManualAssignmentQueueIds **   <a name="connect-Type-RoutingProfile-AssociatedManualAssignmentQueueIds"></a>
The IDs of the associated manual assignment queues.
Type: Array of strings
Required: No

 ** AssociatedQueueIds **   <a name="connect-Type-RoutingProfile-AssociatedQueueIds"></a>
The IDs of the associated queue.
Type: Array of strings
Required: No

 ** DefaultOutboundQueueId **   <a name="connect-Type-RoutingProfile-DefaultOutboundQueueId"></a>
The identifier of the default outbound queue for this routing profile.
Type: String
Required: No

 ** Description **   <a name="connect-Type-RoutingProfile-Description"></a>
The description of the routing profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** InstanceId **   <a name="connect-Type-RoutingProfile-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** IsDefault **   <a name="connect-Type-RoutingProfile-IsDefault"></a>
Whether this a default routing profile.
Type: Boolean
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-RoutingProfile-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-RoutingProfile-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** MediaConcurrencies **   <a name="connect-Type-RoutingProfile-MediaConcurrencies"></a>
The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.
Type: Array of [MediaConcurrency](API_MediaConcurrency.md) objects
Required: No

 ** Name **   <a name="connect-Type-RoutingProfile-Name"></a>
The name of the routing profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

 ** NumberOfAssociatedManualAssignmentQueues **   <a name="connect-Type-RoutingProfile-NumberOfAssociatedManualAssignmentQueues"></a>
The number of associated manual assignment queues in routing profile.
Type: Long
Required: No

 ** NumberOfAssociatedQueues **   <a name="connect-Type-RoutingProfile-NumberOfAssociatedQueues"></a>
The number of associated queues in routing profile.
Type: Long
Required: No

 ** NumberOfAssociatedUsers **   <a name="connect-Type-RoutingProfile-NumberOfAssociatedUsers"></a>
The number of associated users in routing profile.
Type: Long
Required: No

 ** RoutingProfileArn **   <a name="connect-Type-RoutingProfile-RoutingProfileArn"></a>
The Amazon Resource Name (ARN) of the routing profile.
Type: String
Required: No

 ** RoutingProfileId **   <a name="connect-Type-RoutingProfile-RoutingProfileId"></a>
The identifier of the routing profile.
Type: String
Required: No

 ** Tags **   <a name="connect-Type-RoutingProfile-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_RoutingProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RoutingProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RoutingProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RoutingProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
