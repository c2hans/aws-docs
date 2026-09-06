---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-policygrant-domainunitfilterforproject.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::PolicyGrant DomainUnitFilterForProject
<a name="aws-properties-datazone-policygrant-domainunitfilterforproject"></a>

The domain unit filter of the project grant filter.

## Syntax
<a name="aws-properties-datazone-policygrant-domainunitfilterforproject-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-policygrant-domainunitfilterforproject-syntax.json"></a>

```
{
  "[DomainUnit](#cfn-datazone-policygrant-domainunitfilterforproject-domainunit)" : {{String}},
  "[IncludeChildDomainUnits](#cfn-datazone-policygrant-domainunitfilterforproject-includechilddomainunits)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-datazone-policygrant-domainunitfilterforproject-syntax.yaml"></a>

```
  [DomainUnit](#cfn-datazone-policygrant-domainunitfilterforproject-domainunit): {{String}}
  [IncludeChildDomainUnits](#cfn-datazone-policygrant-domainunitfilterforproject-includechilddomainunits): {{Boolean}}
```

## Properties
<a name="aws-properties-datazone-policygrant-domainunitfilterforproject-properties"></a>

`DomainUnit`  <a name="cfn-datazone-policygrant-domainunitfilterforproject-domainunit"></a>
The domain unit ID to use in the filter.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9_\-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IncludeChildDomainUnits`  <a name="cfn-datazone-policygrant-domainunitfilterforproject-includechilddomainunits"></a>
Specifies whether to include child domain units.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
