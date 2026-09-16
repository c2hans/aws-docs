---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-filecache-datarepositoryassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::FileCache DataRepositoryAssociation
<a name="aws-properties-fsx-filecache-datarepositoryassociation"></a>

The configuration of a data repository association that links an Amazon FSx for Lustre file system to an Amazon S3 bucket or an Amazon File Cache resource to an Amazon S3 bucket or an NFS file system. The data repository association configuration object is returned in the response of the following operations:
+  `CreateDataRepositoryAssociation`
+  `UpdateDataRepositoryAssociation`
+  `DescribeDataRepositoryAssociations`

Data repository associations are supported on Amazon File Cache resources and all FSx for Lustre 2.12 and 2.15 file systems, excluding Intelligent-Tiering and `scratch_1` file systems.

## Syntax
<a name="aws-properties-fsx-filecache-datarepositoryassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-filecache-datarepositoryassociation-syntax.json"></a>

```
{
  "[DataRepositoryPath](#cfn-fsx-filecache-datarepositoryassociation-datarepositorypath)" : {{String}},
  "[FileCachePath](#cfn-fsx-filecache-datarepositoryassociation-filecachepath)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-filecache-datarepositoryassociation-syntax.yaml"></a>

```
  [DataRepositoryPath](#cfn-fsx-filecache-datarepositoryassociation-datarepositorypath): {{String}}
  [FileCachePath](#cfn-fsx-filecache-datarepositoryassociation-filecachepath): {{String}}
```

## Properties
<a name="aws-properties-fsx-filecache-datarepositoryassociation-properties"></a>

`DataRepositoryPath`  <a name="cfn-fsx-filecache-datarepositoryassociation-datarepositorypath"></a>
The path to the data repository that will be linked to the cache or file system.
+ For Amazon File Cache, the path can be an NFS data repository that will be linked to the cache. The path can be in one of two formats:
  + If you are not using the `DataRepositorySubdirectories` parameter, the path is to an NFS Export directory (or one of its subdirectories) in the format `nsf://nfs-domain-name/exportpath`. You can therefore link a single NFS Export to a single data repository association.
  + If you are using the `DataRepositorySubdirectories` parameter, the path is the domain name of the NFS file system in the format `nfs://filer-domain-name`, which indicates the root of the subdirectories specified with the `DataRepositorySubdirectories` parameter.
+ For Amazon File Cache, the path can be an S3 bucket or prefix in the format `s3://bucket-name/prefix/` (where `prefix` is optional).
+ For Amazon FSx for Lustre, the path can be an S3 bucket or prefix in the format `s3://bucket-name/prefix/` (where `prefix` is optional).
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `4357`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FileCachePath`  <a name="cfn-fsx-filecache-datarepositoryassociation-filecachepath"></a>
A path on the Amazon File Cache that points to a high-level directory (such as `/ns1/`) or subdirectory (such as `/ns1/subdir/`) that will be mapped 1-1 with `DataRepositoryPath`. The leading forward slash in the path is required. Two data repository associations cannot have overlapping cache paths. For example, if a data repository is associated with cache path `/ns1/`, then you cannot link another data repository with cache path `/ns1/ns2`.
This path specifies the directory in your cache where files will be exported from. This cache directory can be linked to only one data repository (S3 or NFS) and no other data repository can be linked to the directory.
The cache path can only be set to root (/) on an NFS DRA when `DataRepositorySubdirectories` is specified. If you specify root (/) as the cache path, you can create only one DRA on the cache.
The cache path cannot be set to root (/) for an S3 DRA.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
