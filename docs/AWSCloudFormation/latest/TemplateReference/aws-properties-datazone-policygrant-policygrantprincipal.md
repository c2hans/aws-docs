---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-policygrant-policygrantprincipal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::PolicyGrant PolicyGrantPrincipal
<a name="aws-properties-datazone-policygrant-policygrantprincipal"></a>

The policy grant principal.

## Syntax
<a name="aws-properties-datazone-policygrant-policygrantprincipal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-policygrant-policygrantprincipal-syntax.json"></a>

```
{
  "[DomainUnit](#cfn-datazone-policygrant-policygrantprincipal-domainunit)" : {{DomainUnitPolicyGrantPrincipal}},
  "[Group](#cfn-datazone-policygrant-policygrantprincipal-group)" : {{GroupPolicyGrantPrincipal}},
  "[Project](#cfn-datazone-policygrant-policygrantprincipal-project)" : {{ProjectPolicyGrantPrincipal}},
  "[User](#cfn-datazone-policygrant-policygrantprincipal-user)" : {{UserPolicyGrantPrincipal}}
}
```

### YAML
<a name="aws-properties-datazone-policygrant-policygrantprincipal-syntax.yaml"></a>

```
  [DomainUnit](#cfn-datazone-policygrant-policygrantprincipal-domainunit): {{
    DomainUnitPolicyGrantPrincipal}}
  [Group](#cfn-datazone-policygrant-policygrantprincipal-group): {{
    GroupPolicyGrantPrincipal}}
  [Project](#cfn-datazone-policygrant-policygrantprincipal-project): {{
    ProjectPolicyGrantPrincipal}}
  [User](#cfn-datazone-policygrant-policygrantprincipal-user): {{
    UserPolicyGrantPrincipal}}
```

## Properties
<a name="aws-properties-datazone-policygrant-policygrantprincipal-properties"></a>

`DomainUnit`  <a name="cfn-datazone-policygrant-policygrantprincipal-domainunit"></a>
The domain unit of the policy grant principal.
*Required*: No
*Type*: [DomainUnitPolicyGrantPrincipal](aws-properties-datazone-policygrant-domainunitpolicygrantprincipal.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Group`  <a name="cfn-datazone-policygrant-policygrantprincipal-group"></a>
The group of the policy grant principal.
*Required*: No
*Type*: [GroupPolicyGrantPrincipal](aws-properties-datazone-policygrant-grouppolicygrantprincipal.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Project`  <a name="cfn-datazone-policygrant-policygrantprincipal-project"></a>
The project of the policy grant principal.
*Required*: No
*Type*: [ProjectPolicyGrantPrincipal](aws-properties-datazone-policygrant-projectpolicygrantprincipal.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`User`  <a name="cfn-datazone-policygrant-policygrantprincipal-user"></a>
The user of the policy grant principal.
*Required*: No
*Type*: [UserPolicyGrantPrincipal](aws-properties-datazone-policygrant-userpolicygrantprincipal.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
