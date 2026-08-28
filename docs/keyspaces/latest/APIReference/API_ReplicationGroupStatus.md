---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ReplicationGroupStatus.html
---

# ReplicationGroupStatus
<a name="API_ReplicationGroupStatus"></a>

 This shows the summary status of the keyspace after a new AWS Region was added.

## Contents
<a name="API_ReplicationGroupStatus_Contents"></a>

 ** keyspaceStatus **   <a name="keyspaces-Type-ReplicationGroupStatus-keyspaceStatus"></a>
 The status of the keyspace.
Type: String
Valid Values: `ACTIVE | CREATING | UPDATING | DELETING`
Required: Yes

 ** region **   <a name="keyspaces-Type-ReplicationGroupStatus-region"></a>
 The name of the Region that was added to the keyspace.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.
Required: Yes

 ** tablesReplicationProgress **   <a name="keyspaces-Type-ReplicationGroupStatus-tablesReplicationProgress"></a>
 This shows the replication progress of tables in the keyspace. The value is expressed as a percentage of the newly replicated tables with status `Active` compared to the total number of tables in the keyspace.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 7.
Pattern: `[0-9]{1,3}(?:[.][0-9]{1,2})?%`
Required: No

## See Also
<a name="API_ReplicationGroupStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/ReplicationGroupStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/ReplicationGroupStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/ReplicationGroupStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces (for Apache Cassandra). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
