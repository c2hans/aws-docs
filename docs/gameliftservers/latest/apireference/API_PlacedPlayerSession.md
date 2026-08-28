---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_PlacedPlayerSession.html
---

# PlacedPlayerSession
<a name="API_PlacedPlayerSession"></a>

Information about a player session. This object contains only the player ID and player session ID. To retrieve full details on a player session, call [DescribePlayerSessions](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribePlayerSessions.html) with the player session ID.

## Contents
<a name="API_PlacedPlayerSession_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** PlayerId **   <a name="gameliftservers-Type-PlacedPlayerSession-PlayerId"></a>
A unique identifier for a player that is associated with this player session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** PlayerSessionId **   <a name="gameliftservers-Type-PlacedPlayerSession-PlayerSessionId"></a>
A unique identifier for a player session.
Type: String
Pattern: `^psess-\S+`
Required: No

## See Also
<a name="API_PlacedPlayerSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/PlacedPlayerSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/PlacedPlayerSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/PlacedPlayerSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
