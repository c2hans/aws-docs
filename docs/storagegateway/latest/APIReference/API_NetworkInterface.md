---
source_url: https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_NetworkInterface.html
---

# NetworkInterface
<a name="API_NetworkInterface"></a>

Describes a gateway's network interface.

## Contents
<a name="API_NetworkInterface_Contents"></a>

 ** Ipv4Address **   <a name="StorageGateway-Type-NetworkInterface-Ipv4Address"></a>
The Internet Protocol version 4 (IPv4) address of the interface.
Type: String
Required: No

 ** Ipv6Address **   <a name="StorageGateway-Type-NetworkInterface-Ipv6Address"></a>
The Internet Protocol version 6 (IPv6) address of the interface.
This element returns IPv6 addresses for all gateway types except FSx File Gateway.
Type: String
Required: No

 ** MacAddress **   <a name="StorageGateway-Type-NetworkInterface-MacAddress"></a>
The Media Access Control (MAC) address of the interface.
This is currently unsupported and will not be returned in output.
Type: String
Required: No

## See Also
<a name="API_NetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/NetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/NetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/NetworkInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
