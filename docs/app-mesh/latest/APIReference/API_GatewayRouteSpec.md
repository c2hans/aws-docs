---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_GatewayRouteSpec.html
---

# GatewayRouteSpec
<a name="API_GatewayRouteSpec"></a>

An object that represents a gateway route specification. Specify one gateway route type.

## Contents
<a name="API_GatewayRouteSpec_Contents"></a>

 ** grpcRoute **   <a name="appmesh-Type-GatewayRouteSpec-grpcRoute"></a>
An object that represents the specification of a gRPC gateway route.
Type: [GrpcGatewayRoute](API_GrpcGatewayRoute.md) object
Required: No

 ** http2Route **   <a name="appmesh-Type-GatewayRouteSpec-http2Route"></a>
An object that represents the specification of an HTTP/2 gateway route.
Type: [HttpGatewayRoute](API_HttpGatewayRoute.md) object
Required: No

 ** httpRoute **   <a name="appmesh-Type-GatewayRouteSpec-httpRoute"></a>
An object that represents the specification of an HTTP gateway route.
Type: [HttpGatewayRoute](API_HttpGatewayRoute.md) object
Required: No

 ** priority **   <a name="appmesh-Type-GatewayRouteSpec-priority"></a>
The ordering of the gateway routes spec.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

## See Also
<a name="API_GatewayRouteSpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GatewayRouteSpec)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GatewayRouteSpec)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GatewayRouteSpec)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
