---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-cfns3logsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::Detector CFNS3LogsConfiguration
<a name="aws-properties-guardduty-detector-cfns3logsconfiguration"></a>

Describes whether S3 data event logs will be enabled as a data source when the detector is created.

## Syntax
<a name="aws-properties-guardduty-detector-cfns3logsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-guardduty-detector-cfns3logsconfiguration-syntax.json"></a>

```
{
  "[Enable](#cfn-guardduty-detector-cfns3logsconfiguration-enable)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-guardduty-detector-cfns3logsconfiguration-syntax.yaml"></a>

```
  [Enable](#cfn-guardduty-detector-cfns3logsconfiguration-enable): {{Boolean}}
```

## Properties
<a name="aws-properties-guardduty-detector-cfns3logsconfiguration-properties"></a>

`Enable`  <a name="cfn-guardduty-detector-cfns3logsconfiguration-enable"></a>
 The status of S3 data event logs as a data source.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
