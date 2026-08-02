---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-globaltable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable
<a name="aws-resource-dynamodb-globaltable"></a>

The `AWS::DynamoDB::GlobalTable` resource enables you to create and manage a Version 2019.11.21 global table. This resource cannot be used to create or manage a Version 2017.11.29 global table. For more information, see [Global tables](https://docs.aws.amazon.com//amazondynamodb/latest/developerguide/GlobalTables.html).

**Important**
You cannot convert a resource of type `AWS::DynamoDB::Table` into a resource of type `AWS::DynamoDB::GlobalTable` by changing its type in your template. **Doing so might result in the deletion of your DynamoDB table.**
You can instead use the GlobalTable resource to create a new table in a single Region. This will be billed the same as a single Region table. If you later update the stack to add other Regions then Global Tables pricing will apply.

You should be aware of the following behaviors when working with DynamoDB global tables.
+ The IAM Principal executing the stack operation must have the permissions listed below in all regions where you plan to have a global table replica. The IAM Principal's permissions should not have restrictions based on IP source address. Some global tables operations (for example, adding a replica) are asynchronous, and require that the IAM Principal is valid until they complete. You should not delete the Principal (user or IAM role) until CloudFormation has finished updating your stack.
  +  `application-autoscaling:DeleteScalingPolicy`
  +  `application-autoscaling:DeleteScheduledAction`
  +  `application-autoscaling:DeregisterScalableTarget`
  +  `application-autoscaling:DescribeScalableTargets`
  +  `application-autoscaling:DescribeScalingPolicies`
  +  `application-autoscaling:PutScalingPolicy`
  +  `application-autoscaling:PutScheduledAction`
  +  `application-autoscaling:RegisterScalableTarget`
  +  `dynamodb:BatchWriteItem`
  +  `dynamodb:CreateGlobalTableWitness`
  +  `dynamodb:CreateTable`
  +  `dynamodb:CreateTableReplica`
  +  `dynamodb:DeleteGlobalTableWitness`
  +  `dynamodb:DeleteItem`
  +  `dynamodb:DeleteTable`
  +  `dynamodb:DeleteTableReplica`
  +  `dynamodb:DescribeContinuousBackups`
  +  `dynamodb:DescribeContributorInsights`
  +  `dynamodb:DescribeTable`
  +  `dynamodb:DescribeTableReplicaAutoScaling`
  +  `dynamodb:DescribeTimeToLive`
  +  `dynamodb:DisableKinesisStreamingDestination`
  +  `dynamodb:EnableKinesisStreamingDestination`
  +  `dynamodb:GetItem`
  +  `dynamodb:ListTables`
  +  `dynamodb:ListTagsOfResource`
  +  `dynamodb:PutItem`
  +  `dynamodb:Query`
  +  `dynamodb:Scan`
  +  `dynamodb:TagResource`
  +  `dynamodb:UntagResource`
  +  `dynamodb:UpdateContinuousBackups`
  +  `dynamodb:UpdateContributorInsights`
  +  `dynamodb:UpdateItem`
  +  `dynamodb:UpdateTable`
  +  `dynamodb:UpdateTableReplicaAutoScaling`
  +  `dynamodb:UpdateTimeToLive`
  +  `iam:CreateServiceLinkedRole`
  +  `kms:CreateGrant`
  +  `kms:DescribeKey`
+ When using provisioned billing mode, CloudFormation will create an auto scaling policy on each of your replicas to control their write capacities. You must configure this policy using the `WriteProvisionedThroughputSettings` property. CloudFormation will ensure that all replicas have the same write capacity auto scaling property. You cannot directly specify a value for write capacity for a global table.
+ If your table uses provisioned capacity, you must configure auto scaling directly in the `AWS::DynamoDB::GlobalTable` resource. You should not configure additional auto scaling policies on any of the table replicas or global secondary indexes, either via API or via `AWS::ApplicationAutoScaling::ScalableTarget` or `AWS::ApplicationAutoScaling::ScalingPolicy`. Doing so might result in unexpected behavior and is unsupported.
+ In AWS CloudFormation, each global table is controlled by a single stack, in a single region, regardless of the number of replicas. When you deploy your template, CloudFormation will create/update all replicas as part of a single stack operation. You should not deploy the same `AWS::DynamoDB::GlobalTable` resource in multiple regions. Doing so will result in errors, and is unsupported. If you deploy your application template in multiple regions, you can use conditions to only create the resource in a single region. Alternatively, you can choose to define your `AWS::DynamoDB::GlobalTable` resources in a stack separate from your application stack, and make sure it is only deployed to a single region.

## Syntax
<a name="aws-resource-dynamodb-globaltable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-dynamodb-globaltable-syntax.json"></a>

```
{
  "Type" : "AWS::DynamoDB::GlobalTable",
  "Properties" : {
      "[AttributeDefinitions](#cfn-dynamodb-globaltable-attributedefinitions)" : {{[ AttributeDefinition, ... ]}},
      "[BillingMode](#cfn-dynamodb-globaltable-billingmode)" : {{String}},
      "[GlobalSecondaryIndexes](#cfn-dynamodb-globaltable-globalsecondaryindexes)" : {{[ GlobalSecondaryIndex, ... ]}},
      "[GlobalTableSourceArn](#cfn-dynamodb-globaltable-globaltablesourcearn)" : {{String}},
      "[GlobalTableWitnesses](#cfn-dynamodb-globaltable-globaltablewitnesses)" : {{[ GlobalTableWitness, ... ]}},
      "[KeySchema](#cfn-dynamodb-globaltable-keyschema)" : {{[ KeySchema, ... ]}},
      "[LocalSecondaryIndexes](#cfn-dynamodb-globaltable-localsecondaryindexes)" : {{[ LocalSecondaryIndex, ... ]}},
      "[MultiRegionConsistency](#cfn-dynamodb-globaltable-multiregionconsistency)" : {{String}},
      "[ReadOnDemandThroughputSettings](#cfn-dynamodb-globaltable-readondemandthroughputsettings)" : {{ReadOnDemandThroughputSettings}},
      "[ReadProvisionedThroughputSettings](#cfn-dynamodb-globaltable-readprovisionedthroughputsettings)" : {{GlobalReadProvisionedThroughputSettings}},
      "[Replicas](#cfn-dynamodb-globaltable-replicas)" : {{[ ReplicaSpecification, ... ]}},
      "[SSESpecification](#cfn-dynamodb-globaltable-ssespecification)" : {{SSESpecification}},
      "[StreamSpecification](#cfn-dynamodb-globaltable-streamspecification)" : {{StreamSpecification}},
      "[TableName](#cfn-dynamodb-globaltable-tablename)" : {{String}},
      "[TimeToLiveSpecification](#cfn-dynamodb-globaltable-timetolivespecification)" : {{TimeToLiveSpecification}},
      "[WarmThroughput](#cfn-dynamodb-globaltable-warmthroughput)" : {{WarmThroughput}},
      "[WriteOnDemandThroughputSettings](#cfn-dynamodb-globaltable-writeondemandthroughputsettings)" : {{WriteOnDemandThroughputSettings}},
      "[WriteProvisionedThroughputSettings](#cfn-dynamodb-globaltable-writeprovisionedthroughputsettings)" : {{WriteProvisionedThroughputSettings}}
    }
}
```

### YAML
<a name="aws-resource-dynamodb-globaltable-syntax.yaml"></a>

```
Type: AWS::DynamoDB::GlobalTable
Properties:
  [AttributeDefinitions](#cfn-dynamodb-globaltable-attributedefinitions): {{
    - AttributeDefinition}}
  [BillingMode](#cfn-dynamodb-globaltable-billingmode): {{String}}
  [GlobalSecondaryIndexes](#cfn-dynamodb-globaltable-globalsecondaryindexes): {{
    - GlobalSecondaryIndex}}
  [GlobalTableSourceArn](#cfn-dynamodb-globaltable-globaltablesourcearn): {{String}}
  [GlobalTableWitnesses](#cfn-dynamodb-globaltable-globaltablewitnesses): {{
    - GlobalTableWitness}}
  [KeySchema](#cfn-dynamodb-globaltable-keyschema): {{
    - KeySchema}}
  [LocalSecondaryIndexes](#cfn-dynamodb-globaltable-localsecondaryindexes): {{
    - LocalSecondaryIndex}}
  [MultiRegionConsistency](#cfn-dynamodb-globaltable-multiregionconsistency): {{String}}
  [ReadOnDemandThroughputSettings](#cfn-dynamodb-globaltable-readondemandthroughputsettings): {{
    ReadOnDemandThroughputSettings}}
  [ReadProvisionedThroughputSettings](#cfn-dynamodb-globaltable-readprovisionedthroughputsettings): {{
    GlobalReadProvisionedThroughputSettings}}
  [Replicas](#cfn-dynamodb-globaltable-replicas): {{
    - ReplicaSpecification}}
  [SSESpecification](#cfn-dynamodb-globaltable-ssespecification): {{
    SSESpecification}}
  [StreamSpecification](#cfn-dynamodb-globaltable-streamspecification): {{
    StreamSpecification}}
  [TableName](#cfn-dynamodb-globaltable-tablename): {{String}}
  [TimeToLiveSpecification](#cfn-dynamodb-globaltable-timetolivespecification): {{
    TimeToLiveSpecification}}
  [WarmThroughput](#cfn-dynamodb-globaltable-warmthroughput): {{
    WarmThroughput}}
  [WriteOnDemandThroughputSettings](#cfn-dynamodb-globaltable-writeondemandthroughputsettings): {{
    WriteOnDemandThroughputSettings}}
  [WriteProvisionedThroughputSettings](#cfn-dynamodb-globaltable-writeprovisionedthroughputsettings): {{
    WriteProvisionedThroughputSettings}}
```

## Properties
<a name="aws-resource-dynamodb-globaltable-properties"></a>

`AttributeDefinitions`  <a name="cfn-dynamodb-globaltable-attributedefinitions"></a>
A list of attributes that describe the key schema for the global table and indexes.
*Required*: No
*Type*: Array of [AttributeDefinition](aws-properties-dynamodb-globaltable-attributedefinition.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BillingMode`  <a name="cfn-dynamodb-globaltable-billingmode"></a>
Specifies how you are charged for read and write throughput and how you manage capacity. Valid values are:
+  `PAY_PER_REQUEST`
+  `PROVISIONED`
All replicas in your global table will have the same billing mode. If you use `PROVISIONED` billing mode, you must provide an auto scaling configuration via the `WriteProvisionedThroughputSettings` property. The default value of this property is `PROVISIONED`.
*Required*: No
*Type*: String
*Allowed values*: `PROVISIONED | PAY_PER_REQUEST`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalSecondaryIndexes`  <a name="cfn-dynamodb-globaltable-globalsecondaryindexes"></a>
Global secondary indexes to be created on the global table. You can create up to 20 global secondary indexes. Each replica in your global table will have the same global secondary index settings. You can only create or delete one global secondary index in a single stack operation.
Since the backfilling of an index could take a long time, CloudFormation does not wait for the index to become active. If a stack operation rolls back, CloudFormation might not delete an index that has been added. In that case, you will need to delete the index manually.
*Required*: No
*Type*: Array of [GlobalSecondaryIndex](aws-properties-dynamodb-globaltable-globalsecondaryindex.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalTableSourceArn`  <a name="cfn-dynamodb-globaltable-globaltablesourcearn"></a>
The ARN of the source table for multi-account global table replication.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`GlobalTableWitnesses`  <a name="cfn-dynamodb-globaltable-globaltablewitnesses"></a>
The list of witnesses of the MRSC global table. Only one witness Region can be configured per MRSC global table.
*Required*: No
*Type*: Array of [GlobalTableWitness](aws-properties-dynamodb-globaltable-globaltablewitness.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeySchema`  <a name="cfn-dynamodb-globaltable-keyschema"></a>
Specifies the attributes that make up the primary key for the table. The attributes in the `KeySchema` property must also be defined in the `AttributeDefinitions` property.
*Required*: No
*Type*: [Array](aws-properties-dynamodb-globaltable-keyschema.md) of [KeySchema](aws-properties-dynamodb-globaltable-keyschema.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LocalSecondaryIndexes`  <a name="cfn-dynamodb-globaltable-localsecondaryindexes"></a>
Local secondary indexes to be created on the table. You can create up to five local secondary indexes. Each index is scoped to a given hash key value. The size of each hash key can be up to 10 gigabytes. Each replica in your global table will have the same local secondary index settings.
*Required*: No
*Type*: Array of [LocalSecondaryIndex](aws-properties-dynamodb-globaltable-localsecondaryindex.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`MultiRegionConsistency`  <a name="cfn-dynamodb-globaltable-multiregionconsistency"></a>
Specifies the consistency mode for a new global table.
You can specify one of the following consistency modes:
+ `EVENTUAL`: Configures a new global table for multi-Region eventual consistency (MREC).
+ `STRONG`: Configures a new global table for multi-Region strong consistency (MRSC).
If you don't specify this field, the global table consistency mode defaults to `EVENTUAL`. For more information about global tables consistency modes, see [ Consistency modes](https://docs.aws.amazon.com/V2globaltables_HowItWorks.html#V2globaltables_HowItWorks.consistency-modes) in DynamoDB developer guide.
*Required*: No
*Type*: String
*Allowed values*: `EVENTUAL | STRONG`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReadOnDemandThroughputSettings`  <a name="cfn-dynamodb-globaltable-readondemandthroughputsettings"></a>
Sets the read request settings for the global table, which applies to all replicas. This can only be applied for multi-account global tables.
*Required*: No
*Type*: [ReadOnDemandThroughputSettings](aws-properties-dynamodb-globaltable-readondemandthroughputsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReadProvisionedThroughputSettings`  <a name="cfn-dynamodb-globaltable-readprovisionedthroughputsettings"></a>
Sets read capacity settings for the global table, which applies to all replicas. This can only be applied for multi-account global tables.
*Required*: No
*Type*: [GlobalReadProvisionedThroughputSettings](aws-properties-dynamodb-globaltable-globalreadprovisionedthroughputsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Replicas`  <a name="cfn-dynamodb-globaltable-replicas"></a>
Specifies the list of replicas for your global table. The list must contain at least one element, the region where the stack defining the global table is deployed. For example, if you define your table in a stack deployed to us-east-1, you must have an entry in `Replicas` with the region us-east-1. You cannot remove the replica in the stack region.
Adding a replica might take a few minutes for an empty table, or up to several hours for large tables. If you want to add or remove a replica, we recommend submitting an `UpdateStack` operation containing only that change.
If you add or delete a replica during an update, we recommend that you don't update any other resources. If your stack fails to update and is rolled back while adding a new replica, you might need to manually delete the replica.
You can create a new global table with as many replicas as needed. You can add or remove replicas after table creation, but you can only add or remove a single replica in each update. For Multi-Region Strong Consistency (MRSC), you can add or remove up to 3 replicas, or 2 replicas plus a witness Region.
*Required*: Yes
*Type*: Array of [ReplicaSpecification](aws-properties-dynamodb-globaltable-replicaspecification.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SSESpecification`  <a name="cfn-dynamodb-globaltable-ssespecification"></a>
Specifies the settings to enable server-side encryption. These settings will be applied to all replicas. If you plan to use customer-managed KMS keys, you must provide a key for each replica using the `ReplicaSpecification.ReplicaSSESpecification` property.
*Required*: No
*Type*: [SSESpecification](aws-properties-dynamodb-globaltable-ssespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamSpecification`  <a name="cfn-dynamodb-globaltable-streamspecification"></a>
Specifies the streams settings on your global table. You must provide a value for this property if your global table contains more than one replica. You can only change the streams settings if your global table has only one replica. For Multi-Region Strong Consistency (MRSC), you do not need to provide a value for this property and can change the settings at any time.
*Required*: No
*Type*: [StreamSpecification](aws-properties-dynamodb-globaltable-streamspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableName`  <a name="cfn-dynamodb-globaltable-tablename"></a>
A name for the global table. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID as the table name. For more information, see [Name type](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).
If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9_.-]+`
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TimeToLiveSpecification`  <a name="cfn-dynamodb-globaltable-timetolivespecification"></a>
Specifies the time to live (TTL) settings for the table. This setting will be applied to all replicas.
*Required*: No
*Type*: [TimeToLiveSpecification](aws-properties-dynamodb-globaltable-timetolivespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WarmThroughput`  <a name="cfn-dynamodb-globaltable-warmthroughput"></a>
Provides visibility into the number of read and write operations your table or secondary index can instantaneously support. The settings can be modified using the `UpdateTable` operation to meet the throughput requirements of an upcoming peak event.
*Required*: No
*Type*: [WarmThroughput](aws-properties-dynamodb-globaltable-warmthroughput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WriteOnDemandThroughputSettings`  <a name="cfn-dynamodb-globaltable-writeondemandthroughputsettings"></a>
Sets the write request settings for a global table or a global secondary index. You can only specify this setting if your resource uses the `PAY_PER_REQUEST``BillingMode`.
*Required*: No
*Type*: [WriteOnDemandThroughputSettings](aws-properties-dynamodb-globaltable-writeondemandthroughputsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WriteProvisionedThroughputSettings`  <a name="cfn-dynamodb-globaltable-writeprovisionedthroughputsettings"></a>
Specifies an auto scaling policy for write capacity. This policy will be applied to all replicas. This setting must be specified if `BillingMode` is set to `PROVISIONED`.
*Required*: No
*Type*: [WriteProvisionedThroughputSettings](aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-dynamodb-globaltable-return-values"></a>

### Ref
<a name="aws-resource-dynamodb-globaltable-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the table name.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-dynamodb-globaltable-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-dynamodb-globaltable-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the DynamoDB table, such as `arn:aws:dynamodb:us-east-2:123456789012:table/myDynamoDBTable`. The ARN returned is that of the replica in the region the stack is deployed to.

`StreamArn`  <a name="StreamArn-fn::getatt"></a>
The ARN of the DynamoDB stream, such as `arn:aws:dynamodb:us-east-1:123456789012:table/testddbstack-myDynamoDBTable-012A1SL7SMP5Q/stream/2015-11-30T20:10:00.000`. The `StreamArn` returned is that of the replica in the region the stack is deployed to.
You must specify the `StreamSpecification` property to use this attribute.

`TableId`  <a name="TableId-fn::getatt"></a>
Unique identifier for the table, such as `a123b456-01ab-23cd-123a-111222aaabbb`. The `TableId` returned is that of the replica in the region the stack is deployed to.
