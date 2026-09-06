---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpcEndpointConnection.html
---

# VpcEndpointConnection
<a name="API_VpcEndpointConnection"></a>

Describes a VPC endpoint connection to a service.

## Contents
<a name="API_VpcEndpointConnection_Contents"></a>

 ** creationTimestamp **
The date and time that the VPC endpoint was created.
Type: Timestamp
Required: No

 ** DnsEntrySet.N **
The DNS entries for the VPC endpoint.
Type: Array of [DnsEntry](API_DnsEntry.md) objects
Required: No

 ** GatewayLoadBalancerArnSet.N **
The Amazon Resource Names (ARNs) of the Gateway Load Balancers for the service.
Type: Array of strings
Required: No

 ** ipAddressType **
The IP address type for the endpoint.
Type: String
Valid Values: `ipv4 | dualstack | ipv6`
Required: No

 ** NetworkLoadBalancerArnSet.N **
The Amazon Resource Names (ARNs) of the network load balancers for the service.
Type: Array of strings
Required: No

 ** PayerResponsibilitySet.N **
The payer responsibility settings for the endpoint.
Type: Array of [PayerResponsibilityEntry](API_PayerResponsibilityEntry.md) objects
Required: No

 ** serviceId **
The ID of the service to which the endpoint is connected.
Type: String
Required: No

 ** TagSet.N **
The tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcEndpointConnectionId **
The ID of the VPC endpoint connection.
Type: String
Required: No

 ** vpcEndpointId **
The ID of the VPC endpoint.
Type: String
Required: No

 ** vpcEndpointOwner **
The ID of the AWS account that owns the VPC endpoint.
Type: String
Required: No

 ** vpcEndpointRegion **
The Region of the endpoint.
Type: String
Required: No

 ** vpcEndpointState **
The state of the VPC endpoint.
Type: String
Valid Values: `PendingAcceptance | Pending | Available | Deleting | Deleted | Rejected | Failed | Expired | Partial`
Required: No

## See Also
<a name="API_VpcEndpointConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/VpcEndpointConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/VpcEndpointConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/VpcEndpointConnection)
