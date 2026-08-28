---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rolesanywhere-profile-mappingrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RolesAnywhere::Profile MappingRule
<a name="aws-properties-rolesanywhere-profile-mappingrule"></a>

A single mapping entry for each supported specifier or sub-field.

## Syntax
<a name="aws-properties-rolesanywhere-profile-mappingrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rolesanywhere-profile-mappingrule-syntax.json"></a>

```
{
  "[Specifier](#cfn-rolesanywhere-profile-mappingrule-specifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-rolesanywhere-profile-mappingrule-syntax.yaml"></a>

```
  [Specifier](#cfn-rolesanywhere-profile-mappingrule-specifier): {{String}}
```

## Properties
<a name="aws-properties-rolesanywhere-profile-mappingrule-properties"></a>

`Specifier`  <a name="cfn-rolesanywhere-profile-mappingrule-specifier"></a>
Specifier within a certificate field, such as CN, OU, or UID from the Subject field.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
