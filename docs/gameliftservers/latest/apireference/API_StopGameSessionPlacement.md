---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StopGameSessionPlacement.html
---

# StopGameSessionPlacement
<a name="API_StopGameSessionPlacement"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Cancels a game session placement that's in `PENDING` status. To stop a placement, provide the placement ID value.

Results

If successful, this operation removes the placement request from the queue and moves the `GameSessionPlacement` to `CANCELLED` status.

This operation results in an `InvalidRequestExecption` (400) error if a game session has already been created for this placement. You can clean up an unneeded game session by calling [TerminateGameSession](https://docs.aws.amazon.com/gamelift/latest/apireference/API_TerminateGameSession).

## Request Syntax
<a name="API_StopGameSessionPlacement_RequestSyntax"></a>

```
{
   "PlacementId": "{{string}}"
}
```

## Request Parameters
<a name="API_StopGameSessionPlacement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [PlacementId](#API_StopGameSessionPlacement_RequestSyntax) **   <a name="gameliftservers-StopGameSessionPlacement-request-PlacementId"></a>
A unique identifier for a game session placement to stop.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_StopGameSessionPlacement_ResponseSyntax"></a>

```
{
   "GameSessionPlacement": {
      "DnsName": "string",
      "EndTime": number,
      "GameProperties": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "GameSessionArn": "string",
      "GameSessionData": "string",
      "GameSessionId": "string",
      "GameSessionName": "string",
      "GameSessionQueueName": "string",
      "GameSessionRegion": "string",
      "IpAddress": "string",
      "MatchmakerData": "string",
      "MaximumPlayerSessionCount": number,
      "PlacedPlayerSessions": [
         {
            "PlayerId": "string",
            "PlayerSessionId": "string"
         }
      ],
      "PlacementId": "string",
      "PlayerGatewayStatus": "string",
      "PlayerLatencies": [
         {
            "LatencyInMilliseconds": number,
            "PlayerId": "string",
            "RegionIdentifier": "string"
         }
      ],
      "Port": number,
      "PriorityConfigurationOverride": {
         "LocationOrder": [ "string" ],
         "PlacementFallbackStrategy": "string"
      },
      "StartTime": number,
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_StopGameSessionPlacement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameSessionPlacement](#API_StopGameSessionPlacement_ResponseSyntax) **   <a name="gameliftservers-StopGameSessionPlacement-response-GameSessionPlacement"></a>
Object that describes the canceled game session placement, with `CANCELLED` status and an end time stamp.
Type: [GameSessionPlacement](API_GameSessionPlacement.md) object

## Errors
<a name="API_StopGameSessionPlacement_Errors"></a>

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

## See Also
<a name="API_StopGameSessionPlacement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/StopGameSessionPlacement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/StopGameSessionPlacement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/StopGameSessionPlacement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/StopGameSessionPlacement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/StopGameSessionPlacement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/StopGameSessionPlacement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/StopGameSessionPlacement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/StopGameSessionPlacement)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/StopGameSessionPlacement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/StopGameSessionPlacement)
