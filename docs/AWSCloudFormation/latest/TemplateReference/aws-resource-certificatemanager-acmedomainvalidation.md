---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-certificatemanager-acmedomainvalidation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CertificateManager::AcmeDomainValidation
<a name="aws-resource-certificatemanager-acmedomainvalidation"></a>

Creates a domain validation for an ACME endpoint. Domain validations authorize the endpoint to issue certificates for specified domain names. You configure prevalidation to prove domain ownership.

## Syntax
<a name="aws-resource-certificatemanager-acmedomainvalidation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-certificatemanager-acmedomainvalidation-syntax.json"></a>

```
{
  "Type" : "AWS::CertificateManager::AcmeDomainValidation",
  "Properties" : {
      "[AcmeEndpointArn](#cfn-certificatemanager-acmedomainvalidation-acmeendpointarn)" : {{String}},
      "[DomainName](#cfn-certificatemanager-acmedomainvalidation-domainname)" : {{String}},
      "[PrevalidationOptions](#cfn-certificatemanager-acmedomainvalidation-prevalidationoptions)" : {{PrevalidationOptions}},
      "[Tags](#cfn-certificatemanager-acmedomainvalidation-tags)" : {{[ TagsItems, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-certificatemanager-acmedomainvalidation-syntax.yaml"></a>

```
Type: AWS::CertificateManager::AcmeDomainValidation
Properties:
  [AcmeEndpointArn](#cfn-certificatemanager-acmedomainvalidation-acmeendpointarn): {{String}}
  [DomainName](#cfn-certificatemanager-acmedomainvalidation-domainname): {{String}}
  [PrevalidationOptions](#cfn-certificatemanager-acmedomainvalidation-prevalidationoptions): {{
    PrevalidationOptions}}
  [Tags](#cfn-certificatemanager-acmedomainvalidation-tags): {{
    - TagsItems}}
```

## Properties
<a name="aws-resource-certificatemanager-acmedomainvalidation-properties"></a>

`AcmeEndpointArn`  <a name="cfn-certificatemanager-acmedomainvalidation-acmeendpointarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainName`  <a name="cfn-certificatemanager-acmedomainvalidation-domainname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrevalidationOptions`  <a name="cfn-certificatemanager-acmedomainvalidation-prevalidationoptions"></a>
Specifies prevalidation options for domain validation.
*Required*: Yes
*Type*: [PrevalidationOptions](aws-properties-certificatemanager-acmedomainvalidation-prevalidationoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-certificatemanager-acmedomainvalidation-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-certificatemanager-acmedomainvalidation-tagsitems.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-certificatemanager-acmedomainvalidation-return-values"></a>

### Ref
<a name="aws-resource-certificatemanager-acmedomainvalidation-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-certificatemanager-acmedomainvalidation-return-values-fn--getatt"></a>

####
<a name="aws-resource-certificatemanager-acmedomainvalidation-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
