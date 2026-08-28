---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-exportwithhiddenfieldsoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ExportWithHiddenFieldsOption
<a name="aws-properties-quicksight-dashboard-exportwithhiddenfieldsoption"></a>

Determines whether or not hidden fields are visible on exported dashbaords.

## Syntax
<a name="aws-properties-quicksight-dashboard-exportwithhiddenfieldsoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-exportwithhiddenfieldsoption-syntax.json"></a>

```
{
  "[AvailabilityStatus](#cfn-quicksight-dashboard-exportwithhiddenfieldsoption-availabilitystatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-exportwithhiddenfieldsoption-syntax.yaml"></a>

```
  [AvailabilityStatus](#cfn-quicksight-dashboard-exportwithhiddenfieldsoption-availabilitystatus): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-exportwithhiddenfieldsoption-properties"></a>

`AvailabilityStatus`  <a name="cfn-quicksight-dashboard-exportwithhiddenfieldsoption-availabilitystatus"></a>
The status of the export with hidden fields options.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
