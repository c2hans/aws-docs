---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-omics-runcache.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::RunCache
<a name="aws-resource-omics-runcache"></a>

<a name="aws-resource-omics-runcache-description"></a>The `AWS::Omics::RunCache` resource Property description not available. for Omics.

## Syntax
<a name="aws-resource-omics-runcache-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-omics-runcache-syntax.json"></a>

```
{
  "Type" : "AWS::Omics::RunCache",
  "Properties" : {
      "[CacheBehavior](#cfn-omics-runcache-cachebehavior)" : {{String}},
      "[CacheBucketOwnerId](#cfn-omics-runcache-cachebucketownerid)" : {{String}},
      "[CacheS3Location](#cfn-omics-runcache-caches3location)" : {{String}},
      "[Description](#cfn-omics-runcache-description)" : {{String}},
      "[Name](#cfn-omics-runcache-name)" : {{String}},
      "[Tags](#cfn-omics-runcache-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-omics-runcache-syntax.yaml"></a>

```
Type: AWS::Omics::RunCache
Properties:
  [CacheBehavior](#cfn-omics-runcache-cachebehavior): {{String}}
  [CacheBucketOwnerId](#cfn-omics-runcache-cachebucketownerid): {{String}}
  [CacheS3Location](#cfn-omics-runcache-caches3location): {{String}}
  [Description](#cfn-omics-runcache-description): {{String}}
  [Name](#cfn-omics-runcache-name): {{String}}
  [Tags](#cfn-omics-runcache-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-omics-runcache-properties"></a>

`CacheBehavior`  <a name="cfn-omics-runcache-cachebehavior"></a>
Default cache behavior for the run cache.
*Required*: No
*Type*: String
*Allowed values*: `CACHE_ON_FAILURE | CACHE_ALWAYS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CacheBucketOwnerId`  <a name="cfn-omics-runcache-cachebucketownerid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]+$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CacheS3Location`  <a name="cfn-omics-runcache-caches3location"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])(/(.{0,1024}))?$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-omics-runcache-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-omics-runcache-name"></a>
The name of the run cache.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-omics-runcache-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-omics-runcache-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-omics-runcache-return-values"></a>

### Ref
<a name="aws-resource-omics-runcache-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-omics-runcache-return-values-fn--getatt"></a>

####
<a name="aws-resource-omics-runcache-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Unique resource identifier for the run cache.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time that this run cache was created (an ISO 8601 formatted string).

`Id`  <a name="Id-fn::getatt"></a>
The identifier for this run cache.

`Status`  <a name="Status-fn::getatt"></a>
The run cache status.
