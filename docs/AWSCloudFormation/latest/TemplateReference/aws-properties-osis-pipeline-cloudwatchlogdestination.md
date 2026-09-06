---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-osis-pipeline-cloudwatchlogdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OSIS::Pipeline CloudWatchLogDestination
<a name="aws-properties-osis-pipeline-cloudwatchlogdestination"></a>

The destination for OpenSearch Ingestion logs sent to Amazon CloudWatch.

## Syntax
<a name="aws-properties-osis-pipeline-cloudwatchlogdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-osis-pipeline-cloudwatchlogdestination-syntax.json"></a>

```
{
  "[LogGroup](#cfn-osis-pipeline-cloudwatchlogdestination-loggroup)" : {{String}}
}
```

### YAML
<a name="aws-properties-osis-pipeline-cloudwatchlogdestination-syntax.yaml"></a>

```
  [LogGroup](#cfn-osis-pipeline-cloudwatchlogdestination-loggroup): {{String}}
```

## Properties
<a name="aws-properties-osis-pipeline-cloudwatchlogdestination-properties"></a>

`LogGroup`  <a name="cfn-osis-pipeline-cloudwatchlogdestination-loggroup"></a>
The name of the CloudWatch Logs group to send pipeline logs to. You can specify an existing log group or create a new one. For example, `/aws/vendedlogs/OpenSearchService/pipelines`.
*Required*: Yes
*Type*: String
*Pattern*: `\/aws\/vendedlogs\/[\.\-_/#A-Za-z0-9]+`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
