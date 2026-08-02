---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-crawler-catalogtarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Crawler CatalogTarget
<a name="aws-properties-glue-crawler-catalogtarget"></a>

Specifies an AWS Glue Data Catalog target.

## Syntax
<a name="aws-properties-glue-crawler-catalogtarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-crawler-catalogtarget-syntax.json"></a>

```
{
  "[ConnectionName](#cfn-glue-crawler-catalogtarget-connectionname)" : {{String}},
  "[DatabaseName](#cfn-glue-crawler-catalogtarget-databasename)" : {{String}},
  "[DlqEventQueueArn](#cfn-glue-crawler-catalogtarget-dlqeventqueuearn)" : {{String}},
  "[EventQueueArn](#cfn-glue-crawler-catalogtarget-eventqueuearn)" : {{String}},
  "[Tables](#cfn-glue-crawler-catalogtarget-tables)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-crawler-catalogtarget-syntax.yaml"></a>

```
  [ConnectionName](#cfn-glue-crawler-catalogtarget-connectionname): {{String}}
  [DatabaseName](#cfn-glue-crawler-catalogtarget-databasename): {{String}}
  [DlqEventQueueArn](#cfn-glue-crawler-catalogtarget-dlqeventqueuearn): {{String}}
  [EventQueueArn](#cfn-glue-crawler-catalogtarget-eventqueuearn): {{String}}
  [Tables](#cfn-glue-crawler-catalogtarget-tables): {{
    - String}}
```

## Properties
<a name="aws-properties-glue-crawler-catalogtarget-properties"></a>

`ConnectionName`  <a name="cfn-glue-crawler-catalogtarget-connectionname"></a>
The name of the connection for an Amazon S3-backed Data Catalog table to be a target of the crawl when using a `Catalog` connection type paired with a `NETWORK` Connection type.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-glue-crawler-catalogtarget-databasename"></a>
The name of the database to be synchronized.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DlqEventQueueArn`  <a name="cfn-glue-crawler-catalogtarget-dlqeventqueuearn"></a>
A valid Amazon dead-letter SQS ARN. For example, `arn:aws:sqs:region:account:deadLetterQueue`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventQueueArn`  <a name="cfn-glue-crawler-catalogtarget-eventqueuearn"></a>
A valid Amazon SQS ARN. For example, `arn:aws:sqs:region:account:sqs`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tables`  <a name="cfn-glue-crawler-catalogtarget-tables"></a>
A list of the tables to be synchronized.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
