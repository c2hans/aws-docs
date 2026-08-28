---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_GatewayRouteTarget.html
---

# GatewayRouteTarget
<a name="API_GatewayRouteTarget"></a>

An object that represents a gateway route target.

## Contents
<a name="API_GatewayRouteTarget_Contents"></a>

 ** virtualService **   <a name="appmesh-Type-GatewayRouteTarget-virtualService"></a>
An object that represents a virtual service gateway route target.
Type: [GatewayRouteVirtualService](API_GatewayRouteVirtualService.md) object
Required: Yes

 ** port **   <a name="appmesh-Type-GatewayRouteTarget-port"></a>
The port number of the gateway route target.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

## See Also
<a name="API_GatewayRouteTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GatewayRouteTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GatewayRouteTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GatewayRouteTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
