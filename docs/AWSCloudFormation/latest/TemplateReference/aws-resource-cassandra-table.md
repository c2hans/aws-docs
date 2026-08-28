---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cassandra-table.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Table
<a name="aws-resource-cassandra-table"></a>

You can use the `AWS::Cassandra::Table` resource to create a new table in Amazon Keyspaces (for Apache Cassandra). For more information, see [Create a table](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.tables.html) in the *Amazon Keyspaces Developer Guide*.

## Syntax
<a name="aws-resource-cassandra-table-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cassandra-table-syntax.json"></a>

```
{
  "Type" : "AWS::Cassandra::Table",
  "Properties" : {
      "[AutoScalingSpecifications](#cfn-cassandra-table-autoscalingspecifications)" : {{AutoScalingSpecification}},
      "[BillingMode](#cfn-cassandra-table-billingmode)" : {{BillingMode}},
      "[CdcSpecification](#cfn-cassandra-table-cdcspecification)" : {{CdcSpecification}},
      "[ClientSideTimestampsEnabled](#cfn-cassandra-table-clientsidetimestampsenabled)" : {{Boolean}},
      "[ClusteringKeyColumns](#cfn-cassandra-table-clusteringkeycolumns)" : {{[ ClusteringKeyColumn, ... ]}},
      "[DefaultTimeToLive](#cfn-cassandra-table-defaulttimetolive)" : {{Integer}},
      "[EncryptionSpecification](#cfn-cassandra-table-encryptionspecification)" : {{EncryptionSpecification}},
      "[KeyspaceName](#cfn-cassandra-table-keyspacename)" : {{String}},
      "[PartitionKeyColumns](#cfn-cassandra-table-partitionkeycolumns)" : {{[ Column, ... ]}},
      "[PointInTimeRecoveryEnabled](#cfn-cassandra-table-pointintimerecoveryenabled)" : {{Boolean}},
      "[RegularColumns](#cfn-cassandra-table-regularcolumns)" : {{[ Column, ... ]}},
      "[ReplicaSpecifications](#cfn-cassandra-table-replicaspecifications)" : {{[ ReplicaSpecification, ... ]}},
      "[TableName](#cfn-cassandra-table-tablename)" : {{String}},
      "[Tags](#cfn-cassandra-table-tags)" : {{[ Tag, ... ]}},
      "[WarmThroughput](#cfn-cassandra-table-warmthroughput)" : {{WarmThroughput}}
    }
}
```

### YAML
<a name="aws-resource-cassandra-table-syntax.yaml"></a>

```
Type: AWS::Cassandra::Table
Properties:
  [AutoScalingSpecifications](#cfn-cassandra-table-autoscalingspecifications): {{
    AutoScalingSpecification}}
  [BillingMode](#cfn-cassandra-table-billingmode): {{
    BillingMode}}
  [CdcSpecification](#cfn-cassandra-table-cdcspecification): {{
    CdcSpecification}}
  [ClientSideTimestampsEnabled](#cfn-cassandra-table-clientsidetimestampsenabled): {{Boolean}}
  [ClusteringKeyColumns](#cfn-cassandra-table-clusteringkeycolumns): {{
    - ClusteringKeyColumn}}
  [DefaultTimeToLive](#cfn-cassandra-table-defaulttimetolive): {{Integer}}
  [EncryptionSpecification](#cfn-cassandra-table-encryptionspecification): {{
    EncryptionSpecification}}
  [KeyspaceName](#cfn-cassandra-table-keyspacename): {{String}}
  [PartitionKeyColumns](#cfn-cassandra-table-partitionkeycolumns): {{
    - Column}}
  [PointInTimeRecoveryEnabled](#cfn-cassandra-table-pointintimerecoveryenabled): {{Boolean}}
  [RegularColumns](#cfn-cassandra-table-regularcolumns): {{
    - Column}}
  [ReplicaSpecifications](#cfn-cassandra-table-replicaspecifications): {{
    - ReplicaSpecification}}
  [TableName](#cfn-cassandra-table-tablename): {{String}}
  [Tags](#cfn-cassandra-table-tags): {{
    - Tag}}
  [WarmThroughput](#cfn-cassandra-table-warmthroughput): {{
    WarmThroughput}}
```

## Properties
<a name="aws-resource-cassandra-table-properties"></a>

`AutoScalingSpecifications`  <a name="cfn-cassandra-table-autoscalingspecifications"></a>
The optional auto scaling capacity settings for a table in provisioned capacity mode.
*Required*: No
*Type*: [AutoScalingSpecification](aws-properties-cassandra-table-autoscalingspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BillingMode`  <a name="cfn-cassandra-table-billingmode"></a>
The billing mode for the table, which determines how you'll be charged for reads and writes:
+ **On-demand mode** (default) - You pay based on the actual reads and writes your application performs.
+ **Provisioned mode** - Lets you specify the number of reads and writes per second that you need for your application.
If you don't specify a value for this property, then the table will use on-demand mode.
*Required*: No
*Type*: [BillingMode](aws-properties-cassandra-table-billingmode.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CdcSpecification`  <a name="cfn-cassandra-table-cdcspecification"></a>
The settings for the CDC stream of a table. For more information about CDC streams, see [Working with change data capture (CDC) streams in Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/cdc.html) in the *Amazon Keyspaces Developer Guide*.
*Required*: No
*Type*: [CdcSpecification](aws-properties-cassandra-table-cdcspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientSideTimestampsEnabled`  <a name="cfn-cassandra-table-clientsidetimestampsenabled"></a>
Enables client-side timestamps for the table. By default, the setting is disabled. You can enable client-side timestamps with the following option:
+  `status: "enabled"`
After client-side timestamps are enabled for a table, you can't disable this setting.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClusteringKeyColumns`  <a name="cfn-cassandra-table-clusteringkeycolumns"></a>
One or more columns that determine how the table data is sorted.
*Required*: No
*Type*: Array of [ClusteringKeyColumn](aws-properties-cassandra-table-clusteringkeycolumn.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefaultTimeToLive`  <a name="cfn-cassandra-table-defaulttimetolive"></a>
The default Time To Live (TTL) value for all rows in a table in seconds. The maximum configurable value is 630,720,000 seconds, which is the equivalent of 20 years. By default, the TTL value for a table is 0, which means data does not expire.
For more information, see [Setting the default TTL value for a table](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-it-works.html#ttl-howitworks_default_ttl) in the *Amazon Keyspaces Developer Guide*.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionSpecification`  <a name="cfn-cassandra-table-encryptionspecification"></a>
The encryption at rest options for the table.
+ **AWS owned key** (default) - The key is owned by Amazon Keyspaces.
+ **Customer managed key** - The key is stored in your account and is created, owned, and managed by you.
**Note**
If you choose encryption with a customer managed key, you must specify a valid customer managed KMS key with permissions granted to Amazon Keyspaces.
For more information, see [Encryption at rest in Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html) in the *Amazon Keyspaces Developer Guide*.
*Required*: No
*Type*: [EncryptionSpecification](aws-properties-cassandra-table-encryptionspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyspaceName`  <a name="cfn-cassandra-table-keyspacename"></a>
The name of the keyspace to create the table in. The keyspace must already exist.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_]{1,47}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PartitionKeyColumns`  <a name="cfn-cassandra-table-partitionkeycolumns"></a>
One or more columns that uniquely identify every row in the table. Every table must have a partition key.
*Required*: Yes
*Type*: Array of [Column](aws-properties-cassandra-table-column.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PointInTimeRecoveryEnabled`  <a name="cfn-cassandra-table-pointintimerecoveryenabled"></a>
Specifies if point-in-time recovery is enabled or disabled for the table. The options are `PointInTimeRecoveryEnabled=true` and `PointInTimeRecoveryEnabled=false`. If not specified, the default is `PointInTimeRecoveryEnabled=false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegularColumns`  <a name="cfn-cassandra-table-regularcolumns"></a>
One or more columns that are not part of the primary key - that is, columns that are *not* defined as partition key columns or clustering key columns.
You can add regular columns to existing tables by adding them to the template.
*Required*: No
*Type*: Array of [Column](aws-properties-cassandra-table-column.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicaSpecifications`  <a name="cfn-cassandra-table-replicaspecifications"></a>
The AWS Region specific settings of a multi-Region table.
For a multi-Region table, you can configure the table's read capacity differently per AWS Region. You can do this by configuring the following parameters.
+ `region`: The Region where these settings are applied. (Required)
+ `readCapacityUnits`: The provisioned read capacity units. (Optional)
+ `readCapacityAutoScaling`: The read capacity auto scaling settings for the table. (Optional)
*Required*: No
*Type*: Array of [ReplicaSpecification](aws-properties-cassandra-table-replicaspecification.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableName`  <a name="cfn-cassandra-table-tablename"></a>
The name of the table to be created. The table name is case sensitive. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the table name. For more information, see [Name type](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).
If you specify a name, you can't perform updates that require replacing this resource. You can perform updates that require no interruption or some interruption. If you must replace the resource, specify a new name.
*Length constraints:* Minimum length of 3. Maximum length of 255.
 *Pattern:* `^[a-zA-Z0-9][a-zA-Z0-9_]{1,47}$`
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_]{1,47}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cassandra-table-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-cassandra-table-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WarmThroughput`  <a name="cfn-cassandra-table-warmthroughput"></a>
Property description not available.
*Required*: No
*Type*: [WarmThroughput](aws-properties-cassandra-table-warmthroughput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cassandra-table-return-values"></a>

### Ref
<a name="aws-resource-cassandra-table-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the table and the keyspace where the table exists (delimited by '\|'). For example:

 `{ "Ref": "myKeyspace|myTable" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-cassandra-table--examples"></a>

**Topics**
+ [Create a table with minimal options](#aws-resource-cassandra-table--examples--Create_a_table_with_minimal_options)
+ [Create a table with frozen collections](#aws-resource-cassandra-table--examples--Create_a_table_with_frozen_collections)
+ [Create a table with static columns](#aws-resource-cassandra-table--examples--Create_a_table_with_static_columns)
+ [Create a table with a stream](#aws-resource-cassandra-table--examples--Create_a_table_with_a_stream)
+ [Create a table with a stream and tags](#aws-resource-cassandra-table--examples--Create_a_table_with_a_stream_and_tags)
+ [Create a table with client-side timestamps and other options](#aws-resource-cassandra-table--examples--Create_a_table_with_client-side_timestamps_and_other_options)
+ [Create a single Region table in provisioned capacity mode with auto scaling](#aws-resource-cassandra-table--examples--Create_a_single_Region_table_in_provisioned_capacity_mode_with_auto_scaling)
+ [Create a multi-Region table in provisioned capacity mode with auto scaling](#aws-resource-cassandra-table--examples--Create_a_multi-Region_table_in_provisioned_capacity_mode_with_auto_scaling)
+ [Create a table with customer managed keys and other options](#aws-resource-cassandra-table--examples--Create_a_table_with_customer_managed_keys_and_other_options)
+ [Add new columns to an existing table](#aws-resource-cassandra-table--examples--Add_new_columns_to_an_existing_table)

### Create a table with minimal options
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_minimal_options"></a>

The following example creates a new table. The table has the name `my_table`, and uses on-demand billing.

#### JSON
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_minimal_options--JSON"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "myNewTable": {
      "Type": "AWS::Cassandra::Table",
      "Properties": {
        "KeyspaceName": "my_keyspace",
        "TableName":"my_table",
        "PartitionKeyColumns": [
          {
            "ColumnName": "Message",
            "ColumnType": "ASCII"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_minimal_options--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myNewTable:
    Type: 'AWS::Cassandra::Table'
    Properties:
      KeyspaceName: my_keyspace
      TableName: my_table
      PartitionKeyColumns:
        - ColumnName: Message
          ColumnType: ASCII
```

### Create a table with frozen collections
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_frozen_collections"></a>

The following example creates a new table with the name `my_table` where the columns `projects`, `addresses`, and `org_members_by_dept` use frozen collections.

#### JSON
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_frozen_collections--JSON"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "myTable": {
      "Type": "AWS::Cassandra::Table",
      "Properties": {
        "KeyspaceName": "my_keyspace",
        "TableName":"my_table",
        "PartitionKeyColumns": [
          {
            "ColumnName": "message",
            "ColumnType": "ASCII"
          }
        ],
        "RegularColumns": [
          {
            "ColumnName": "name",
            "ColumnType": "TEXT"
          },
          {
            "ColumnName": "region",
            "ColumnType": "TEXT"
          },
          {
            "ColumnName": "projects",
            "ColumnType": "FROZEN<SET<TEXT>>"
          },
          {
            "ColumnName": "role",
            "ColumnType": "TEXT"
          },
          {
            "ColumnName": "addresses",
            "ColumnType": "FROZEN<MAP<TEXT, SET<TEXT>>>"
          },
          {
            "ColumnName": "pay_scale",
            "ColumnType": "TEXT"
          },
          {
            "ColumnName": "vacation_hrs",
            "ColumnType": "FLOAT"
          },
          {
            "ColumnName": "manager_id",
            "ColumnType": "TEXT"
          },
          {
            "ColumnName": "org_members_by_dept",
            "ColumnType": "MAP<INT, FROZEN<LIST<TEXT>>>"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_frozen_collections--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myTable:
    Type: 'AWS::Cassandra::Table'
    Properties:
      KeyspaceName: my_keyspace
      TableName: my_table
      PartitionKeyColumns:
        - ColumnName: message
          ColumnType: ASCII
      RegularColumns:
        - ColumnName: name
          ColumnType: TEXT
        - ColumnName: region
          ColumnType: TEXT
        - ColumnName: projects
          ColumnType: FROZEN<SET<TEXT>>
        - ColumnName: role
          ColumnType: TEXT
        - ColumnName: addresses
          ColumnType: FROZEN<MAP<TEXT, SET<TEXT>>>
        - ColumnName: pay_scale
          ColumnType: TEXT
        - ColumnName: vacation_hrs
          ColumnType: FLOAT
        - ColumnName: manager_id
          ColumnType: TEXT
        - ColumnName: org_members_by_dept
          ColumnType: MAP<INT, FROZEN<LIST<TEXT>>>
```

### Create a table with static columns
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_static_columns"></a>

The following example creates a new table with the name `my_table`. The columns `company_name` and `company_id` are static columns.

#### JSON
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_static_columns--JSON"></a>

```
{
   "AWSTemplateFormatVersion":"2010-09-09",
   "Resources":{
      "myNewTable":{
         "Type":"AWS::Cassandra::Table",
         "Properties":{
            "KeyspaceName":"my_keyspace",
            "TableName":"my_table",
            "PartitionKeyColumns":[
               {
                  "ColumnName":"id",
                  "ColumnType":"ASCII"
               }
            ],
            "ClusteringKeyColumns":[
               {
                  "Column":{
                     "ColumnName":"division",
                     "ColumnType":"ASCII"
                  },
                  "OrderBy":"ASC"
               }
            ],
            "RegularColumns":[
               {
                  "ColumnName":"name",
                  "ColumnType":"TEXT"
               },
               {
                  "ColumnName":"company_name",
                  "ColumnType":"TEXT STATIC"
               },
               {
                  "ColumnName":"company_id",
                  "ColumnType":"INT STATIC"
               },
               {
                  "ColumnName":"region",
                  "ColumnType":"TEXT"
               },
               {
                  "ColumnName":"project",
                  "ColumnType":"TEXT"
               },
               {
                  "ColumnName":"role",
                  "ColumnType":"TEXT"
               },
               {
                  "ColumnName":"pay_scale",
                  "ColumnType":"TEXT"
               },
               {
                  "ColumnName":"vacation_hrs",
                  "ColumnType":"FLOAT"
               },
               {
                  "ColumnName":"manager_id",
                  "ColumnType":"TEXT"
               }
            ],
            "BillingMode":{
               "Mode":"PROVISIONED",
               "ProvisionedThroughput":{
                  "ReadCapacityUnits":5,
                  "WriteCapacityUnits":5
               }
            },
            "ClientSideTimestampsEnabled":true,
            "DefaultTimeToLive":63072000,
            "PointInTimeRecoveryEnabled":true,
            "Tags":[
              {
                 "Key":"tag1",
                 "Value":"val1"
              },
              {
                 "Key":"tag2",
                 "Value":"val2"
              }
           ]
         }
      }
   }
}
```

#### YAML
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_static_columns--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  myNewTable:
    Type: AWS::Cassandra::Table
    Properties:
      KeyspaceName: my_keyspace
      TableName: my_table
      PartitionKeyColumns:
      - ColumnName: id
        ColumnType: ASCII
      ClusteringKeyColumns:
      - Column:
          ColumnName: division
          ColumnType: ASCII
        OrderBy: ASC
      RegularColumns:
      - ColumnName: name
        ColumnType: TEXT
      - ColumnName: company_name
        ColumnType: TEXT STATIC
      - ColumnName: company_id
        ColumnType: INT STATIC
      - ColumnName: region
        ColumnType: TEXT
      - ColumnName: project
        ColumnType: TEXT
      - ColumnName: role
        ColumnType: TEXT
      - ColumnName: pay_scale
        ColumnType: TEXT
      - ColumnName: vacation_hrs
        ColumnType: FLOAT
      - ColumnName: manager_id
        ColumnType: TEXT
      BillingMode:
        Mode: PROVISIONED
        ProvisionedThroughput:
          ReadCapacityUnits: 5
          WriteCapacityUnits: 5
      ClientSideTimestampsEnabled: true
      DefaultTimeToLive: 63072000
      PointInTimeRecoveryEnabled: true
      Tags:
        - Key: tag1
          Value: val1
        - Key: tag2
          Value: val2
```

### Create a table with a stream
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_a_stream"></a>

The following example creates a new table. The table has the name `my_table`, and the table has a stream.

#### JSON
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_a_stream--JSON"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "myNewTable": {
      "Type": "AWS::Cassandra::Table",
      "Properties": {
        "KeyspaceName": "my_keyspace",
        "TableName":"my_table",
        "PartitionKeyColumns": [
          {
            "ColumnName": "Message",
            "ColumnType": "ASCII"
          }
        ],
        "CdcSpecification": {
          "Status": "ENABLED",
          "ViewType": "NEW_AND_OLD_IMAGES"
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_a_stream--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myNewTable:
    Type: 'AWS::Cassandra::Table'
    Properties:
      KeyspaceName: my_keyspace
      TableName: my_table
      PartitionKeyColumns:
        - ColumnName: Message
          ColumnType: ASCII
      CdcSpecification:
        Status: ENABLED
        ViewType: NEW_AND_OLD_IMAGES
```

### Create a table with a stream and tags
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_a_stream_and_tags"></a>

The following example creates a new table. The table has the name `my_table`, and the table has a stream with two tags.

#### JSON
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_a_stream_and_tags--JSON"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "myNewTable": {
      "Type": "AWS::Cassandra::Table",
      "Properties": {
        "KeyspaceName": "my_keyspace",
        "TableName":"my_table",
        "PartitionKeyColumns": [
          {
            "ColumnName": "Message",
            "ColumnType": "ASCII"
          }
        ],
        "CdcSpecification": {
          "Status": "ENABLED",
          "ViewType": "NEW_AND_OLD_IMAGES",
          "Tags":[
            {
               "Key":"tag1",
               "Value":"val1"
            },
            {
               "Key":"tag2",
               "Value":"val2"
            }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_a_stream_and_tags--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myNewTable:
    Type: 'AWS::Cassandra::Table'
    Properties:
      KeyspaceName: my_keyspace
      TableName: my_table
      PartitionKeyColumns:
        - ColumnName: Message
          ColumnType: ASCII
      CdcSpecification:
        Status: ENABLED
        ViewType: NEW_AND_OLD_IMAGES
        Tags:
          - Key: tag1
            Value: val1
          - Key: tag2
            Value: val2
```

### Create a table with client-side timestamps and other options
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_client-side_timestamps_and_other_options"></a>

The following example creates a table `my_table` with client-side timestamps, provisioned read and write capacity, default TTL, PITR, and tags.

#### JSON
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_client-side_timestamps_and_other_options--JSON"></a>

```
{
   "AWSTemplateFormatVersion":"2010-09-09",
   "Resources":{
      "myNewTable":{
         "Type":"AWS::Cassandra::Table",
         "Properties":{
            "KeyspaceName":"my_keyspace",
            "TableName":"my_table",
            "PartitionKeyColumns":[
               {
                  "ColumnName":"id",
                  "ColumnType":"ASCII"
               }
            ],
            "ClusteringKeyColumns":[
               {
                  "Column":{
                     "ColumnName":"division",
                     "ColumnType":"ASCII"
                  },
                  "OrderBy":"ASC"
               }
            ],
            "RegularColumns":[
               {
                  "ColumnName":"name",
                  "ColumnType":"TEXT"
               },
               {
                  "ColumnName":"region",
                  "ColumnType":"TEXT"
               },
               {
                  "ColumnName":"project",
                  "ColumnType":"TEXT"
               },
               {
                  "ColumnName":"role",
                  "ColumnType":"TEXT"
               },
               {
                  "ColumnName":"pay_scale",
                  "ColumnType":"TEXT"
               },
               {
                  "ColumnName":"vacation_hrs",
                  "ColumnType":"FLOAT"
               },
               {
                  "ColumnName":"manager_id",
                  "ColumnType":"TEXT"
               }
            ],
            "BillingMode":{
               "Mode":"PROVISIONED",
               "ProvisionedThroughput":{
                  "ReadCapacityUnits":5,
                  "WriteCapacityUnits":5
               }
            },
            "ClientSideTimestampsEnabled":true,
            "DefaultTimeToLive":63072000,
            "PointInTimeRecoveryEnabled":true,
            "Tags":[
              {
                 "Key":"tag1",
                 "Value":"val1"
              },
              {
                 "Key":"tag2",
                 "Value":"val2"
              }
           ]
         }
      }
   }
}
```

#### YAML
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_client-side_timestamps_and_other_options--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  myNewTable:
    Type: AWS::Cassandra::Table
    Properties:
      KeyspaceName: my_keyspace
      TableName: my_table
      PartitionKeyColumns:
      - ColumnName: id
        ColumnType: ASCII
      ClusteringKeyColumns:
      - Column:
          ColumnName: division
          ColumnType: ASCII
        OrderBy: ASC
      RegularColumns:
      - ColumnName: name
        ColumnType: TEXT
      - ColumnName: region
        ColumnType: TEXT
      - ColumnName: project
        ColumnType: TEXT
      - ColumnName: role
        ColumnType: TEXT
      - ColumnName: pay_scale
        ColumnType: TEXT
      - ColumnName: vacation_hrs
        ColumnType: FLOAT
      - ColumnName: manager_id
        ColumnType: TEXT
      BillingMode:
        Mode: PROVISIONED
        ProvisionedThroughput:
          ReadCapacityUnits: 5
          WriteCapacityUnits: 5
      ClientSideTimestampsEnabled: true
      DefaultTimeToLive: 63072000
      PointInTimeRecoveryEnabled: true
      Tags:
        - Key: tag1
          Value: val1
        - Key: tag2
          Value: val2
```

### Create a single Region table in provisioned capacity mode with auto scaling
<a name="aws-resource-cassandra-table--examples--Create_a_single_Region_table_in_provisioned_capacity_mode_with_auto_scaling"></a>

The following example creates a table `my_table` with provisioned read and write capacity and auto scaling enabled.

#### JSON
<a name="aws-resource-cassandra-table--examples--Create_a_single_Region_table_in_provisioned_capacity_mode_with_auto_scaling--JSON"></a>

```
{
  "AWSTemplateFormatVersion" : "2010-09-09",
  "Resources" : {
    "myNewTable" : {
      "Type" : "AWS::Cassandra::Table",
      "Properties" : {
        "KeyspaceName" : "my_keyspace",
        "TableName" : "my_table",
        "PartitionKeyColumns" : [ {
          "ColumnName" : "Message",
          "ColumnType" : "ASCII"
        } ],
        "BillingMode" : {
          "Mode" : "PROVISIONED",
          "ProvisionedThroughput" : {
            "ReadCapacityUnits" : 5,
            "WriteCapacityUnits" : 5
          }
        },
        "AutoScalingSpecifications" : {
          "WriteCapacityAutoScaling" : {
            "AutoScalingDisabled" : false,
            "MinimumUnits" : 5,
            "MaximumUnits" : 10,
            "ScalingPolicy" : {
              "TargetTrackingScalingPolicyConfiguration" : {
                "ScaleInCooldown" : 60,
                "ScaleOutCooldown" : 60,
                "TargetValue" : 70,
                "DisableScaleIn" : false
              }
            }
          },
          "ReadCapacityAutoScaling" : {
            "AutoScalingDisabled" : false,
            "MinimumUnits" : 5,
            "MaximumUnits" : 10,
            "ScalingPolicy" : {
              "TargetTrackingScalingPolicyConfiguration" : {
                "ScaleInCooldown" : 60,
                "ScaleOutCooldown" : 60,
                "TargetValue" : 70,
                "DisableScaleIn" : false
              }
            }
          }
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cassandra-table--examples--Create_a_single_Region_table_in_provisioned_capacity_mode_with_auto_scaling--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myNewTable:
    Type: 'AWS::Cassandra::Table'
    Properties:
      KeyspaceName: my_keyspace
      TableName: my_table
      PartitionKeyColumns:
        - ColumnName: Message
          ColumnType: ASCII
      BillingMode:
        Mode: PROVISIONED
        ProvisionedThroughput:
          ReadCapacityUnits: 5
          WriteCapacityUnits: 5
      AutoScalingSpecifications:
        WriteCapacityAutoScaling:
          AutoScalingDisabled: false
          MinimumUnits: 5
          MaximumUnits: 10
          ScalingPolicy:
            TargetTrackingScalingPolicyConfiguration:
              ScaleInCooldown: 60
              ScaleOutCooldown: 60
              TargetValue: 70
              DisableScaleIn: false
        ReadCapacityAutoScaling:
          AutoScalingDisabled: false
          MinimumUnits: 5
          MaximumUnits: 10
          ScalingPolicy:
            TargetTrackingScalingPolicyConfiguration:
              ScaleInCooldown: 60
              ScaleOutCooldown: 60
              TargetValue: 70
              DisableScaleIn: false
```

### Create a multi-Region table in provisioned capacity mode with auto scaling
<a name="aws-resource-cassandra-table--examples--Create_a_multi-Region_table_in_provisioned_capacity_mode_with_auto_scaling"></a>

The following example creates a table `my_table` with provisioned read and write capacity and auto scaling enabled. In this example, first the default auto scaling settings are defined. Then using `ReplicaSpecifications`, different auto scaling settings that override the default settings are defined for the Regions `us-east-1` and `eu-west-1`.

#### JSON
<a name="aws-resource-cassandra-table--examples--Create_a_multi-Region_table_in_provisioned_capacity_mode_with_auto_scaling--JSON"></a>

```
{
  "AWSTemplateFormatVersion" : "2010-09-09",
  "Resources" : {
    "myNewTable" : {
      "Type" : "AWS::Cassandra::Table",
      "Properties" : {
        "KeyspaceName" : "my_keyspace",
        "TableName" : "my_table",
        "PartitionKeyColumns" : [ {
          "ColumnName" : "Message",
          "ColumnType" : "ASCII"
        } ],
        "BillingMode" : {
          "Mode" : "PROVISIONED",
          "ProvisionedThroughput" : {
            "ReadCapacityUnits" : 5,
            "WriteCapacityUnits" : 5
          }
        },
        "AutoScalingSpecifications" : {
          "WriteCapacityAutoScaling" : {
            "AutoScalingDisabled" : false,
            "MinimumUnits" : 5,
            "MaximumUnits" : 10,
            "ScalingPolicy" : {
              "TargetTrackingScalingPolicyConfiguration" : {
                "ScaleInCooldown" : 60,
                "ScaleOutCooldown" : 60,
                "TargetValue" : 70
              }
            }
          },
          "ReadCapacityAutoScaling" : {
            "AutoScalingDisabled" : false,
            "MinimumUnits" : 5,
            "MaximumUnits" : 10,
            "ScalingPolicy" : {
              "TargetTrackingScalingPolicyConfiguration" : {
                "ScaleInCooldown" : 60,
                "ScaleOutCooldown" : 60,
                "TargetValue" : 70
              }
            }
          }
        },
        "ReplicaSpecifications" : [ {
          "Region" : "us-east-1",
          "ReadCapacityAutoScaling" : {
            "AutoScalingDisabled" : false,
            "MinimumUnits" : 5,
            "MaximumUnits" : 20,
            "ScalingPolicy" : {
              "TargetTrackingScalingPolicyConfiguration" : {
                "ScaleInCooldown" : 60,
                "ScaleOutCooldown" : 60,
                "TargetValue" : 75,
                "DisableScaleIn" : false
              }
            }
          }
        }, {
          "Region" : "eu-west-1",
          "ReadCapacityAutoScaling" : {
            "AutoScalingDisabled" : false,
            "MinimumUnits" : 5,
            "MaximumUnits" : 50,
            "ScalingPolicy" : {
              "TargetTrackingScalingPolicyConfiguration" : {
                "ScaleInCooldown" : 60,
                "ScaleOutCooldown" : 60,
                "TargetValue" : 65,
                "DisableScaleIn" : false
              }
            }
          }
        } ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cassandra-table--examples--Create_a_multi-Region_table_in_provisioned_capacity_mode_with_auto_scaling--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myNewTable:
    Type: 'AWS::Cassandra::Table'
    Properties:
      KeyspaceName: my_keyspace
      TableName: my_table
      PartitionKeyColumns:
        - ColumnName: Message
          ColumnType: ASCII
      BillingMode:
        Mode: PROVISIONED
        ProvisionedThroughput:
          ReadCapacityUnits: 5
          WriteCapacityUnits: 5
      AutoScalingSpecifications:
        WriteCapacityAutoScaling:
          AutoScalingDisabled: false
          MinimumUnits: 5
          MaximumUnits: 10
          ScalingPolicy:
            TargetTrackingScalingPolicyConfiguration:
              ScaleInCooldown: 60
              ScaleOutCooldown: 60
              TargetValue: 70
        ReadCapacityAutoScaling:
          AutoScalingDisabled: false
          MinimumUnits: 5
          MaximumUnits: 10
          ScalingPolicy:
            TargetTrackingScalingPolicyConfiguration:
              ScaleInCooldown: 60
              ScaleOutCooldown: 60
              TargetValue: 70
      ReplicaSpecifications:
        - Region: us-east-1
          ReadCapacityAutoScaling:
            AutoScalingDisabled: false
            MinimumUnits: 5
            MaximumUnits: 20
            ScalingPolicy:
              TargetTrackingScalingPolicyConfiguration:
                ScaleInCooldown: 60
                ScaleOutCooldown: 60
                TargetValue: 75
                DisableScaleIn: false
        - Region: eu-west-1
          ReadCapacityAutoScaling:
            AutoScalingDisabled: false
            MinimumUnits: 5
            MaximumUnits: 50
            ScalingPolicy:
              TargetTrackingScalingPolicyConfiguration:
                ScaleInCooldown: 60
                ScaleOutCooldown: 60
                TargetValue: 65
                DisableScaleIn: false
```

### Create a table with customer managed keys and other options
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_customer_managed_keys_and_other_options"></a>

The following example creates a table `my_table` with customer managed encryption keys and all other available options. For example, provisioned read and write capacity, default TTL, PITR, and tags. To use this sample, you must replace the key ARN in the example with your own.

#### JSON
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_customer_managed_keys_and_other_options--JSON"></a>

```
{
   "AWSTemplateFormatVersion":"2010-09-09",
   "Resources":{
      "myNewTable":{
         "Type":"AWS::Cassandra::Table",
         "Properties":{
            "KeyspaceName":"my_keyspace",
            "TableName":"my_table",
            "PartitionKeyColumns":[
               {
                  "ColumnName":"id",
                  "ColumnType":"ASCII"
               }
            ],
            "ClusteringKeyColumns":[
               {
                  "Column":{
                     "ColumnName":"division",
                     "ColumnType":"ASCII"
                  },
                  "OrderBy":"ASC"
               }
            ],
            "RegularColumns":[
               {
                  "ColumnName":"name",
                  "ColumnType":"TEXT"
               },
               {
                  "ColumnName":"region",
                  "ColumnType":"TEXT"
               },
               {
                  "ColumnName":"project",
                  "ColumnType":"TEXT"
               },
               {
                  "ColumnName":"role",
                  "ColumnType":"TEXT"
               },
               {
                  "ColumnName":"pay_scale",
                  "ColumnType":"TEXT"
               },
               {
                  "ColumnName":"vacation_hrs",
                  "ColumnType":"FLOAT"
               },
               {
                  "ColumnName":"manager_id",
                  "ColumnType":"TEXT"
               }
            ],
            "BillingMode":{
               "Mode":"PROVISIONED",
               "ProvisionedThroughput":{
                  "ReadCapacityUnits":5,
                  "WriteCapacityUnits":5
               }
            },
            "DefaultTimeToLive":63072000,
            "EncryptionSpecification":{
               "EncryptionType":"CUSTOMER_MANAGED_KMS_KEY",
               "KmsKeyIdentifier":"arn:aws:kms:eu-west-1:5555555555555:key/11111111-1111-111-1111-111111111111"
            },
            "PointInTimeRecoveryEnabled":true,
            "Tags":[
               {
                  "Key":"tag1",
                  "Value":"val1"
               },
               {
                  "Key":"tag2",
                  "Value":"val2"
               }
            ]
         }
      }
   }
}
```

#### YAML
<a name="aws-resource-cassandra-table--examples--Create_a_table_with_customer_managed_keys_and_other_options--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  myNewTable:
    Type: AWS::Cassandra::Table
    Properties:
      KeyspaceName: my_keyspace
      TableName: my_table
      PartitionKeyColumns:
      - ColumnName: id
        ColumnType: ASCII
      ClusteringKeyColumns:
      - Column:
          ColumnName: division
          ColumnType: ASCII
        OrderBy: ASC
      RegularColumns:
      - ColumnName: name
        ColumnType: TEXT
      - ColumnName: region
        ColumnType: TEXT
      - ColumnName: project
        ColumnType: TEXT
      - ColumnName: role
        ColumnType: TEXT
      - ColumnName: pay_scale
        ColumnType: TEXT
      - ColumnName: vacation_hrs
        ColumnType: FLOAT
      - ColumnName: manager_id
        ColumnType: TEXT
      BillingMode:
        Mode: PROVISIONED
        ProvisionedThroughput:
          ReadCapacityUnits: 5
          WriteCapacityUnits: 5
      DefaultTimeToLive: 63072000
      EncryptionSpecification:
        EncryptionType: CUSTOMER_MANAGED_KMS_KEY
        KmsKeyIdentifier: arn:aws:kms:eu-west-1:5555555555555:key/11111111-1111-111-1111-111111111111
      PointInTimeRecoveryEnabled: true
      Tags:
        - Key: tag1
          Value: val1
        - Key: tag2
          Value: val2
```

### Add new columns to an existing table
<a name="aws-resource-cassandra-table--examples--Add_new_columns_to_an_existing_table"></a>

The following example shows how to add five new columns to the existing table `my_table`. You can only add regular columns to a table.

#### JSON
<a name="aws-resource-cassandra-table--examples--Add_new_columns_to_an_existing_table--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "myTable": {
      "Type": "AWS::Cassandra::Table",
      "Properties": {
        "KeyspaceName": "my_keyspace",
        "TableName":"my_table",
        "PartitionKeyColumns": [
          {
            "ColumnName": "Message",
            "ColumnType": "ASCII"
          }
        ],
        "RegularColumns": [
          {
            "ColumnName": "name",
            "ColumnType": "TEXT"
          },
          {
            "ColumnName": "region",
            "ColumnType": "TEXT"
          }
        ]
      }
    }
  }
}
```

#### JSON
<a name="aws-resource-cassandra-table--examples--Add_new_columns_to_an_existing_table--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "myTable": {
      "Type": "AWS::Cassandra::Table",
      "Properties": {
        "KeyspaceName": "my_keyspace",
        "TableName":"my_table",
        "PartitionKeyColumns": [
          {
            "ColumnName": "Message",
            "ColumnType": "ASCII"
          }
        ],
        "RegularColumns": [
          {
            "ColumnName": "name",
            "ColumnType": "TEXT"
          },
          {
            "ColumnName": "region",
            "ColumnType": "TEXT"
          },
          {
            "ColumnName": "project",
            "ColumnType": "TEXT"
          },
          {
            "ColumnName": "role",
            "ColumnType": "TEXT"
          },
          {
            "ColumnName": "pay_scale",
            "ColumnType": "TEXT"
          },
          {
            "ColumnName": "vacation_hrs",
            "ColumnType": "FLOAT"
          },
          {
            "ColumnName": "manager_id",
            "ColumnType": "TEXT"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cassandra-table--examples--Add_new_columns_to_an_existing_table--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myTable:
    Type: 'AWS::Cassandra::Table'
    Properties:
      KeyspaceName: my_keyspace
      TableName: my_table
      PartitionKeyColumns:
        - ColumnName: Message
          ColumnType: ASCII
      RegularColumns:
        - ColumnName: name
          ColumnType: TEXT
        - ColumnName: region
          ColumnType: TEXT
```

#### YAML
<a name="aws-resource-cassandra-table--examples--Add_new_columns_to_an_existing_table--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  myTable:
    Type: 'AWS::Cassandra::Table'
    Properties:
      KeyspaceName: my_keyspace
      TableName: my_table
      PartitionKeyColumns:
        - ColumnName: Message
          ColumnType: ASCII
      RegularColumns:
        - ColumnName: name
          ColumnType: TEXT
        - ColumnName: region
          ColumnType: TEXT
        - ColumnName: project
          ColumnType: TEXT
        - ColumnName: role
          ColumnType: TEXT
        - ColumnName: pay_scale
          ColumnType: TEXT
        - ColumnName: vacation_hrs
          ColumnType: FLOAT
        - ColumnName: manager_id
          ColumnType: TEXT
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
