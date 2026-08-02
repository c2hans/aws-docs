---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameSessionDetail.html
---

# GameSessionDetail
<a name="API_GameSessionDetail"></a>

A game session's properties plus the protection policy currently in force.

## Contents
<a name="API_GameSessionDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** GameSession **   <a name="gameliftservers-Type-GameSessionDetail-GameSession"></a>
Object that describes a game session.
Type: [GameSession](API_GameSession.md) object
Required: No

 ** ProtectionPolicy **   <a name="gameliftservers-Type-GameSessionDetail-ProtectionPolicy"></a>
Current status of protection for the game session.
+  **NoProtection** -- The game session can be terminated during a scale-down event.
+  **FullProtection** -- If the game session is in an `ACTIVE` status, it cannot be terminated during a scale-down event.
Type: String
Valid Values: `NoProtection | FullProtection`
Required: No

## See Also
<a name="API_GameSessionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GameSessionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GameSessionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GameSessionDetail)
