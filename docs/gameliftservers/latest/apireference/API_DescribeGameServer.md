---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameServer.html
---

# DescribeGameServer
<a name="API_DescribeGameServer"></a>

 **This API works with the following fleet types:** EC2 (FleetIQ)

Retrieves information for a registered game server. Information includes game server status, health check info, and the instance that the game server is running on.

To retrieve game server information, specify the game server ID. If successful, the requested game server object is returned.

 **Learn more**

 [Amazon GameLift Servers FleetIQ Guide](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html)

## Request Syntax
<a name="API_DescribeGameServer_RequestSyntax"></a>

```
{
   "GameServerGroupName": "{{string}}",
   "GameServerId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeGameServer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameServerGroupName](#API_DescribeGameServer_RequestSyntax) **   <a name="gameliftservers-DescribeGameServer-request-GameServerGroupName"></a>
A unique identifier for the game server group where the game server is running.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]+|^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]+`
Required: Yes

 ** [GameServerId](#API_DescribeGameServer_RequestSyntax) **   <a name="gameliftservers-DescribeGameServer-request-GameServerId"></a>
A custom string that uniquely identifies the game server information to be retrieved.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]+`
Required: Yes

## Response Syntax
<a name="API_DescribeGameServer_ResponseSyntax"></a>

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
<a name="API_DescribeGameServer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameServer](#API_DescribeGameServer_ResponseSyntax) **   <a name="gameliftservers-DescribeGameServer-response-GameServer"></a>
Object that describes the requested game server.
Type: [GameServer](API_GameServer.md) object

## Errors
<a name="API_DescribeGameServer_Errors"></a>

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
<a name="API_DescribeGameServer_Examples"></a>

### Retrieve details for a game server
<a name="API_DescribeGameServer_Example_1"></a>

This example retrieves attributes for a specified game server.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeGameServer_Example_1_Request"></a>

```
{
   "GameServerGroupName": "MegaFrogServers_NA",
   "GameServerId": "mega-frog-game-12345678"
}

CLI command:

aws gamelift describe-game-server \
    --game-server-group-name MegaFrogServers_NA \
    --game-server-id mega-frog-game-12345678
```

#### Sample Response
<a name="API_DescribeGameServer_Example_1_Response"></a>

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
      "LastClaimTime": 1580218197.293,
      "LastHealthCheckTime": 1580218197.293,
      "RegistrationTime": 1580218197.293,
      "UtilizationStatus": "AVAILABLE"
   }
}
```

## See Also
<a name="API_DescribeGameServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeGameServer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeGameServer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeGameServer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeGameServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeGameServer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeGameServer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeGameServer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeGameServer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeGameServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeGameServer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
