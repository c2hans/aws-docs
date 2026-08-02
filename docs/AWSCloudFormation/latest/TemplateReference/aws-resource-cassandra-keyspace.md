---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cassandra-keyspace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Keyspace
<a name="aws-resource-cassandra-keyspace"></a>

You can use the `AWS::Cassandra::Keyspace` resource to create a new keyspace in Amazon Keyspaces (for Apache Cassandra). For more information, see [Create a keyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.keyspaces.html) in the *Amazon Keyspaces Developer Guide*.

## Syntax
<a name="aws-resource-cassandra-keyspace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cassandra-keyspace-syntax.json"></a>

```
{
  "Type" : "AWS::Cassandra::Keyspace",
  "Properties" : {
      "[ClientSideTimestampsEnabled](#cfn-cassandra-keyspace-clientsidetimestampsenabled)" : {{Boolean}},
      "[KeyspaceName](#cfn-cassandra-keyspace-keyspacename)" : {{String}},
      "[ReplicationSpecification](#cfn-cassandra-keyspace-replicationspecification)" : {{ReplicationSpecification}},
      "[Tags](#cfn-cassandra-keyspace-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cassandra-keyspace-syntax.yaml"></a>

```
Type: AWS::Cassandra::Keyspace
Properties:
  [ClientSideTimestampsEnabled](#cfn-cassandra-keyspace-clientsidetimestampsenabled): {{Boolean}}
  [KeyspaceName](#cfn-cassandra-keyspace-keyspacename): {{String}}
  [ReplicationSpecification](#cfn-cassandra-keyspace-replicationspecification): {{
    ReplicationSpecification}}
  [Tags](#cfn-cassandra-keyspace-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cassandra-keyspace-properties"></a>

`ClientSideTimestampsEnabled`  <a name="cfn-cassandra-keyspace-clientsidetimestampsenabled"></a>
Indicates whether client-side timestamps are enabled (true) or disabled (false) for all tables in the keyspace. To add a Region to a single-Region keyspace with at least one table, the value must be set to true. After you've enabled client-side timestamps for a table, you can’t disable it again.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyspaceName`  <a name="cfn-cassandra-keyspace-keyspacename"></a>
The name of the keyspace to be created. The keyspace name is case sensitive. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the keyspace name. For more information, see [Name type](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).
*Length constraints:* Minimum length of 1. Maximum length of 48.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_]{1,47}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReplicationSpecification`  <a name="cfn-cassandra-keyspace-replicationspecification"></a>
Specifies the `ReplicationStrategy` of a keyspace. The options are:
+ `SINGLE_REGION` for a single Region keyspace (optional) or
+ `MULTI_REGION` for a multi-Region keyspace
 If no `ReplicationStrategy` is provided, the default is `SINGLE_REGION`. If you choose `MULTI_REGION`, you must also provide a `RegionList` with the AWS Regions that the keyspace is replicated in.
*Required*: No
*Type*: [ReplicationSpecification](aws-properties-cassandra-keyspace-replicationspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cassandra-keyspace-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-cassandra-keyspace-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cassandra-keyspace-return-values"></a>

### Ref
<a name="aws-resource-cassandra-keyspace-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the keyspace. For example:

 `{ "Ref": "MyNewKeyspace" }`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Examples
<a name="aws-resource-cassandra-keyspace--examples"></a>

This section includes code examples that demonstrate how to create a keyspace using the different options.

**Topics**
+ [Create a new keyspace with tags](#aws-resource-cassandra-keyspace--examples--Create_a_new_keyspace_with_tags)
+ [Create a new multi-Region keyspace](#aws-resource-cassandra-keyspace--examples--Create_a_new_multi-Region_keyspace)
+ [Add a new AWS Region to a single-Region keyspace](#aws-resource-cassandra-keyspace--examples--Add_a_new_Region_to_a_single-Region_keyspace)
+ [Add a new AWS Region to a multi-Region keyspace](#aws-resource-cassandra-keyspace--examples--Add_a_new_Region_to_a_multi-Region_keyspace)

### Create a new keyspace with tags
<a name="aws-resource-cassandra-keyspace--examples--Create_a_new_keyspace_with_tags"></a>

The following example creates a new keyspace named `MyNewKeyspace` with the following tags: `{'key1':'val1', 'key2':'val2'}`.

#### JSON
<a name="aws-resource-cassandra-keyspace--examples--Create_a_new_keyspace_with_tags--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyNewKeyspace": {
      "Type": "AWS::Cassandra::Keyspace",
      "Properties": {
        "KeyspaceName": "MyNewKeyspace",
        "Tags": [{"Key":"tag1","Value":"val1"}, {"Key":"tag2","Value":"val2"}]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cassandra-keyspace--examples--Create_a_new_keyspace_with_tags--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  MyNewKeyspace:
    Type: AWS::Cassandra::Keyspace
    Properties:
      KeyspaceName: MyNewKeyspace
      Tags:
      - Key: tag1
      Value: val1
      - Key: tag2
      Value: val2
```

### Create a new multi-Region keyspace
<a name="aws-resource-cassandra-keyspace--examples--Create_a_new_multi-Region_keyspace"></a>

The following example creates a new multi-Region keyspace named `MultiRegionKeyspace` that is replicated across three AWS Regions.

#### JSON
<a name="aws-resource-cassandra-keyspace--examples--Create_a_new_multi-Region_keyspace--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MultiRegionKeyspace": {
      "Type": "AWS::Cassandra::Keyspace",
      "Properties": {
        "KeyspaceName": "MultiRegionKeyspace",
        "ReplicationSpecification": {
          "ReplicationStrategy": "MULTI_REGION",
          "RegionList": ["us-east-1", "us-west-2", "eu-west-1"]
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cassandra-keyspace--examples--Create_a_new_multi-Region_keyspace--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  MultiRegionKeyspace:
    Type: AWS::Cassandra::Keyspace
    Properties:
      KeyspaceName: MultiRegionKeyspace
      ReplicationSpecification:
        ReplicationStrategy: MULTI_REGION
        RegionList:
          - us-east-1
          - us-west-2
          - eu-west-1
```

### Add a new AWS Region to a single-Region keyspace
<a name="aws-resource-cassandra-keyspace--examples--Add_a_new_Region_to_a_single-Region_keyspace"></a>

The following example shows how to add the Region `eu-west-1` to a single-Region keyspace named `MyNewKeyspace` that is currently available in `us-east-1`.

#### JSON
<a name="aws-resource-cassandra-keyspace--examples--Add_a_new_Region_to_a_single-Region_keyspace--json"></a>

```
{
   "AWSTemplateFormatVersion":"2010-09-09",
   "Resources":{
      "MultiRegionKeyspace":{
         "Type":"AWS::Cassandra::Keyspace",
         "Properties":{
            "KeyspaceName":"MyNewKeyspace",
            "ReplicationSpecification":{
               "ReplicationStrategy":"MULTI_REGION",
               "RegionList":[
                  "us-east-1",
                  "eu-west-1"
               ]
            },
            "ClientSideTimestampsEnabled":true
         }
      }
   }
}
```

#### YAML
<a name="aws-resource-cassandra-keyspace--examples--Add_a_new_Region_to_a_single-Region_keyspace--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  MultiRegionKeyspace:
    Type: AWS::Cassandra::Keyspace
    Properties:
      KeyspaceName: MyNewKeyspace
      ReplicationSpecification:
        ReplicationStrategy: MULTI_REGION
        RegionList:
          - us-east-1
          - eu-west-1
     ClientSideTimestampsEnabled: true
```

### Add a new AWS Region to a multi-Region keyspace
<a name="aws-resource-cassandra-keyspace--examples--Add_a_new_Region_to_a_multi-Region_keyspace"></a>

The following example shows how to add the new Region `us-west-2` to the existing multi-Region keyspace named `MultiRegionKeyspace` that is already replicated across `us-east-1` and `eu-west-1`.

#### JSON
<a name="aws-resource-cassandra-keyspace--examples--Add_a_new_Region_to_a_multi-Region_keyspace--json"></a>

```
{
   "AWSTemplateFormatVersion":"2010-09-09",
   "Resources":{
      "MultiRegionKeyspace":{
         "Type":"AWS::Cassandra::Keyspace",
         "Properties":{
            "KeyspaceName":"MultiRegionKeyspace",
            "ReplicationSpecification":{
               "ReplicationStrategy":"MULTI_REGION",
               "RegionList":[
                  "us-east-1",
                  "eu-west-1",
                  "us-west-2"
               ]
            }
         }
      }
   }
}
```

#### YAML
<a name="aws-resource-cassandra-keyspace--examples--Add_a_new_Region_to_a_multi-Region_keyspace--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  MultiRegionKeyspace:
    Type: AWS::Cassandra::Keyspace
    Properties:
      KeyspaceName: MultiRegionKeyspace
      ReplicationSpecification:
        ReplicationStrategy: MULTI_REGION
        RegionList:
          - us-east-1
          - us-west-1
          - us-west-2
```
