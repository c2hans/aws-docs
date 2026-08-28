---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ActorSession.html
---

# ActorSession
<a name="API_ActorSession"></a>

 Contains information about the authenticated session used by the threat actor identified in an Amazon GuardDuty Extended Threat Detection attack sequence. GuardDuty generates an attack sequence finding when multiple events align to a potentially suspicious activity. To receive GuardDuty attack sequence findings in AWS Security Hub CSPM, you must have GuardDuty enabled. For more information, see [GuardDuty Extended Threat Detection ](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-extended-threat-detection.html) in the *Amazon GuardDuty User Guide*.

## Contents
<a name="API_ActorSession_Contents"></a>

 ** CreatedTime **   <a name="securityhub-Type-ActorSession-CreatedTime"></a>
The timestamp for when the session was created.
In AWS CloudTrail, you can find this value as `userIdentity.sessionContext.attributes.creationDate`.
Type: Long
Required: No

 ** Issuer **   <a name="securityhub-Type-ActorSession-Issuer"></a>
 The issuer of the session.
In AWS CloudTrail, you can find this value as `userIdentity.sessionContext.sessionIssuer.arn`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MfaStatus **   <a name="securityhub-Type-ActorSession-MfaStatus"></a>
 Indicates whether multi-factor authentication (MFA) was used for authentication during the session.
In AWS CloudTrail, you can find this value as `userIdentity.sessionContext.attributes.mfaAuthenticated`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** Uid **   <a name="securityhub-Type-ActorSession-Uid"></a>
 Unique identifier of the session.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ActorSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ActorSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ActorSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ActorSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
