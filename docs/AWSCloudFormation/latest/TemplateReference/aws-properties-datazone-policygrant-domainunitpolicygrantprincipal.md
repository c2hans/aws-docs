---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-policygrant-domainunitpolicygrantprincipal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::PolicyGrant DomainUnitPolicyGrantPrincipal
<a name="aws-properties-datazone-policygrant-domainunitpolicygrantprincipal"></a>

The domain unit principal to whom the policy is granted.

## Syntax
<a name="aws-properties-datazone-policygrant-domainunitpolicygrantprincipal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-policygrant-domainunitpolicygrantprincipal-syntax.json"></a>

```
{
  "[DomainUnitDesignation](#cfn-datazone-policygrant-domainunitpolicygrantprincipal-domainunitdesignation)" : {{String}},
  "[DomainUnitGrantFilter](#cfn-datazone-policygrant-domainunitpolicygrantprincipal-domainunitgrantfilter)" : {{DomainUnitGrantFilter}},
  "[DomainUnitIdentifier](#cfn-datazone-policygrant-domainunitpolicygrantprincipal-domainunitidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-policygrant-domainunitpolicygrantprincipal-syntax.yaml"></a>

```
  [DomainUnitDesignation](#cfn-datazone-policygrant-domainunitpolicygrantprincipal-domainunitdesignation): {{String}}
  [DomainUnitGrantFilter](#cfn-datazone-policygrant-domainunitpolicygrantprincipal-domainunitgrantfilter): {{
    DomainUnitGrantFilter}}
  [DomainUnitIdentifier](#cfn-datazone-policygrant-domainunitpolicygrantprincipal-domainunitidentifier): {{String}}
```

## Properties
<a name="aws-properties-datazone-policygrant-domainunitpolicygrantprincipal-properties"></a>

`DomainUnitDesignation`  <a name="cfn-datazone-policygrant-domainunitpolicygrantprincipal-domainunitdesignation"></a>
Specifes the designation of the domain unit users.
*Required*: No
*Type*: String
*Allowed values*: `OWNER`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainUnitGrantFilter`  <a name="cfn-datazone-policygrant-domainunitpolicygrantprincipal-domainunitgrantfilter"></a>
The grant filter for the domain unit.
*Required*: No
*Type*: [DomainUnitGrantFilter](aws-properties-datazone-policygrant-domainunitgrantfilter.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainUnitIdentifier`  <a name="cfn-datazone-policygrant-domainunitpolicygrantprincipal-domainunitidentifier"></a>
The ID of the domain unit.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9_\-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
