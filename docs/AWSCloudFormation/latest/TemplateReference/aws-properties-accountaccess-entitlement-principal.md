---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accountaccess-entitlement-principal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccountAccess::Entitlement Principal
<a name="aws-properties-accountaccess-entitlement-principal"></a>

Identifies a principal (user or group) that can be granted entitlements.

## Syntax
<a name="aws-properties-accountaccess-entitlement-principal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accountaccess-entitlement-principal-syntax.json"></a>

```
{
  "[IdentityCenter](#cfn-accountaccess-entitlement-principal-identitycenter)" : {{IdentityCenterPrincipal}}
}
```

### YAML
<a name="aws-properties-accountaccess-entitlement-principal-syntax.yaml"></a>

```
  [IdentityCenter](#cfn-accountaccess-entitlement-principal-identitycenter): {{
    IdentityCenterPrincipal}}
```

## Properties
<a name="aws-properties-accountaccess-entitlement-principal-properties"></a>

`IdentityCenter`  <a name="cfn-accountaccess-entitlement-principal-identitycenter"></a>
The IAM Identity Center principal (user or group).
*Required*: Yes
*Type*: [IdentityCenterPrincipal](aws-properties-accountaccess-entitlement-identitycenterprincipal.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
