---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Event.html
---

# Event
<a name="API_Event"></a>

Represents a single occurrence of something interesting within the system. Some examples of events are creating a cluster or adding or removing a node.

## Contents
<a name="API_Event_Contents"></a>

 ** Date **   <a name="MemoryDB-Type-Event-Date"></a>
The date and time when the event occurred.
Type: Timestamp
Required: No

 ** Message **   <a name="MemoryDB-Type-Event-Message"></a>
The text of the event.
Type: String
Required: No

 ** SourceName **   <a name="MemoryDB-Type-Event-SourceName"></a>
The name for the source of the event. For example, if the event occurred at the cluster level, the identifier would be the name of the cluster.
Type: String
Required: No

 ** SourceType **   <a name="MemoryDB-Type-Event-SourceType"></a>
Specifies the origin of this event - a cluster, a parameter group, a security group, etc.
Type: String
Valid Values: `node | parameter-group | subnet-group | cluster | user | acl`
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/Event)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/Event)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/Event)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
