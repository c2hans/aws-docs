---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-identitypoolroleattachment-rulesconfigurationtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::IdentityPoolRoleAttachment RulesConfigurationType
<a name="aws-properties-cognito-identitypoolroleattachment-rulesconfigurationtype"></a>

`RulesConfigurationType` is a subproperty of the [RoleMapping](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping.html) property that defines the rules to be used for mapping users to roles.

## Syntax
<a name="aws-properties-cognito-identitypoolroleattachment-rulesconfigurationtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-identitypoolroleattachment-rulesconfigurationtype-syntax.json"></a>

```
{
  "[Rules](#cfn-cognito-identitypoolroleattachment-rulesconfigurationtype-rules)" : {{[ MappingRule, ... ]}}
}
```

### YAML
<a name="aws-properties-cognito-identitypoolroleattachment-rulesconfigurationtype-syntax.yaml"></a>

```
  [Rules](#cfn-cognito-identitypoolroleattachment-rulesconfigurationtype-rules): {{
    - MappingRule}}
```

## Properties
<a name="aws-properties-cognito-identitypoolroleattachment-rulesconfigurationtype-properties"></a>

`Rules`  <a name="cfn-cognito-identitypoolroleattachment-rulesconfigurationtype-rules"></a>
The rules. You can specify up to 25 rules per identity provider.
*Required*: Yes
*Type*: Array of [MappingRule](aws-properties-cognito-identitypoolroleattachment-mappingrule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
