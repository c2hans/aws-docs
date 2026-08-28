---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualNodeConnectionPool.html
---

# VirtualNodeConnectionPool
<a name="API_VirtualNodeConnectionPool"></a>

An object that represents the type of virtual node connection pool.

Only one protocol is used at a time and should be the same protocol as the one chosen under port mapping.

If not present the default value for `maxPendingRequests` is `2147483647`.

## Contents
<a name="API_VirtualNodeConnectionPool_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** grpc **   <a name="appmesh-Type-VirtualNodeConnectionPool-grpc"></a>
An object that represents a type of connection pool.
Type: [VirtualNodeGrpcConnectionPool](API_VirtualNodeGrpcConnectionPool.md) object
Required: No

 ** http **   <a name="appmesh-Type-VirtualNodeConnectionPool-http"></a>
An object that represents a type of connection pool.
Type: [VirtualNodeHttpConnectionPool](API_VirtualNodeHttpConnectionPool.md) object
Required: No

 ** http2 **   <a name="appmesh-Type-VirtualNodeConnectionPool-http2"></a>
An object that represents a type of connection pool.
Type: [VirtualNodeHttp2ConnectionPool](API_VirtualNodeHttp2ConnectionPool.md) object
Required: No

 ** tcp **   <a name="appmesh-Type-VirtualNodeConnectionPool-tcp"></a>
An object that represents a type of connection pool.
Type: [VirtualNodeTcpConnectionPool](API_VirtualNodeTcpConnectionPool.md) object
Required: No

## See Also
<a name="API_VirtualNodeConnectionPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualNodeConnectionPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualNodeConnectionPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualNodeConnectionPool)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
