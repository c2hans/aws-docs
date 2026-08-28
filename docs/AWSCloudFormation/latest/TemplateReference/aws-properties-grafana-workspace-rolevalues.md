---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-grafana-workspace-rolevalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Grafana::Workspace RoleValues
<a name="aws-properties-grafana-workspace-rolevalues"></a>

This structure defines which groups defined in the SAML assertion attribute are to be mapped to the Grafana `Admin` and `Editor` roles in the workspace. SAML authenticated users not part of `Admin` or `Editor` role groups have `Viewer` permission over the workspace.

## Syntax
<a name="aws-properties-grafana-workspace-rolevalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-grafana-workspace-rolevalues-syntax.json"></a>

```
{
  "[Admin](#cfn-grafana-workspace-rolevalues-admin)" : {{[ String, ... ]}},
  "[Editor](#cfn-grafana-workspace-rolevalues-editor)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-grafana-workspace-rolevalues-syntax.yaml"></a>

```
  [Admin](#cfn-grafana-workspace-rolevalues-admin): {{
    - String}}
  [Editor](#cfn-grafana-workspace-rolevalues-editor): {{
    - String}}
```

## Properties
<a name="aws-properties-grafana-workspace-rolevalues-properties"></a>

`Admin`  <a name="cfn-grafana-workspace-rolevalues-admin"></a>
A list of groups from the SAML assertion attribute to grant the Grafana `Admin` role to.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Editor`  <a name="cfn-grafana-workspace-rolevalues-editor"></a>
A list of groups from the SAML assertion attribute to grant the Grafana `Editor` role to.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
