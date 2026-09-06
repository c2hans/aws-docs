---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-certificatemanager-acmedomainvalidation-prevalidationoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CertificateManager::AcmeDomainValidation PrevalidationOptions
<a name="aws-properties-certificatemanager-acmedomainvalidation-prevalidationoptions"></a>

Specifies prevalidation options for domain validation.

## Syntax
<a name="aws-properties-certificatemanager-acmedomainvalidation-prevalidationoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-certificatemanager-acmedomainvalidation-prevalidationoptions-syntax.json"></a>

```
{
  "[DnsPrevalidation](#cfn-certificatemanager-acmedomainvalidation-prevalidationoptions-dnsprevalidation)" : {{DnsPrevalidationOptions}}
}
```

### YAML
<a name="aws-properties-certificatemanager-acmedomainvalidation-prevalidationoptions-syntax.yaml"></a>

```
  [DnsPrevalidation](#cfn-certificatemanager-acmedomainvalidation-prevalidationoptions-dnsprevalidation): {{
    DnsPrevalidationOptions}}
```

## Properties
<a name="aws-properties-certificatemanager-acmedomainvalidation-prevalidationoptions-properties"></a>

`DnsPrevalidation`  <a name="cfn-certificatemanager-acmedomainvalidation-prevalidationoptions-dnsprevalidation"></a>
DNS-based prevalidation options.
*Required*: Yes
*Type*: [DnsPrevalidationOptions](aws-properties-certificatemanager-acmedomainvalidation-dnsprevalidationoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
