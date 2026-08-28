---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-owner-ownerproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Owner OwnerProperties
<a name="aws-properties-datazone-owner-ownerproperties"></a>

The properties of a domain unit's owner.

## Syntax
<a name="aws-properties-datazone-owner-ownerproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-owner-ownerproperties-syntax.json"></a>

```
{
  "[Group](#cfn-datazone-owner-ownerproperties-group)" : {{OwnerGroupProperties}},
  "[User](#cfn-datazone-owner-ownerproperties-user)" : {{OwnerUserProperties}}
}
```

### YAML
<a name="aws-properties-datazone-owner-ownerproperties-syntax.yaml"></a>

```
  [Group](#cfn-datazone-owner-ownerproperties-group): {{
    OwnerGroupProperties}}
  [User](#cfn-datazone-owner-ownerproperties-user): {{
    OwnerUserProperties}}
```

## Properties
<a name="aws-properties-datazone-owner-ownerproperties-properties"></a>

`Group`  <a name="cfn-datazone-owner-ownerproperties-group"></a>
Specifies that the domain unit owner is a group.
*Required*: No
*Type*: [OwnerGroupProperties](aws-properties-datazone-owner-ownergroupproperties.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`User`  <a name="cfn-datazone-owner-ownerproperties-user"></a>
Specifies that the domain unit owner is a user.
*Required*: No
*Type*: [OwnerUserProperties](aws-properties-datazone-owner-owneruserproperties.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
