---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_DnsServiceDiscovery.html
---

# DnsServiceDiscovery
<a name="API_DnsServiceDiscovery"></a>

An object that represents the DNS service discovery information for your virtual node.

## Contents
<a name="API_DnsServiceDiscovery_Contents"></a>

 ** hostname **   <a name="appmesh-Type-DnsServiceDiscovery-hostname"></a>
Specifies the DNS service discovery hostname for the virtual node.
Type: String
Required: Yes

 ** ipPreference **   <a name="appmesh-Type-DnsServiceDiscovery-ipPreference"></a>
The preferred IP version that this virtual node uses. Setting the IP preference on the virtual node only overrides the IP preference set for the mesh on this specific node.
Type: String
Valid Values: `IPv6_PREFERRED | IPv4_PREFERRED | IPv4_ONLY | IPv6_ONLY`
Required: No

 ** responseType **   <a name="appmesh-Type-DnsServiceDiscovery-responseType"></a>
Specifies the DNS response type for the virtual node.
Type: String
Valid Values: `LOADBALANCER | ENDPOINTS`
Required: No

## See Also
<a name="API_DnsServiceDiscovery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/DnsServiceDiscovery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/DnsServiceDiscovery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/DnsServiceDiscovery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
