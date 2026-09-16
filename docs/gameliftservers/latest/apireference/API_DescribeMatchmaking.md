---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeMatchmaking.html
---

# DescribeMatchmaking
<a name="API_DescribeMatchmaking"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Retrieves one or more matchmaking tickets. Use this operation to retrieve ticket information, including--after a successful match is made--connection information for the resulting new game session.

To request matchmaking tickets, provide a list of up to 10 ticket IDs. If the request is successful, a ticket object is returned for each requested ID that currently exists.

This operation is not designed to be continually called to track matchmaking ticket status. This practice can cause you to exceed your API limit, which results in errors. Instead, as a best practice, set up an Amazon Simple Notification Service to receive notifications, and provide the topic ARN in the matchmaking configuration.

 **Learn more**

 [ Add FlexMatch to a game client](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-client.html)

 [ Set Up FlexMatch event notification](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html)

## Request Syntax
<a name="API_DescribeMatchmaking_RequestSyntax"></a>

```
{
   "TicketIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeMatchmaking_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [TicketIds](#API_DescribeMatchmaking_RequestSyntax) **   <a name="gameliftservers-DescribeMatchmaking-request-TicketIds"></a>
A unique identifier for a matchmaking ticket. You can include up to 10 ID values.
Type: Array of strings
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]*`
Required: Yes

## Response Syntax
<a name="API_DescribeMatchmaking_ResponseSyntax"></a>

```
{
   "TicketList": [
      {
         "ConfigurationArn": "string",
         "ConfigurationName": "string",
         "EndTime": number,
         "EstimatedWaitTime": number,
         "GameSessionConnectionInfo": {
            "DnsName": "string",
            "GameSessionArn": "string",
            "IpAddress": "string",
            "MatchedPlayerSessions": [
               {
                  "PlayerId": "string",
                  "PlayerSessionId": "string"
               }
            ],
            "PlayerGatewayStatus": "string",
            "Port": number
         },
         "Players": [
            {
               "LatencyInMs": {
                  "string" : number
               },
               "PlayerAttributes": {
                  "string" : {
                     "N": number,
                     "S": "string",
                     "SDM": {
                        "string" : number
                     },
                     "SL": [ "string" ]
                  }
               },
               "PlayerId": "string",
               "Team": "string"
            }
         ],
         "StartTime": number,
         "Status": "string",
         "StatusMessage": "string",
         "StatusReason": "string",
         "TicketId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeMatchmaking_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TicketList](#API_DescribeMatchmaking_ResponseSyntax) **   <a name="gameliftservers-DescribeMatchmaking-response-TicketList"></a>
A collection of existing matchmaking ticket objects matching the request.
Type: Array of [MatchmakingTicket](API_MatchmakingTicket.md) objects

## Errors
<a name="API_DescribeMatchmaking_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## See Also
<a name="API_DescribeMatchmaking_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeMatchmaking)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeMatchmaking)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeMatchmaking)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeMatchmaking)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeMatchmaking)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeMatchmaking)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeMatchmaking)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeMatchmaking)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeMatchmaking)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeMatchmaking)
