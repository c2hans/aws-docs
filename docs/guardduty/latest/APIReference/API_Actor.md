---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Actor.html
---

# Actor
<a name="API_Actor"></a>

Information about the actors involved in an attack sequence.

## Contents
<a name="API_Actor_Contents"></a>

 ** id **   <a name="guardduty-Type-Actor-id"></a>
ID of the threat actor.
Type: String
Required: Yes

 ** process **   <a name="guardduty-Type-Actor-process"></a>
Contains information about the process associated with the threat actor. This includes details such as process name, path, execution time, and unique identifiers that help track the actor's activities within the system.
Type: [ActorProcess](API_ActorProcess.md) object
Required: No

 ** session **   <a name="guardduty-Type-Actor-session"></a>
Contains information about the user session where the activity initiated.
Type: [Session](API_Session.md) object
Required: No

 ** user **   <a name="guardduty-Type-Actor-user"></a>
Contains information about the user credentials used by the threat actor.
Type: [User](API_User.md) object
Required: No

## See Also
<a name="API_Actor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Actor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Actor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Actor)
