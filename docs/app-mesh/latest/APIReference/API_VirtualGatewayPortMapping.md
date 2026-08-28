---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualGatewayPortMapping.html
---

# VirtualGatewayPortMapping
<a name="API_VirtualGatewayPortMapping"></a>

An object that represents a port mapping.

## Contents
<a name="API_VirtualGatewayPortMapping_Contents"></a>

 ** port **   <a name="appmesh-Type-VirtualGatewayPortMapping-port"></a>
The port used for the port mapping. Specify one protocol.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: Yes

 ** protocol **   <a name="appmesh-Type-VirtualGatewayPortMapping-protocol"></a>
The protocol used for the port mapping.
Type: String
Valid Values: `http | http2 | grpc`
Required: Yes

## See Also
<a name="API_VirtualGatewayPortMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayPortMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayPortMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayPortMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
