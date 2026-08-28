---
source_url: https://docs.aws.amazon.com/documentdb/latest/APIReference/API_GlobalClusterMember.html
---

# GlobalClusterMember
<a name="API_GlobalClusterMember"></a>

A data structure with information about any primary and secondary clusters associated with an Amazon DocumentDB global clusters.

## Contents
<a name="API_GlobalClusterMember_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DBClusterArn **
The Amazon Resource Name (ARN) for each Amazon DocumentDB cluster.
Type: String
Required: No

 ** IsWriter **
 Specifies whether the Amazon DocumentDB cluster is the primary cluster (that is, has read-write capability) for the Amazon DocumentDB global cluster with which it is associated.
Type: Boolean
Required: No

 ** Readers.member.N **
The Amazon Resource Name (ARN) for each read-only secondary cluster associated with the Amazon DocumentDB global cluster.
Type: Array of strings
Required: No

 ** SynchronizationStatus **
The status of synchronization of each Amazon DocumentDB cluster in the global cluster.
Type: String
Valid Values: `connected | pending-resync`
Required: No

## See Also
<a name="API_GlobalClusterMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/GlobalClusterMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/GlobalClusterMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/GlobalClusterMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
