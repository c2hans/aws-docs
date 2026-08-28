---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_DnsOptions.html
---

# DnsOptions
<a name="API_DnsOptions"></a>

 The DNS configuration options.

## Contents
<a name="API_DnsOptions_Contents"></a>

 ** privateDnsPreference **   <a name="vpclattice-Type-DnsOptions-privateDnsPreference"></a>
 The preference for which private domains have a private hosted zone created for and associated with the specified VPC. Only supported when private DNS is enabled and when the VPC endpoint type is ServiceNetwork or Resource.
+  `ALL_DOMAINS` - VPC Lattice provisions private hosted zones for all custom domain names.
+  `VERIFIED_DOMAINS_ONLY` - VPC Lattice provisions a private hosted zone only if custom domain name has been verified by the provider.
+  `VERIFIED_DOMAINS_AND_SPECIFIED_DOMAINS` - VPC Lattice provisions private hosted zones for all verified custom domain names and other domain names that the resource consumer specifies. The resource consumer specifies the domain names in the privateDnsSpecifiedDomains parameter.
+  `SPECIFIED_DOMAINS_ONLY` - VPC Lattice provisions a private hosted zone for domain names specified by the resource consumer. The resource consumer specifies the domain names in the privateDnsSpecifiedDomains parameter.
Type: String
Valid Values: `VERIFIED_DOMAINS_ONLY | ALL_DOMAINS | VERIFIED_DOMAINS_AND_SPECIFIED_DOMAINS | SPECIFIED_DOMAINS_ONLY`
Required: No

 ** privateDnsSpecifiedDomains **   <a name="vpclattice-Type-DnsOptions-privateDnsSpecifiedDomains"></a>
 Indicates which of the private domains to create private hosted zones for and associate with the specified VPC. Only supported when private DNS is enabled and the private DNS preference is `VERIFIED_DOMAINS_AND_SPECIFIED_DOMAINS` or `SPECIFIED_DOMAINS_ONLY`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_DnsOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/DnsOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/DnsOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/DnsOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
