---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-tablebucket-replicationdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::TableBucket ReplicationDestination
<a name="aws-properties-s3tables-tablebucket-replicationdestination"></a>

Specifies a destination table bucket for replication.

## Syntax
<a name="aws-properties-s3tables-tablebucket-replicationdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-tablebucket-replicationdestination-syntax.json"></a>

```
{
  "[DestinationTableBucketARN](#cfn-s3tables-tablebucket-replicationdestination-destinationtablebucketarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3tables-tablebucket-replicationdestination-syntax.yaml"></a>

```
  [DestinationTableBucketARN](#cfn-s3tables-tablebucket-replicationdestination-destinationtablebucketarn): {{String}}
```

## Properties
<a name="aws-properties-s3tables-tablebucket-replicationdestination-properties"></a>

`DestinationTableBucketARN`  <a name="cfn-s3tables-tablebucket-replicationdestination-destinationtablebucketarn"></a>
The Amazon Resource Name (ARN) of the destination table bucket where tables will be replicated.
*Required*: Yes
*Type*: String
*Pattern*: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
