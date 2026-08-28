---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appmesh-virtualnode-fileaccesslog.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppMesh::VirtualNode FileAccessLog
<a name="aws-properties-appmesh-virtualnode-fileaccesslog"></a>

An object that represents an access log file.

## Syntax
<a name="aws-properties-appmesh-virtualnode-fileaccesslog-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appmesh-virtualnode-fileaccesslog-syntax.json"></a>

```
{
  "[Format](#cfn-appmesh-virtualnode-fileaccesslog-format)" : {{LoggingFormat}},
  "[Path](#cfn-appmesh-virtualnode-fileaccesslog-path)" : {{String}}
}
```

### YAML
<a name="aws-properties-appmesh-virtualnode-fileaccesslog-syntax.yaml"></a>

```
  [Format](#cfn-appmesh-virtualnode-fileaccesslog-format): {{
    LoggingFormat}}
  [Path](#cfn-appmesh-virtualnode-fileaccesslog-path): {{String}}
```

## Properties
<a name="aws-properties-appmesh-virtualnode-fileaccesslog-properties"></a>

`Format`  <a name="cfn-appmesh-virtualnode-fileaccesslog-format"></a>
The specified format for the logs. The format is either `json_format` or `text_format`.
*Required*: No
*Type*: [LoggingFormat](aws-properties-appmesh-virtualnode-loggingformat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-appmesh-virtualnode-fileaccesslog-path"></a>
The file path to write access logs to. You can use `/dev/stdout` to send access logs to standard out and configure your Envoy container to use a log driver, such as `awslogs`, to export the access logs to a log storage service such as Amazon CloudWatch Logs. You can also specify a path in the Envoy container's file system to write the files to disk.
The Envoy process must have write permissions to the path that you specify here. Otherwise, Envoy fails to bootstrap properly.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
