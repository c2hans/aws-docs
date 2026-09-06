---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualNodeHttpConnectionPool.html
---

# VirtualNodeHttpConnectionPool
<a name="API_VirtualNodeHttpConnectionPool"></a>

An object that represents a type of connection pool.

## Contents
<a name="API_VirtualNodeHttpConnectionPool_Contents"></a>

 ** maxConnections **   <a name="appmesh-Type-VirtualNodeHttpConnectionPool-maxConnections"></a>
Maximum number of outbound TCP connections Envoy can establish concurrently with all hosts in upstream cluster.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** maxPendingRequests **   <a name="appmesh-Type-VirtualNodeHttpConnectionPool-maxPendingRequests"></a>
Number of overflowing requests after `max_connections` Envoy will queue to upstream cluster.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_VirtualNodeHttpConnectionPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualNodeHttpConnectionPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualNodeHttpConnectionPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualNodeHttpConnectionPool)
