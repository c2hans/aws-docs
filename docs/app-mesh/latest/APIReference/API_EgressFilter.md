---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_EgressFilter.html
---

# EgressFilter
<a name="API_EgressFilter"></a>

An object that represents the egress filter rules for a service mesh.

## Contents
<a name="API_EgressFilter_Contents"></a>

 ** type **   <a name="appmesh-Type-EgressFilter-type"></a>
The egress filter type. By default, the type is `DROP_ALL`, which allows egress only from virtual nodes to other defined resources in the service mesh (and any traffic to `*.amazonaws.com` for AWS API calls). You can set the egress filter type to `ALLOW_ALL` to allow egress to any endpoint inside or outside of the service mesh.
When using `DROP_ALL`, the egress filter is a traffic-routing control, not a security boundary. The `*.amazonaws.com` allowance is based on the TLS Server Name Indication (SNI) that the client presents, and isn't verified against the destination IP address. To restrict the destinations that your workloads can reach, use security groups or network ACLs.
If you specify any backends on a virtual node when using `ALLOW_ALL`, you must specifiy all egress for that virtual node as backends. Otherwise, `ALLOW_ALL` will no longer work for that virtual node.
Type: String
Valid Values: `ALLOW_ALL | DROP_ALL`
Required: Yes

## See Also
<a name="API_EgressFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/EgressFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/EgressFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/EgressFilter)
