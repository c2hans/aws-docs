---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fsx-filecache.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::FileCache
<a name="aws-resource-fsx-filecache"></a>

A description of a specific Amazon File Cache resource, which is a response object from the `DescribeFileCaches` operation.

## Syntax
<a name="aws-resource-fsx-filecache-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fsx-filecache-syntax.json"></a>

```
{
  "Type" : "AWS::FSx::FileCache",
  "Properties" : {
      "[CopyTagsToDataRepositoryAssociations](#cfn-fsx-filecache-copytagstodatarepositoryassociations)" : {{Boolean}},
      "[DataRepositoryAssociations](#cfn-fsx-filecache-datarepositoryassociations)" : {{[ DataRepositoryAssociation, ... ]}},
      "[FileCacheType](#cfn-fsx-filecache-filecachetype)" : {{String}},
      "[FileCacheTypeVersion](#cfn-fsx-filecache-filecachetypeversion)" : {{String}},
      "[KmsKeyId](#cfn-fsx-filecache-kmskeyid)" : {{String}},
      "[LustreConfiguration](#cfn-fsx-filecache-lustreconfiguration)" : {{LustreConfiguration}},
      "[SecurityGroupIds](#cfn-fsx-filecache-securitygroupids)" : {{[ String, ... ]}},
      "[StorageCapacity](#cfn-fsx-filecache-storagecapacity)" : {{Integer}},
      "[SubnetIds](#cfn-fsx-filecache-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-fsx-filecache-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-fsx-filecache-syntax.yaml"></a>

```
Type: AWS::FSx::FileCache
Properties:
  [CopyTagsToDataRepositoryAssociations](#cfn-fsx-filecache-copytagstodatarepositoryassociations): {{Boolean}}
  [DataRepositoryAssociations](#cfn-fsx-filecache-datarepositoryassociations): {{
    - DataRepositoryAssociation}}
  [FileCacheType](#cfn-fsx-filecache-filecachetype): {{String}}
  [FileCacheTypeVersion](#cfn-fsx-filecache-filecachetypeversion): {{String}}
  [KmsKeyId](#cfn-fsx-filecache-kmskeyid): {{String}}
  [LustreConfiguration](#cfn-fsx-filecache-lustreconfiguration): {{
    LustreConfiguration}}
  [SecurityGroupIds](#cfn-fsx-filecache-securitygroupids): {{
    - String}}
  [StorageCapacity](#cfn-fsx-filecache-storagecapacity): {{Integer}}
  [SubnetIds](#cfn-fsx-filecache-subnetids): {{
    - String}}
  [Tags](#cfn-fsx-filecache-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-fsx-filecache-properties"></a>

`CopyTagsToDataRepositoryAssociations`  <a name="cfn-fsx-filecache-copytagstodatarepositoryassociations"></a>
A boolean flag indicating whether tags for the cache should be copied to data repository associations.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataRepositoryAssociations`  <a name="cfn-fsx-filecache-datarepositoryassociations"></a>
Property description not available.
*Required*: No
*Type*: Array of [DataRepositoryAssociation](aws-properties-fsx-filecache-datarepositoryassociation.md)
*Maximum*: `8`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileCacheType`  <a name="cfn-fsx-filecache-filecachetype"></a>
The type of cache, which must be `LUSTRE`.
*Required*: Yes
*Type*: String
*Allowed values*: `LUSTRE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileCacheTypeVersion`  <a name="cfn-fsx-filecache-filecachetypeversion"></a>
The Lustre version of the cache, which must be `2.12`.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9](\.[0-9]*)*$`
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-fsx-filecache-kmskeyid"></a>
Specifies the ID of the AWS Key Management Service (AWS KMS) key to use for encrypting data on an Amazon File Cache. If a `KmsKeyId` isn't specified, the Amazon FSx-managed AWS KMS key for your account is used. For more information, see [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) in the *AWS Key Management Service API Reference*.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LustreConfiguration`  <a name="cfn-fsx-filecache-lustreconfiguration"></a>
The configuration for the Amazon File Cache resource.
*Required*: No
*Type*: [LustreConfiguration](aws-properties-fsx-filecache-lustreconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-fsx-filecache-securitygroupids"></a>
A list of IDs specifying the security groups to apply to all network interfaces created for file system access. This list isn't returned in later requests to describe the file system.
*Required*: No
*Type*: Array of String
*Minimum*: `11`
*Maximum*: `20 | 50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageCapacity`  <a name="cfn-fsx-filecache-storagecapacity"></a>
The storage capacity of the cache in gibibytes (GiB).
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-fsx-filecache-subnetids"></a>
A list of subnet IDs that the cache will be accessible from. You can specify only one subnet ID in a call to the `CreateFileCache` operation.
*Required*: Yes
*Type*: Array of String
*Minimum*: `15`
*Maximum*: `24 | 50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-fsx-filecache-tags"></a>
A list of `Tag` values, with a maximum of 50 elements.
*Required*: No
*Type*: Array of [Tag](aws-properties-fsx-filecache-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-fsx-filecache-return-values"></a>

### Ref
<a name="aws-resource-fsx-filecache-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-fsx-filecache-return-values-fn--getatt"></a>

####
<a name="aws-resource-fsx-filecache-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

`DataRepositoryAssociationIds`  <a name="DataRepositoryAssociationIds-fn::getatt"></a>
A list of IDs of data repository associations that are associated with this cache.

`DNSName`  <a name="DNSName-fn::getatt"></a>
The Domain Name System (DNS) name for the cache.

`FileCacheId`  <a name="FileCacheId-fn::getatt"></a>
The system-generated, unique ID of the cache.

`Lifecycle`  <a name="Lifecycle-fn::getatt"></a>
The lifecycle status of the cache. The following are the possible values and what they mean:
+ `AVAILABLE` - The cache is in a healthy state, and is reachable and available for use.
+ `CREATING` - The new cache is being created.
+ `DELETING` - An existing cache is being deleted.
+ `UPDATING` - The cache is undergoing a customer-initiated update.
+ `FAILED` - An existing cache has experienced an unrecoverable failure. When creating a new cache, the cache was unable to be created.

`LustreConfiguration.MountName`  <a name="LustreConfiguration.MountName-fn::getatt"></a>
You use the `MountName` value when mounting the cache. If you pass a cache ID to the `DescribeFileCaches` operation, it returns the the `MountName` value as part of the cache's description.

`NetworkInterfaceIds`  <a name="NetworkInterfaceIds-fn::getatt"></a>
A list of network interface IDs.

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
Property description not available.

`ResourceARN`  <a name="ResourceARN-fn::getatt"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference*.

`VpcId`  <a name="VpcId-fn::getatt"></a>
The ID of your virtual private cloud (VPC). For more information, see [VPC and subnets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) in the *Amazon VPC User Guide*.
