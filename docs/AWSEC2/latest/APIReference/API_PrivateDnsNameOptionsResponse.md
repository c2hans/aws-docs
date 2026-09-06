---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PrivateDnsNameOptionsResponse.html
---

# PrivateDnsNameOptionsResponse
<a name="API_PrivateDnsNameOptionsResponse"></a>

Describes the options for instance hostnames.

## Contents
<a name="API_PrivateDnsNameOptionsResponse_Contents"></a>

 ** enableResourceNameDnsAAAARecord **
Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.
Type: Boolean
Required: No

 ** enableResourceNameDnsARecord **
Indicates whether to respond to DNS queries for instance hostnames with DNS A records.
Type: Boolean
Required: No

 ** hostnameType **
The type of hostname to assign to an instance.
Type: String
Valid Values: `ip-name | resource-name`
Required: No

## See Also
<a name="API_PrivateDnsNameOptionsResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PrivateDnsNameOptionsResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PrivateDnsNameOptionsResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PrivateDnsNameOptionsResponse)
