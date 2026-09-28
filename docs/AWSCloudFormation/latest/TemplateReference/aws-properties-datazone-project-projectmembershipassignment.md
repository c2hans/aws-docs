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
*Pattern*: `^[a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Member`  <a name="cfn-datazone-project-projectmembershipassignment-member"></a>
Property description not available.
*Required*: Yes
*Type*: [Member](aws-properties-datazone-project-member.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
