---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameServerGroup.html
---

# GameServerGroup
<a name="API_GameServerGroup"></a>

Properties that describe a game server group resource. A game server group manages certain properties related to a corresponding Amazon EC2 Auto Scaling group.

A game server group is created by a successful call to `CreateGameServerGroup` and deleted by calling `DeleteGameServerGroup`. Game server group activity can be temporarily suspended and resumed by calling `SuspendGameServerGroup` and `ResumeGameServerGroup`, respectively.

## Contents
<a name="API_GameServerGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AutoScalingGroupArn **   <a name="gameliftservers-Type-GameServerGroup-AutoScalingGroupArn"></a>
A generated unique ID for the Amazon EC2 Auto Scaling group that is associated with this game server group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** BalancingStrategy **   <a name="gameliftservers-Type-GameServerGroup-BalancingStrategy"></a>
Indicates how Amazon GameLift Servers FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group. Method options include the following:
+  `SPOT_ONLY` - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced.
+  `SPOT_PREFERRED` - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances.
+  `ON_DEMAND_ONLY` - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.
Type: String
Valid Values: `SPOT_ONLY | SPOT_PREFERRED | ON_DEMAND_ONLY`
Required: No

 ** CreationTime **   <a name="gameliftservers-Type-GameServerGroup-CreationTime"></a>
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** GameServerGroupArn **   <a name="gameliftservers-Type-GameServerGroup-GameServerGroupArn"></a>
A generated unique ID for the game server group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]*`
Required: No

 ** GameServerGroupName **   <a name="gameliftservers-Type-GameServerGroup-GameServerGroupName"></a>
A developer-defined identifier for the game server group. The name is unique for each Region in each AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]+`
Required: No

 ** GameServerProtectionPolicy **   <a name="gameliftservers-Type-GameServerGroup-GameServerProtectionPolicy"></a>
A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see ). An exception to this is with Spot Instances, which can be terminated by AWS regardless of protection status.
Type: String
Valid Values: `NO_PROTECTION | FULL_PROTECTION`
Required: No

 ** InstanceDefinitions **   <a name="gameliftservers-Type-GameServerGroup-InstanceDefinitions"></a>
The set of Amazon EC2 instance types that Amazon GameLift Servers FleetIQ can use when balancing and automatically scaling instances in the corresponding Auto Scaling group.
Type: Array of [InstanceDefinition](API_InstanceDefinition.md) objects
Array Members: Minimum number of 2 items. Maximum number of 20 items.
Required: No

 ** LastUpdatedTime **   <a name="gameliftservers-Type-GameServerGroup-LastUpdatedTime"></a>
A timestamp that indicates when this game server group was last updated.
Type: Timestamp
Required: No

 ** RoleArn **   <a name="gameliftservers-Type-GameServerGroup-RoleArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) for an IAM role that allows Amazon GameLift Servers to access your Amazon EC2 Auto Scaling groups.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:.*:role\/[\w+=,.@-]+`
Required: No

 ** Status **   <a name="gameliftservers-Type-GameServerGroup-Status"></a>
The current status of the game server group. Possible statuses include:
+  `NEW` - Amazon GameLift Servers FleetIQ has validated the `CreateGameServerGroup()` request.
+  `ACTIVATING` - Amazon GameLift Servers FleetIQ is setting up a game server group, which includes creating an Auto Scaling group in your AWS account.
+  `ACTIVE` - The game server group has been successfully created.
+  `DELETE_SCHEDULED` - A request to delete the game server group has been received.
+  `DELETING` - Amazon GameLift Servers FleetIQ has received a valid `DeleteGameServerGroup()` request and is processing it. Amazon GameLift Servers FleetIQ must first complete and release hosts before it deletes the Auto Scaling group and the game server group.
+  `DELETED` - The game server group has been successfully deleted.
+  `ERROR` - The asynchronous processes of activating or deleting a game server group has failed, resulting in an error state.
Type: String
Valid Values: `NEW | ACTIVATING | ACTIVE | DELETE_SCHEDULED | DELETING | DELETED | ERROR`
Required: No

 ** StatusReason **   <a name="gameliftservers-Type-GameServerGroup-StatusReason"></a>
Additional information about the current game server group status. This information might provide additional insight on groups that are in `ERROR` status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** SuspendedActions **   <a name="gameliftservers-Type-GameServerGroup-SuspendedActions"></a>
A list of activities that are currently suspended for this game server group. If this property is empty, all activities are occurring.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `REPLACE_INSTANCE_TYPES`
Required: No

## See Also
<a name="API_GameServerGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GameServerGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GameServerGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GameServerGroup)
