---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesis-resourcepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::ResourcePolicy
<a name="aws-resource-kinesis-resourcepolicy"></a>

Attaches a resource-based policy to a data stream or registered consumer. If you are using an identity other than the root user of the AWS account that owns the resource, the calling identity must have the `PutResourcePolicy` permissions on the specified Kinesis Data Streams resource and belong to the owner's account in order to use this operation. If you don't have `PutResourcePolicy` permissions, Amazon Kinesis Data Streams returns a `403 Access Denied error`. If you receive a `ResourceNotFoundException`, check to see if you passed a valid stream or consumer resource.

 Request patterns can be one of the following:
+ Data stream pattern: `arn:aws.*:kinesis:.*:\d{12}:.*stream/\S+`
+ Consumer pattern: `^(arn):aws.*:kinesis:.*:\d{12}:.*stream\/[a-zA-Z0-9_.-]+\/consumer\/[a-zA-Z0-9_.-]+:[0-9]+`

For more information, see [Controlling Access to Amazon Kinesis Data Streams Resources Using IAM](https://docs.aws.amazon.com/streams/latest/dev/controlling-access.html).

## Syntax
<a name="aws-resource-kinesis-resourcepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-kinesis-resourcepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::Kinesis::ResourcePolicy",
  "Properties" : {
      "[ResourceArn](#cfn-kinesis-resourcepolicy-resourcearn)" : {{String}},
      "[ResourcePolicy](#cfn-kinesis-resourcepolicy-resourcepolicy)" : {{Json}}
    }
}
```

### YAML
<a name="aws-resource-kinesis-resourcepolicy-syntax.yaml"></a>

```
Type: AWS::Kinesis::ResourcePolicy
Properties:
  [ResourceArn](#cfn-kinesis-resourcepolicy-resourcearn): {{String}}
  [ResourcePolicy](#cfn-kinesis-resourcepolicy-resourcepolicy): {{Json}}
```

## Properties
<a name="aws-resource-kinesis-resourcepolicy-properties"></a>

`ResourceArn`  <a name="cfn-kinesis-resourcepolicy-resourcearn"></a>
Returns the Amazon Resource Name (ARN) of the resource-based policy.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws.*:kinesis:.*:\d{12}:stream/\S+`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourcePolicy`  <a name="cfn-kinesis-resourcepolicy-resourcepolicy"></a>
This is the description for the resource policy.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-kinesis-resourcepolicy-return-values"></a>

### Ref
<a name="aws-resource-kinesis-resourcepolicy-return-values-ref"></a>

## Examples
<a name="aws-resource-kinesis-resourcepolicy--examples"></a>

### Resource policy that gives write access to a specific data stream
<a name="aws-resource-kinesis-resourcepolicy--examples--Resource_policy_that_gives_write_access_to_a_specific_data_stream"></a>

This policy allows Account12345 to perform the `DescribeStreamSummary`, `ListShards`, `PutRecord`, and `PutRecords` operations on the specified stream `datastreamABC`.

#### JSON
<a name="aws-resource-kinesis-resourcepolicy--examples--Resource_policy_that_gives_write_access_to_a_specific_data_stream--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Kinesis Data Streams resource policy example",
  "Resources": {
    "SampleStreamPolicy": {
      "Type": "AWS::Kinesis::ResourcePolicy",
      "Properties": {
        "ResourceArn": "arn:aws:kinesis:us-east-2:123456789012:stream/datastreamABC",
        "ResourcePolicy": {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "WriteStatement",
              "Effect": "Allow",
              "Principal": {
                "AWS": "arn:aws:iam::123456789012:root"
              },
              "Action": [
                "kinesis:DescribeStreamSummary",
                "kinesis:ListShards",
                "kinesis:PutRecord",
                "kinesis:PutRecords"
              ],
              "Resource": "arn:aws:kinesis:us-east-2:123456789012:stream/datastreamABC"
            }
          ]
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-kinesis-resourcepolicy--examples--Resource_policy_that_gives_write_access_to_a_specific_data_stream--yaml"></a>

```
SampleResourcePolicy:
  Type: AWS::Kinesis::ResourcePolicy
  Properties:
    ResourceArn: arn:aws:kinesis:us-east-2:123456789012:stream/datastreamABC
    ResourcePolicy:
      Version: 2012-10-17
      Statement:
        - Action:
            - 'kinesis:DescribeStreamSummary'
            - 'kinesis:ListShards'
            - 'kinesis:PutRecord'
            - 'kinesis:PutRecords'
          Effect: Allow
          Resource:
            - 'arn:aws:kinesis:us-east-2:123456789012:stream/datastreamABC'
          Principal:
            AWS: 'arn:aws:iam::123456789012:root'
```
