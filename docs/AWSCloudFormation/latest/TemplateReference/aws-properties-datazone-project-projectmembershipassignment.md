---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-project-projectmembershipassignment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Project ProjectMembershipAssignment
<a name="aws-properties-datazone-project-projectmembershipassignment"></a>

<a name="aws-properties-datazone-project-projectmembershipassignment-description"></a>The `ProjectMembershipAssignment` property type specifies Property description not available. for an [AWS::DataZone::Project](aws-resource-datazone-project.md).

## Syntax
<a name="aws-properties-datazone-project-projectmembershipassignment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-project-projectmembershipassignment-syntax.json"></a>

```
{
  "[Designation](#cfn-datazone-project-projectmembershipassignment-designation)" : {{String}},
  "[Member](#cfn-datazone-project-projectmembershipassignment-member)" : {{Member}}
}
```

### YAML
<a name="aws-properties-datazone-project-projectmembershipassignment-syntax.yaml"></a>

```
  [Designation](#cfn-datazone-project-projectmembershipassignment-designation): {{String}}
  [Member](#cfn-datazone-project-projectmembershipassignment-member): {{
    Member}}
```

## Properties
<a name="aws-properties-datazone-project-projectmembershipassignment-properties"></a>

`Designation`  <a name="cfn-datazone-project-projectmembershipassignment-designation"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `PROJECT_OWNER | PROJECT_CONTRIBUTOR`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Member`  <a name="cfn-datazone-project-projectmembershipassignment-member"></a>
Property description not available.
*Required*: Yes
*Type*: [Member](aws-properties-datazone-project-member.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
