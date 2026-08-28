---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-workspaceipgroup-ipruleitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::WorkspaceIpGroup IpRuleItem
<a name="aws-properties-workspaces-workspaceipgroup-ipruleitem"></a>

Describes a rule for an IP access control group.

## Syntax
<a name="aws-properties-workspaces-workspaceipgroup-ipruleitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-workspaceipgroup-ipruleitem-syntax.json"></a>

```
{
  "[IpRule](#cfn-workspaces-workspaceipgroup-ipruleitem-iprule)" : {{String}},
  "[RuleDesc](#cfn-workspaces-workspaceipgroup-ipruleitem-ruledesc)" : {{String}}
}
```

### YAML
<a name="aws-properties-workspaces-workspaceipgroup-ipruleitem-syntax.yaml"></a>

```
  [IpRule](#cfn-workspaces-workspaceipgroup-ipruleitem-iprule): {{String}}
  [RuleDesc](#cfn-workspaces-workspaceipgroup-ipruleitem-ruledesc): {{String}}
```

## Properties
<a name="aws-properties-workspaces-workspaceipgroup-ipruleitem-properties"></a>

`IpRule`  <a name="cfn-workspaces-workspaceipgroup-ipruleitem-iprule"></a>
The IP address range, in CIDR notation.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuleDesc`  <a name="cfn-workspaces-workspaceipgroup-ipruleitem-ruledesc"></a>
The description.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
