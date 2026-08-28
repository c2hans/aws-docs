---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_EventActor.html
---

# EventActor
<a name="API_EventActor"></a>

Identifies the actor that triggered an event.

## Contents
<a name="API_EventActor_Contents"></a>

 ** principalId **   <a name="ngresiliencehub-Type-EventActor-principalId"></a>
The principal ID of the actor.
Type: String
Required: Yes

 ** type **   <a name="ngresiliencehub-Type-EventActor-type"></a>
The type of actor, either USER or SYSTEM.
Type: String
Valid Values: `USER | SYSTEM`
Required: Yes

 ** accountId **   <a name="ngresiliencehub-Type-EventActor-accountId"></a>
The AWS account ID of the actor.
Type: String
Required: No

 ** userName **   <a name="ngresiliencehub-Type-EventActor-userName"></a>
The user name of the actor.
Type: String
Required: No

## See Also
<a name="API_EventActor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/EventActor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/EventActor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/EventActor)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
