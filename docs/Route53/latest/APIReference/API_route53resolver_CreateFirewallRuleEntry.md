---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateFirewallRuleEntry.html
---

# CreateFirewallRuleEntry
<a name="API_route53resolver_CreateFirewallRuleEntry"></a>

The details for creating a single firewall rule in a batch operation.

## Contents
<a name="API_route53resolver_CreateFirewallRuleEntry_Contents"></a>

 ** Action **   <a name="Route53Resolver-Type-route53resolver_CreateFirewallRuleEntry-Action"></a>
The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule:
+  `ALLOW` - Permit the request to go through. Not available for DNS Firewall Advanced rules.
+  `ALERT` - Permit the request and send metrics and logs to CloudWatch.
+  `BLOCK` - Disallow the request. This option requires additional details in the rule's `BlockResponse`.
Type: String
Valid Values: `ALLOW | BLOCK | ALERT`
Required: Yes

 ** CreatorRequestId **   <a name="Route53Resolver-Type-route53resolver_CreateFirewallRuleEntry-CreatorRequestId"></a>
A unique string that identifies the request and that allows you to retry failed requests without the risk of running the operation twice. `CreatorRequestId` can be any unique string, for example, a date/time stamp.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** FirewallRuleGroupId **   <a name="Route53Resolver-Type-route53resolver_CreateFirewallRuleEntry-FirewallRuleGroupId"></a>
The unique identifier of the firewall rule group where you want to create the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** Name **   <a name="Route53Resolver-Type-route53resolver_CreateFirewallRuleEntry-Name"></a>
A name that lets you identify the rule in the rule group.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: Yes

 ** Priority **   <a name="Route53Resolver-Type-route53resolver_CreateFirewallRuleEntry-Priority"></a>
The setting that determines the processing order of the rule in the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.
Type: Integer
Required: Yes

 ** BlockOverrideDnsType **   <a name="Route53Resolver-Type-route53resolver_CreateFirewallRuleEntry-BlockOverrideDnsType"></a>
The DNS record's type. This determines the format of the record value that you provided in `BlockOverrideDomain`. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
Type: String
Valid Values: `CNAME`
Required: No

 ** BlockOverrideDomain **   <a name="Route53Resolver-Type-route53resolver_CreateFirewallRuleEntry-BlockOverrideDomain"></a>
The custom DNS record to send back in response to the query. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** BlockOverrideTtl **   <a name="Route53Resolver-Type-route53resolver_CreateFirewallRuleEntry-BlockOverrideTtl"></a>
The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
This setting is required if the `BlockResponse` setting is `OVERRIDE`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 604800.
Required: No

 ** BlockResponse **   <a name="Route53Resolver-Type-route53resolver_CreateFirewallRuleEntry-BlockResponse"></a>
The way that you want DNS Firewall to block the request, used with the rule action setting `BLOCK`.
+  `NODATA` - Respond indicating that the query was successful, but no response is available for it.
+  `NXDOMAIN` - Respond indicating that the domain name that's in the query doesn't exist.
+  `OVERRIDE` - Provide a custom override in the response. This option requires custom handling details in the rule's `BlockOverride*` settings.
Type: String
Valid Values: `NODATA | NXDOMAIN | OVERRIDE`
Required: No

 ** ConfidenceThreshold **   <a name="Route53Resolver-Type-route53resolver_CreateFirewallRuleEntry-ConfidenceThreshold"></a>
The confidence threshold for DNS Firewall Advanced. You must provide this value when you create or update a DNS Firewall Advanced rule. The confidence level values mean:
+  `LOW`: Provides the highest detection rate for threats, but also increases false positives.
+  `MEDIUM`: Provides a balance between detecting threats and false positives.
+  `HIGH`: Detects only the most well corroborated threats with a low rate of false positives.
Type: String
Valid Values: `LOW | MEDIUM | HIGH`
Required: No

 ** DnsThreatProtection **   <a name="Route53Resolver-Type-route53resolver_CreateFirewallRuleEntry-DnsThreatProtection"></a>
The type of the DNS Firewall Advanced rule. This setting is mutually exclusive with `FirewallDomainListId` and `FirewallRuleType`. Valid values are:
+  `DGA`: Domain generation algorithms detection. DGAs are used by attackers to generate a large number of domains to launch malware attacks.
+  `DNS_TUNNELING`: DNS tunneling detection. DNS tunneling is used by attackers to exfiltrate data from the client by using the DNS tunnel without making a network connection to the client.
+  `DICTIONARY_DGA`: Dictionary-based domain generation algorithms detection. Dictionary DGAs use wordlists to generate domains that appear more legitimate, making them harder to detect than traditional DGAs.
Type: String
Valid Values: `DGA | DNS_TUNNELING | DICTIONARY_DGA`
Required: No

 ** FirewallDomainListId **   <a name="Route53Resolver-Type-route53resolver_CreateFirewallRuleEntry-FirewallDomainListId"></a>
The ID of the domain list that you want to use in the rule. This setting is mutually exclusive with `DnsThreatProtection` and `FirewallRuleType`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** FirewallDomainRedirectionAction **   <a name="Route53Resolver-Type-route53resolver_CreateFirewallRuleEntry-FirewallDomainRedirectionAction"></a>
How you want the rule to evaluate DNS redirection in the DNS redirection chain, such as CNAME or DNAME.
 `INSPECT_REDIRECTION_DOMAIN`: (Default) inspects all domains in the redirection chain. The individual domains in the redirection chain must be added to the domain list.
 `TRUST_REDIRECTION_DOMAIN`: Inspects only the first domain in the redirection chain. You don't need to add the subsequent domains in the redirection list to the domain list.
Type: String
Valid Values: `INSPECT_REDIRECTION_DOMAIN | TRUST_REDIRECTION_DOMAIN`
Required: No

 ** FirewallRuleType **   <a name="Route53Resolver-Type-route53resolver_CreateFirewallRuleEntry-FirewallRuleType"></a>
The rule type configuration for the firewall rule. This is a tagged union — set exactly one of its members. This setting is mutually exclusive with the top-level `FirewallDomainListId` and `DnsThreatProtection` fields. Use one of:
+  `FirewallAdvancedContentCategory` — match an AWS-managed content category (for example, `VIOLENCE_AND_HATE_SPEECH`).
+  `FirewallAdvancedThreatCategory` — match an AWS-managed advanced threat category (for example, `PHISHING`).
+  `DnsThreatProtection` — match a built-in DNS Firewall Advanced threat detector (`DGA`, `DNS_TUNNELING`, or `DICTIONARY_DGA`).
+  `PartnerThreatProtection` — match a third-party threat feed delivered through AWS Marketplace. The selected partner must be an active subscription on the calling account.
To enumerate the values supported in your account, call [ListFirewallRuleTypes](API_route53resolver_ListFirewallRuleTypes.md).
Type: [FirewallRuleType](API_route53resolver_FirewallRuleType.md) object
Required: No

 ** Qtype **   <a name="Route53Resolver-Type-route53resolver_CreateFirewallRuleEntry-Qtype"></a>
The DNS query type you want the rule to evaluate. Allowed values are:
+ A: Returns an IPv4 address.
+ AAAA: Returns an IPv6 address.
+ CAA: Restricts CAs that can create SSL/TLS certifications for the domain.
+ CNAME: Returns another domain name.
+ DS: Record that identifies the DNSSEC signing key of a delegated zone.
+ MX: Specifies mail servers.
+ NAPTR: Regular-expression-based rewriting of domain names.
+ NS: Authoritative name servers.
+ PTR: Maps an IP address to a domain name.
+ SOA: Start of authority record for the zone.
+ SPF: Lists the servers authorized to send emails from a domain.
+ SRV: Application specific values that identify servers.
+ TXT: Verifies email senders and application-specific values.
+ A query type you define by using the DNS type ID, for example 28 for AAAA. The values must be defined as TYPENUMBER, where the NUMBER can be 1-65534, for example, TYPE28. For more information, see [List of DNS record types](https://en.wikipedia.org/wiki/List_of_DNS_record_types).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Required: No

## See Also
<a name="API_route53resolver_CreateFirewallRuleEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/CreateFirewallRuleEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/CreateFirewallRuleEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/CreateFirewallRuleEntry)
