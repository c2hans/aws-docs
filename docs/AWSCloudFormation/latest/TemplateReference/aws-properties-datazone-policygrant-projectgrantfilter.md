---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-policygrant-projectgrantfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::PolicyGrant ProjectGrantFilter
<a name="aws-properties-datazone-policygrant-projectgrantfilter"></a>

The project grant filter.

## Syntax
<a name="aws-properties-datazone-policygrant-projectgrantfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-policygrant-projectgrantfilter-syntax.json"></a>

```
{
  "[DomainUnitFilter](#cfn-datazone-policygrant-projectgrantfilter-domainunitfilter)" : {{DomainUnitFilterForProject}}
}
```

### YAML
<a name="aws-properties-datazone-policygrant-projectgrantfilter-syntax.yaml"></a>

```
  [DomainUnitFilter](#cfn-datazone-policygrant-projectgrantfilter-domainunitfilter): {{
    DomainUnitFilterForProject}}
```

## Properties
<a name="aws-properties-datazone-policygrant-projectgrantfilter-properties"></a>

`DomainUnitFilter`  <a name="cfn-datazone-policygrant-projectgrantfilter-domainunitfilter"></a>
The domain unit filter of the project grant filter.
*Required*: Yes
*Type*: [DomainUnitFilterForProject](aws-properties-datazone-policygrant-domainunitfilterforproject.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
