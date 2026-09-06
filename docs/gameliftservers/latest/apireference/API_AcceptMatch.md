---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_AcceptMatch.html
---

# AcceptMatch
<a name="API_AcceptMatch"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Registers a player's acceptance or rejection of a proposed FlexMatch match. A matchmaking configuration may require player acceptance; if so, then matches built with that configuration cannot be completed unless all players accept the proposed match within a specified time limit.

When FlexMatch builds a match, all the matchmaking tickets involved in the proposed match are placed into status `REQUIRES_ACCEPTANCE`. This is a trigger for your game to get acceptance from all players in each ticket. Calls to this action are only valid for tickets that are in this status; calls for tickets not in this status result in an error.

To register acceptance, specify the ticket ID, one or more players, and an acceptance response. When all players have accepted, Amazon GameLift Servers advances the matchmaking tickets to status `PLACING`, and attempts to create a new game session for the match.

If any player rejects the match, or if acceptances are not received before a specified timeout, the proposed match is dropped. Each matchmaking ticket in the failed match is handled as follows:
+ If the ticket has one or more players who rejected the match or failed to respond, the ticket status is set `CANCELLED` and processing is terminated.
+ If all players in the ticket accepted the match, the ticket status is returned to `SEARCHING` to find a new match.

 **Learn more**

 [ Add FlexMatch to a game client](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-client.html)

 [ FlexMatch events](https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html) (reference)

## Request Syntax
<a name="API_AcceptMatch_RequestSyntax"></a>

```
{
   "AcceptanceType": "{{string}}",
   "PlayerIds": [ "{{string}}" ],
   "TicketId": "{{string}}"
}
```

## Request Parameters
<a name="API_AcceptMatch_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AcceptanceType](#API_AcceptMatch_RequestSyntax) **   <a name="gameliftservers-AcceptMatch-request-AcceptanceType"></a>
Player response to the proposed match.
Type: String
Valid Values: `ACCEPT | REJECT`
Required: Yes

 ** [PlayerIds](#API_AcceptMatch_RequestSyntax) **   <a name="gameliftservers-AcceptMatch-request-PlayerIds"></a>
A unique identifier for a player delivering the response. This parameter can include one or multiple player IDs.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [TicketId](#API_AcceptMatch_RequestSyntax) **   <a name="gameliftservers-AcceptMatch-request-TicketId"></a>
A unique identifier for a matchmaking ticket. The ticket must be in status `REQUIRES_ACCEPTANCE`; otherwise this request will fail.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]*`
Required: Yes

## Response Elements
<a name="API_AcceptMatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AcceptMatch_Errors"></a>

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
<a name="API_AcceptMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/AcceptMatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/AcceptMatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/AcceptMatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/AcceptMatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/AcceptMatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/AcceptMatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/AcceptMatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/AcceptMatch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/AcceptMatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/AcceptMatch)
