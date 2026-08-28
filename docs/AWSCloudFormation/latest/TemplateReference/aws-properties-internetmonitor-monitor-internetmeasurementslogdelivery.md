---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-internetmonitor-monitor-internetmeasurementslogdelivery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InternetMonitor::Monitor InternetMeasurementsLogDelivery
<a name="aws-properties-internetmonitor-monitor-internetmeasurementslogdelivery"></a>

Publish internet measurements to an Amazon S3 bucket in addition to CloudWatch Logs.

## Syntax
<a name="aws-properties-internetmonitor-monitor-internetmeasurementslogdelivery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-internetmonitor-monitor-internetmeasurementslogdelivery-syntax.json"></a>

```
{
  "[S3Config](#cfn-internetmonitor-monitor-internetmeasurementslogdelivery-s3config)" : {{S3Config}}
}
```

### YAML
<a name="aws-properties-internetmonitor-monitor-internetmeasurementslogdelivery-syntax.yaml"></a>

```
  [S3Config](#cfn-internetmonitor-monitor-internetmeasurementslogdelivery-s3config): {{
    S3Config}}
```

## Properties
<a name="aws-properties-internetmonitor-monitor-internetmeasurementslogdelivery-properties"></a>

`S3Config`  <a name="cfn-internetmonitor-monitor-internetmeasurementslogdelivery-s3config"></a>
The configuration for publishing Amazon CloudWatch Internet Monitor internet measurements to Amazon S3.
*Required*: No
*Type*: [S3Config](aws-properties-internetmonitor-monitor-s3config.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
