---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSO::InstanceAccessControlAttributeConfiguration AccessControlAttribute
<a name="aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute"></a>

These are IAM Identity Center identity store attributes that you can configure for use in attributes-based access control (ABAC). You can create permissions policies that determine who can access your AWS resources based upon the configured attribute values. When you enable ABAC and specify `AccessControlAttributes`, IAM Identity Center passes the attribute values of the authenticated user into IAM for use in policy evaluation.

## Syntax
<a name="aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-syntax.json"></a>

```
{
  "[Key](#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-key)" : {{String}},
  "[Value](#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-value)" : {{AccessControlAttributeValue}}
}
```

### YAML
<a name="aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-syntax.yaml"></a>

```
  [Key](#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-key): {{String}}
  [Value](#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-value): {{
    AccessControlAttributeValue}}
```

## Properties
<a name="aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-properties"></a>

`Key`  <a name="cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-key"></a>
The name of the attribute associated with your identities in your identity source. This is used to map a specified attribute in your identity source with an attribute in IAM Identity Center.
*Required*: Yes
*Type*: String
*Pattern*: `[\p{L}\p{Z}\p{N}_.:\/=+\-@]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-value"></a>
The value used for mapping a specified attribute to an identity source.
*Required*: Yes
*Type*: [AccessControlAttributeValue](aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
