---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accountaccess-entitlement-entitlement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccountAccess::Entitlement Entitlement
<a name="aws-properties-accountaccess-entitlement-entitlement"></a>

Specifies the entitlement configuration for an account access manager application, defining which principal can assume which IAM role.

## Syntax
<a name="aws-properties-accountaccess-entitlement-entitlement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accountaccess-entitlement-entitlement-syntax.json"></a>

```
{
  "[PrincipalRole](#cfn-accountaccess-entitlement-entitlement-principalrole)" : {{PrincipalRoleEntitlement}}
}
```

### YAML
<a name="aws-properties-accountaccess-entitlement-entitlement-syntax.yaml"></a>

```
  [PrincipalRole](#cfn-accountaccess-entitlement-entitlement-principalrole): {{
    PrincipalRoleEntitlement}}
```

## Properties
<a name="aws-properties-accountaccess-entitlement-entitlement-properties"></a>

`PrincipalRole`  <a name="cfn-accountaccess-entitlement-entitlement-principalrole"></a>
The principal-to-role mapping for the entitlement.
*Required*: Yes
*Type*: [PrincipalRoleEntitlement](aws-properties-accountaccess-entitlement-principalroleentitlement.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
