---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3express-directorybucket-metricsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::DirectoryBucket MetricsConfiguration
<a name="aws-properties-s3express-directorybucket-metricsconfiguration"></a>

Specifies a metrics configuration for the CloudWatch request metrics (specified by the metrics configuration ID) from an Amazon S3 bucket. If you're updating an existing metrics configuration, note that this is a full replacement of the existing metrics configuration. If you don't include the elements you want to keep, they are erased. For more information, see [PutBucketMetricsConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTMetricConfiguration.html).

## Syntax
<a name="aws-properties-s3express-directorybucket-metricsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3express-directorybucket-metricsconfiguration-syntax.json"></a>

```
{
  "[AccessPointArn](#cfn-s3express-directorybucket-metricsconfiguration-accesspointarn)" : {{String}},
  "[Id](#cfn-s3express-directorybucket-metricsconfiguration-id)" : {{String}},
  "[Prefix](#cfn-s3express-directorybucket-metricsconfiguration-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3express-directorybucket-metricsconfiguration-syntax.yaml"></a>

```
  [AccessPointArn](#cfn-s3express-directorybucket-metricsconfiguration-accesspointarn): {{String}}
  [Id](#cfn-s3express-directorybucket-metricsconfiguration-id): {{String}}
  [Prefix](#cfn-s3express-directorybucket-metricsconfiguration-prefix): {{String}}
```

## Properties
<a name="aws-properties-s3express-directorybucket-metricsconfiguration-properties"></a>

`AccessPointArn`  <a name="cfn-s3express-directorybucket-metricsconfiguration-accesspointarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-s3express-directorybucket-metricsconfiguration-id"></a>
The ID used to identify the metrics configuration. The ID has a 64 character limit and can only contain letters, numbers, periods, dashes, and underscores.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-s3express-directorybucket-metricsconfiguration-prefix"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
