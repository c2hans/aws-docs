---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-crawler-dynamodbtarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Crawler DynamoDBTarget
<a name="aws-properties-glue-crawler-dynamodbtarget"></a>

Specifies an Amazon DynamoDB table to crawl.

## Syntax
<a name="aws-properties-glue-crawler-dynamodbtarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-crawler-dynamodbtarget-syntax.json"></a>

```
{
  "[Path](#cfn-glue-crawler-dynamodbtarget-path)" : {{String}},
  "[ScanAll](#cfn-glue-crawler-dynamodbtarget-scanall)" : {{Boolean}},
  "[ScanRate](#cfn-glue-crawler-dynamodbtarget-scanrate)" : {{Number}}
}
```

### YAML
<a name="aws-properties-glue-crawler-dynamodbtarget-syntax.yaml"></a>

```
  [Path](#cfn-glue-crawler-dynamodbtarget-path): {{String}}
  [ScanAll](#cfn-glue-crawler-dynamodbtarget-scanall): {{Boolean}}
  [ScanRate](#cfn-glue-crawler-dynamodbtarget-scanrate): {{Number}}
```

## Properties
<a name="aws-properties-glue-crawler-dynamodbtarget-properties"></a>

`Path`  <a name="cfn-glue-crawler-dynamodbtarget-path"></a>
The name of the DynamoDB table to crawl.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScanAll`  <a name="cfn-glue-crawler-dynamodbtarget-scanall"></a>
Indicates whether to scan all the records, or to sample rows from the table. Scanning all the records can take a long time when the table is not a high throughput table.
A value of `true` means to scan all records, while a value of `false` means to sample the records. If no value is specified, the value defaults to `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScanRate`  <a name="cfn-glue-crawler-dynamodbtarget-scanrate"></a>
The percentage of the configured read capacity units to use by the AWS Glue crawler. Read capacity units is a term defined by DynamoDB, and is a numeric value that acts as rate limiter for the number of reads that can be performed on that table per second.
The valid values are null or a value between 0.1 to 1.5. A null value is used when user does not provide a value, and defaults to 0.5 of the configured Read Capacity Unit (for provisioned tables), or 0.25 of the max configured Read Capacity Unit (for tables using on-demand mode).
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
