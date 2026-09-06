---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRedshiftClusterPendingModifiedValues.html
---

# AwsRedshiftClusterPendingModifiedValues
<a name="API_AwsRedshiftClusterPendingModifiedValues"></a>

Changes to the Amazon Redshift cluster that are currently pending.

## Contents
<a name="API_AwsRedshiftClusterPendingModifiedValues_Contents"></a>

 ** AutomatedSnapshotRetentionPeriod **   <a name="securityhub-Type-AwsRedshiftClusterPendingModifiedValues-AutomatedSnapshotRetentionPeriod"></a>
The pending or in-progress change to the automated snapshot retention period.
Type: Integer
Required: No

 ** ClusterIdentifier **   <a name="securityhub-Type-AwsRedshiftClusterPendingModifiedValues-ClusterIdentifier"></a>
The pending or in-progress change to the identifier for the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClusterType **   <a name="securityhub-Type-AwsRedshiftClusterPendingModifiedValues-ClusterType"></a>
The pending or in-progress change to the cluster type.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClusterVersion **   <a name="securityhub-Type-AwsRedshiftClusterPendingModifiedValues-ClusterVersion"></a>
The pending or in-progress change to the service version.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EncryptionType **   <a name="securityhub-Type-AwsRedshiftClusterPendingModifiedValues-EncryptionType"></a>
The encryption type for a cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EnhancedVpcRouting **   <a name="securityhub-Type-AwsRedshiftClusterPendingModifiedValues-EnhancedVpcRouting"></a>
Indicates whether to create the cluster with enhanced VPC routing enabled.
Type: Boolean
Required: No

 ** MaintenanceTrackName **   <a name="securityhub-Type-AwsRedshiftClusterPendingModifiedValues-MaintenanceTrackName"></a>
The name of the maintenance track that the cluster changes to during the next maintenance window.
Type: String
Pattern: `.*\S.*`
Required: No

 ** MasterUserPassword **   <a name="securityhub-Type-AwsRedshiftClusterPendingModifiedValues-MasterUserPassword"></a>
The pending or in-progress change to the master user password for the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NodeType **   <a name="securityhub-Type-AwsRedshiftClusterPendingModifiedValues-NodeType"></a>
The pending or in-progress change to the cluster's node type.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NumberOfNodes **   <a name="securityhub-Type-AwsRedshiftClusterPendingModifiedValues-NumberOfNodes"></a>
The pending or in-progress change to the number of nodes in the cluster.
Type: Integer
Required: No

 ** PubliclyAccessible **   <a name="securityhub-Type-AwsRedshiftClusterPendingModifiedValues-PubliclyAccessible"></a>
The pending or in-progress change to whether the cluster can be connected to from the public network.
Type: Boolean
Required: No

## See Also
<a name="API_AwsRedshiftClusterPendingModifiedValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRedshiftClusterPendingModifiedValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRedshiftClusterPendingModifiedValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRedshiftClusterPendingModifiedValues)
