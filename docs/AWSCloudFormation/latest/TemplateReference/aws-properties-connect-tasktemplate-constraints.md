---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-tasktemplate-constraints.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::TaskTemplate Constraints
<a name="aws-properties-connect-tasktemplate-constraints"></a>

Describes constraints that apply to the template fields.

## Syntax
<a name="aws-properties-connect-tasktemplate-constraints-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-tasktemplate-constraints-syntax.json"></a>

```
{
  "[InvisibleFields](#cfn-connect-tasktemplate-constraints-invisiblefields)" : {{[ InvisibleFieldInfo, ... ]}},
  "[ReadOnlyFields](#cfn-connect-tasktemplate-constraints-readonlyfields)" : {{[ ReadOnlyFieldInfo, ... ]}},
  "[RequiredFields](#cfn-connect-tasktemplate-constraints-requiredfields)" : {{[ RequiredFieldInfo, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-tasktemplate-constraints-syntax.yaml"></a>

```
  [InvisibleFields](#cfn-connect-tasktemplate-constraints-invisiblefields): {{
    - InvisibleFieldInfo}}
  [ReadOnlyFields](#cfn-connect-tasktemplate-constraints-readonlyfields): {{
    - ReadOnlyFieldInfo}}
  [RequiredFields](#cfn-connect-tasktemplate-constraints-requiredfields): {{
    - RequiredFieldInfo}}
```

## Properties
<a name="aws-properties-connect-tasktemplate-constraints-properties"></a>

`InvisibleFields`  <a name="cfn-connect-tasktemplate-constraints-invisiblefields"></a>
Lists the fields that are invisible to agents.
*Required*: No
*Type*: Array of [InvisibleFieldInfo](aws-properties-connect-tasktemplate-invisiblefieldinfo.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReadOnlyFields`  <a name="cfn-connect-tasktemplate-constraints-readonlyfields"></a>
Lists the fields that are read-only to agents, and cannot be edited.
*Required*: No
*Type*: Array of [ReadOnlyFieldInfo](aws-properties-connect-tasktemplate-readonlyfieldinfo.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RequiredFields`  <a name="cfn-connect-tasktemplate-constraints-requiredfields"></a>
Lists the fields that are required to be filled by agents.
*Required*: No
*Type*: Array of [RequiredFieldInfo](aws-properties-connect-tasktemplate-requiredfieldinfo.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
