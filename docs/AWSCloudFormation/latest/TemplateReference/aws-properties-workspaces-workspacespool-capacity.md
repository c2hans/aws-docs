---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-workspacespool-capacity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::WorkspacesPool Capacity
<a name="aws-properties-workspaces-workspacespool-capacity"></a>

Describes the user capacity for the pool.

## Syntax
<a name="aws-properties-workspaces-workspacespool-capacity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-workspacespool-capacity-syntax.json"></a>

```
{
  "[DesiredUserSessions](#cfn-workspaces-workspacespool-capacity-desiredusersessions)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-workspaces-workspacespool-capacity-syntax.yaml"></a>

```
  [DesiredUserSessions](#cfn-workspaces-workspacespool-capacity-desiredusersessions): {{Integer}}
```

## Properties
<a name="aws-properties-workspaces-workspacespool-capacity-properties"></a>

`DesiredUserSessions`  <a name="cfn-workspaces-workspacespool-capacity-desiredusersessions"></a>
The desired number of user sessions for the WorkSpaces in the pool.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
