---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3express-directorybucket-inventoryconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::DirectoryBucket InventoryConfiguration
<a name="aws-properties-s3express-directorybucket-inventoryconfiguration"></a>

Specifies the S3 Inventory configuration for an Amazon S3 bucket. For more information, see [GET Bucket inventory](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketGETInventoryConfig.html) in the *Amazon S3 API Reference*.

## Syntax
<a name="aws-properties-s3express-directorybucket-inventoryconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3express-directorybucket-inventoryconfiguration-syntax.json"></a>

```
{
  "[Destination](#cfn-s3express-directorybucket-inventoryconfiguration-destination)" : {{Destination}},
  "[Enabled](#cfn-s3express-directorybucket-inventoryconfiguration-enabled)" : {{Boolean}},
  "[Id](#cfn-s3express-directorybucket-inventoryconfiguration-id)" : {{String}},
  "[IncludedObjectVersions](#cfn-s3express-directorybucket-inventoryconfiguration-includedobjectversions)" : {{String}},
  "[OptionalFields](#cfn-s3express-directorybucket-inventoryconfiguration-optionalfields)" : {{[ String, ... ]}},
  "[Prefix](#cfn-s3express-directorybucket-inventoryconfiguration-prefix)" : {{String}},
  "[ScheduleFrequency](#cfn-s3express-directorybucket-inventoryconfiguration-schedulefrequency)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3express-directorybucket-inventoryconfiguration-syntax.yaml"></a>

```
  [Destination](#cfn-s3express-directorybucket-inventoryconfiguration-destination): {{
    Destination}}
  [Enabled](#cfn-s3express-directorybucket-inventoryconfiguration-enabled): {{Boolean}}
  [Id](#cfn-s3express-directorybucket-inventoryconfiguration-id): {{String}}
  [IncludedObjectVersions](#cfn-s3express-directorybucket-inventoryconfiguration-includedobjectversions): {{String}}
  [OptionalFields](#cfn-s3express-directorybucket-inventoryconfiguration-optionalfields): {{
    - String}}
  [Prefix](#cfn-s3express-directorybucket-inventoryconfiguration-prefix): {{String}}
  [ScheduleFrequency](#cfn-s3express-directorybucket-inventoryconfiguration-schedulefrequency): {{String}}
```

## Properties
<a name="aws-properties-s3express-directorybucket-inventoryconfiguration-properties"></a>

`Destination`  <a name="cfn-s3express-directorybucket-inventoryconfiguration-destination"></a>
Contains information about where to publish the inventory results.
*Required*: Yes
*Type*: [Destination](aws-properties-s3express-directorybucket-destination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-s3express-directorybucket-inventoryconfiguration-enabled"></a>
Property description not available.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-s3express-directorybucket-inventoryconfiguration-id"></a>
The ID used to identify the inventory configuration.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludedObjectVersions`  <a name="cfn-s3express-directorybucket-inventoryconfiguration-includedobjectversions"></a>
Object versions to include in the inventory list. If set to `All`, the list includes all the object versions, which adds the version-related fields `VersionId`, `IsLatest`, and `DeleteMarker` to the list. If set to `Current`, the list does not contain these version-related fields.
*Required*: Yes
*Type*: String
*Allowed values*: `All | Current`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OptionalFields`  <a name="cfn-s3express-directorybucket-inventoryconfiguration-optionalfields"></a>
Contains the optional fields that are included in the inventory results.
The following optional fields are supported for directory buckets `Size | LastModifiedDate | StorageClass | ETag | IsMultipartUploaded | EncryptionStatus | BucketKeyStatus | ChecksumAlgorithm | LifecycleExpirationDate.` Throws MalformedXML error if unsupported optional field is provided.
*Required*: No
*Type*: Array of String
*Allowed values*: `Size | LastModifiedDate | StorageClass | ETag | IsMultipartUploaded | EncryptionStatus | BucketKeyStatus | ChecksumAlgorithm | LifecycleExpirationDate`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-s3express-directorybucket-inventoryconfiguration-prefix"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleFrequency`  <a name="cfn-s3express-directorybucket-inventoryconfiguration-schedulefrequency"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `Daily | Weekly`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
