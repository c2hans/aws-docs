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
