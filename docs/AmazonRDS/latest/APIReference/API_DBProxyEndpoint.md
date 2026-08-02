---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBProxyEndpoint.html
---

# DBProxyEndpoint
<a name="API_DBProxyEndpoint"></a>

The data structure representing an endpoint associated with a DB proxy. RDS automatically creates one endpoint for each DB proxy. For Aurora DB clusters, you can associate additional endpoints with the same DB proxy. These endpoints can be read/write or read-only. They can also reside in different VPCs than the associated DB proxy.

This data type is used as a response element in the `DescribeDBProxyEndpoints` operation.

## Contents
<a name="API_DBProxyEndpoint_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreatedDate **
The date and time when the DB proxy endpoint was first created.
Type: Timestamp
Required: No

 ** DBProxyEndpointArn **
The Amazon Resource Name (ARN) for the DB proxy endpoint.
Type: String
Required: No

 ** DBProxyEndpointName **
The name for the DB proxy endpoint. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.
Type: String
Required: No

 ** DBProxyName **
The identifier for the DB proxy that is associated with this DB proxy endpoint.
Type: String
Required: No

 ** Endpoint **
The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.
Type: String
Required: No

 ** EndpointNetworkType **
The network type of the DB proxy endpoint. The network type determines the IP version that the proxy endpoint supports.
Valid values:
+  `IPV4` - The proxy endpoint supports IPv4 only.
+  `IPV6` - The proxy endpoint supports IPv6 only.
+  `DUAL` - The proxy endpoint supports both IPv4 and IPv6.
Type: String
Valid Values: `IPV4 | IPV6 | DUAL`
Required: No

 ** IsDefault **
Indicates whether this endpoint is the default endpoint for the associated DB proxy. Default DB proxy endpoints always have read/write capability. Other endpoints that you associate with the DB proxy can be either read/write or read-only.
Type: Boolean
Required: No

 ** Status **
The current status of this DB proxy endpoint. A status of `available` means the endpoint is ready to handle requests. Other values indicate that you must wait for the endpoint to be ready, or take some action to resolve an issue.
Type: String
Valid Values: `available | modifying | incompatible-network | insufficient-resource-limits | creating | deleting`
Required: No

 ** TargetRole **
A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.
Type: String
Valid Values: `READ_WRITE | READ_ONLY`
Required: No

 ** VpcId **
Provides the VPC ID of the DB proxy endpoint.
Type: String
Required: No

 ** VpcSecurityGroupIds.member.N **
Provides a list of VPC security groups that the DB proxy endpoint belongs to.
Type: Array of strings
Required: No

 ** VpcSubnetIds.member.N **
The EC2 subnet IDs for the DB proxy endpoint.
Type: Array of strings
Required: No

## See Also
<a name="API_DBProxyEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBProxyEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBProxyEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBProxyEndpoint)
