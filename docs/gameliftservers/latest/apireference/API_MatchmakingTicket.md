---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_MatchmakingTicket.html
---

# MatchmakingTicket
<a name="API_MatchmakingTicket"></a>

Ticket generated to track the progress of a matchmaking request. Each ticket is uniquely identified by a ticket ID, supplied by the requester, when creating a matchmaking request.

## Contents
<a name="API_MatchmakingTicket_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ConfigurationArn **   <a name="gameliftservers-Type-MatchmakingTicket-ConfigurationArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) associated with the GameLift matchmaking configuration resource that is used with this ticket.
Type: String
Pattern: `^arn:.*:matchmakingconfiguration\/[a-zA-Z0-9-\.]*`
Required: No

 ** ConfigurationName **   <a name="gameliftservers-Type-MatchmakingTicket-ConfigurationName"></a>
Name of the matchmaking configuration that is used with this ticket. Matchmaking configurations determine how players are grouped into a match and how a new game session is created for the match.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]*`
Required: No

 ** EndTime **   <a name="gameliftservers-Type-MatchmakingTicket-EndTime"></a>
Time stamp indicating when the matchmaking request stopped being processed due to successful completion, timeout, or cancellation. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** EstimatedWaitTime **   <a name="gameliftservers-Type-MatchmakingTicket-EstimatedWaitTime"></a>
Average amount of time (in seconds) that players are currently waiting for a match. If there is not enough recent data, this property may be empty.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** GameSessionConnectionInfo **   <a name="gameliftservers-Type-MatchmakingTicket-GameSessionConnectionInfo"></a>
Connection information for a new game session. Once a match is made, the FlexMatch engine creates a new game session for it. This information is added to the matchmaking ticket, which you can be retrieve by calling [DescribeMatchmaking](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeMatchmaking.html) .
Type: [GameSessionConnectionInfo](API_GameSessionConnectionInfo.md) object
Required: No

 ** Players **   <a name="gameliftservers-Type-MatchmakingTicket-Players"></a>
A set of `Player` objects, each representing a player to find matches for. Players are identified by a unique player ID and may include latency data for use during matchmaking. If the ticket is in status `COMPLETED`, the `Player` objects include the team the players were assigned to in the resulting match.
Type: Array of [Player](API_Player.md) objects
Required: No

 ** StartTime **   <a name="gameliftservers-Type-MatchmakingTicket-StartTime"></a>
Time stamp indicating when this matchmaking request was received. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** Status **   <a name="gameliftservers-Type-MatchmakingTicket-Status"></a>
Current status of the matchmaking request.
+  **QUEUED** -- The matchmaking request has been received and is currently waiting to be processed.
+  **SEARCHING** -- The matchmaking request is currently being processed.
+  **REQUIRES\_ACCEPTANCE** -- A match has been proposed and the players must accept the match. This status is used only with requests that use a matchmaking configuration with a player acceptance requirement.
+  **PLACING** -- The FlexMatch engine has matched players and is in the process of placing a new game session for the match.
+  **COMPLETED** -- Players have been matched and a game session is ready to host the players. A ticket in this state contains the necessary connection information for players.
+  **FAILED** -- The matchmaking request was not completed.
+  **CANCELLED** -- The matchmaking request was canceled. This may be the result of a `StopMatchmaking` operation or a proposed match that one or more players failed to accept.
+  **TIMED\_OUT** -- The matchmaking request was not successful within the duration specified in the matchmaking configuration.
Matchmaking requests that fail to successfully complete (statuses FAILED, CANCELLED, TIMED\_OUT) can be resubmitted as new requests with new ticket IDs.
Type: String
Valid Values: `CANCELLED | COMPLETED | FAILED | PLACING | QUEUED | REQUIRES_ACCEPTANCE | SEARCHING | TIMED_OUT`
Required: No

 ** StatusMessage **   <a name="gameliftservers-Type-MatchmakingTicket-StatusMessage"></a>
Additional information about the current status.
Type: String
Required: No

 ** StatusReason **   <a name="gameliftservers-Type-MatchmakingTicket-StatusReason"></a>
Code to explain the current status. For example, a status reason may indicate when a ticket has returned to `SEARCHING` status after a proposed match fails to receive player acceptances.
Type: String
Required: No

 ** TicketId **   <a name="gameliftservers-Type-MatchmakingTicket-TicketId"></a>
A unique identifier for a matchmaking ticket.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-\.]*`
Required: No

## See Also
<a name="API_MatchmakingTicket_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/MatchmakingTicket)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/MatchmakingTicket)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/MatchmakingTicket)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
