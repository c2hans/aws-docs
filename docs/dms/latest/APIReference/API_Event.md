---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_Event.html
---

# Event
<a name="API_Event"></a>

Describes an identifiable significant activity that affects a replication instance or task. This object can provide the message, the available event categories, the date and source of the event, and the AWS DMS resource type.

## Contents
<a name="API_Event_Contents"></a>

 ** Date **   <a name="DMS-Type-Event-Date"></a>
The date of the event.
Type: Timestamp
Required: No

 ** EventCategories **   <a name="DMS-Type-Event-EventCategories"></a>
The event categories available for the specified source type.
Type: Array of strings
Required: No

 ** Message **   <a name="DMS-Type-Event-Message"></a>
The event message.
Type: String
Required: No

 ** SourceIdentifier **   <a name="DMS-Type-Event-SourceIdentifier"></a>
 The identifier of an event source.
Type: String
Required: No

 ** SourceType **   <a name="DMS-Type-Event-SourceType"></a>
 The type of AWS DMS resource that generates events.
Valid values: replication-instance \| endpoint \| replication-task
Type: String
Valid Values: `replication-instance`
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/Event)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/Event)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/Event)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
