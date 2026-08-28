---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-policygrant-createdomainunitpolicygrantdetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::PolicyGrant CreateDomainUnitPolicyGrantDetail
<a name="aws-properties-datazone-policygrant-createdomainunitpolicygrantdetail"></a>

The details of the policy grant.

## Syntax
<a name="aws-properties-datazone-policygrant-createdomainunitpolicygrantdetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-policygrant-createdomainunitpolicygrantdetail-syntax.json"></a>

```
{
  "[IncludeChildDomainUnits](#cfn-datazone-policygrant-createdomainunitpolicygrantdetail-includechilddomainunits)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-datazone-policygrant-createdomainunitpolicygrantdetail-syntax.yaml"></a>

```
  [IncludeChildDomainUnits](#cfn-datazone-policygrant-createdomainunitpolicygrantdetail-includechilddomainunits): {{Boolean}}
```

## Properties
<a name="aws-properties-datazone-policygrant-createdomainunitpolicygrantdetail-properties"></a>

`IncludeChildDomainUnits`  <a name="cfn-datazone-policygrant-createdomainunitpolicygrantdetail-includechilddomainunits"></a>
Specifies whether the policy grant is applied to child domain units.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
