---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RouteServerPeer.html
---

# RouteServerPeer
<a name="API_RouteServerPeer"></a>

Describes a BGP peer configuration for a route server endpoint.

A route server peer is a session between a route server endpoint and the device deployed in AWS (such as a firewall appliance or other network security function running on an EC2 instance). The device must meet these requirements:
+ Have an elastic network interface in the VPC
+ Support BGP (Border Gateway Protocol)
+ Can initiate BGP sessions

## Contents
<a name="API_RouteServerPeer_Contents"></a>

 ** bfdStatus **
The current status of the BFD session with this peer.
Type: [RouteServerBfdStatus](API_RouteServerBfdStatus.md) object
Required: No

 ** bgpOptions **
The BGP configuration options for this peer, including ASN (Autonomous System Number) and BFD (Bidrectional Forwarding Detection) settings.
Type: [RouteServerBgpOptions](API_RouteServerBgpOptions.md) object
Required: No

 ** bgpStatus **
The current status of the BGP session with this peer.
Type: [RouteServerBgpStatus](API_RouteServerBgpStatus.md) object
Required: No

 ** endpointEniAddress **
The IP address of the Elastic network interface for the route server endpoint.
Type: String
Required: No

 ** endpointEniId **
The ID of the Elastic network interface for the route server endpoint.
Type: String
Required: No

 ** failureReason **
The reason for any failure in peer creation or operation.
Type: String
Required: No

 ** peerAddress **
The IPv4 address of the peer device.
Type: String
Required: No

 ** routeServerEndpointId **
The ID of the route server endpoint associated with this peer.
Type: String
Required: No

 ** routeServerId **
The ID of the route server associated with this peer.
Type: String
Required: No

 ** routeServerPeerId **
The unique identifier of the route server peer.
Type: String
Required: No

 ** state **
The current state of the route server peer.
Type: String
Valid Values: `pending | available | deleting | deleted | failing | failed`
Required: No

 ** subnetId **
The ID of the subnet containing the route server peer.
Type: String
Required: No

 ** TagSet.N **
Any tags assigned to the route server peer.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcId **
The ID of the VPC containing the route server peer.
Type: String
Required: No

## See Also
<a name="API_RouteServerPeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RouteServerPeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RouteServerPeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RouteServerPeer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
