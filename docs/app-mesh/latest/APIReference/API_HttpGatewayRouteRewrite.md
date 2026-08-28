---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_HttpGatewayRouteRewrite.html
---

# HttpGatewayRouteRewrite
<a name="API_HttpGatewayRouteRewrite"></a>

An object representing the gateway route to rewrite.

## Contents
<a name="API_HttpGatewayRouteRewrite_Contents"></a>

 ** hostname **   <a name="appmesh-Type-HttpGatewayRouteRewrite-hostname"></a>
The host name to rewrite.
Type: [GatewayRouteHostnameRewrite](API_GatewayRouteHostnameRewrite.md) object
Required: No

 ** path **   <a name="appmesh-Type-HttpGatewayRouteRewrite-path"></a>
The path to rewrite.
Type: [HttpGatewayRoutePathRewrite](API_HttpGatewayRoutePathRewrite.md) object
Required: No

 ** prefix **   <a name="appmesh-Type-HttpGatewayRouteRewrite-prefix"></a>
The specified beginning characters to rewrite.
Type: [HttpGatewayRoutePrefixRewrite](API_HttpGatewayRoutePrefixRewrite.md) object
Required: No

## See Also
<a name="API_HttpGatewayRouteRewrite_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HttpGatewayRouteRewrite)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HttpGatewayRouteRewrite)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HttpGatewayRouteRewrite)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
