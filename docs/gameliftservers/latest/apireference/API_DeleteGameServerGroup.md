---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeleteGameServerGroup.html
---

# DeleteGameServerGroup
<a name="API_DeleteGameServerGroup"></a>

 **This API works with the following fleet types:** EC2 (FleetIQ)

Terminates a game server group and permanently deletes the game server group record. You have several options for how these resources are impacted when deleting the game server group. Depending on the type of delete operation selected, this operation might affect these resources:
+ The game server group
+ The corresponding Auto Scaling group
+ All game servers that are currently running in the group

To delete a game server group, identify the game server group to delete and specify the type of delete operation to initiate. Game server groups can only be deleted if they are in `ACTIVE` or `ERROR` status.

If the delete request is successful, a series of operations are kicked off. The game server group status is changed to `DELETE_SCHEDULED`, which prevents new game servers from being registered and stops automatic scaling activity. Once all game servers in the game server group are deregistered, Amazon GameLift Servers FleetIQ can begin deleting resources. If any of the delete operations fail, the game server group is placed in `ERROR` status.

Amazon GameLift Servers FleetIQ emits delete events to Amazon CloudWatch.

 **Learn more**

 [Amazon GameLift Servers FleetIQ Guide](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html)

## Request Syntax
<a name="API_DeleteGameServerGroup_RequestSyntax"></a>

```
{
   "DeleteOption": "{{string}}",
   "GameServerGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteGameServerGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameServerGroupName](#API_DeleteGameServerGroup_RequestSyntax) **   <a name="gameliftservers-DeleteGameServerGroup-request-GameServerGroupName"></a>
A unique identifier for the game server group. Use either the name or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]+|^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]+`
Required: Yes

 ** [DeleteOption](#API_DeleteGameServerGroup_RequestSyntax) **   <a name="gameliftservers-DeleteGameServerGroup-request-DeleteOption"></a>
The type of delete to perform. Options include the following:
+  `SAFE_DELETE` – (default) Terminates the game server group and Amazon EC2 Auto Scaling group only when it has no game servers that are in `UTILIZED` status.
+  `FORCE_DELETE` – Terminates the game server group, including all active game servers regardless of their utilization status, and the Amazon EC2 Auto Scaling group.
+  `RETAIN` – Does a safe delete of the game server group but retains the Amazon EC2 Auto Scaling group as is.
Type: String
Valid Values: `SAFE_DELETE | FORCE_DELETE | RETAIN`
Required: No

## Response Syntax
<a name="API_DeleteGameServerGroup_ResponseSyntax"></a>

```
{
   "GameServerGroup": {
      "AutoScalingGroupArn": "string",
      "BalancingStrategy": "string",
      "CreationTime": number,
      "GameServerGroupArn": "string",
      "GameServerGroupName": "string",
      "GameServerProtectionPolicy": "string",
      "InstanceDefinitions": [
         {
            "InstanceType": "string",
            "WeightedCapacity": "string"
         }
      ],
      "LastUpdatedTime": number,
      "RoleArn": "string",
      "Status": "string",
      "StatusReason": "string",
      "SuspendedActions": [ "string" ]
   }
}
```

## Response Elements
<a name="API_DeleteGameServerGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameServerGroup](#API_DeleteGameServerGroup_ResponseSyntax) **   <a name="gameliftservers-DeleteGameServerGroup-response-GameServerGroup"></a>
An object that describes the deleted game server group resource, with status updated to `DELETE_SCHEDULED`.
Type: [GameServerGroup](API_GameServerGroup.md) object

## Errors
<a name="API_DeleteGameServerGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_DeleteGameServerGroup_Examples"></a>

### Delete a game server group
<a name="API_DeleteGameServerGroup_Example_1"></a>

This example deletes a game server group only if there is no hosting activity taking place on instances in the group.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DeleteGameServerGroup_Example_1_Request"></a>

```
{
   "GameServerGroupName": "MegaFrogServers_NA",
   "DeleteOption": [ "SAFE_DELETE" ]
}

CLI command:

aws gamelift delete-game-server-group \
    --game-server-group MegaFrogServers_NA \
    --delete-option SAFE_DELETE
```

#### Sample Response
<a name="API_DeleteGameServerGroup_Example_1_Response"></a>

```
{
   "GameServerGroup": {
      "AutoScalingGroupArn": "arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:1111aaaa-22bb-33cc-44dd-5555eeee66ff:autoScalingGroupName/MegaFrogServers_NA",
      "BalancingStrategy": "SPOT_ONLY",
      "CreationTime": 1496365885.44,
      "GameServerGroupArn": "arn:aws:gamelift:us-west-2::GameServerGroup/MegaFrogServers_NA",
      "GameServerGroupName": " MegaFrogServers_NA",
      "GameServerProtectionPolicy": "NO_PROTECTION",
      "InstanceDefinitions": [
         {
            "InstanceType": "c5.2xlarge",
            "WeightedCapacity": "1"
         },
         {
            "InstanceType": "m5.2xlarge",
            "WeightedCapacity": "1"
         }
      ],
      "LastUpdatedTime": 1496365885.44,
      "RoleArn": "arn:aws:iam:123456789012::role/GameLiftGsgRole",
      "Status": "DELETE_SCHEDULED",
      "StatusReason": "",
      "SuspendedActions": []
}
```

## See Also
<a name="API_DeleteGameServerGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DeleteGameServerGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DeleteGameServerGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DeleteGameServerGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DeleteGameServerGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DeleteGameServerGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DeleteGameServerGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DeleteGameServerGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DeleteGameServerGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DeleteGameServerGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DeleteGameServerGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
