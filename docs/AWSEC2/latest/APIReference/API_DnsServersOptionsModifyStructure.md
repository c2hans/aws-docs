---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DnsServersOptionsModifyStructure.html
---

# DnsServersOptionsModifyStructure
<a name="API_DnsServersOptionsModifyStructure"></a>

Information about the DNS server to be used.

## Contents
<a name="API_DnsServersOptionsModifyStructure_Contents"></a>

 ** CustomDnsServers.N **
The IPv4 address range, in CIDR notation, of the DNS servers to be used. You can specify up to two DNS servers. Ensure that the DNS servers can be reached by the clients. The specified values overwrite the existing values.
Type: Array of strings
Required: No

 ** Enabled **
Indicates whether DNS servers should be used. Specify `False` to delete the existing DNS servers.
Type: Boolean
Required: No

## See Also
<a name="API_DnsServersOptionsModifyStructure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DnsServersOptionsModifyStructure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DnsServersOptionsModifyStructure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DnsServersOptionsModifyStructure)
