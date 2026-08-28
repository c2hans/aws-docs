---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53globalresolver-firewallrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53GlobalResolver::FirewallRule
<a name="aws-resource-route53globalresolver-firewallrule"></a>

Creates a DNS firewall rule. Firewall rules define actions (ALLOW, BLOCK, or ALERT) to take on DNS queries that match specified domain lists, managed domain lists, or advanced threat protections.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Syntax
<a name="aws-resource-route53globalresolver-firewallrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53globalresolver-firewallrule-syntax.json"></a>

```
{
  "Type" : "AWS::Route53GlobalResolver::FirewallRule",
  "Properties" : {
      "[Action](#cfn-route53globalresolver-firewallrule-action)" : {{String}},
      "[BlockOverrideDnsType](#cfn-route53globalresolver-firewallrule-blockoverridednstype)" : {{String}},
      "[BlockOverrideDomain](#cfn-route53globalresolver-firewallrule-blockoverridedomain)" : {{String}},
      "[BlockOverrideTtl](#cfn-route53globalresolver-firewallrule-blockoverridettl)" : {{Integer}},
      "[BlockResponse](#cfn-route53globalresolver-firewallrule-blockresponse)" : {{String}},
      "[ClientToken](#cfn-route53globalresolver-firewallrule-clienttoken)" : {{String}},
      "[ConfidenceThreshold](#cfn-route53globalresolver-firewallrule-confidencethreshold)" : {{String}},
      "[Description](#cfn-route53globalresolver-firewallrule-description)" : {{String}},
      "[DnsAdvancedProtection](#cfn-route53globalresolver-firewallrule-dnsadvancedprotection)" : {{String}},
      "[DnsViewId](#cfn-route53globalresolver-firewallrule-dnsviewid)" : {{String}},
      "[FirewallDomainListId](#cfn-route53globalresolver-firewallrule-firewalldomainlistid)" : {{String}},
      "[Name](#cfn-route53globalresolver-firewallrule-name)" : {{String}},
      "[Priority](#cfn-route53globalresolver-firewallrule-priority)" : {{Integer}},
      "[QType](#cfn-route53globalresolver-firewallrule-qtype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-route53globalresolver-firewallrule-syntax.yaml"></a>

```
Type: AWS::Route53GlobalResolver::FirewallRule
Properties:
  [Action](#cfn-route53globalresolver-firewallrule-action): {{String}}
  [BlockOverrideDnsType](#cfn-route53globalresolver-firewallrule-blockoverridednstype): {{String}}
  [BlockOverrideDomain](#cfn-route53globalresolver-firewallrule-blockoverridedomain): {{String}}
  [BlockOverrideTtl](#cfn-route53globalresolver-firewallrule-blockoverridettl): {{Integer}}
  [BlockResponse](#cfn-route53globalresolver-firewallrule-blockresponse): {{String}}
  [ClientToken](#cfn-route53globalresolver-firewallrule-clienttoken): {{String}}
  [ConfidenceThreshold](#cfn-route53globalresolver-firewallrule-confidencethreshold): {{String}}
  [Description](#cfn-route53globalresolver-firewallrule-description): {{String}}
  [DnsAdvancedProtection](#cfn-route53globalresolver-firewallrule-dnsadvancedprotection): {{String}}
  [DnsViewId](#cfn-route53globalresolver-firewallrule-dnsviewid): {{String}}
  [FirewallDomainListId](#cfn-route53globalresolver-firewallrule-firewalldomainlistid): {{String}}
  [Name](#cfn-route53globalresolver-firewallrule-name): {{String}}
  [Priority](#cfn-route53globalresolver-firewallrule-priority): {{Integer}}
  [QType](#cfn-route53globalresolver-firewallrule-qtype): {{String}}
```

## Properties
<a name="aws-resource-route53globalresolver-firewallrule-properties"></a>

`Action`  <a name="cfn-route53globalresolver-firewallrule-action"></a>
The action configured for the updated firewall rule.
*Required*: Yes
*Type*: String
*Allowed values*: `ALLOW | ALERT | BLOCK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockOverrideDnsType`  <a name="cfn-route53globalresolver-firewallrule-blockoverridednstype"></a>
The DNS record type configured for the updated firewall rule's custom response.
*Required*: No
*Type*: String
*Allowed values*: `CNAME`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockOverrideDomain`  <a name="cfn-route53globalresolver-firewallrule-blockoverridedomain"></a>
The custom domain name configured for the updated firewall rule's BLOCK response.
*Required*: No
*Type*: String
*Pattern*: `\*?[-a-zA-Z0-9.]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockOverrideTtl`  <a name="cfn-route53globalresolver-firewallrule-blockoverridettl"></a>
The TTL value configured for the updated firewall rule's custom response.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `604800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockResponse`  <a name="cfn-route53globalresolver-firewallrule-blockresponse"></a>
The type of block response configured for the updated firewall rule.
*Required*: No
*Type*: String
*Allowed values*: `NODATA | NXDOMAIN | OVERRIDE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientToken`  <a name="cfn-route53globalresolver-firewallrule-clienttoken"></a>
The unique string that identified the request and ensured idempotency.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConfidenceThreshold`  <a name="cfn-route53globalresolver-firewallrule-confidencethreshold"></a>
The confidence threshold configured for the updated firewall rule's advanced threat detection.
*Required*: No
*Type*: String
*Allowed values*: `LOW | MEDIUM | HIGH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-route53globalresolver-firewallrule-description"></a>
The description of the updated firewall rule.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DnsAdvancedProtection`  <a name="cfn-route53globalresolver-firewallrule-dnsadvancedprotection"></a>
Whether advanced DNS threat protection is enabled for the updated firewall rule.
*Required*: No
*Type*: String
*Allowed values*: `DGA | DNS_TUNNELING | DICTIONARY_DGA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DnsViewId`  <a name="cfn-route53globalresolver-firewallrule-dnsviewid"></a>
The ID of the DNS view associated with the updated firewall rule.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FirewallDomainListId`  <a name="cfn-route53globalresolver-firewallrule-firewalldomainlistid"></a>
The ID of the firewall domain list associated with the updated firewall rule.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-route53globalresolver-firewallrule-name"></a>
The name of the updated firewall rule.
*Required*: Yes
*Type*: String
*Pattern*: `(?!^[0-9]+$)([a-zA-Z0-9-_' ']+)`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Priority`  <a name="cfn-route53globalresolver-firewallrule-priority"></a>
The priority of the updated firewall rule.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QType`  <a name="cfn-route53globalresolver-firewallrule-qtype"></a>
The DNS query type that the firewall rule should match.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-route53globalresolver-firewallrule-return-values"></a>

### Ref
<a name="aws-resource-route53globalresolver-firewallrule-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-route53globalresolver-firewallrule-return-values-fn--getatt"></a>

####
<a name="aws-resource-route53globalresolver-firewallrule-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the firewall rule was originally created.

`FirewallRuleId`  <a name="FirewallRuleId-fn::getatt"></a>
The unique identifier of the firewall rule to update.

`QueryType`  <a name="QueryType-fn::getatt"></a>
The DNS query type that the updated firewall rule matches.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the updated firewall rule.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the firewall rule was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
