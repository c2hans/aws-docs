---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Session.html
---

# Session
<a name="API_Session"></a>

Contains information about the authenticated session.

## Contents
<a name="API_Session_Contents"></a>

 ** createdTime **   <a name="guardduty-Type-Session-createdTime"></a>
The timestamp for when the session was created.
In AWS CloudTrail, you can find this value as `userIdentity.sessionContext.attributes.creationDate`.
Type: Timestamp
Required: No

 ** issuer **   <a name="guardduty-Type-Session-issuer"></a>
Identifier of the session issuer.
In AWS CloudTrail, you can find this value as `userIdentity.sessionContext.sessionIssuer.arn`.
Type: String
Required: No

 ** mfaStatus **   <a name="guardduty-Type-Session-mfaStatus"></a>
Indicates whether or not multi-factor authencation (MFA) was used during authentication.
In AWS CloudTrail, you can find this value as `userIdentity.sessionContext.attributes.mfaAuthenticated`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** uid **   <a name="guardduty-Type-Session-uid"></a>
The unique identifier of the session.
Type: String
Required: No

## See Also
<a name="API_Session_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Session)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Session)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Session)
