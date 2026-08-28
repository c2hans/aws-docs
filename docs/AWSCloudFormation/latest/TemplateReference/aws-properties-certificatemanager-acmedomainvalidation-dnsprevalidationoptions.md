---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-certificatemanager-acmedomainvalidation-dnsprevalidationoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CertificateManager::AcmeDomainValidation DnsPrevalidationOptions
<a name="aws-properties-certificatemanager-acmedomainvalidation-dnsprevalidationoptions"></a>

DNS prevalidation options for domain validation.

## Syntax
<a name="aws-properties-certificatemanager-acmedomainvalidation-dnsprevalidationoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-certificatemanager-acmedomainvalidation-dnsprevalidationoptions-syntax.json"></a>

```
{
  "[DomainScope](#cfn-certificatemanager-acmedomainvalidation-dnsprevalidationoptions-domainscope)" : {{DomainScope}},
  "[HostedZoneId](#cfn-certificatemanager-acmedomainvalidation-dnsprevalidationoptions-hostedzoneid)" : {{String}}
}
```

### YAML
<a name="aws-properties-certificatemanager-acmedomainvalidation-dnsprevalidationoptions-syntax.yaml"></a>

```
  [DomainScope](#cfn-certificatemanager-acmedomainvalidation-dnsprevalidationoptions-domainscope): {{
    DomainScope}}
  [HostedZoneId](#cfn-certificatemanager-acmedomainvalidation-dnsprevalidationoptions-hostedzoneid): {{String}}
```

## Properties
<a name="aws-properties-certificatemanager-acmedomainvalidation-dnsprevalidationoptions-properties"></a>

`DomainScope`  <a name="cfn-certificatemanager-acmedomainvalidation-dnsprevalidationoptions-domainscope"></a>
The scope of domains covered by this prevalidation.
*Required*: No
*Type*: [DomainScope](aws-properties-certificatemanager-acmedomainvalidation-domainscope.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostedZoneId`  <a name="cfn-certificatemanager-acmedomainvalidation-dnsprevalidationoptions-hostedzoneid"></a>
The Route 53 hosted zone ID for DNS validation.
*Required*: No
*Type*: String
*Pattern*: `Z[A-Z0-9]+`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
