---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-arcregionswitch-plan-reportoutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ARCRegionSwitch::Plan ReportOutputConfiguration
<a name="aws-properties-arcregionswitch-plan-reportoutputconfiguration"></a>

Configuration for report output destinations used in a Region switch plan.

## Syntax
<a name="aws-properties-arcregionswitch-plan-reportoutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-arcregionswitch-plan-reportoutputconfiguration-syntax.json"></a>

```
{
  "[S3Configuration](#cfn-arcregionswitch-plan-reportoutputconfiguration-s3configuration)" : {{S3ReportOutputConfiguration}}
}
```

### YAML
<a name="aws-properties-arcregionswitch-plan-reportoutputconfiguration-syntax.yaml"></a>

```
  [S3Configuration](#cfn-arcregionswitch-plan-reportoutputconfiguration-s3configuration): {{
    S3ReportOutputConfiguration}}
```

## Properties
<a name="aws-properties-arcregionswitch-plan-reportoutputconfiguration-properties"></a>

`S3Configuration`  <a name="cfn-arcregionswitch-plan-reportoutputconfiguration-s3configuration"></a>
Configuration for delivering reports to an Amazon S3 bucket.
*Required*: Yes
*Type*: [S3ReportOutputConfiguration](aws-properties-arcregionswitch-plan-s3reportoutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
