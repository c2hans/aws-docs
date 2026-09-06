---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_DnsProperties.html
---

# DnsProperties
<a name="API_DnsProperties"></a>

A complex type that contains the ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a namespace.

## Contents
<a name="API_DnsProperties_Contents"></a>

 ** HostedZoneId **   <a name="cloudmap-Type-DnsProperties-HostedZoneId"></a>
The ID for the Route 53 hosted zone that AWS Cloud Map creates when you create a namespace.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** SOA **   <a name="cloudmap-Type-DnsProperties-SOA"></a>
Start of Authority (SOA) record for the hosted zone.
Type: [SOA](API_SOA.md) object
Required: No

## See Also
<a name="API_DnsProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/DnsProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/DnsProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/DnsProperties)
