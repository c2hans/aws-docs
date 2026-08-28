---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualGatewayListener.html
---

# VirtualGatewayListener
<a name="API_VirtualGatewayListener"></a>

An object that represents a listener for a virtual gateway.

## Contents
<a name="API_VirtualGatewayListener_Contents"></a>

 ** portMapping **   <a name="appmesh-Type-VirtualGatewayListener-portMapping"></a>
The port mapping information for the listener.
Type: [VirtualGatewayPortMapping](API_VirtualGatewayPortMapping.md) object
Required: Yes

 ** connectionPool **   <a name="appmesh-Type-VirtualGatewayListener-connectionPool"></a>
The connection pool information for the virtual gateway listener.
Type: [VirtualGatewayConnectionPool](API_VirtualGatewayConnectionPool.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** healthCheck **   <a name="appmesh-Type-VirtualGatewayListener-healthCheck"></a>
The health check information for the listener.
Type: [VirtualGatewayHealthCheckPolicy](API_VirtualGatewayHealthCheckPolicy.md) object
Required: No

 ** tls **   <a name="appmesh-Type-VirtualGatewayListener-tls"></a>
A reference to an object that represents the Transport Layer Security (TLS) properties for the listener.
Type: [VirtualGatewayListenerTls](API_VirtualGatewayListenerTls.md) object
Required: No

## See Also
<a name="API_VirtualGatewayListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayListener)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayListener)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayListener)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
