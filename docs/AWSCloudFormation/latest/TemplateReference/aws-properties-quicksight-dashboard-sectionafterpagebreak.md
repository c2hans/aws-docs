---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-sectionafterpagebreak.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SectionAfterPageBreak
<a name="aws-properties-quicksight-dashboard-sectionafterpagebreak"></a>

The configuration of a page break after a section.

## Syntax
<a name="aws-properties-quicksight-dashboard-sectionafterpagebreak-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-sectionafterpagebreak-syntax.json"></a>

```
{
  "[Status](#cfn-quicksight-dashboard-sectionafterpagebreak-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-sectionafterpagebreak-syntax.yaml"></a>

```
  [Status](#cfn-quicksight-dashboard-sectionafterpagebreak-status): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-sectionafterpagebreak-properties"></a>

`Status`  <a name="cfn-quicksight-dashboard-sectionafterpagebreak-status"></a>
The option that enables or disables a page break at the end of a section.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
