---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mpa-identitysource-identitysourceparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MPA::IdentitySource IdentitySourceParameters
<a name="aws-properties-mpa-identitysource-identitysourceparameters"></a>

Contains details for the resource that provides identities to the identity source. For example, an IAM Identity Center instance.

## Syntax
<a name="aws-properties-mpa-identitysource-identitysourceparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mpa-identitysource-identitysourceparameters-syntax.json"></a>

```
{
  "[IamIdentityCenter](#cfn-mpa-identitysource-identitysourceparameters-iamidentitycenter)" : {{IamIdentityCenter}}
}
```

### YAML
<a name="aws-properties-mpa-identitysource-identitysourceparameters-syntax.yaml"></a>

```
  [IamIdentityCenter](#cfn-mpa-identitysource-identitysourceparameters-iamidentitycenter): {{
    IamIdentityCenter}}
```

## Properties
<a name="aws-properties-mpa-identitysource-identitysourceparameters-properties"></a>

`IamIdentityCenter`  <a name="cfn-mpa-identitysource-identitysourceparameters-iamidentitycenter"></a>
AWS IAM Identity Center credentials.
*Required*: Yes
*Type*: [IamIdentityCenter](aws-properties-mpa-identitysource-iamidentitycenter.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
