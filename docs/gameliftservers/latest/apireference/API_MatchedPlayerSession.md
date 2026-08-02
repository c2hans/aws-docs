---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_MatchedPlayerSession.html
---

# MatchedPlayerSession
<a name="API_MatchedPlayerSession"></a>

Represents a new player session that is created as a result of a successful FlexMatch match. A successful match automatically creates new player sessions for every player ID in the original matchmaking request.

When players connect to the match's game session, they must include both player ID and player session ID in order to claim their assigned player slot.

## Contents
<a name="API_MatchedPlayerSession_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** PlayerId **   <a name="gameliftservers-Type-MatchedPlayerSession-PlayerId"></a>
A unique identifier for a player
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** PlayerSessionId **   <a name="gameliftservers-Type-MatchedPlayerSession-PlayerSessionId"></a>
A unique identifier for a player session. PlayerSessionId will only be populated for player sessions that are in ACTIVE or RESERVED status when the ticket is completed.
Type: String
Pattern: `^psess-\S+`
Required: No

## See Also
<a name="API_MatchedPlayerSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/MatchedPlayerSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/MatchedPlayerSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/MatchedPlayerSession)
