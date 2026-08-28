---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_GlobalReplicationGroupMember.html
---

# GlobalReplicationGroupMember
<a name="API_GlobalReplicationGroupMember"></a>

A member of a Global datastore. It contains the Replication Group Id, the Amazon region and the role of the replication group.

## Contents
<a name="API_GlobalReplicationGroupMember_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AutomaticFailover **
Indicates whether automatic failover is enabled for the replication group.
Type: String
Valid Values: `enabled | disabled | enabling | disabling`
Required: No

 ** ReplicationGroupId **
The replication group id of the Global datastore member.
Type: String
Required: No

 ** ReplicationGroupRegion **
The Amazon region of the Global datastore member.
Type: String
Required: No

 ** Role **
Indicates the role of the replication group, primary or secondary.
Type: String
Required: No

 ** Status **
The status of the membership of the replication group.
Type: String
Required: No

## See Also
<a name="API_GlobalReplicationGroupMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/GlobalReplicationGroupMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/GlobalReplicationGroupMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/GlobalReplicationGroupMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
