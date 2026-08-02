---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DnsResource.html
---

# DnsResource
<a name="API_DnsResource"></a>

The DNS name of the resource.

## Contents
<a name="API_DnsResource_Contents"></a>

 ** domainName **   <a name="vpclattice-Type-DnsResource-domainName"></a>
The domain name of the resource.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: No

 ** ipAddressType **   <a name="vpclattice-Type-DnsResource-ipAddressType"></a>
The type of IP address. Dualstack is currently not supported.
Type: String
Valid Values: `IPV4 | IPV6 | DUALSTACK`
Required: No

## See Also
<a name="API_DnsResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/DnsResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/DnsResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/DnsResource)
