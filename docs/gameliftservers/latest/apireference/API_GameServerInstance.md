---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameServerInstance.html
---

# GameServerInstance
<a name="API_GameServerInstance"></a>

 Additional properties, including status, that describe an EC2 instance in a game server group. Instance configurations are set with game server group properties (see `DescribeGameServerGroup` and with the EC2 launch template that was used when creating the game server group.

Retrieve game server instances for a game server group by calling `DescribeGameServerInstances`.

## Contents
<a name="API_GameServerInstance_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** GameServerGroupArn **   <a name="gameliftservers-Type-GameServerInstance-GameServerGroupArn"></a>
A generated unique identifier for the game server group that includes the game server instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]*`
Required: No

 ** GameServerGroupName **   <a name="gameliftservers-Type-GameServerInstance-GameServerGroupName"></a>
A developer-defined identifier for the game server group that includes the game server instance. The name is unique for each Region in each AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]+`
Required: No

 ** InstanceId **   <a name="gameliftservers-Type-GameServerInstance-InstanceId"></a>
The unique identifier for the instance where the game server is running. This ID is available in the instance metadata. EC2 instance IDs use a 17-character format, for example: `i-1234567890abcdef0`.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `^i-[0-9a-zA-Z]{17}$`
Required: No

 ** InstanceStatus **   <a name="gameliftservers-Type-GameServerInstance-InstanceStatus"></a>
Current status of the game server instance
Type: String
Valid Values: `ACTIVE | DRAINING | SPOT_TERMINATING`
Required: No

## See Also
<a name="API_GameServerInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GameServerInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GameServerInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GameServerInstance)
