---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_Nameserver.html
---

# Nameserver
<a name="API_domains_Nameserver"></a>

Name server includes the following elements.

## Contents
<a name="API_domains_Nameserver_Contents"></a>

 ** Name **   <a name="Route53Domains-Type-domains_Nameserver-Name"></a>
The fully qualified host name of the name server.
Constraint: Maximum 255 characters
Type: String
Length Constraints: Maximum length of 255.
Pattern: `[a-zA-Z0-9_\-.]*`
Required: Yes

 ** GlueIps **   <a name="Route53Domains-Type-domains_Nameserver-GlueIps"></a>
Glue IP address of a name server entry. Glue IP addresses are required only when the name of the name server is a subdomain of the domain. For example, if your domain is example.com and the name server for the domain is ns.example.com, you need to specify the IP address for ns.example.com.
Constraints: The list can contain only one IPv4 and one IPv6 address.
Type: Array of strings
Length Constraints: Maximum length of 45.
Required: No

## See Also
<a name="API_domains_Nameserver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/Nameserver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/Nameserver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/Nameserver)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
