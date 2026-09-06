---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-resourcepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable ResourcePolicy
<a name="aws-properties-dynamodb-globaltable-resourcepolicy"></a>

Creates or updates a resource-based policy document that contains the permissions for DynamoDB resources, such as a table, its indexes, and stream. Resource-based policies let you define access permissions by specifying who has access to each resource, and the actions they are allowed to perform on each resource.

In a CloudFormation template, you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to DynamoDB. For more information about resource-based policies, see [Using resource-based policies for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access-control-resource-based.html) and [Resource-based policy examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-examples.html).

While defining resource-based policies in your CloudFormation templates, the following considerations apply:
+ The maximum size supported for a resource-based policy document in JSON format is 20 KB. DynamoDB counts whitespaces when calculating the size of a policy against this limit.
+ Resource-based policies don't support [drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html#). If you update a policy outside of the CloudFormation stack template, you'll need to update the CloudFormation stack with the changes.
+ Resource-based policies don't support out-of-band changes. If you add, update, or delete a policy outside of the CloudFormation template, the change won't be overwritten if there are no changes to the policy within the template.

  For example, say that your template contains a resource-based policy, which you later update outside of the template. If you don't make any changes to the policy in the template, the updated policy in DynamoDB won’t be synced with the policy in the template.

  Conversely, say that your template doesn’t contain a resource-based policy, but you add a policy outside of the template. This policy won’t be removed from DynamoDB as long as you don’t add it to the template. When you add a policy to the template and update the stack, the existing policy in DynamoDB will be updated to match the one defined in the template.
+ Within a resource-based policy, if the action for a DynamoDB service-linked role (SLR) to replicate data for a global table is denied, adding or deleting a replica will fail with an error.
+ The [AWS::DynamoDB::GlobalTable](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html) resource doesn't support creating a replica in the same stack update in Regions other than the Region where you deploy the stack update.

For a full list of all considerations, see [Resource-based policy considerations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-considerations.html).

## Syntax
<a name="aws-properties-dynamodb-globaltable-resourcepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-resourcepolicy-syntax.json"></a>

```
{
  "[PolicyDocument](#cfn-dynamodb-globaltable-resourcepolicy-policydocument)" : {{Json}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-resourcepolicy-syntax.yaml"></a>

```
  [PolicyDocument](#cfn-dynamodb-globaltable-resourcepolicy-policydocument): {{Json}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-resourcepolicy-properties"></a>

`PolicyDocument`  <a name="cfn-dynamodb-globaltable-resourcepolicy-policydocument"></a>
A resource-based policy document that contains permissions to add to the specified DynamoDB table, its indexes, and stream. In a CloudFormation template, you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to DynamoDB. For more information about resource-based policies, see [Using resource-based policies for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access-control-resource-based.html) and [Resource-based policy examples](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/rbac-examples.html).
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-dynamodb-globaltable-resourcepolicy--examples"></a>

### Attaching a resource-based policy to a DynamoDB table created using the `AWS::DynamoDB::GlobalTable` resource.
<a name="aws-properties-dynamodb-globaltable-resourcepolicy--examples--Attaching_a_resource-based_policy_to_a_table_created_using_the_::DynamoDB::GlobalTable_resource."></a>

The following CloudFormation template creates a table with the [AWS::DynamoDB::GlobalTable](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.html) resource and attaches a resource-based policy to the table and its stream. This policy allows the user `foobar` to perform the [GetItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html) operation on the table. Additionally, the following template enables a stream and then attaches a resource-based policy to the stream. The resource-based policy for the stream allows the user `foobar` to perform the [GetRecords](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetRecords.html), [GetShardIterator](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html), and [DescribeStream](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_DescribeStream.html) operations on the stream.

**Important**
If you enable a stream within a CloudFormation template and also define a policy for the stream, the policy is attached to the stream only after the stream is enabled, but before the stack update is complete.

#### JSON
<a name="aws-properties-dynamodb-globaltable-resourcepolicy--examples--Attaching_a_resource-based_policy_to_a_table_created_using_the_::DynamoDB::GlobalTable_resource.--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "GlobalMusicCollection": {
      "Type": "AWS::DynamoDB::GlobalTable",
      "Properties": {
        "TableName": "MusicCollection",
        "AttributeDefinitions": [
          {
            "AttributeName": "Artist",
            "AttributeType": "S"
          }
        ],
        "KeySchema": [
          {
            "AttributeName": "Artist",
            "KeyType": "HASH"
          }
        ],
        "BillingMode": "PAY_PER_REQUEST",
        "StreamSpecification": {
          "StreamViewType": "NEW_AND_OLD_IMAGES"
        },
        "Replicas": [
          {
            "Region": "us-east-1",
            "ResourcePolicy": {
              "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                  {
                    "Principal": {
                      "AWS": [
                        "arn:aws:iam::111122223333:user/foobar"
                      ]
                    },
                    "Effect": "Allow",
                    "Action": "dynamodb:GetItem",
                    "Resource": "*"
                  }
                ]
              }
            },
            "ReplicaStreamSpecification": {
              "ResourcePolicy": {
                "PolicyDocument": {
                  "Version": "2012-10-17",
                  "Statement": [
                    {
                      "Principal": {
                        "AWS": "arn:aws:iam::111122223333:user/foobar"
                      },
                      "Effect": "Allow",
                      "Action": [
                        "dynamodb:GetRecords",
                        "dynamodb:GetShardIterator",
                        "dynamodb:DescribeStream"
                      ],
                      "Resource": "*"
                    }
                  ]
                }
              }
            }
          }
        ]
      }
    }
  }
}
```
