---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Actor.html
---

# Actor
<a name="API_Actor"></a>

 Information about the threat actor identified in an Amazon GuardDuty Extended Threat Detection attack sequence. GuardDuty generates an attack sequence finding when multiple events align to a potentially suspicious activity. To receive GuardDuty attack sequence findings in AWS Security Hub CSPM, you must have GuardDuty enabled. For more information, see [GuardDuty Extended Threat Detection ](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-extended-threat-detection.html) in the *Amazon GuardDuty User Guide*.

## Contents
<a name="API_Actor_Contents"></a>

 ** Id **   <a name="securityhub-Type-Actor-Id"></a>
 The ID of the threat actor.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Session **   <a name="securityhub-Type-Actor-Session"></a>
 Contains information about the user session where the activity initiated.
Type: [ActorSession](API_ActorSession.md) object
Required: No

 ** User **   <a name="securityhub-Type-Actor-User"></a>
 Contains information about the user credentials used by the threat actor.
Type: [ActorUser](API_ActorUser.md) object
Required: No

## See Also
<a name="API_Actor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Actor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Actor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Actor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
