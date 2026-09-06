---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PrivateDnsNameOptionsOnLaunch.html
---

# PrivateDnsNameOptionsOnLaunch
<a name="API_PrivateDnsNameOptionsOnLaunch"></a>

Describes the options for instance hostnames.

## Contents
<a name="API_PrivateDnsNameOptionsOnLaunch_Contents"></a>

 ** enableResourceNameDnsAAAARecord **
Indicates whether to respond to DNS queries for instance hostname with DNS AAAA records.
Type: Boolean
Required: No

 ** enableResourceNameDnsARecord **
Indicates whether to respond to DNS queries for instance hostnames with DNS A records.
Type: Boolean
Required: No

 ** hostnameType **
The type of hostname for EC2 instances. For IPv4 only subnets, an instance DNS name must be based on the instance IPv4 address. For IPv6 only subnets, an instance DNS name must be based on the instance ID. For dual-stack subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID.
Type: String
Valid Values: `ip-name | resource-name`
Required: No

## See Also
<a name="API_PrivateDnsNameOptionsOnLaunch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PrivateDnsNameOptionsOnLaunch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PrivateDnsNameOptionsOnLaunch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PrivateDnsNameOptionsOnLaunch)
