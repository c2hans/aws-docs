---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-scheduledquery-errorreportconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::ScheduledQuery ErrorReportConfiguration
<a name="aws-properties-timestream-scheduledquery-errorreportconfiguration"></a>

Configuration required for error reporting.

## Syntax
<a name="aws-properties-timestream-scheduledquery-errorreportconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-scheduledquery-errorreportconfiguration-syntax.json"></a>

```
{
  "[S3Configuration](#cfn-timestream-scheduledquery-errorreportconfiguration-s3configuration)" : {{S3Configuration}}
}
```

### YAML
<a name="aws-properties-timestream-scheduledquery-errorreportconfiguration-syntax.yaml"></a>

```
  [S3Configuration](#cfn-timestream-scheduledquery-errorreportconfiguration-s3configuration): {{
    S3Configuration}}
```

## Properties
<a name="aws-properties-timestream-scheduledquery-errorreportconfiguration-properties"></a>

`S3Configuration`  <a name="cfn-timestream-scheduledquery-errorreportconfiguration-s3configuration"></a>
The S3 configuration for the error reports.
*Required*: Yes
*Type*: [S3Configuration](aws-properties-timestream-scheduledquery-s3configuration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
