---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3-statistics.html
---

# Data Sources - Amazon S3 Statistics
<a name="datasources-s3-statistics"></a>

The Amazon S3 Data Source Statistics resource provides aggregated statistical data for all the Amazon Simple Storage Service (Amazon S3) buckets that Amazon Macie monitors and analyzes for your account. If you're the Macie administrator for an organization, this includes S3 buckets that your member accounts own.

This resource provides aggregated data for key security metrics such as the number of S3 buckets that are publicly accessible or shared with other AWS accounts. If automated sensitive data discovery is enabled, it also provides aggregated data for metrics such as the number of buckets that Macie has found sensitive data in. Note that statistical data is available only for S3 general purpose buckets. Macie doesn't monitor or analyze S3 directory buckets.

You can use the Amazon S3 Data Source Statistics resource to retrieve (query) aggregated data for data security and sensitivity metrics that apply to all the S3 general purpose buckets that Macie monitors and analyzes for your account. To retrieve additional data for these buckets, use the [Amazon S3 Data Sources](datasources-s3.md) resource.

## URI
<a name="datasources-s3-statistics-url"></a>

`/datasources/s3/statistics`

## HTTP methods
<a name="datasources-s3-statistics-http-methods"></a>

### POST
<a name="datasources-s3-statisticspost"></a>

**Operation ID:** `GetBucketStatistics`

Retrieves (queries) aggregated statistical data about all the S3 buckets that Amazon Macie monitors and analyzes for an account.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetBucketStatisticsResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="datasources-s3-statistics-schemas"></a>

### Request bodies
<a name="datasources-s3-statistics-request-examples"></a>

#### POST schema
<a name="datasources-s3-statistics-request-body-post-example"></a>

```
{
  "accountId": "string"
}
```

### Response bodies
<a name="datasources-s3-statistics-response-examples"></a>

#### GetBucketStatisticsResponse schema
<a name="datasources-s3-statistics-response-body-getbucketstatisticsresponse-example"></a>

```
{
  "bucketCount": integer,
  "bucketCountByEffectivePermission": {
    "publiclyAccessible": integer,
    "publiclyReadable": integer,
    "publiclyWritable": integer,
    "unknown": integer
  },
  "bucketCountByEncryptionType": {
    "kmsManaged": integer,
    "s3Managed": integer,
    "unencrypted": integer,
    "unknown": integer
  },
  "bucketCountByObjectEncryptionRequirement": {
    "allowsUnencryptedObjectUploads": integer,
    "deniesUnencryptedObjectUploads": integer,
    "unknown": integer
  },
  "bucketCountBySharedAccessType": {
    "external": integer,
    "internal": integer,
    "notShared": integer,
    "unknown": integer
  },
  "bucketStatisticsBySensitivity": {
    "classificationError": {
      "classifiableSizeInBytes": integer,
      "publiclyAccessibleCount": integer,
      "totalCount": integer,
      "totalSizeInBytes": integer
    },
    "notClassified": {
      "classifiableSizeInBytes": integer,
      "publiclyAccessibleCount": integer,
      "totalCount": integer,
      "totalSizeInBytes": integer
    },
    "notSensitive": {
      "classifiableSizeInBytes": integer,
      "publiclyAccessibleCount": integer,
      "totalCount": integer,
      "totalSizeInBytes": integer
    },
    "sensitive": {
      "classifiableSizeInBytes": integer,
      "publiclyAccessibleCount": integer,
      "totalCount": integer,
      "totalSizeInBytes": integer
    }
  },
  "classifiableObjectCount": integer,
  "classifiableSizeInBytes": integer,
  "lastUpdated": "string",
  "objectCount": integer,
  "sizeInBytes": integer,
  "sizeInBytesCompressed": integer,
  "unclassifiableObjectCount": {
    "fileType": integer,
    "storageClass": integer,
    "total": integer
  },
  "unclassifiableObjectSizeInBytes": {
    "fileType": integer,
    "storageClass": integer,
    "total": integer
  }
}
```

#### ValidationException schema
<a name="datasources-s3-statistics-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="datasources-s3-statistics-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="datasources-s3-statistics-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="datasources-s3-statistics-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="datasources-s3-statistics-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="datasources-s3-statistics-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="datasources-s3-statistics-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="datasources-s3-statistics-properties"></a>

### AccessDeniedException
<a name="datasources-s3-statistics-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### BucketCountByEffectivePermission
<a name="datasources-s3-statistics-model-bucketcountbyeffectivepermission"></a>

Provides information about the number of S3 buckets that are publicly accessible due to a combination of permissions settings for each bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| publiclyAccessible | integer<br />Format: int64 | False | The total number of buckets that allow the general public to have read or write access to the bucket. |
| publiclyReadable | integer<br />Format: int64 | False | The total number of buckets that allow the general public to have read access to the bucket. |
| publiclyWritable | integer<br />Format: int64 | False | The total number of buckets that allow the general public to have write access to the bucket. |
| unknown | integer<br />Format: int64 | False | The total number of buckets that Amazon Macie wasn't able to evaluate permissions settings for. For example, the buckets' policies or a quota prevented Macie from retrieving the requisite data. Macie can't determine whether the buckets are publicly accessible. |

### BucketCountByEncryptionType
<a name="datasources-s3-statistics-model-bucketcountbyencryptiontype"></a>

Provides information about the number of S3 buckets whose settings do or don't specify default server-side encryption behavior for objects that are added to the buckets. For detailed information about these settings, see [Setting default server-side encryption behavior for Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html) in the *Amazon Simple Storage Service User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| kmsManaged | integer<br />Format: int64 | False | The total number of buckets whose default encryption settings are configured to encrypt new objects with an AWS KMS key, either an AWS managed key or a customer managed key. By default, these buckets encrypt new objects automatically using DSSE-KMS or SSE-KMS encryption. |
| s3Managed | integer<br />Format: int64 | False | The total number of buckets whose default encryption settings are configured to encrypt new objects with an Amazon S3 managed key. By default, these buckets encrypt new objects automatically using SSE-S3 encryption. |
| unencrypted | integer<br />Format: int64 | False | The total number of buckets that don't specify default server-side encryption behavior for new objects. Default encryption settings aren't configured for these buckets. |
| unknown | integer<br />Format: int64 | False | The total number of buckets that Amazon Macie doesn't have current encryption metadata for. For example, the buckets' permissions settings or a quota prevented Macie from retrieving the default encryption settings for the buckets. |

### BucketCountBySharedAccessType
<a name="datasources-s3-statistics-model-bucketcountbysharedaccesstype"></a>

Provides information about the number of S3 buckets that are or aren't shared with other AWS accounts, Amazon CloudFront origin access identities (OAIs), or CloudFront origin access controls (OACs). In this data, an *Amazon Macie organization* is defined as a set of Macie accounts that are centrally managed as a group of related accounts through AWS Organizations or by Macie invitation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| external | integer<br />Format: int64 | False | The total number of buckets that are shared with one or more of the following or any combination of the following: an Amazon CloudFront OAI, a CloudFront OAC, or an AWS account that isn't in the same Amazon Macie organization. |
| internal | integer<br />Format: int64 | False | The total number of buckets that are shared with one or more AWS accounts in the same Amazon Macie organization. These buckets aren't shared with Amazon CloudFront OAIs or OACs. |
| notShared | integer<br />Format: int64 | False | The total number of buckets that aren't shared with other AWS accounts, Amazon CloudFront OAIs, or CloudFront OACs. |
| unknown | integer<br />Format: int64 | False | The total number of buckets that Amazon Macie wasn't able to evaluate shared access settings for. For example, the buckets' permissions settings or a quota prevented Macie from retrieving the requisite data. Macie can't determine whether the buckets are shared with other AWS accounts, Amazon CloudFront OAIs, or CloudFront OACs. |

### BucketCountPolicyAllowsUnencryptedObjectUploads
<a name="datasources-s3-statistics-model-bucketcountpolicyallowsunencryptedobjectuploads"></a>

Provides information about the number of S3 buckets whose bucket policies do or don't require server-side encryption of objects when objects are added to the buckets.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| allowsUnencryptedObjectUploads | integer<br />Format: int64 | False | The total number of buckets that don't have a bucket policy or have a bucket policy that doesn't require server-side encryption of new objects. If a bucket policy exists, the policy doesn't require `PutObject` requests to include a valid server-side encryption header: the `x-amz-server-side-encryption` header with a value of `AES256` or `aws:kms`, or the `x-amz-server-side-encryption-customer-algorithm` header with a value of `AES256`. |
| deniesUnencryptedObjectUploads | integer<br />Format: int64 | False | The total number of buckets whose bucket policies require server-side encryption of new objects. `PutObject` requests for these buckets must include a valid server-side encryption header: the `x-amz-server-side-encryption` header with a value of `AES256` or `aws:kms`, or the `x-amz-server-side-encryption-customer-algorithm` header with a value of `AES256`. |
| unknown | integer<br />Format: int64 | False | The total number of buckets that Amazon Macie wasn't able to evaluate server-side encryption requirements for. For example, the buckets' permissions settings or a quota prevented Macie from retrieving the requisite data. Macie can't determine whether bucket policies for the buckets require server-side encryption of new objects. |

### BucketStatisticsBySensitivity
<a name="datasources-s3-statistics-model-bucketstatisticsbysensitivity"></a>

Provides aggregated statistical data for sensitive data discovery metrics that apply to S3 buckets, grouped by bucket sensitivity score (`sensitivityScore`). If automated sensitive data discovery is currently disabled for your account, the value for most of these metrics is `0`.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| classificationError | [SensitivityAggregations](#datasources-s3-statistics-model-sensitivityaggregations) | False | The aggregated statistical data for all buckets that have a sensitivity score of `-1`. |
| notClassified | [SensitivityAggregations](#datasources-s3-statistics-model-sensitivityaggregations) | False | The aggregated statistical data for all buckets that have a sensitivity score of `50`. |
| notSensitive | [SensitivityAggregations](#datasources-s3-statistics-model-sensitivityaggregations) | False | The aggregated statistical data for all buckets that have a sensitivity score of `1-49`. |
| sensitive | [SensitivityAggregations](#datasources-s3-statistics-model-sensitivityaggregations) | False | The aggregated statistical data for all buckets that have a sensitivity score of `51-100`. |

### ConflictException
<a name="datasources-s3-statistics-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### GetBucketStatisticsRequest
<a name="datasources-s3-statistics-model-getbucketstatisticsrequest"></a>

Specifies the account that owns the S3 buckets to retrieve aggregated statistical data for.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The unique identifier for the AWS account. |

### GetBucketStatisticsResponse
<a name="datasources-s3-statistics-model-getbucketstatisticsresponse"></a>

Provides the results of a query that retrieved aggregated statistical data for all the S3 buckets that Amazon Macie monitors and analyzes for your account. By default, object count and storage size values include data for object parts that are the result of incomplete multipart uploads. For more information, see [How Macie monitors Amazon S3 data security](https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-how-it-works.html) in the *Amazon Macie User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketCount | integer<br />Format: int64 | False | The total number of buckets. |
| bucketCountByEffectivePermission | [BucketCountByEffectivePermission](#datasources-s3-statistics-model-bucketcountbyeffectivepermission) | False | The total number of buckets that are publicly accessible due to a combination of permissions settings for each bucket. |
| bucketCountByEncryptionType | [BucketCountByEncryptionType](#datasources-s3-statistics-model-bucketcountbyencryptiontype) | False | The total number of buckets whose settings do or don't specify default server-side encryption behavior for objects that are added to the buckets. |
| bucketCountByObjectEncryptionRequirement | [BucketCountPolicyAllowsUnencryptedObjectUploads](#datasources-s3-statistics-model-bucketcountpolicyallowsunencryptedobjectuploads) | False | The total number of buckets whose bucket policies do or don't require server-side encryption of objects when objects are added to the buckets. |
| bucketCountBySharedAccessType | [BucketCountBySharedAccessType](#datasources-s3-statistics-model-bucketcountbysharedaccesstype) | False | The total number of buckets that are or aren't shared with other AWS accounts, Amazon CloudFront origin access identities (OAIs), or CloudFront origin access controls (OACs). |
| bucketStatisticsBySensitivity | [BucketStatisticsBySensitivity](#datasources-s3-statistics-model-bucketstatisticsbysensitivity) | False | The aggregated sensitive data discovery statistics for the buckets. If automated sensitive data discovery is currently disabled for your account, the value for most statistics is `0`. |
| classifiableObjectCount | integer<br />Format: int64 | False | The total number of objects that Amazon Macie can analyze in the buckets. These objects use a supported storage class and have a file name extension for a supported file or storage format. |
| classifiableSizeInBytes | integer<br />Format: int64 | False | The total storage size, in bytes, of all the objects that Amazon Macie can analyze in the buckets. These objects use a supported storage class and have a file name extension for a supported file or storage format.<br />If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each applicable object in the buckets. This value doesn't reflect the storage size of all versions of all applicable objects in the buckets. |
| lastUpdated | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when Amazon Macie most recently retrieved bucket or object metadata from Amazon S3 for the buckets. |
| objectCount | integer<br />Format: int64 | False | The total number of objects in the buckets. |
| sizeInBytes | integer<br />Format: int64 | False | The total storage size, in bytes, of the buckets.<br />If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each object in the buckets. This value doesn't reflect the storage size of all versions of the objects in the buckets. |
| sizeInBytesCompressed | integer<br />Format: int64 | False | The total storage size, in bytes, of the objects that are compressed (.gz, .gzip, .zip) files in the buckets.<br />If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each applicable object in the buckets. This value doesn't reflect the storage size of all versions of the applicable objects in the buckets. |
| unclassifiableObjectCount | [ObjectLevelStatistics](#datasources-s3-statistics-model-objectlevelstatistics) | False | The total number of objects that Amazon Macie can't analyze in the buckets. These objects don't use a supported storage class or don't have a file name extension for a supported file or storage format. |
| unclassifiableObjectSizeInBytes | [ObjectLevelStatistics](#datasources-s3-statistics-model-objectlevelstatistics) | False | The total storage size, in bytes, of the objects that Amazon Macie can't analyze in the buckets. These objects don't use a supported storage class or don't have a file name extension for a supported file or storage format. |

### InternalServerException
<a name="datasources-s3-statistics-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ObjectLevelStatistics
<a name="datasources-s3-statistics-model-objectlevelstatistics"></a>

Provides information about the total storage size (in bytes) or number of objects that Amazon Macie can't analyze in one or more S3 buckets. In a `BucketMetadata` or `MatchingBucket` object, this data is for a specific bucket. In a `GetBucketStatisticsResponse` object, this data is aggregated for all the buckets in the query results. If versioning is enabled for a bucket, storage size values are based on the size of the latest version of each applicable object in the bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| fileType | integer<br />Format: int64 | False | The total storage size (in bytes) or number of objects that Amazon Macie can't analyze because the objects don't have a file name extension for a supported file or storage format. |
| storageClass | integer<br />Format: int64 | False | The total storage size (in bytes) or number of objects that Amazon Macie can't analyze because the objects use an unsupported storage class. |
| total | integer<br />Format: int64 | False | The total storage size (in bytes) or number of objects that Amazon Macie can't analyze because the objects use an unsupported storage class or don't have a file name extension for a supported file or storage format. |

### ResourceNotFoundException
<a name="datasources-s3-statistics-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### SensitivityAggregations
<a name="datasources-s3-statistics-model-sensitivityaggregations"></a>

Provides aggregated statistical data for sensitive data discovery metrics that apply to S3 buckets. Each field contains aggregated data for all the buckets that have a sensitivity score (`sensitivityScore`) of a specified value or within a specified range (`BucketStatisticsBySensitivity`). If automated sensitive data discovery is currently disabled for your account, the value for most fields is `0`.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| classifiableSizeInBytes | integer<br />Format: int64 | False | The total storage size, in bytes, of all the objects that Amazon Macie can analyze in the buckets. These objects use a supported storage class and have a file name extension for a supported file or storage format.<br />If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each applicable object in the buckets. This value doesn't reflect the storage size of all versions of all applicable objects in the buckets. |
| publiclyAccessibleCount | integer<br />Format: int64 | False | The total number of buckets that are publicly accessible due to a combination of permissions settings for each bucket. |
| totalCount | integer<br />Format: int64 | False | The total number of buckets. |
| totalSizeInBytes | integer<br />Format: int64 | False | The total storage size, in bytes, of the buckets.<br />If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each object in the buckets. This value doesn't reflect the storage size of all versions of the objects in the buckets. |

### ServiceQuotaExceededException
<a name="datasources-s3-statistics-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="datasources-s3-statistics-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="datasources-s3-statistics-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="datasources-s3-statistics-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetBucketStatistics
<a name="GetBucketStatistics-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetBucketStatistics)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetBucketStatistics)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetBucketStatistics)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetBucketStatistics)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetBucketStatistics)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetBucketStatistics)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetBucketStatistics)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetBucketStatistics)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/GetBucketStatistics)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetBucketStatistics)
