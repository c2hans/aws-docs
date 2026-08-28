---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-transformer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Logs::Transformer
<a name="aws-resource-logs-transformer"></a>

Creates or updates a *log transformer* for a single log group. You use log transformers to transform log events into a different format, making them easier for you to process and analyze. You can also transform logs from different sources into standardized formats that contains relevant, source-specific information.

After you have created a transformer, CloudWatch Logs performs the transformations at the time of log ingestion. You can then refer to the transformed versions of the logs during operations such as querying with CloudWatch Logs Insights or creating metric filters or subscription filers.

You can also use a transformer to copy metadata from metadata keys into the log events themselves. This metadata can include log group name, log stream name, account ID and Region.

A transformer for a log group is a series of processors, where each processor applies one type of transformation to the log events ingested into this log group. The processors work one after another, in the order that you list them, like a pipeline. For more information about the available processors to use in a transformer, see [ Processors that you can use](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-Processors).

Having log events in standardized format enables visibility across your applications for your log analysis, reporting, and alarming needs. CloudWatch Logs provides transformation for common log types with out-of-the-box transformation templates for major AWS log sources such as VPC flow logs, Lambda, and Amazon RDS. You can use pre-built transformation templates or create custom transformation policies.

You can create transformers only for the log groups in the Standard log class.

You can also set up a transformer at the account level. For more information, see [PutAccountPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutAccountPolicy.html). If there is both a log-group level transformer created with `PutTransformer` and an account-level transformer that could apply to the same log group, the log group uses only the log-group level transformer. It ignores the account-level transformer.

## Syntax
<a name="aws-resource-logs-transformer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-logs-transformer-syntax.json"></a>

```
{
  "Type" : "AWS::Logs::Transformer",
  "Properties" : {
      "[LogGroupIdentifier](#cfn-logs-transformer-loggroupidentifier)" : {{String}},
      "[TransformerConfig](#cfn-logs-transformer-transformerconfig)" : {{[ Processor, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-logs-transformer-syntax.yaml"></a>

```
Type: AWS::Logs::Transformer
Properties:
  [LogGroupIdentifier](#cfn-logs-transformer-loggroupidentifier): {{String}}
  [TransformerConfig](#cfn-logs-transformer-transformerconfig): {{
    - Processor}}
```

## Properties
<a name="aws-resource-logs-transformer-properties"></a>

`LogGroupIdentifier`  <a name="cfn-logs-transformer-loggroupidentifier"></a>
Specify either the name or ARN of the log group to create the transformer for.
*Required*: Yes
*Type*: String
*Pattern*: `[\w#+=/:,.@-]*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TransformerConfig`  <a name="cfn-logs-transformer-transformerconfig"></a>
This structure is an array that contains the configuration of this log transformer. A log transformer is an array of processors, where each processor applies one type of transformation to the log events that are ingested.
*Required*: Yes
*Type*: Array of [Processor](aws-properties-logs-transformer-processor.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-logs-transformer-return-values"></a>

### Ref
<a name="aws-resource-logs-transformer-return-values-ref"></a>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
