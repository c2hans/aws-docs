---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualGatewayHttpConnectionPool.html
---

# VirtualGatewayHttpConnectionPool
<a name="API_VirtualGatewayHttpConnectionPool"></a>

An object that represents a type of connection pool.

## Contents
<a name="API_VirtualGatewayHttpConnectionPool_Contents"></a>

 ** maxConnections **   <a name="appmesh-Type-VirtualGatewayHttpConnectionPool-maxConnections"></a>
Maximum number of outbound TCP connections Envoy can establish concurrently with all hosts in upstream cluster.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** maxPendingRequests **   <a name="appmesh-Type-VirtualGatewayHttpConnectionPool-maxPendingRequests"></a>
Number of overflowing requests after `max_connections` Envoy will queue to upstream cluster.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_VirtualGatewayHttpConnectionPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayHttpConnectionPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayHttpConnectionPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayHttpConnectionPool)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
