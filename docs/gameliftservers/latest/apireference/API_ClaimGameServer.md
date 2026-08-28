---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ClaimGameServer.html
---

# ClaimGameServer
<a name="API_ClaimGameServer"></a>

 **This API works with the following fleet types:** EC2 (FleetIQ)

Locates an available game server and temporarily reserves it to host gameplay and players. This operation is called from a game client or client service (such as a matchmaker) to request hosting resources for a new game session. In response, Amazon GameLift Servers FleetIQ locates an available game server, places it in `CLAIMED` status for 60 seconds, and returns connection information that players can use to connect to the game server.

To claim a game server, identify a game server group. You can also specify a game server ID, although this approach bypasses Amazon GameLift Servers FleetIQ placement optimization. Optionally, include game data to pass to the game server at the start of a game session, such as a game map or player information. Add filter options to further restrict how a game server is chosen, such as only allowing game servers on `ACTIVE` instances to be claimed.

When a game server is successfully claimed, connection information is returned. A claimed game server's utilization status remains `AVAILABLE` while the claim status is set to `CLAIMED` for up to 60 seconds. This time period gives the game server time to update its status to `UTILIZED` after players join. If the game server's status is not updated within 60 seconds, the game server reverts to unclaimed status and is available to be claimed by another request. The claim time period is a fixed value and is not configurable.

If you try to claim a specific game server, this request will fail in the following cases:
+ If the game server utilization status is `UTILIZED`.
+ If the game server claim status is `CLAIMED`.
+ If the game server is running on an instance in `DRAINING` status and the provided filter option does not allow placing on `DRAINING` instances.

 **Learn more**

 [Amazon GameLift Servers FleetIQ Guide](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html)

## Request Syntax
<a name="API_ClaimGameServer_RequestSyntax"></a>

```
{
   "FilterOption": {
      "InstanceStatuses": [ "{{string}}" ]
   },
   "GameServerData": "{{string}}",
   "GameServerGroupName": "{{string}}",
   "GameServerId": "{{string}}"
}
```

## Request Parameters
<a name="API_ClaimGameServer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameServerGroupName](#API_ClaimGameServer_RequestSyntax) **   <a name="gameliftservers-ClaimGameServer-request-GameServerGroupName"></a>
A unique identifier for the game server group where the game server is running. If you are not specifying a game server to claim, this value identifies where you want Amazon GameLift Servers FleetIQ to look for an available game server to claim.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]+|^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]+`
Required: Yes

 ** [FilterOption](#API_ClaimGameServer_RequestSyntax) **   <a name="gameliftservers-ClaimGameServer-request-FilterOption"></a>
Object that restricts how a claimed game server is chosen.
Type: [ClaimFilterOption](API_ClaimFilterOption.md) object
Required: No

 ** [GameServerData](#API_ClaimGameServer_RequestSyntax) **   <a name="gameliftservers-ClaimGameServer-request-GameServerData"></a>
A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on game servers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** [GameServerId](#API_ClaimGameServer_RequestSyntax) **   <a name="gameliftservers-ClaimGameServer-request-GameServerId"></a>
A custom string that uniquely identifies the game server to claim. If this parameter is left empty, Amazon GameLift Servers FleetIQ searches for an available game server in the specified game server group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]+`
Required: No

## Response Syntax
<a name="API_ClaimGameServer_ResponseSyntax"></a>

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
<a name="API_ClaimGameServer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameServer](#API_ClaimGameServer_ResponseSyntax) **   <a name="gameliftservers-ClaimGameServer-response-GameServer"></a>
Object that describes the newly claimed game server.
Type: [GameServer](API_GameServer.md) object

## Errors
<a name="API_ClaimGameServer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.

HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** OutOfCapacityException **
The specified game server group has no available game servers to fulfill a `ClaimGameServer` request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_ClaimGameServer_Examples"></a>

### Reserve a game server for a new game session
<a name="API_ClaimGameServer_Example_1"></a>

This example reserves an available game server to host a new game session. Because the request does not specify a game server ID, Amazon GameLift Servers selects an available game server with optimal placement.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_ClaimGameServer_Example_1_Request"></a>

```
{
   "GameServerGroupName": "MegaFrogServers_NA"
}

CLI command:

aws gamelift claim-game-server \
    --game-server-group-name MegaFrogServers_NA
```

#### Sample Response
<a name="API_ClaimGameServer_Example_1_Response"></a>

```
{
   "GameServer": {
      "ClaimStatus": "CLAIMED",
      "ConnectionInfo": "192.0.2.0.80",
      "GameServerData": "",
      "GameServerGroupArn": "arn:aws:gamelift:us-west-2::GameServerGroup/MegaFrogServers_NA",
      "GameServerGroupName": "MegaFrogServers_NA",
      "GameServerId": "mega-frog-game-12345678",
      "InstanceId": "i-1234567890abcdef0",
      "LastClaimTime": 1580218197.293,
      "LastHealthCheckTime": 1580218197.293,
      "RegistrationTime": 1580218197.293,
      "UtilizationStatus": "AVAILABLE"
   }
}
```

## See Also
<a name="API_ClaimGameServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/ClaimGameServer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/ClaimGameServer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ClaimGameServer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/ClaimGameServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ClaimGameServer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/ClaimGameServer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/ClaimGameServer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/ClaimGameServer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/ClaimGameServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ClaimGameServer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
