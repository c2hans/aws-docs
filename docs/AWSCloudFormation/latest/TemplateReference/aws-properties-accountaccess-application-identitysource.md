---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accountaccess-application-identitysource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccountAccess::Application IdentitySource
<a name="aws-properties-accountaccess-application-identitysource"></a>

Specifies the identity source for an account access manager application.

## Syntax
<a name="aws-properties-accountaccess-application-identitysource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accountaccess-application-identitysource-syntax.json"></a>

```
{
  "[IdentityCenter](#cfn-accountaccess-application-identitysource-identitycenter)" : {{IdentityCenter}}
}
```

### YAML
<a name="aws-properties-accountaccess-application-identitysource-syntax.yaml"></a>

```
  [IdentityCenter](#cfn-accountaccess-application-identitysource-identitycenter): {{
    IdentityCenter}}
```

## Properties
<a name="aws-properties-accountaccess-application-identitysource-properties"></a>

`IdentityCenter`  <a name="cfn-accountaccess-application-identitysource-identitycenter"></a>
The IAM Identity Center instance to use as the identity source.
*Required*: Yes
*Type*: [IdentityCenter](aws-properties-accountaccess-application-identitycenter.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
