---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-policygrant-createenvironmentprofilepolicygrantdetail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::PolicyGrant CreateEnvironmentProfilePolicyGrantDetail
<a name="aws-properties-datazone-policygrant-createenvironmentprofilepolicygrantdetail"></a>

The details of the policy grant.

## Syntax
<a name="aws-properties-datazone-policygrant-createenvironmentprofilepolicygrantdetail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-policygrant-createenvironmentprofilepolicygrantdetail-syntax.json"></a>

```
{
  "[DomainUnitId](#cfn-datazone-policygrant-createenvironmentprofilepolicygrantdetail-domainunitid)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-policygrant-createenvironmentprofilepolicygrantdetail-syntax.yaml"></a>

```
  [DomainUnitId](#cfn-datazone-policygrant-createenvironmentprofilepolicygrantdetail-domainunitid): {{String}}
```

## Properties
<a name="aws-properties-datazone-policygrant-createenvironmentprofilepolicygrantdetail-properties"></a>

`DomainUnitId`  <a name="cfn-datazone-policygrant-createenvironmentprofilepolicygrantdetail-domainunitid"></a>
The ID of the domain unit.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9_\-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
