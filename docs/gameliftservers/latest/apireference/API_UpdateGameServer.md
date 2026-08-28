---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateGameServer.html
---

# UpdateGameServer
<a name="API_UpdateGameServer"></a>

 **This API works with the following fleet types:** EC2 (FleetIQ)

Updates information about a registered game server to help Amazon GameLift Servers FleetIQ track game server availability. This operation is called by a game server process that is running on an instance in a game server group.

Use this operation to update the following types of game server information. You can make all three types of updates in the same request:
+ To update the game server's utilization status from `AVAILABLE` (when the game server is available to be claimed) to `UTILIZED` (when the game server is currently hosting games). Identify the game server and game server group and specify the new utilization status. You can't change the status from to `UTILIZED` to `AVAILABLE` .
+ To report health status, identify the game server and game server group and set health check to `HEALTHY`. If a game server does not report health status for a certain length of time, the game server is no longer considered healthy. As a result, it will be eventually deregistered from the game server group to avoid affecting utilization metrics. The best practice is to report health every 60 seconds.
+ To change game server metadata, provide updated game server data.

Once a game server is successfully updated, the relevant statuses and timestamps are updated.

 **Learn more**

 [Amazon GameLift Servers FleetIQ Guide](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html)

## Request Syntax
<a name="API_UpdateGameServer_RequestSyntax"></a>

```
{
   "GameServerData": "{{string}}",
   "GameServerGroupName": "{{string}}",
   "GameServerId": "{{string}}",
   "HealthCheck": "{{string}}",
   "UtilizationStatus": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateGameServer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameServerGroupName](#API_UpdateGameServer_RequestSyntax) **   <a name="gameliftservers-UpdateGameServer-request-GameServerGroupName"></a>
A unique identifier for the game server group where the game server is running.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]+|^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]+`
Required: Yes

 ** [GameServerId](#API_UpdateGameServer_RequestSyntax) **   <a name="gameliftservers-UpdateGameServer-request-GameServerId"></a>
A custom string that uniquely identifies the game server to update.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]+`
Required: Yes

 ** [GameServerData](#API_UpdateGameServer_RequestSyntax) **   <a name="gameliftservers-UpdateGameServer-request-GameServerData"></a>
A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on game servers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** [HealthCheck](#API_UpdateGameServer_RequestSyntax) **   <a name="gameliftservers-UpdateGameServer-request-HealthCheck"></a>
Indicates health status of the game server. A request that includes this parameter updates the game server's *LastHealthCheckTime* timestamp.
Type: String
Valid Values: `HEALTHY`
Required: No

 ** [UtilizationStatus](#API_UpdateGameServer_RequestSyntax) **   <a name="gameliftservers-UpdateGameServer-request-UtilizationStatus"></a>
Indicates if the game server is available or is currently hosting gameplay. You can update a game server status from `AVAILABLE` to `UTILIZED`, but you can't change a the status from `UTILIZED` to `AVAILABLE`.
Type: String
Valid Values: `AVAILABLE | UTILIZED`
Required: No

## Response Syntax
<a name="API_UpdateGameServer_ResponseSyntax"></a>

```
{
   "GameServer": {
      "ClaimStatus": "string",
      "ConnectionInfo": "string",
      "GameServerData": "string",
      "GameServerGroupArn": "string",
      "GameServerGroupName": "string",
      "GameServerId": "string",
      "InstanceId": "string",
      "LastClaimTime": number,
      "LastHealthCheckTime": number,
      "RegistrationTime": number,
      "UtilizationStatus": "string"
   }
}
```

## Response Elements
<a name="API_UpdateGameServer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameServer](#API_UpdateGameServer_ResponseSyntax) **   <a name="gameliftservers-UpdateGameServer-response-GameServer"></a>
Object that describes the newly updated game server.
Type: [GameServer](API_GameServer.md) object

## Errors
<a name="API_UpdateGameServer_Errors"></a>

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
<a name="API_UpdateGameServer_Examples"></a>

### Report that a game server is now hosting gameplay
<a name="API_UpdateGameServer_Example_1"></a>

This example changes the utilization status of a game server and reports the results of a health check. Prior to this call, the game server's utilization status is `AVAILABLE` and the claim status is `CLAIMED`.

#### Sample Request
<a name="API_UpdateGameServer_Example_1_Request"></a>

```
{
   "GameServerGroupName": "MegaFrogServers_NA",
   "HealthCheck": "HEALTHY"},
   "UtilizationStatus": "UTILIZED"
}

CLI command:

aws gamelift update-game-server \
    --game-server-group-name MegaFrogServers_NA \
    --health-check HEALTHY \
    --utilization-status UTILIZED
```

#### Sample Response
<a name="API_UpdateGameServer_Example_1_Response"></a>

```
{
   "GameServer": {
      "ClaimStatus": "",
      "ConnectionInfo": "192.0.2.0.80",
      "GameServerData": "",
      "GameServerGroupArn": "arn:aws:gamelift:us-west-2::GameServerGroup/MegaFrogServers_NA",
      "GameServerGroupName": "MegaFrogServers_NA",
      "GameServerId": "mega-frog-game-12345678",
      "InstanceId": "i-1234567890abcdef0",
      "LastClaimTime": 1580218290.293,
      "LastHealthCheckTime": 1580218294.293,
      "RegistrationTime": 1580218197.293,
      "UtilizationStatus": "UTILIZED"
   }
}
```

## See Also
<a name="API_UpdateGameServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/UpdateGameServer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/UpdateGameServer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/UpdateGameServer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/UpdateGameServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/UpdateGameServer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/UpdateGameServer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/UpdateGameServer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/UpdateGameServer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/UpdateGameServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/UpdateGameServer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
