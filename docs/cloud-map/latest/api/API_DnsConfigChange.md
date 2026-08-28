---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_DnsConfigChange.html
---

# DnsConfigChange
<a name="API_DnsConfigChange"></a>

A complex type that contains information about changes to the Route 53 DNS records that AWS Cloud Map creates when you register an instance.

## Contents
<a name="API_DnsConfigChange_Contents"></a>

 ** DnsRecords **   <a name="cloudmap-Type-DnsConfigChange-DnsRecords"></a>
An array that contains one `DnsRecord` object for each Route 53 record that you want AWS Cloud Map to create when you register an instance.
Type: Array of [DnsRecord](API_DnsRecord.md) objects
Required: Yes

## See Also
<a name="API_DnsConfigChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/DnsConfigChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/DnsConfigChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/DnsConfigChange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Map. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloud-map` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
