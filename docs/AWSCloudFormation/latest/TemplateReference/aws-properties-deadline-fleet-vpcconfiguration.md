---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-vpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet VpcConfiguration
<a name="aws-properties-deadline-fleet-vpcconfiguration"></a>

The configuration options for a service managed fleet's VPC.

## Syntax
<a name="aws-properties-deadline-fleet-vpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-vpcconfiguration-syntax.json"></a>

```
{
  "[ResourceConfigurationArns](#cfn-deadline-fleet-vpcconfiguration-resourceconfigurationarns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-vpcconfiguration-syntax.yaml"></a>

```
  [ResourceConfigurationArns](#cfn-deadline-fleet-vpcconfiguration-resourceconfigurationarns): {{
    - String}}
```

## Properties
<a name="aws-properties-deadline-fleet-vpcconfiguration-properties"></a>

`ResourceConfigurationArns`  <a name="cfn-deadline-fleet-vpcconfiguration-resourceconfigurationarns"></a>
The ARNs of the VPC Lattice resource configurations attached to the fleet.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
