---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateRouteServerEndpoint.html
---

# CreateRouteServerEndpoint
<a name="API_CreateRouteServerEndpoint"></a>

Creates a new endpoint for a route server in a specified subnet.

A route server endpoint is an AWS-managed component inside a subnet that facilitates [BGP (Border Gateway Protocol)](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) connections between your route server and your BGP peers.

For more information see [Dynamic routing in your VPC with VPC Route Server](https://docs.aws.amazon.com/vpc/latest/userguide/dynamic-routing-route-server.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_CreateRouteServerEndpoint_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Required: No

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **RouteServerId**
The ID of the route server for which to create an endpoint.
Type: String
Required: Yes

 **SubnetId**
The ID of the subnet in which to create the route server endpoint.
Type: String
Required: Yes

 **TagSpecification.N**
The tags to apply to the route server endpoint during creation.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateRouteServerEndpoint_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **routeServerEndpoint**
Information about the created route server endpoint.
Type: [RouteServerEndpoint](API_RouteServerEndpoint.md) object

## Errors
<a name="API_CreateRouteServerEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateRouteServerEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateRouteServerEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateRouteServerEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateRouteServerEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateRouteServerEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateRouteServerEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateRouteServerEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateRouteServerEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateRouteServerEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateRouteServerEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateRouteServerEndpoint)
