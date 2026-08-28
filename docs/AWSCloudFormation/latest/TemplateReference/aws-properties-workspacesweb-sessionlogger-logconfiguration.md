---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspacesweb-sessionlogger-logconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesWeb::SessionLogger LogConfiguration
<a name="aws-properties-workspacesweb-sessionlogger-logconfiguration"></a>

The configuration of the log.

## Syntax
<a name="aws-properties-workspacesweb-sessionlogger-logconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspacesweb-sessionlogger-logconfiguration-syntax.json"></a>

```
{
  "[S3](#cfn-workspacesweb-sessionlogger-logconfiguration-s3)" : {{S3LogConfiguration}}
}
```

### YAML
<a name="aws-properties-workspacesweb-sessionlogger-logconfiguration-syntax.yaml"></a>

```
  [S3](#cfn-workspacesweb-sessionlogger-logconfiguration-s3): {{
    S3LogConfiguration}}
```

## Properties
<a name="aws-properties-workspacesweb-sessionlogger-logconfiguration-properties"></a>

`S3`  <a name="cfn-workspacesweb-sessionlogger-logconfiguration-s3"></a>
The configuration for delivering the logs to S3.
*Required*: No
*Type*: [S3LogConfiguration](aws-properties-workspacesweb-sessionlogger-s3logconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
