---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-contextmenuoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ContextMenuOption
<a name="aws-properties-quicksight-dashboard-contextmenuoption"></a>

The context menu options for a visual's interactions.

## Syntax
<a name="aws-properties-quicksight-dashboard-contextmenuoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-contextmenuoption-syntax.json"></a>

```
{
  "[AvailabilityStatus](#cfn-quicksight-dashboard-contextmenuoption-availabilitystatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-contextmenuoption-syntax.yaml"></a>

```
  [AvailabilityStatus](#cfn-quicksight-dashboard-contextmenuoption-availabilitystatus): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-contextmenuoption-properties"></a>

`AvailabilityStatus`  <a name="cfn-quicksight-dashboard-contextmenuoption-availabilitystatus"></a>
The availability status of the context menu options. If the value of this property is set to `ENABLED`, dashboard readers can interact with the context menu.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
