---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-projectmembership-member.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::ProjectMembership Member
<a name="aws-properties-datazone-projectmembership-member"></a>

The details about a project member.

Important - this data type is a UNION, so only one of the following members can be specified when used or returned.

## Syntax
<a name="aws-properties-datazone-projectmembership-member-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-projectmembership-member-syntax.json"></a>

```
{
  "[GroupIdentifier](#cfn-datazone-projectmembership-member-groupidentifier)" : {{String}},
  "[UserIdentifier](#cfn-datazone-projectmembership-member-useridentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-projectmembership-member-syntax.yaml"></a>

```
  [GroupIdentifier](#cfn-datazone-projectmembership-member-groupidentifier): {{String}}
  [UserIdentifier](#cfn-datazone-projectmembership-member-useridentifier): {{String}}
```

## Properties
<a name="aws-properties-datazone-projectmembership-member-properties"></a>

`GroupIdentifier`  <a name="cfn-datazone-projectmembership-member-groupidentifier"></a>
The ID of the group of a project member.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserIdentifier`  <a name="cfn-datazone-projectmembership-member-useridentifier"></a>
The user ID of a project member.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
