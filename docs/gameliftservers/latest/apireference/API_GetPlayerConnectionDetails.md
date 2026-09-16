---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GetPlayerConnectionDetails.html
---

# GetPlayerConnectionDetails
<a name="API_GetPlayerConnectionDetails"></a>

 **This API works with the following fleet types:** EC2 (server SDK 5.x or later), Container

Retrieves connection details for game clients to connect to game sessions.

 **Player gateway benefits:** DDoS protection with negligible impact to latency.

To enable player gateway on your fleet, set `PlayerGatewayMode` to `ENABLED` or `REQUIRED` when calling [CreateFleet](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateFleet.html) or [CreateContainerFleet](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerFleet.html).

 **How to use:** After creating a game session and adding players, call this operation with the game session ID and player IDs. When player gateway is enabled, the response includes connection endpoints and player gateway tokens that your game clients can use to connect to the game session through player gateway. To learn more about player gateway integration, see [DDoS protection with Amazon GameLift Servers player gateway](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/ddos-protection-intro.html).

When player gateway is disabled or in locations where player gateway is not supported, this operation returns game server connection information without player gateway tokens, so that your game clients directly connect to the game server endpoint.

## Request Syntax
<a name="API_GetPlayerConnectionDetails_RequestSyntax"></a>

```
{
   "GameSessionId": "{{string}}",
   "PlayerIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetPlayerConnectionDetails_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameSessionId](#API_GetPlayerConnectionDetails_RequestSyntax) **   <a name="gameliftservers-GetPlayerConnectionDetails-request-GameSessionId"></a>
An identifier for the game session that is unique across all regions for which to retrieve player connection details. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]+`
Required: Yes

 ** [PlayerIds](#API_GetPlayerConnectionDetails_RequestSyntax) **   <a name="gameliftservers-GetPlayerConnectionDetails-request-PlayerIds"></a>
List of unique identifiers for players. Connection details are returned for each player in this list.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_GetPlayerConnectionDetails_ResponseSyntax"></a>

```
{
   "GameSessionId": "string",
   "PlayerConnectionDetails": [
      {
         "Endpoints": [
            {
               "IpAddress": "string",
               "Port": number
            }
         ],
         "Expiration": number,
         "PlayerGatewayToken": "string",
         "PlayerId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetPlayerConnectionDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameSessionId](#API_GetPlayerConnectionDetails_ResponseSyntax) **   <a name="gameliftservers-GetPlayerConnectionDetails-response-GameSessionId"></a>
An identifier for the game session that is unique across all regions for which the player connection details were retrieved. The value is always a full ARN in the following format: For Home Region game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string>`. For Remote Location game session - `arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string>`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]+`

 ** [PlayerConnectionDetails](#API_GetPlayerConnectionDetails_ResponseSyntax) **   <a name="gameliftservers-GetPlayerConnectionDetails-response-PlayerConnectionDetails"></a>
A collection of player connection detail objects, one for each requested player.
Type: Array of [PlayerConnectionDetail](API_PlayerConnectionDetail.md) objects
Array Members: Minimum number of 1 item.

## Errors
<a name="API_GetPlayerConnectionDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidGameSessionStatusException **
The requested operation would cause a conflict with the current state of a resource associated with the request and/or the game instance. Resolve the conflict before retrying.
HTTP Status Code: 400

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** LimitExceededException **
The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_GetPlayerConnectionDetails_Examples"></a>

### Get player connection details with player gateway enabled
<a name="API_GetPlayerConnectionDetails_Example_1"></a>

This example retrieves connection details for a game client to connect to a game session through player gateway.

#### Sample Request
<a name="API_GetPlayerConnectionDetails_Example_1_Request"></a>

```
{
    "GameSessionId": "arn:aws:gamelift:ap-northeast-2::gamesession/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa/gsess-4444dddd-55ee-66ff-77aa-8888bbbb99cc",
    "PlayerIds": ["player1"]
}
```

#### Sample Response
<a name="API_GetPlayerConnectionDetails_Example_1_Response"></a>

```
{
    "GameSessionId": "arn:aws:gamelift:ap-northeast-2::gamesession/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa/gsess-4444dddd-55ee-66ff-77aa-8888bbbb99cc",
    "PlayerConnectionDetails": [
        {
            "PlayerId": "player1",
            "Endpoints": [
                {
                    "IpAddress": "192.0.2.0",
                    "Port": 7777
                },
                {
                    "IpAddress": "198.51.100.0",
                    "Port": 7777
                },
                {
                    "IpAddress": "203.0.113.0",
                    "Port": 7777
                }
            ],
            "PlayerGatewayToken": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "Expiration": "1736365885.22"
        }
    ]
}
```

## See Also
<a name="API_GetPlayerConnectionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/GetPlayerConnectionDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/GetPlayerConnectionDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GetPlayerConnectionDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/GetPlayerConnectionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GetPlayerConnectionDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/GetPlayerConnectionDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/GetPlayerConnectionDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/GetPlayerConnectionDetails)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/GetPlayerConnectionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GetPlayerConnectionDetails)
