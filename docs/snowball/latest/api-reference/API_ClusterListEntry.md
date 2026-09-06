---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_ClusterListEntry.html
---

# ClusterListEntry
<a name="API_ClusterListEntry"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Contains a cluster's state, a cluster's ID, and other important information.

## Contents
<a name="API_ClusterListEntry_Contents"></a>

 ** ClusterId **   <a name="Snowball-Type-ClusterListEntry-ClusterId"></a>
The 39-character ID for the cluster that you want to list, for example `CID123e4567-e89b-12d3-a456-426655440000`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** ClusterState **   <a name="Snowball-Type-ClusterListEntry-ClusterState"></a>
The current state of this cluster. For information about the state of a specific node, see [JobListEntry:JobState](API_JobListEntry.md#Snowball-Type-JobListEntry-JobState).
Type: String
Valid Values: `AwaitingQuorum | Pending | InUse | Complete | Cancelled`
Required: No

 ** CreationDate **   <a name="Snowball-Type-ClusterListEntry-CreationDate"></a>
The creation date for this cluster.
Type: Timestamp
Required: No

 ** Description **   <a name="Snowball-Type-ClusterListEntry-Description"></a>
Defines an optional description of the cluster, for example `Environmental Data Cluster-01`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## See Also
<a name="API_ClusterListEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/ClusterListEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/ClusterListEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/ClusterListEntry)
