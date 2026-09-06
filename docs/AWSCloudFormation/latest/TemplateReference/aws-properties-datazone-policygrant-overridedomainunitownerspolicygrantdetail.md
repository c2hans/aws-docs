---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-policygrant-overridedomainunitownerspolicygrantdetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::PolicyGrant OverrideDomainUnitOwnersPolicyGrantDetail
<a name="aws-properties-datazone-policygrant-overridedomainunitownerspolicygrantdetail"></a>

The grant details of the override domain unit owners policy.

## Syntax
<a name="aws-properties-datazone-policygrant-overridedomainunitownerspolicygrantdetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-policygrant-overridedomainunitownerspolicygrantdetail-syntax.json"></a>

```
{
  "[IncludeChildDomainUnits](#cfn-datazone-policygrant-overridedomainunitownerspolicygrantdetail-includechilddomainunits)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-datazone-policygrant-overridedomainunitownerspolicygrantdetail-syntax.yaml"></a>

```
  [IncludeChildDomainUnits](#cfn-datazone-policygrant-overridedomainunitownerspolicygrantdetail-includechilddomainunits): {{Boolean}}
```

## Properties
<a name="aws-properties-datazone-policygrant-overridedomainunitownerspolicygrantdetail-properties"></a>

`IncludeChildDomainUnits`  <a name="cfn-datazone-policygrant-overridedomainunitownerspolicygrantdetail-includechilddomainunits"></a>
Specifies whether the policy is inherited by child domain units.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
