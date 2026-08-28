---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application DeployAsApplicationConfiguration
<a name="aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration"></a>

The information required to deploy a Kinesis Data Analytics Studio notebook as an application with durable state.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration-syntax.json"></a>

```
{
  "[S3ContentLocation](#cfn-kinesisanalyticsv2-application-deployasapplicationconfiguration-s3contentlocation)" : {{S3ContentBaseLocation}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration-syntax.yaml"></a>

```
  [S3ContentLocation](#cfn-kinesisanalyticsv2-application-deployasapplicationconfiguration-s3contentlocation): {{
    S3ContentBaseLocation}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-deployasapplicationconfiguration-properties"></a>

`S3ContentLocation`  <a name="cfn-kinesisanalyticsv2-application-deployasapplicationconfiguration-s3contentlocation"></a>
The description of an Amazon S3 object that contains the Amazon Data Analytics application, including the Amazon Resource Name (ARN) of the S3 bucket, the name of the Amazon S3 object that contains the data, and the version number of the Amazon S3 object that contains the data.
*Required*: Yes
*Type*: [S3ContentBaseLocation](aws-properties-kinesisanalyticsv2-application-s3contentbaselocation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
