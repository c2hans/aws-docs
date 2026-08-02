---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_GlobalCluster.html
---

# GlobalCluster
<a name="API_GlobalCluster"></a>

Contains the details of an Amazon Neptune global database.

This data type is used as a response element for the [CreateGlobalCluster](API_CreateGlobalCluster.md), [DescribeGlobalClusters](API_DescribeGlobalClusters.md), [ModifyGlobalCluster](API_ModifyGlobalCluster.md), [DeleteGlobalCluster](API_DeleteGlobalCluster.md), [FailoverGlobalCluster](API_FailoverGlobalCluster.md), and [RemoveFromGlobalCluster](API_RemoveFromGlobalCluster.md) actions.

## Contents
<a name="API_GlobalCluster_Contents"></a>

 ** DeletionProtection **
The deletion protection setting for the global database.
Type: Boolean
Required: No

 ** Engine **
The Neptune database engine used by the global database (`"neptune"`).
Type: String
Required: No

 ** EngineVersion **
The Neptune engine version used by the global database.
Type: String
Required: No

 ** FailoverState **
A data object containing all properties for the current state of an in-process or pending switchover or failover process for this global cluster (Neptune global database). This object is empty unless the `SwitchoverGlobalCluster` or `FailoverGlobalCluster` operation was called on this global cluster.
Type: [FailoverState](API_FailoverState.md) object
Required: No

 ** GlobalClusterArn **
The Amazon Resource Name (ARN) for the global database.
Type: String
Required: No

 ** GlobalClusterIdentifier **
Contains a user-supplied global database cluster identifier. This identifier is the unique key that identifies a global database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`
Required: No

 ** GlobalClusterMembers.GlobalClusterMember.N **
A list of cluster ARNs and instance ARNs for all the DB clusters that are part of the global database.
Type: Array of [GlobalClusterMember](API_GlobalClusterMember.md) objects
Required: No

 ** GlobalClusterResourceId **
An immutable identifier for the global database that is unique within in all regions. This identifier is found in CloudTrail log entries whenever the KMS key for the DB cluster is accessed.
Type: String
Required: No

 ** Status **
Specifies the current state of this global database.
Type: String
Required: No

 ** StorageEncrypted **
The storage encryption setting for the global database.
Type: Boolean
Required: No

## See Also
<a name="API_GlobalCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/GlobalCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/GlobalCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/GlobalCluster)
