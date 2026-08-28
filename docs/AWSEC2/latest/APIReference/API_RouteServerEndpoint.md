---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RouteServerEndpoint.html
---

# RouteServerEndpoint
<a name="API_RouteServerEndpoint"></a>

Describes a route server endpoint and its properties.

A route server endpoint is an AWS-managed component inside a subnet that facilitates [BGP (Border Gateway Protocol)](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) connections between your route server and your BGP peers.

## Contents
<a name="API_RouteServerEndpoint_Contents"></a>

 ** eniAddress **
The IP address of the Elastic network interface for the endpoint.
Type: String
Required: No

 ** eniId **
The ID of the Elastic network interface for the endpoint.
Type: String
Required: No

 ** failureReason **
The reason for any failure in endpoint creation or operation.
Type: String
Required: No

 ** routeServerEndpointId **
The unique identifier of the route server endpoint.
Type: String
Required: No

 ** routeServerId **
The ID of the route server associated with this endpoint.
Type: String
Required: No

 ** state **
The current state of the route server endpoint.
Type: String
Valid Values: `pending | available | deleting | deleted | failing | failed | delete-failed`
Required: No

 ** subnetId **
The ID of the subnet to place the route server endpoint into.
Type: String
Required: No

 ** TagSet.N **
Any tags assigned to the route server endpoint.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** vpcId **
The ID of the VPC containing the endpoint.
Type: String
Required: No

## See Also
<a name="API_RouteServerEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RouteServerEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RouteServerEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RouteServerEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
