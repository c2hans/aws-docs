---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53resolver-firewallrulegroup-firewallrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Resolver::FirewallRuleGroup FirewallRule
<a name="aws-properties-route53resolver-firewallrulegroup-firewallrule"></a>

A single firewall rule in a rule group.

## Syntax
<a name="aws-properties-route53resolver-firewallrulegroup-firewallrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53resolver-firewallrulegroup-firewallrule-syntax.json"></a>

```
{
  "[Action](#cfn-route53resolver-firewallrulegroup-firewallrule-action)" : {{String}},
  "[BlockOverrideDnsType](#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridednstype)" : {{String}},
  "[BlockOverrideDomain](#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridedomain)" : {{String}},
  "[BlockOverrideTtl](#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridettl)" : {{Integer}},
  "[BlockResponse](#cfn-route53resolver-firewallrulegroup-firewallrule-blockresponse)" : {{String}},
  "[ConfidenceThreshold](#cfn-route53resolver-firewallrulegroup-firewallrule-confidencethreshold)" : {{String}},
  "[DnsThreatProtection](#cfn-route53resolver-firewallrulegroup-firewallrule-dnsthreatprotection)" : {{String}},
  "[FirewallDomainListId](#cfn-route53resolver-firewallrulegroup-firewallrule-firewalldomainlistid)" : {{String}},
  "[FirewallDomainRedirectionAction](#cfn-route53resolver-firewallrulegroup-firewallrule-firewalldomainredirectionaction)" : {{String}},
  "[FirewallRuleType](#cfn-route53resolver-firewallrulegroup-firewallrule-firewallruletype)" : {{FirewallRuleType}},
  "[FirewallThreatProtectionId](#cfn-route53resolver-firewallrulegroup-firewallrule-firewallthreatprotectionid)" : {{String}},
  "[Priority](#cfn-route53resolver-firewallrulegroup-firewallrule-priority)" : {{Integer}},
  "[Qtype](#cfn-route53resolver-firewallrulegroup-firewallrule-qtype)" : {{String}},
  "[Status](#cfn-route53resolver-firewallrulegroup-firewallrule-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53resolver-firewallrulegroup-firewallrule-syntax.yaml"></a>

```
  [Action](#cfn-route53resolver-firewallrulegroup-firewallrule-action): {{String}}
  [BlockOverrideDnsType](#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridednstype): {{String}}
  [BlockOverrideDomain](#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridedomain): {{String}}
  [BlockOverrideTtl](#cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridettl): {{Integer}}
  [BlockResponse](#cfn-route53resolver-firewallrulegroup-firewallrule-blockresponse): {{String}}
  [ConfidenceThreshold](#cfn-route53resolver-firewallrulegroup-firewallrule-confidencethreshold): {{String}}
  [DnsThreatProtection](#cfn-route53resolver-firewallrulegroup-firewallrule-dnsthreatprotection): {{String}}
  [FirewallDomainListId](#cfn-route53resolver-firewallrulegroup-firewallrule-firewalldomainlistid): {{String}}
  [FirewallDomainRedirectionAction](#cfn-route53resolver-firewallrulegroup-firewallrule-firewalldomainredirectionaction): {{String}}
  [FirewallRuleType](#cfn-route53resolver-firewallrulegroup-firewallrule-firewallruletype): {{
    FirewallRuleType}}
  [FirewallThreatProtectionId](#cfn-route53resolver-firewallrulegroup-firewallrule-firewallthreatprotectionid): {{String}}
  [Priority](#cfn-route53resolver-firewallrulegroup-firewallrule-priority): {{Integer}}
  [Qtype](#cfn-route53resolver-firewallrulegroup-firewallrule-qtype): {{String}}
  [Status](#cfn-route53resolver-firewallrulegroup-firewallrule-status): {{String}}
```

## Properties
<a name="aws-properties-route53resolver-firewallrulegroup-firewallrule-properties"></a>

`Action`  <a name="cfn-route53resolver-firewallrulegroup-firewallrule-action"></a>
The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advvanced rule:
+ `ALLOW` - Permit the request to go through. Not available for DNS Firewall Advanced rules.
+ `ALERT` - Permit the request to go through but send an alert to the logs.
+ `BLOCK` - Disallow the request. If this is specified,then `BlockResponse` must also be specified.

  if `BlockResponse` is `OVERRIDE`, then all of the following `OVERRIDE` attributes must be specified:
  +  `BlockOverrideDnsType`
  +  `BlockOverrideDomain`
  +  `BlockOverrideTtl`
*Required*: Yes
*Type*: String
*Allowed values*: `ALLOW | BLOCK | ALERT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockOverrideDnsType`  <a name="cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridednstype"></a>
The DNS record's type. This determines the format of the record value that you provided in `BlockOverrideDomain`. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
*Required*: No
*Type*: String
*Allowed values*: `CNAME`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockOverrideDomain`  <a name="cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridedomain"></a>
The custom DNS record to send back in response to the query. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockOverrideTtl`  <a name="cfn-route53resolver-firewallrulegroup-firewallrule-blockoverridettl"></a>
The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action `BLOCK` with a `BlockResponse` setting of `OVERRIDE`.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `604800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockResponse`  <a name="cfn-route53resolver-firewallrulegroup-firewallrule-blockresponse"></a>
The way that you want DNS Firewall to block the request. Used for the rule action setting `BLOCK`.
+ `NODATA` - Respond indicating that the query was successful, but no response is available for it.
+ `NXDOMAIN` - Respond indicating that the domain name that's in the query doesn't exist.
+ `OVERRIDE` - Provide a custom override in the response. This option requires custom handling details in the rule's `BlockOverride*` settings.
*Required*: No
*Type*: String
*Allowed values*: `NODATA | NXDOMAIN | OVERRIDE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfidenceThreshold`  <a name="cfn-route53resolver-firewallrulegroup-firewallrule-confidencethreshold"></a>
 The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule. The confidence level values mean:
+ `LOW`: Provides the highest detection rate for threats, but also increases false positives.
+ `MEDIUM`: Provides a balance between detecting threats and false positives.
+ `HIGH`: Detects only the most well corroborated threats with a low rate of false positives.
*Required*: No
*Type*: String
*Allowed values*: `LOW | MEDIUM | HIGH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DnsThreatProtection`  <a name="cfn-route53resolver-firewallrulegroup-firewallrule-dnsthreatprotection"></a>
 The type of the DNS Firewall Advanced rule. Valid values are:
+ `DGA`: Domain generation algorithms detection. DGAs are used by attackers to generate a large number of domains to launch malware attacks.
+ `DNS_TUNNELING`: DNS tunneling detection. DNS tunneling is used by attackers to exfiltrate data from the client by using the DNS tunnel without making a network connection to the client.
+ `DICTIONARY_DGA`: Dictionary-based domain generation algorithms detection. Dictionary DGAs use wordlists to generate domains that appear more legitimate, making them harder to detect than traditional DGAs.
*Required*: No
*Type*: String
*Allowed values*: `DGA | DNS_TUNNELING | DICTIONARY_DGA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirewallDomainListId`  <a name="cfn-route53resolver-firewallrulegroup-firewallrule-firewalldomainlistid"></a>
The ID of the domain list that's used in the rule.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirewallDomainRedirectionAction`  <a name="cfn-route53resolver-firewallrulegroup-firewallrule-firewalldomainredirectionaction"></a>
 How you want the the rule to evaluate DNS redirection in the DNS redirection chain, such as CNAME, or DNAME.
`Inspect_Redirection_Domain `(Default) inspects all domains in the redirection chain. The individual domains in the redirection chain must be added to the domain list.
`Trust_Redirection_Domain ` inspects only the first domain in the redirection chain. You don't need to add the subsequent domains in the domain in the redirection list to the domain list.
*Required*: No
*Type*: String
*Allowed values*: `INSPECT_REDIRECTION_DOMAIN | TRUST_REDIRECTION_DOMAIN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirewallRuleType`  <a name="cfn-route53resolver-firewallrulegroup-firewallrule-firewallruletype"></a>
The rule type configuration for the firewall rule. This is a tagged union — exactly one of its members will be populated. Possible members are:
+ `FirewallAdvancedContentCategory` — an AWS-managed content category (for example, `VIOLENCE_AND_HATE_SPEECH`).
+ `FirewallAdvancedThreatCategory` — an AWS-managed advanced threat category (for example, `PHISHING`).
+ `DnsThreatProtection` — a built-in DNS Firewall Advanced threat detector (`DGA`, `DNS_TUNNELING`, or `DICTIONARY_DGA`).
+ `PartnerThreatProtection` — a third-party threat feed delivered through AWS Marketplace.
To enumerate the values supported in your account, call ListFirewallRuleTypes.
*Required*: No
*Type*: [FirewallRuleType](aws-properties-route53resolver-firewallrulegroup-firewallruletype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirewallThreatProtectionId`  <a name="cfn-route53resolver-firewallrulegroup-firewallrule-firewallthreatprotectionid"></a>
 ID of the DNS Firewall Advanced rule.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Priority`  <a name="cfn-route53resolver-firewallrulegroup-firewallrule-priority"></a>
The priority of the rule in the rule group. This value must be unique within the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Qtype`  <a name="cfn-route53resolver-firewallrulegroup-firewallrule-qtype"></a>
 The DNS query type you want the rule to evaluate. Allowed values are;
+  A: Returns an IPv4 address.
+ AAAA: Returns an Ipv6 address.
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
+ A query type you define by using the DNS type ID, for example 28 for AAAA. The values must be defined as TYPENUMBER, where the NUMBER can be 1-65334, for example, TYPE28. For more information, see [List of DNS record types](https://en.wikipedia.org/wiki/List_of_DNS_record_types).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-route53resolver-firewallrulegroup-firewallrule-status"></a>
The lifecycle state of the firewall rule. Possible values:
+ `CREATING` — DNS Firewall is provisioning the rule. Rules created with the `PartnerThreatProtection` rule type begin in this state while DNS Firewall verifies the calling account's AWS Marketplace entitlement.
+ `COMPLETE` — The rule is provisioned and enforcing matches.
+ `CREATION_FAILED` — Provisioning failed. `StatusMessage` contains a human-readable reason. A rule in this state is immutable: UpdateFirewallRule rejects the request, and the rule must be removed with DeleteFirewallRule.
For rules that do not require asynchronous provisioning, this field may be absent.
*Required*: No
*Type*: String
*Allowed values*: `COMPLETE | CREATING | CREATION_FAILED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
