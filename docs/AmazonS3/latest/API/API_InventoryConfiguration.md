---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_InventoryConfiguration.html
---

# InventoryConfiguration
<a name="API_InventoryConfiguration"></a>

Specifies the S3 Inventory configuration for an Amazon S3 bucket. For more information, see [GET Bucket inventory](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketGETInventoryConfig.html) in the *Amazon S3 API Reference*.

## Contents
<a name="API_InventoryConfiguration_Contents"></a>

 ** Destination **   <a name="AmazonS3-Type-InventoryConfiguration-Destination"></a>
Contains information about where to publish the inventory results.
Type: [InventoryDestination](API_InventoryDestination.md) data type
Required: Yes

 ** Id **   <a name="AmazonS3-Type-InventoryConfiguration-Id"></a>
The ID used to identify the inventory configuration.
Type: String
Required: Yes

 ** IncludedObjectVersions **   <a name="AmazonS3-Type-InventoryConfiguration-IncludedObjectVersions"></a>
Object versions to include in the inventory list. If set to `All`, the list includes all the object versions, which adds the version-related fields `VersionId`, `IsLatest`, and `DeleteMarker` to the list. If set to `Current`, the list does not contain these version-related fields.
Type: String
Valid Values: `All | Current`
Required: Yes

 ** IsEnabled **   <a name="AmazonS3-Type-InventoryConfiguration-IsEnabled"></a>
Specifies whether the inventory is enabled or disabled. If set to `True`, an inventory list is generated. If set to `False`, no inventory list is generated.
Type: Boolean
Required: Yes

 ** Schedule **   <a name="AmazonS3-Type-InventoryConfiguration-Schedule"></a>
Specifies the schedule for generating inventory results.
Type: [InventorySchedule](API_InventorySchedule.md) data type
Required: Yes

 ** Filter **   <a name="AmazonS3-Type-InventoryConfiguration-Filter"></a>
Specifies an inventory filter. The inventory only includes objects that meet the filter's criteria.
Type: [InventoryFilter](API_InventoryFilter.md) data type
Required: No

 ** OptionalFields **   <a name="AmazonS3-Type-InventoryConfiguration-OptionalFields"></a>
Contains the optional fields that are included in the inventory results.
The following optional fields are supported for directory buckets `Size | LastModifiedDate | StorageClass | ETag | IsMultipartUploaded | EncryptionStatus | BucketKeyStatus | ChecksumAlgorithm | LifecycleExpirationDate.` Throws MalformedXML error if unsupported optional field is provided.
Type: Array of strings
Valid Values: `Size | LastModifiedDate | StorageClass | ETag | IsMultipartUploaded | ReplicationStatus | EncryptionStatus | ObjectLockRetainUntilDate | ObjectLockMode | ObjectLockLegalHoldStatus | IntelligentTieringAccessTier | BucketKeyStatus | ChecksumAlgorithm | ObjectAccessControlList | ObjectOwner | LifecycleExpirationDate`
Required: No

## See Also
<a name="API_InventoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/InventoryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/InventoryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/InventoryConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
