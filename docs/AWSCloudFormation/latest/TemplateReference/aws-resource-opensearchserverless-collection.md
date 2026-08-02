---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opensearchserverless-collection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::Collection
<a name="aws-resource-opensearchserverless-collection"></a>

Specifies an OpenSearch Serverless collection. For more information, see [Creating and managing Amazon OpenSearch Serverless collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html) in the *Amazon OpenSearch Service Developer Guide*.

**Important**
 To create a collection successfully, you must associate a KMS key for encryption. You have two options: 1. Specify the KMS key directly in the CreateCollection request – Use the encryption-config parameter when creating the collection. 2. Define the KMS key in an encryption security policy – Create a matching [encryption policy](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html) before or alongside your collection. Note: If you specify a KMS key in both locations, the key provided in the CreateCollection request takes precedence over the security policy configuration. When using CloudFormation templates, you can include the encryption policy resource in the same template as the collection resource by using the [DependsOn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html) attribute to ensure proper resource creation order. Alternatively, ensure the encryption policy or KMS key configuration exists before creating the collection.

## Syntax
<a name="aws-resource-opensearchserverless-collection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-opensearchserverless-collection-syntax.json"></a>

```
{
  "Type" : "AWS::OpenSearchServerless::Collection",
  "Properties" : {
      "[CollectionGroupName](#cfn-opensearchserverless-collection-collectiongroupname)" : {{String}},
      "[DeletionProtection](#cfn-opensearchserverless-collection-deletionprotection)" : {{String}},
      "[Description](#cfn-opensearchserverless-collection-description)" : {{String}},
      "[EncryptionConfig](#cfn-opensearchserverless-collection-encryptionconfig)" : {{EncryptionConfig}},
      "[Name](#cfn-opensearchserverless-collection-name)" : {{String}},
      "[StandbyReplicas](#cfn-opensearchserverless-collection-standbyreplicas)" : {{String}},
      "[Tags](#cfn-opensearchserverless-collection-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-opensearchserverless-collection-type)" : {{String}},
      "[VectorOptions](#cfn-opensearchserverless-collection-vectoroptions)" : {{VectorOptions}}
    }
}
```

### YAML
<a name="aws-resource-opensearchserverless-collection-syntax.yaml"></a>

```
Type: AWS::OpenSearchServerless::Collection
Properties:
  [CollectionGroupName](#cfn-opensearchserverless-collection-collectiongroupname): {{String}}
  [DeletionProtection](#cfn-opensearchserverless-collection-deletionprotection): {{String}}
  [Description](#cfn-opensearchserverless-collection-description): {{String}}
  [EncryptionConfig](#cfn-opensearchserverless-collection-encryptionconfig): {{
    EncryptionConfig}}
  [Name](#cfn-opensearchserverless-collection-name): {{String}}
  [StandbyReplicas](#cfn-opensearchserverless-collection-standbyreplicas): {{String}}
  [Tags](#cfn-opensearchserverless-collection-tags): {{
    - Tag}}
  [Type](#cfn-opensearchserverless-collection-type): {{String}}
  [VectorOptions](#cfn-opensearchserverless-collection-vectoroptions): {{
    VectorOptions}}
```

## Properties
<a name="aws-resource-opensearchserverless-collection-properties"></a>

`CollectionGroupName`  <a name="cfn-opensearchserverless-collection-collectiongroupname"></a>
The name of the collection group to associate with the collection.
*Required*: No
*Type*: String
*Pattern*: `[a-z][a-z0-9-]+`
*Minimum*: `3`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DeletionProtection`  <a name="cfn-opensearchserverless-collection-deletionprotection"></a>
Indicates whether deletion protection is `ENABLED` or `DISABLED` for the collection.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-opensearchserverless-collection-description"></a>
A description of the collection.
*Required*: No
*Type*: String
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionConfig`  <a name="cfn-opensearchserverless-collection-encryptionconfig"></a>
Encryption settings for the collection.
*Required*: No
*Type*: [EncryptionConfig](aws-properties-opensearchserverless-collection-encryptionconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-opensearchserverless-collection-name"></a>
The name of the collection.
Collection names must meet the following criteria:
+ Starts with a lowercase letter
+ Unique to your account and AWS Region
+ Contains between 3 and 28 characters
+ Contains only lowercase letters a-z, the numbers 0-9, and the hyphen (-)
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9-]{2,63}$`
*Minimum*: `3`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StandbyReplicas`  <a name="cfn-opensearchserverless-collection-standbyreplicas"></a>
Indicates whether to use standby replicas for the collection. You can't update this property after the collection is already created. If you attempt to modify this property, the collection continues to use the original value.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-opensearchserverless-collection-tags"></a>
An arbitrary set of tags (key–value pairs) to associate with the collection.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-opensearchserverless-collection-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-opensearchserverless-collection-type"></a>
The type of collection. Possible values are `SEARCH`, `TIMESERIES`, and `VECTORSEARCH`. For more information, see [Choosing a collection type](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html#serverless-usecase).
*Required*: No
*Type*: String
*Allowed values*: `SEARCH | TIMESERIES | VECTORSEARCH`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VectorOptions`  <a name="cfn-opensearchserverless-collection-vectoroptions"></a>
Configuration options for vector search capabilities in the collection.
*Required*: No
*Type*: [VectorOptions](aws-properties-opensearchserverless-collection-vectoroptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-opensearchserverless-collection-return-values"></a>

### Ref
<a name="aws-resource-opensearchserverless-collection-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the collection ID. For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-opensearchserverless-collection-return-values-fn--getatt"></a>

`GetAtt` returns a value for a specified attribute of this type. For more information, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html). The following are the available attributes and sample return values.

####
<a name="aws-resource-opensearchserverless-collection-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the collection. For example, `arn:aws:aoss:us-east-1:123456789012:collection/07tjusf2h91cunochc`.

`CollectionEndpoint`  <a name="CollectionEndpoint-fn::getatt"></a>
Collection-specific endpoint used to submit index, search, and data upload requests to an OpenSearch Serverless collection. For example, `https://07tjusf2h91cunochc.us-east-1.aoss.amazonaws.com`.

`DashboardEndpoint`  <a name="DashboardEndpoint-fn::getatt"></a>
The collection-specific endpoint used to access OpenSearch Dashboards. For example, `https://07tjusf2h91cunochc.us-east-1.aoss.amazonaws.com/_dashboards`.

`Id`  <a name="Id-fn::getatt"></a>
A unique identifier for the collection. For example, `07tjusf2h91cunochc`.

`KmsKeyArn`  <a name="KmsKeyArn-fn::getatt"></a>
The ARN of the AWS KMS key used to encrypt the collection.

## Examples
<a name="aws-resource-opensearchserverless-collection--examples"></a>

### Create a collection
<a name="aws-resource-opensearchserverless-collection--examples--Create_a_collection"></a>

The following example specifies an OpenSearch Serverless collection named `test-collection`. The collection type is `SEARCH`. The template also creates a matching encryption policy, which is required in order for the collection to be created successfully.

For a complete sample policy that creates network, encryption, and access policies, as well as a matching collection, see [Using AWS CloudFormation to create Amazon OpenSearch Serverless collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-cfn.html) in the *Amazon OpenSearch Service Developer Guide.*

**Note**
This example uses public network access, which isn't recommended for production workloads. We recommend using VPC access to protect your collections. For more information, see [AWS::OpenSearchServerless::VpcEndpoint](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-vpcendpoint.html) and [Access Amazon OpenSearch Serverless using an interface endpoint](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html).

#### JSON
<a name="aws-resource-opensearchserverless-collection--examples--Create_a_collection--json"></a>

```
{
   "Description":"OpenSearch Serverless collection template",
   "Resources":{
      "TestCollection":{
         "Type":"AWS::OpenSearchServerless::Collection",
         "Properties":{
            "Name":"test-collection",
            "Type":"SEARCH",
            "Description":"Search collection"
         },
         "DependsOn":"EncryptionPolicy"
      },
      "EncryptionPolicy":{
         "Type":"AWS::OpenSearchServerless::SecurityPolicy",
         "Properties":{
            "Name":"test-encryption-policy",
            "Type":"encryption",
            "Description":"Encryption policy for test collection",
            "Policy":"{\"Rules\":[{\"ResourceType\":\"collection\",\"Resource\":[\"collection/test-collection\"]}],\"AWSOwnedKey\":true}"
         }
      }
   }
```

#### YAML
<a name="aws-resource-opensearchserverless-collection--examples--Create_a_collection--yaml"></a>

```
Description: OpenSearch Serverless collection template
Resources:
  TestCollection:
    Type: 'AWS::OpenSearchServerless::Collection'
    Properties:
      Name: test-collection
      Type: SEARCH
      Description: Search collection
    DependsOn: EncryptionPolicy
  EncryptionPolicy:
    Type: 'AWS::OpenSearchServerless::SecurityPolicy'
    Properties:
      Name: test-encryption-policy
      Type: encryption
      Description: Encryption policy for test collection
      Policy: >-
        {"Rules":[{"ResourceType":"collection","Resource":["collection/test-collection"]}],"AWSOwnedKey":true}
```
