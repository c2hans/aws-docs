---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet ServiceManagedEc2InstanceMarketOptions
<a name="aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions"></a>

The details of the Amazon EC2 instance market options for a service managed fleet.

## Syntax
<a name="aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions-syntax.json"></a>

```
{
  "[Type](#cfn-deadline-fleet-servicemanagedec2instancemarketoptions-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions-syntax.yaml"></a>

```
  [Type](#cfn-deadline-fleet-servicemanagedec2instancemarketoptions-type): {{String}}
```

## Properties
<a name="aws-properties-deadline-fleet-servicemanagedec2instancemarketoptions-properties"></a>

`Type`  <a name="cfn-deadline-fleet-servicemanagedec2instancemarketoptions-type"></a>
The Amazon EC2 instance type.
*Required*: Yes
*Type*: String
*Allowed values*: `on-demand | spot | wait-and-save`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
