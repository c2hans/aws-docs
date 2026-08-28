---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-policygrant-domainunitgrantfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::PolicyGrant DomainUnitGrantFilter
<a name="aws-properties-datazone-policygrant-domainunitgrantfilter"></a>

The grant filter for the domain unit. In the current release of Amazon DataZone, the only supported filter is the `allDomainUnitsGrantFilter`.

## Syntax
<a name="aws-properties-datazone-policygrant-domainunitgrantfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-policygrant-domainunitgrantfilter-syntax.json"></a>

```
{
  "[AllDomainUnitsGrantFilter](#cfn-datazone-policygrant-domainunitgrantfilter-alldomainunitsgrantfilter)" : {{Json}}
}
```

### YAML
<a name="aws-properties-datazone-policygrant-domainunitgrantfilter-syntax.yaml"></a>

```
  [AllDomainUnitsGrantFilter](#cfn-datazone-policygrant-domainunitgrantfilter-alldomainunitsgrantfilter): {{Json}}
```

## Properties
<a name="aws-properties-datazone-policygrant-domainunitgrantfilter-properties"></a>

`AllDomainUnitsGrantFilter`  <a name="cfn-datazone-policygrant-domainunitgrantfilter-alldomainunitsgrantfilter"></a>
Specifies a grant filter containing all domain units.
*Required*: Yes
*Type*: Json
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
