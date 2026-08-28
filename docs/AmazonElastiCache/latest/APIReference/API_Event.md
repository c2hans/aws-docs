---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_Event.html
---

# Event
<a name="API_Event"></a>

Represents a single occurrence of something interesting within the system. Some examples of events are creating a cluster, adding or removing a cache node, or rebooting a node.

## Contents
<a name="API_Event_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Date **
The date and time when the event occurred.
Type: Timestamp
Required: No

 ** Message **
The text of the event.
Type: String
Required: No

 ** SourceIdentifier **
The identifier for the source of the event. For example, if the event occurred at the cluster level, the identifier would be the name of the cluster.
Type: String
Required: No

 ** SourceType **
Specifies the origin of this event - a cluster, a parameter group, a security group, etc.
Type: String
Valid Values: `cache-cluster | cache-parameter-group | cache-security-group | cache-subnet-group | replication-group | serverless-cache | serverless-cache-snapshot | user | user-group`
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/Event)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/Event)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/Event)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
