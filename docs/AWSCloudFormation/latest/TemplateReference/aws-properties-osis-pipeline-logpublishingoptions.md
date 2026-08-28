---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-osis-pipeline-logpublishingoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OSIS::Pipeline LogPublishingOptions
<a name="aws-properties-osis-pipeline-logpublishingoptions"></a>

Container for the values required to configure logging for the pipeline. If you don't specify these values, OpenSearch Ingestion will not publish logs from your application to CloudWatch Logs.

## Syntax
<a name="aws-properties-osis-pipeline-logpublishingoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-osis-pipeline-logpublishingoptions-syntax.json"></a>

```
{
  "[CloudWatchLogDestination](#cfn-osis-pipeline-logpublishingoptions-cloudwatchlogdestination)" : {{CloudWatchLogDestination}},
  "[IsLoggingEnabled](#cfn-osis-pipeline-logpublishingoptions-isloggingenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-osis-pipeline-logpublishingoptions-syntax.yaml"></a>

```
  [CloudWatchLogDestination](#cfn-osis-pipeline-logpublishingoptions-cloudwatchlogdestination): {{
    CloudWatchLogDestination}}
  [IsLoggingEnabled](#cfn-osis-pipeline-logpublishingoptions-isloggingenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-osis-pipeline-logpublishingoptions-properties"></a>

`CloudWatchLogDestination`  <a name="cfn-osis-pipeline-logpublishingoptions-cloudwatchlogdestination"></a>
The destination for OpenSearch Ingestion logs sent to Amazon CloudWatch Logs. This parameter is required if `IsLoggingEnabled` is set to `true`.
*Required*: No
*Type*: [CloudWatchLogDestination](aws-properties-osis-pipeline-cloudwatchlogdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsLoggingEnabled`  <a name="cfn-osis-pipeline-logpublishingoptions-isloggingenabled"></a>
Whether logs should be published.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
