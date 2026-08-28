---
source_url: https://docs.aws.amazon.com/documentdb/latest/APIReference/API_elastic_ClusterSnapshotInList.html
---

# ClusterSnapshotInList
<a name="API_elastic_ClusterSnapshotInList"></a>

A list of elastic cluster snapshots.

## Contents
<a name="API_elastic_ClusterSnapshotInList_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** clusterArn **   <a name="documentdb-Type-elastic_ClusterSnapshotInList-clusterArn"></a>
The ARN identifier of the elastic cluster.
Type: String
Required: Yes

 ** snapshotArn **   <a name="documentdb-Type-elastic_ClusterSnapshotInList-snapshotArn"></a>
The ARN identifier of the elastic cluster snapshot.
Type: String
Required: Yes

 ** snapshotCreationTime **   <a name="documentdb-Type-elastic_ClusterSnapshotInList-snapshotCreationTime"></a>
The time when the elastic cluster snapshot was created in Universal Coordinated Time (UTC).
Type: String
Required: Yes

 ** snapshotName **   <a name="documentdb-Type-elastic_ClusterSnapshotInList-snapshotName"></a>
The name of the elastic cluster snapshot.
Type: String
Required: Yes

 ** status **   <a name="documentdb-Type-elastic_ClusterSnapshotInList-status"></a>
The status of the elastic cluster snapshot.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | UPDATING | VPC_ENDPOINT_LIMIT_EXCEEDED | IP_ADDRESS_LIMIT_EXCEEDED | INVALID_SECURITY_GROUP_ID | INVALID_SUBNET_ID | INACCESSIBLE_ENCRYPTION_CREDS | INACCESSIBLE_SECRET_ARN | INACCESSIBLE_VPC_ENDPOINT | INCOMPATIBLE_NETWORK | MERGING | MODIFYING | SPLITTING | COPYING | STARTING | STOPPING | STOPPED | MAINTENANCE | INACCESSIBLE_ENCRYPTION_CREDENTIALS_RECOVERABLE`
Required: Yes

## See Also
<a name="API_elastic_ClusterSnapshotInList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-elastic-2022-11-28/ClusterSnapshotInList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-elastic-2022-11-28/ClusterSnapshotInList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-elastic-2022-11-28/ClusterSnapshotInList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
