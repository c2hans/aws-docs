---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-crawler-s3target.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Crawler S3Target
<a name="aws-properties-glue-crawler-s3target"></a>

Specifies a data store in Amazon Simple Storage Service (Amazon S3).

## Syntax
<a name="aws-properties-glue-crawler-s3target-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-crawler-s3target-syntax.json"></a>

```
{
  "[ConnectionName](#cfn-glue-crawler-s3target-connectionname)" : {{String}},
  "[DlqEventQueueArn](#cfn-glue-crawler-s3target-dlqeventqueuearn)" : {{String}},
  "[EventQueueArn](#cfn-glue-crawler-s3target-eventqueuearn)" : {{String}},
  "[Exclusions](#cfn-glue-crawler-s3target-exclusions)" : {{[ String, ... ]}},
  "[Path](#cfn-glue-crawler-s3target-path)" : {{String}},
  "[SampleSize](#cfn-glue-crawler-s3target-samplesize)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-glue-crawler-s3target-syntax.yaml"></a>

```
  [ConnectionName](#cfn-glue-crawler-s3target-connectionname): {{String}}
  [DlqEventQueueArn](#cfn-glue-crawler-s3target-dlqeventqueuearn): {{String}}
  [EventQueueArn](#cfn-glue-crawler-s3target-eventqueuearn): {{String}}
  [Exclusions](#cfn-glue-crawler-s3target-exclusions): {{
    - String}}
  [Path](#cfn-glue-crawler-s3target-path): {{String}}
  [SampleSize](#cfn-glue-crawler-s3target-samplesize): {{Integer}}
```

## Properties
<a name="aws-properties-glue-crawler-s3target-properties"></a>

`ConnectionName`  <a name="cfn-glue-crawler-s3target-connectionname"></a>
The name of a connection which allows a job or crawler to access data in Amazon S3 within an Amazon Virtual Private Cloud environment (Amazon VPC).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DlqEventQueueArn`  <a name="cfn-glue-crawler-s3target-dlqeventqueuearn"></a>
A valid Amazon dead-letter SQS ARN. For example, `arn:aws:sqs:region:account:deadLetterQueue`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventQueueArn`  <a name="cfn-glue-crawler-s3target-eventqueuearn"></a>
A valid Amazon SQS ARN. For example, `arn:aws:sqs:region:account:sqs`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Exclusions`  <a name="cfn-glue-crawler-s3target-exclusions"></a>
A list of glob patterns used to exclude from the crawl. For more information, see [Catalog Tables with a Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-glue-crawler-s3target-path"></a>
The path to the Amazon S3 target.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SampleSize`  <a name="cfn-glue-crawler-s3target-samplesize"></a>
Sets the number of files in each leaf folder to be crawled when crawling sample files in a dataset. If not set, all the files are crawled. A valid value is an integer between 1 and 249.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
