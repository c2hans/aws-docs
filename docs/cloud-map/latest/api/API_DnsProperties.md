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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
