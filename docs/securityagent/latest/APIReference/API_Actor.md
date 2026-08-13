---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_Actor.html
---

# Actor
<a name="API_Actor"></a>

Represents an actor used during penetration testing. An actor defines a user or entity that interacts with the target application, including authentication credentials and target URIs.

## Contents
<a name="API_Actor_Contents"></a>

 ** authentication **   <a name="securityagent-Type-Actor-authentication"></a>
The authentication configuration for the actor.
Type: [Authentication](API_Authentication.md) object
Required: No

 ** description **   <a name="securityagent-Type-Actor-description"></a>
A description of the actor.
Type: String
Required: No

 ** enableEmailMfa **   <a name="securityagent-Type-Actor-enableEmailMfa"></a>
Whether email-based MFA is enabled for this actor.
Type: Boolean
Required: No

 ** identifier **   <a name="securityagent-Type-Actor-identifier"></a>
The unique identifier for the actor.
Type: String
Required: No

 ** mfaForwardingAddress **   <a name="securityagent-Type-Actor-mfaForwardingAddress"></a>
Server-generated email forwarding address for receiving MFA codes.
Type: String
Required: No

 ** uris **   <a name="securityagent-Type-Actor-uris"></a>
The list of URIs that the actor targets during testing.
Type: Array of strings
Required: No

## See Also
<a name="API_Actor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/Actor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/Actor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/Actor)
