---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_Cluster.html
---

# Cluster
<a name="API_dax_Cluster"></a>

Contains all of the attributes of a specific DAX cluster.

## Contents
<a name="API_dax_Cluster_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ActiveNodes **   <a name="DDB-Type-dax_Cluster-ActiveNodes"></a>
The number of nodes in the cluster that are active (i.e., capable of serving requests).
Type: Integer
Required: No

 ** ClusterArn **   <a name="DDB-Type-dax_Cluster-ClusterArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the cluster.
Type: String
Required: No

 ** ClusterDiscoveryEndpoint **   <a name="DDB-Type-dax_Cluster-ClusterDiscoveryEndpoint"></a>
The endpoint for this DAX cluster, consisting of a DNS name, a port number, and a URL. Applications should use the URL to configure the DAX client to find their cluster.
Type: [Endpoint](API_dax_Endpoint.md) object
Required: No

 ** ClusterEndpointEncryptionType **   <a name="DDB-Type-dax_Cluster-ClusterEndpointEncryptionType"></a>
The type of encryption supported by the cluster's endpoint. Values are:
+  `NONE` for no encryption

   `TLS` for Transport Layer Security
Type: String
Valid Values: `NONE | TLS`
Required: No

 ** ClusterName **   <a name="DDB-Type-dax_Cluster-ClusterName"></a>
The name of the DAX cluster.
Type: String
Required: No

 ** Description **   <a name="DDB-Type-dax_Cluster-Description"></a>
The description of the cluster.
Type: String
Required: No

 ** IamRoleArn **   <a name="DDB-Type-dax_Cluster-IamRoleArn"></a>
A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role's permissions to access DynamoDB on your behalf.
Type: String
Required: No

 ** NetworkType **   <a name="DDB-Type-dax_Cluster-NetworkType"></a>
The IP address type of the cluster. Values are:
+  `ipv4` - IPv4 addresses only
+  `ipv6` - IPv6 addresses only
+  `dual_stack` - Both IPv4 and IPv6 addresses
Type: String
Valid Values: `ipv4 | ipv6 | dual_stack`
Required: No

 ** NodeIdsToRemove **   <a name="DDB-Type-dax_Cluster-NodeIdsToRemove"></a>
A list of nodes to be removed from the cluster.
Type: Array of strings
Required: No

 ** Nodes **   <a name="DDB-Type-dax_Cluster-Nodes"></a>
A list of nodes that are currently in the cluster.
Type: Array of [Node](API_dax_Node.md) objects
Required: No

 ** NodeType **   <a name="DDB-Type-dax_Cluster-NodeType"></a>
The node type for the nodes in the cluster. (All nodes in a DAX cluster are of the same type.)
Type: String
Required: No

 ** NotificationConfiguration **   <a name="DDB-Type-dax_Cluster-NotificationConfiguration"></a>
Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).
Type: [NotificationConfiguration](API_dax_NotificationConfiguration.md) object
Required: No

 ** ParameterGroup **   <a name="DDB-Type-dax_Cluster-ParameterGroup"></a>
The parameter group being used by nodes in the cluster.
Type: [ParameterGroupStatus](API_dax_ParameterGroupStatus.md) object
Required: No

 ** PreferredMaintenanceWindow **   <a name="DDB-Type-dax_Cluster-PreferredMaintenanceWindow"></a>
A range of time when maintenance of DAX cluster software will be performed. For example: `sun:01:00-sun:09:00`. Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.
Type: String
Required: No

 ** SecurityGroups **   <a name="DDB-Type-dax_Cluster-SecurityGroups"></a>
A list of security groups, and the status of each, for the nodes in the cluster.
Type: Array of [SecurityGroupMembership](API_dax_SecurityGroupMembership.md) objects
Required: No

 ** SSEDescription **   <a name="DDB-Type-dax_Cluster-SSEDescription"></a>
The description of the server-side encryption status on the specified DAX cluster.
Type: [SSEDescription](API_dax_SSEDescription.md) object
Required: No

 ** Status **   <a name="DDB-Type-dax_Cluster-Status"></a>
The current status of the cluster.
Type: String
Required: No

 ** SubnetGroup **   <a name="DDB-Type-dax_Cluster-SubnetGroup"></a>
The subnet group where the DAX cluster is running.
Type: String
Required: No

 ** TotalNodes **   <a name="DDB-Type-dax_Cluster-TotalNodes"></a>
The total number of nodes in the cluster.
Type: Integer
Required: No

## See Also
<a name="API_dax_Cluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/Cluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/Cluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/Cluster)
