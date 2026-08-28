---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mwaaserverless-workflow-loggingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MWAAServerless::Workflow LoggingConfiguration
<a name="aws-properties-mwaaserverless-workflow-loggingconfiguration"></a>

Configuration for workflow logging that specifies where you should store your workflow execution logs. Amazon Managed Workflows for Apache Airflow Serverless provides comprehensive logging capabilities that capture workflow execution details, task-level information, and system events. Logs are automatically exported to your specified CloudWatch log group using remote logging functionality, providing centralized observability across the distributed, multi-tenant execution environment. This enables effective debugging, monitoring, and compliance auditing of workflow executions.

## Syntax
<a name="aws-properties-mwaaserverless-workflow-loggingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mwaaserverless-workflow-loggingconfiguration-syntax.json"></a>

```
{
  "[LogGroupName](#cfn-mwaaserverless-workflow-loggingconfiguration-loggroupname)" : {{String}}
}
```

### YAML
<a name="aws-properties-mwaaserverless-workflow-loggingconfiguration-syntax.yaml"></a>

```
  [LogGroupName](#cfn-mwaaserverless-workflow-loggingconfiguration-loggroupname): {{String}}
```

## Properties
<a name="aws-properties-mwaaserverless-workflow-loggingconfiguration-properties"></a>

`LogGroupName`  <a name="cfn-mwaaserverless-workflow-loggingconfiguration-loggroupname"></a>
The name of the CloudWatch log group where workflow execution logs are stored.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
