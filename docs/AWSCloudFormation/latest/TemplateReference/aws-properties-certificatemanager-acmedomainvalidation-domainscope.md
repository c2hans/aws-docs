---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-certificatemanager-acmedomainvalidation-domainscope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CertificateManager::AcmeDomainValidation DomainScope
<a name="aws-properties-certificatemanager-acmedomainvalidation-domainscope"></a>

Specifies the scope of domain validation.

## Syntax
<a name="aws-properties-certificatemanager-acmedomainvalidation-domainscope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-certificatemanager-acmedomainvalidation-domainscope-syntax.json"></a>

```
{
  "[ExactDomain](#cfn-certificatemanager-acmedomainvalidation-domainscope-exactdomain)" : {{String}},
  "[Subdomains](#cfn-certificatemanager-acmedomainvalidation-domainscope-subdomains)" : {{String}},
  "[Wildcards](#cfn-certificatemanager-acmedomainvalidation-domainscope-wildcards)" : {{String}}
}
```

### YAML
<a name="aws-properties-certificatemanager-acmedomainvalidation-domainscope-syntax.yaml"></a>

```
  [ExactDomain](#cfn-certificatemanager-acmedomainvalidation-domainscope-exactdomain): {{String}}
  [Subdomains](#cfn-certificatemanager-acmedomainvalidation-domainscope-subdomains): {{String}}
  [Wildcards](#cfn-certificatemanager-acmedomainvalidation-domainscope-wildcards): {{String}}
```

## Properties
<a name="aws-properties-certificatemanager-acmedomainvalidation-domainscope-properties"></a>

`ExactDomain`  <a name="cfn-certificatemanager-acmedomainvalidation-domainscope-exactdomain"></a>
Whether validation applies to the exact domain.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subdomains`  <a name="cfn-certificatemanager-acmedomainvalidation-domainscope-subdomains"></a>
Whether validation applies to subdomains.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Wildcards`  <a name="cfn-certificatemanager-acmedomainvalidation-domainscope-wildcards"></a>
Whether validation applies to wildcard domains.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
