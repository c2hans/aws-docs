---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RegisterGameServer.html
---

# RegisterGameServer
<a name="API_RegisterGameServer"></a>

 **This API works with the following fleet types:** EC2 (FleetIQ)

Creates a new game server resource and notifies Amazon GameLift Servers FleetIQ that the game server is ready to host gameplay and players. This operation is called by a game server process that is running on an instance in a game server group. Registering game servers enables Amazon GameLift Servers FleetIQ to track available game servers and enables game clients and services to claim a game server for a new game session.

To register a game server, identify the game server group and instance where the game server is running, and provide a unique identifier for the game server. You can also include connection and game server data.

Once a game server is successfully registered, it is put in status `AVAILABLE`. A request to register a game server may fail if the instance it is running on is in the process of shutting down as part of instance balancing or scale-down activity.

 **Learn more**

 [Amazon GameLift Servers FleetIQ Guide](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html)

## Request Syntax
<a name="API_RegisterGameServer_RequestSyntax"></a>

```
{
   "ConnectionInfo": "{{string}}",
   "GameServerData": "{{string}}",
   "GameServerGroupName": "{{string}}",
   "GameServerId": "{{string}}",
   "InstanceId": "{{string}}"
}
```

## Request Parameters
<a name="API_RegisterGameServer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameServerGroupName](#API_RegisterGameServer_RequestSyntax) **   <a name="gameliftservers-RegisterGameServer-request-GameServerGroupName"></a>
A unique identifier for the game server group where the game server is running.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]+|^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]+`
Required: Yes

 ** [GameServerId](#API_RegisterGameServer_RequestSyntax) **   <a name="gameliftservers-RegisterGameServer-request-GameServerId"></a>
A custom string that uniquely identifies the game server to register. Game server IDs are developer-defined and must be unique across all game server groups in your AWS account.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]+`
Required: Yes

 ** [InstanceId](#API_RegisterGameServer_RequestSyntax) **   <a name="gameliftservers-RegisterGameServer-request-InstanceId"></a>
The unique identifier for the instance where the game server is running. This ID is available in the instance metadata. EC2 instance IDs use a 17-character format, for example: `i-1234567890abcdef0`.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `^i-[0-9a-zA-Z]{17}$`
Required: Yes

 ** [ConnectionInfo](#API_RegisterGameServer_RequestSyntax) **   <a name="gameliftservers-RegisterGameServer-request-ConnectionInfo"></a>
Information that is needed to make inbound client connections to the game server. This might include the IP address and port, DNS name, and other information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*\S.*`
Required: No

 ** [GameServerData](#API_RegisterGameServer_RequestSyntax) **   <a name="gameliftservers-RegisterGameServer-request-GameServerData"></a>
A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on game servers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

## Response Syntax
<a name="API_RegisterGameServer_ResponseSyntax"></a>

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
<a name="API_RegisterGameServer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameServer](#API_RegisterGameServer_ResponseSyntax) **   <a name="gameliftservers-RegisterGameServer-response-GameServer"></a>
Object that describes the newly registered game server.
Type: [GameServer](API_GameServer.md) object

## Errors
<a name="API_RegisterGameServer_Errors"></a>

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

 ** LimitExceededException **
The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

## Examples
<a name="API_RegisterGameServer_Examples"></a>

### Register a game server
<a name="API_RegisterGameServer_Example_1"></a>

This example illustrates how an game server process notifies GameLift that it is ready to host a game.

#### Sample Request
<a name="API_RegisterGameServer_Example_1_Request"></a>

```
{
   "GameServerGroupName": "MegaFrogServers_NA",
   "ConnectionInfo": "192.0.2.0.80",
   "GameServerId": "mega-frog-game-12345678",
   "InstanceId": "i-1234567890abcdef0"
}

CLI command:

aws gamelift register-game-server \
    --game-server-group-name MegaFrogServers_NA \
    --connection-info "192.0.2.0.80" \
    --game-server-id mega-frog-game-12345678 \
    --instance-id i-1234567890abcdef0
```

#### Sample Response
<a name="API_RegisterGameServer_Example_1_Response"></a>

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
      "LastClaimTime": ,
      "LastHealthCheckTime": 1580218197.293,
      "RegistrationTime": 1580218197.293,
      "UtilizationStatus": "AVAILABLE"
   }
}
```

## See Also
<a name="API_RegisterGameServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/RegisterGameServer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/RegisterGameServer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/RegisterGameServer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/RegisterGameServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/RegisterGameServer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/RegisterGameServer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/RegisterGameServer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/RegisterGameServer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/RegisterGameServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/RegisterGameServer)
