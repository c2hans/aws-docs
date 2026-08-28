---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_EventBus.html
---

# EventBus
<a name="API_EventBus"></a>

An event bus receives events from a source, uses rules to evaluate them, applies any configured input transformation, and routes them to the appropriate target(s). Your account's default event bus receives events from AWS services. A custom event bus can receive events from your custom applications and services. A partner event bus receives events from an event source created by an SaaS partner. These events come from the partners services or applications.

## Contents
<a name="API_EventBus_Contents"></a>

 ** Arn **   <a name="eventbridge-Type-EventBus-Arn"></a>
The ARN of the event bus.
Type: String
Required: No

 ** CreationTime **   <a name="eventbridge-Type-EventBus-CreationTime"></a>
The time the event bus was created.
Type: Timestamp
Required: No

 ** Description **   <a name="eventbridge-Type-EventBus-Description"></a>
The event bus description.
Type: String
Length Constraints: Maximum length of 512.
Required: No

 ** LastModifiedTime **   <a name="eventbridge-Type-EventBus-LastModifiedTime"></a>
The time the event bus was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="eventbridge-Type-EventBus-Name"></a>
The name of the event bus.
Type: String
Required: No

 ** Policy **   <a name="eventbridge-Type-EventBus-Policy"></a>
The permissions policy of the event bus, describing which other AWS accounts can write events to this event bus.
Type: String
Required: No

## See Also
<a name="API_EventBus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/EventBus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/EventBus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/EventBus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
