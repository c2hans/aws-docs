---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_StopMatchmaking.html
---

# StopMatchmaking
<a name="API_StopMatchmaking"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Cancels a matchmaking ticket or match backfill ticket that is currently being processed. To stop the matchmaking operation, specify the ticket ID. If successful, work on the ticket is stopped, and the ticket status is changed to `CANCELLED`.

This call is also used to turn off automatic backfill for an individual game session. This is for game sessions that are created with a matchmaking configuration that has automatic backfill enabled. The ticket ID is included in the `MatchmakerData` of an updated game session object, which is provided to the game server.

**Note**
If the operation is successful, the service sends back an empty JSON struct with the HTTP 200 response (not an empty HTTP body).

 **Learn more**

 [ Add FlexMatch to a game client](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-client.html)

## Request Syntax
<a name="API_StopMatchmaking_RequestSyntax"></a>

```
{
   "TicketId": "{{string}}"
}
```

## Request Parameters
<a name="API_StopMatchmaking_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [TicketId](#API_StopMatchmaking_RequestSyntax) **   <a name="gameliftservers-StopMatchmaking-request-TicketId"></a>
A unique identifier for a matchmaking ticket.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]*`
Required: Yes

## Response Elements
<a name="API_StopMatchmaking_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopMatchmaking_Errors"></a>

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

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## See Also
<a name="API_StopMatchmaking_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/StopMatchmaking)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/StopMatchmaking)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/StopMatchmaking)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/StopMatchmaking)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/StopMatchmaking)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/StopMatchmaking)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/StopMatchmaking)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/StopMatchmaking)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/StopMatchmaking)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/StopMatchmaking)
