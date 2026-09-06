---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html
---

# Data Sources - Amazon S3
<a name="datasources-s3"></a>

The Amazon S3 Data Sources resource provides statistical data and other information about the Amazon Simple Storage Service (Amazon S3) buckets that Amazon Macie monitors and analyzes for your account. This includes a breakdown of each bucket's public access and encryption settings. It also includes details about the size and number of objects that Macie can analyze to detect sensitive data in a bucket, and whether and when that analysis occurred. The data is available for all the S3 buckets that Macie monitors and analyzes for your account. If you're the Macie administrator for an organization, this includes S3 buckets that your member accounts own.

Note that the data is available only for S3 general purpose buckets. Macie doesn't monitor or analyze S3 directory buckets. In addition, complete data is available for a bucket only if Macie can retrieve and process metadata from Amazon S3 for the bucket and the bucket's objects. Permissions settings, errors, or quotas might prevent Macie from retrieving and processing this information. If this happens, Macie can provide only a subset of information about a bucket, such as the bucket's name and the account ID for the AWS account that owns the bucket.

You can use the Amazon S3 Data Sources resource to retrieve (query) statistical data and other information about one or more S3 general purpose buckets that Macie monitors and analyzes for your account. To customize and refine your query, you can use the supported parameters to specify how to filter, sort, and paginate the query results. For more information about filter options, see [Filtering your S3 bucket inventory](https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-inventory-filter.html) in the *Amazon Macie User Guide*.

## URI
<a name="datasources-s3-url"></a>

`/datasources/s3`

## HTTP methods
<a name="datasources-s3-http-methods"></a>

### POST
<a name="datasources-s3post"></a>

**Operation ID:** `DescribeBuckets`

Retrieves (queries) statistical data and other information about one or more S3 buckets that Amazon Macie monitors and analyzes for an account.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DescribeBucketsResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="datasources-s3-schemas"></a>

### Request bodies
<a name="datasources-s3-request-examples"></a>

#### POST schema
<a name="datasources-s3-request-body-post-example"></a>

```
{
  "criteria": {
  },
  "maxResults": integer,
  "nextToken": "string",
  "sortCriteria": {
    "attributeName": "string",
    "orderBy": enum
  }
}
```

### Response bodies
<a name="datasources-s3-response-examples"></a>

#### DescribeBucketsResponse schema
<a name="datasources-s3-response-body-describebucketsresponse-example"></a>

```
{
  "buckets": [
    {
      "accountId": "string",
      "allowsUnencryptedObjectUploads": enum,
      "automatedDiscoveryMonitoringStatus": enum,
      "bucketArn": "string",
      "bucketCreatedAt": "string",
      "bucketName": "string",
      "classifiableObjectCount": integer,
      "classifiableSizeInBytes": integer,
      "errorCode": enum,
      "errorMessage": "string",
      "jobDetails": {
        "isDefinedInJob": enum,
        "isMonitoredByJob": enum,
        "lastJobId": "string",
        "lastJobRunTime": "string"
      },
      "lastAutomatedDiscoveryTime": "string",
      "lastUpdated": "string",
      "objectCount": integer,
      "objectCountByEncryptionType": {
        "customerManaged": integer,
        "kmsManaged": integer,
        "s3Managed": integer,
        "unencrypted": integer,
        "unknown": integer
      },
      "publicAccess": {
        "effectivePermission": enum,
        "permissionConfiguration": {
          "accountLevelPermissions": {
            "blockPublicAccess": {
              "blockPublicAcls": boolean,
              "blockPublicPolicy": boolean,
              "ignorePublicAcls": boolean,
              "restrictPublicBuckets": boolean
            }
          },
          "bucketLevelPermissions": {
            "accessControlList": {
              "allowsPublicReadAccess": boolean,
              "allowsPublicWriteAccess": boolean
            },
            "blockPublicAccess": {
              "blockPublicAcls": boolean,
              "blockPublicPolicy": boolean,
              "ignorePublicAcls": boolean,
              "restrictPublicBuckets": boolean
            },
            "bucketPolicy": {
              "allowsPublicReadAccess": boolean,
              "allowsPublicWriteAccess": boolean
            }
          }
        }
      },
      "region": "string",
      "replicationDetails": {
        "replicated": boolean,
        "replicatedExternally": boolean,
        "replicationAccounts": [
          "string"
        ]
      },
      "sensitivityScore": integer,
      "serverSideEncryption": {
        "kmsMasterKeyId": "string",
        "type": enum
      },
      "sharedAccess": enum,
      "sizeInBytes": integer,
      "sizeInBytesCompressed": integer,
      "tags": [
        {
          "key": "string",
          "value": "string"
        }
      ],
      "unclassifiableObjectCount": {
        "fileType": integer,
        "storageClass": integer,
        "total": integer
      },
      "unclassifiableObjectSizeInBytes": {
        "fileType": integer,
        "storageClass": integer,
        "total": integer
      },
      "versioning": boolean
    }
  ],
  "nextToken": "string"
}
```

#### ValidationException schema
<a name="datasources-s3-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="datasources-s3-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="datasources-s3-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="datasources-s3-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="datasources-s3-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="datasources-s3-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="datasources-s3-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="datasources-s3-properties"></a>

### AccessControlList
<a name="datasources-s3-model-accesscontrollist"></a>

Provides information about the permissions settings of the bucket-level access control list (ACL) for an S3 bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| allowsPublicReadAccess | boolean | False | Specifies whether the ACL grants the general public with read access permissions for the bucket. |
| allowsPublicWriteAccess | boolean | False | Specifies whether the ACL grants the general public with write access permissions for the bucket. |

### AccessDeniedException
<a name="datasources-s3-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### AccountLevelPermissions
<a name="datasources-s3-model-accountlevelpermissions"></a>

Provides information about the account-level permissions settings that apply to an S3 bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| blockPublicAccess | [BlockPublicAccess](#datasources-s3-model-blockpublicaccess) | False | The block public access settings for the AWS account that owns the bucket. |

### AutomatedDiscoveryMonitoringStatus
<a name="datasources-s3-model-automateddiscoverymonitoringstatus"></a>

Specifies whether automated sensitive data discovery is currently configured to analyze objects in an S3 bucket. Possible values are:
+ `MONITORED`
+ `NOT_MONITORED`

### BlockPublicAccess
<a name="datasources-s3-model-blockpublicaccess"></a>

Provides information about the block public access settings for an S3 bucket. These settings can apply to a bucket at the account or bucket level. For detailed information about each setting, see [Blocking public access to your Amazon S3 storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) in the *Amazon Simple Storage Service User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| blockPublicAcls | boolean | False | Specifies whether Amazon S3 blocks public access control lists (ACLs) for the bucket and objects in the bucket. |
| blockPublicPolicy | boolean | False | Specifies whether Amazon S3 blocks public bucket policies for the bucket. |
| ignorePublicAcls | boolean | False | Specifies whether Amazon S3 ignores public ACLs for the bucket and objects in the bucket. |
| restrictPublicBuckets | boolean | False | Specifies whether Amazon S3 restricts public bucket policies for the bucket. |

### BucketCriteria
<a name="datasources-s3-model-bucketcriteria"></a>

Specifies, as a map, one or more property-based conditions that filter the results of a query for information about S3 buckets.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | object | False |  |

### BucketCriteriaAdditionalProperties
<a name="datasources-s3-model-bucketcriteriaadditionalproperties"></a>

Specifies the operator to use in a property-based condition that filters the results of a query for information about S3 buckets.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| eq | Array of type string | False | The value for the property matches (equals) the specified value. If you specify multiple values, Amazon Macie uses OR logic to join the values. |
| gt | integer<br />Format: int64 | False | The value for the property is greater than the specified value. |
| gte | integer<br />Format: int64 | False | The value for the property is greater than or equal to the specified value. |
| lt | integer<br />Format: int64 | False | The value for the property is less than the specified value. |
| lte | integer<br />Format: int64 | False | The value for the property is less than or equal to the specified value. |
| neq | Array of type string | False | The value for the property doesn't match (doesn't equal) the specified value. If you specify multiple values, Amazon Macie uses OR logic to join the values. |
| prefix | string | False | The name of the bucket begins with the specified value. |

### BucketLevelPermissions
<a name="datasources-s3-model-bucketlevelpermissions"></a>

Provides information about the bucket-level permissions settings for an S3 bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accessControlList | [AccessControlList](#datasources-s3-model-accesscontrollist) | False | The permissions settings of the access control list (ACL) for the bucket. This value is null if an ACL hasn't been defined for the bucket. |
| blockPublicAccess | [BlockPublicAccess](#datasources-s3-model-blockpublicaccess) | False | The block public access settings for the bucket. |
| bucketPolicy | [BucketPolicy](#datasources-s3-model-bucketpolicy) | False | The permissions settings of the bucket policy for the bucket. This value is null if a bucket policy hasn't been defined for the bucket. |

### BucketMetadata
<a name="datasources-s3-model-bucketmetadata"></a>

Provides statistical data and other information about an S3 bucket that Amazon Macie monitors and analyzes for your account. By default, object count and storage size values include data for object parts that are the result of incomplete multipart uploads. For more information, see [How Macie monitors Amazon S3 data security](https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-how-it-works.html) in the *Amazon Macie User Guide*.

If an error or issue prevents Macie from retrieving and processing metadata from Amazon S3 for the bucket or the bucket's objects, the value for the `versioning` property is `false` and the value for most other properties is null or `UNKNOWN`. Key exceptions are `accountId`, `bucketArn`, `bucketCreatedAt`, `bucketName`, `lastUpdated`, and `region`. To identify the cause, refer to the `errorCode` and `errorMessage` values.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The unique identifier for the AWS account that owns the bucket. |
| allowsUnencryptedObjectUploads | string<br />Values: `TRUE \| FALSE \| UNKNOWN` | False | Specifies whether the bucket policy for the bucket requires server-side encryption of objects when objects are added to the bucket. Possible values are:+   `FALSE` - The bucket policy requires server-side encryption of new objects. `PutObject` requests must include a valid server-side encryption header. <br />+   `TRUE` - The bucket doesn't have a bucket policy or it has a bucket policy that doesn't require server-side encryption of new objects. If a bucket policy exists, it doesn't require `PutObject` requests to include a valid server-side encryption header. <br />+   `UNKNOWN` - Amazon Macie can't determine whether the bucket policy requires server-side encryption of new objects. <br />Valid server-side encryption headers are: `x-amz-server-side-encryption` with a value of `AES256` or `aws:kms`, and `x-amz-server-side-encryption-customer-algorithm` with a value of `AES256`. |
| automatedDiscoveryMonitoringStatus | [AutomatedDiscoveryMonitoringStatus](#datasources-s3-model-automateddiscoverymonitoringstatus) | False | Specifies whether automated sensitive data discovery is currently configured to analyze objects in the bucket. Possible values are: `MONITORED`, the bucket is included in analyses; and, `NOT_MONITORED`, the bucket is excluded from analyses. If automated sensitive data discovery is disabled for your account, this value is `NOT_MONITORED`. |
| bucketArn | string | False | The Amazon Resource Name (ARN) of the bucket. |
| bucketCreatedAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the bucket was created. This value can also indicate when changes such as edits to the bucket's policy were most recently made to the bucket. |
| bucketName | string | False | The name of the bucket. |
| classifiableObjectCount | integer<br />Format: int64 | False | The total number of objects that Amazon Macie can analyze in the bucket. These objects use a supported storage class and have a file name extension for a supported file or storage format. |
| classifiableSizeInBytes | integer<br />Format: int64 | False | The total storage size, in bytes, of the objects that Amazon Macie can analyze in the bucket. These objects use a supported storage class and have a file name extension for a supported file or storage format.<br />If versioning is enabled for the bucket, Macie calculates this value based on the size of the latest version of each applicable object in the bucket. This value doesn't reflect the storage size of all versions of each applicable object in the bucket. |
| errorCode | [BucketMetadataErrorCode](#datasources-s3-model-bucketmetadataerrorcode) | False | The code for an error or issue that prevented Amazon Macie from retrieving and processing information about the bucket and the bucket's objects. Possible values are:+  `ACCESS_DENIED` - Macie doesn't have permission to retrieve the information. For example, the bucket has a restrictive bucket policy and Amazon S3 denied the request. <br />+  `BUCKET_COUNT_EXCEEDS_QUOTA` - Retrieving and processing the information would exceed the quota for the number of buckets that Macie monitors for an account (10,000). <br />If this value is null, Macie was able to retrieve and process the information. |
| errorMessage | string | False | A brief description of the error or issue (`errorCode`) that prevented Amazon Macie from retrieving and processing information about the bucket and the bucket's objects. This value is null if Macie was able to retrieve and process the information. |
| jobDetails | [JobDetails](#datasources-s3-model-jobdetails) | False | Specifies whether any one-time or recurring classification jobs are configured to analyze objects in the bucket, and, if so, the details of the job that ran most recently. |
| lastAutomatedDiscoveryTime | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when Amazon Macie most recently analyzed objects in the bucket while performing automated sensitive data discovery. This value is null if this analysis hasn't occurred. |
| lastUpdated | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when Amazon Macie most recently retrieved bucket or object metadata from Amazon S3 for the bucket. |
| objectCount | integer<br />Format: int64 | False | The total number of objects in the bucket. |
| objectCountByEncryptionType | [ObjectCountByEncryptionType](#datasources-s3-model-objectcountbyencryptiontype) | False | The total number of objects in the bucket, grouped by server-side encryption type. This includes a grouping that reports the total number of objects that aren't encrypted or use client-side encryption. |
| publicAccess | [BucketPublicAccess](#datasources-s3-model-bucketpublicaccess) | False | Specifies whether the bucket is publicly accessible due to the combination of permissions settings that apply to the bucket, and provides information about those settings. |
| region | string | False | The AWS Region that hosts the bucket. |
| replicationDetails | [ReplicationDetails](#datasources-s3-model-replicationdetails) | False | Specifies whether the bucket is configured to replicate one or more objects to buckets for other AWS accounts and, if so, which accounts. |
| sensitivityScore | integer<br />Format: int32 | False | The sensitivity score for the bucket, ranging from `-1` (classification error) to `100` (sensitive).<br />If automated sensitive data discovery has never been enabled for your account or it's been disabled for your organization or standalone account for more than 30 days, possible values are: `1`, the bucket is empty; or, `50`, the bucket stores objects but it's been excluded from recent analyses. |
| serverSideEncryption | [BucketServerSideEncryption](#datasources-s3-model-bucketserversideencryption) | False | The default server-side encryption settings for the bucket. |
| sharedAccess | string<br />Values: `EXTERNAL \| INTERNAL \| NOT_SHARED \| UNKNOWN` | False | Specifies whether the bucket is shared with another AWS account, an Amazon CloudFront origin access identity (OAI), or a CloudFront origin access control (OAC). Possible values are:+   `EXTERNAL` - The bucket is shared with one or more of the following or any combination of the following: a CloudFront OAI, a CloudFront OAC, or an AWS account that isn't part of your Amazon Macie organization. <br />+   `INTERNAL` - The bucket is shared with one or more AWS accounts that are part of your Amazon Macie organization. It isn't shared with a CloudFront OAI or OAC. <br />+   `NOT_SHARED` - The bucket isn't shared with another AWS account, a CloudFront OAI, or a CloudFront OAC. <br />+   `UNKNOWN` - Amazon Macie wasn't able to evaluate the shared access settings for the bucket. <br />An *Amazon Macie organization* is a set of Macie accounts that are centrally managed as a group of related accounts through AWS Organizations or by Macie invitation. |
| sizeInBytes | integer<br />Format: int64 | False | The total storage size, in bytes, of the bucket.<br />If versioning is enabled for the bucket, Amazon Macie calculates this value based on the size of the latest version of each object in the bucket. This value doesn't reflect the storage size of all versions of each object in the bucket. |
| sizeInBytesCompressed | integer<br />Format: int64 | False | The total storage size, in bytes, of the objects that are compressed (.gz, .gzip, .zip) files in the bucket.<br />If versioning is enabled for the bucket, Amazon Macie calculates this value based on the size of the latest version of each applicable object in the bucket. This value doesn't reflect the storage size of all versions of each applicable object in the bucket. |
| tags | Array of type [KeyValuePair](#datasources-s3-model-keyvaluepair) | False | An array that specifies the tags (keys and values) that are associated with the bucket. |
| unclassifiableObjectCount | [ObjectLevelStatistics](#datasources-s3-model-objectlevelstatistics) | False | The total number of objects that Amazon Macie can't analyze in the bucket. These objects don't use a supported storage class or don't have a file name extension for a supported file or storage format. |
| unclassifiableObjectSizeInBytes | [ObjectLevelStatistics](#datasources-s3-model-objectlevelstatistics) | False | The total storage size, in bytes, of the objects that Amazon Macie can't analyze in the bucket. These objects don't use a supported storage class or don't have a file name extension for a supported file or storage format. |
| versioning | boolean | False | Specifies whether versioning is enabled for the bucket. |

### BucketMetadataErrorCode
<a name="datasources-s3-model-bucketmetadataerrorcode"></a>

The code for an error or issue that prevented Amazon Macie from retrieving and processing information about an S3 bucket and the bucket's objects.
+ `ACCESS_DENIED`
+ `BUCKET_COUNT_EXCEEDS_QUOTA`

### BucketPermissionConfiguration
<a name="datasources-s3-model-bucketpermissionconfiguration"></a>

Provides information about the account-level and bucket-level permissions settings for an S3 bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountLevelPermissions | [AccountLevelPermissions](#datasources-s3-model-accountlevelpermissions) | False | The account-level permissions settings that apply to the bucket. |
| bucketLevelPermissions | [BucketLevelPermissions](#datasources-s3-model-bucketlevelpermissions) | False | The bucket-level permissions settings for the bucket. |

### BucketPolicy
<a name="datasources-s3-model-bucketpolicy"></a>

Provides information about the permissions settings of the bucket policy for an S3 bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| allowsPublicReadAccess | boolean | False | Specifies whether the bucket policy allows the general public to have read access to the bucket. |
| allowsPublicWriteAccess | boolean | False | Specifies whether the bucket policy allows the general public to have write access to the bucket. |

### BucketPublicAccess
<a name="datasources-s3-model-bucketpublicaccess"></a>

Provides information about the permissions settings that determine whether an S3 bucket is publicly accessible.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| effectivePermission | string<br />Values: `PUBLIC \| NOT_PUBLIC \| UNKNOWN` | False | Specifies whether the bucket is publicly accessible due to the combination of permissions settings that apply to the bucket. Possible values are:+   `NOT_PUBLIC` - The bucket isn't publicly accessible. <br />+   `PUBLIC` - The bucket is publicly accessible. <br />+   `UNKNOWN` - Amazon Macie can't determine whether the bucket is publicly accessible.  |
| permissionConfiguration | [BucketPermissionConfiguration](#datasources-s3-model-bucketpermissionconfiguration) | False | The account-level and bucket-level permissions settings for the bucket. |

### BucketServerSideEncryption
<a name="datasources-s3-model-bucketserversideencryption"></a>

Provides information about the default server-side encryption settings for an S3 bucket. For detailed information about these settings, see [Setting default server-side encryption behavior for Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html) in the *Amazon Simple Storage Service User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| kmsMasterKeyId | string | False | The Amazon Resource Name (ARN) or unique identifier (key ID) for the AWS KMS key that's used by default to encrypt objects that are added to the bucket. This value is null if the bucket is configured to use an Amazon S3 managed key to encrypt new objects. |
| type | string<br />Values: `NONE \| AES256 \| aws:kms \| aws:kms:dsse` | False | The server-side encryption algorithm that's used by default to encrypt objects that are added to the bucket. Possible values are:+   `AES256` - New objects use SSE-S3 encryption. They're encrypted with an Amazon S3 managed key. <br />+   `aws:kms` - New objects use SSE-KMS encryption. They're encrypted with an AWS KMS key (`kmsMasterKeyId`), either an AWS managed key or a customer managed key. <br />+   `aws:kms:dsse` - New objects use DSSE-KMS encryption. They're encrypted with an AWS KMS key (`kmsMasterKeyId`), either an AWS managed key or a customer managed key. <br />+   `NONE` - The bucket's default encryption settings don't specify server-side encryption behavior for new objects.  |

### BucketSortCriteria
<a name="datasources-s3-model-bucketsortcriteria"></a>

Specifies criteria for sorting the results of a query for information about S3 buckets.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| attributeName | string | False | The name of the bucket property to sort the results by. This value can be one of the following properties that Amazon Macie defines as bucket metadata: `accountId`, `bucketName`, `classifiableObjectCount`, `classifiableSizeInBytes`, `objectCount`, `sensitivityScore`, or `sizeInBytes`. |
| orderBy | string<br />Values: `ASC \| DESC` | False | The sort order to apply to the results, based on the value specified by the `attributeName` property. Valid values are: `ASC`, sort the results in ascending order; and, `DESC`, sort the results in descending order. |

### ConflictException
<a name="datasources-s3-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### DescribeBucketsRequest
<a name="datasources-s3-model-describebucketsrequest"></a>

Specifies criteria for filtering, sorting, and paginating the results of a query for statistical data and other information about S3 buckets.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| criteria | [BucketCriteria](#datasources-s3-model-bucketcriteria) | False | The criteria to use to filter the query results. |
| maxResults | integer<br />Format: int32 | False | The maximum number of items to include in each page of the response. The default value is 50. |
| nextToken | string | False | The `nextToken` string that specifies which page of results to return in a paginated response. |
| sortCriteria | [BucketSortCriteria](#datasources-s3-model-bucketsortcriteria) | False | The criteria to use to sort the query results. |

### DescribeBucketsResponse
<a name="datasources-s3-model-describebucketsresponse"></a>

Provides the results of a query that retrieved statistical data and other information about one or more S3 buckets that Amazon Macie monitors and analyzes for your account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| buckets | Array of type [BucketMetadata](#datasources-s3-model-bucketmetadata) | False | An array of objects, one for each bucket that matches the filter criteria specified in the request. |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### InternalServerException
<a name="datasources-s3-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### JobDetails
<a name="datasources-s3-model-jobdetails"></a>

Specifies whether any one-time or recurring classification jobs are configured to analyze objects in an S3 bucket, and, if so, the details of the job that ran most recently.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| isDefinedInJob | string<br />Values: `TRUE \| FALSE \| UNKNOWN` | False | Specifies whether any one-time or recurring jobs are configured to analyze objects in the bucket. Possible values are:+   `TRUE` - The bucket is explicitly included in the bucket definition (`S3BucketDefinitionForJob`) for one or more jobs and at least one of those jobs has a status other than `CANCELLED`. Or the bucket matched the bucket criteria (`S3BucketCriteriaForJob`) for at least one job that previously ran. <br />+   `FALSE` - The bucket isn't explicitly included in the bucket definition (`S3BucketDefinitionForJob`) for any jobs, all the jobs that explicitly include the bucket in their bucket definitions have a status of `CANCELLED`, or the bucket didn't match the bucket criteria (`S3BucketCriteriaForJob`) for any jobs that previously ran. <br />+   `UNKNOWN` - An exception occurred when Amazon Macie attempted to retrieve job data for the bucket.  |
| isMonitoredByJob | string<br />Values: `TRUE \| FALSE \| UNKNOWN` | False | Specifies whether any recurring jobs are configured to analyze objects in the bucket. Possible values are:+   `TRUE` - The bucket is explicitly included in the bucket definition (`S3BucketDefinitionForJob`) for one or more recurring jobs or the bucket matches the bucket criteria (`S3BucketCriteriaForJob`) for one or more recurring jobs. At least one of those jobs has a status other than `CANCELLED`. <br />+   `FALSE` - The bucket isn't explicitly included in the bucket definition (`S3BucketDefinitionForJob`) for any recurring jobs, the bucket doesn't match the bucket criteria (`S3BucketCriteriaForJob`) for any recurring jobs, or all the recurring jobs that are configured to analyze data in the bucket have a status of `CANCELLED`. <br />+   `UNKNOWN` - An exception occurred when Amazon Macie attempted to retrieve job data for the bucket.  |
| lastJobId | string | False | The unique identifier for the job that ran most recently and is configured to analyze objects in the bucket, either the latest run of a recurring job or the only run of a one-time job.<br />This value is typically null if the value for the `isDefinedInJob` property is `FALSE` or `UNKNOWN`. |
| lastJobRunTime | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the job (`lastJobId`) started. If the job is a recurring job, this value indicates when the most recent run started.<br />This value is typically null if the value for the `isDefinedInJob` property is `FALSE` or `UNKNOWN`. |

### KeyValuePair
<a name="datasources-s3-model-keyvaluepair"></a>

Provides information about the tags that are associated with an S3 bucket or object. Each tag consists of a required tag key and an associated tag value.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| key | string | False | One part of a key-value pair that comprises a tag. A tag key is a general label that acts as a category for more specific tag values. |
| value | string | False | One part of a key-value pair that comprises a tag. A tag value acts as a descriptor for a tag key. A tag value can be an empty string. |

### ObjectCountByEncryptionType
<a name="datasources-s3-model-objectcountbyencryptiontype"></a>

Provides information about the number of objects that are in an S3 bucket and use certain types of server-side encryption, use client-side encryption, or aren't encrypted.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| customerManaged | integer<br />Format: int64 | False | The total number of objects that are encrypted with customer-provided keys. The objects use server-side encryption with customer-provided keys (SSE-C). |
| kmsManaged | integer<br />Format: int64 | False | The total number of objects that are encrypted with AWS KMS keys, either AWS managed keys or customer managed keys. The objects use dual-layer server-side encryption or server-side encryption with AWS KMS keys (DSSE-KMS or SSE-KMS). |
| s3Managed | integer<br />Format: int64 | False | The total number of objects that are encrypted with Amazon S3 managed keys. The objects use server-side encryption with Amazon S3 managed keys (SSE-S3). |
| unencrypted | integer<br />Format: int64 | False | The total number of objects that use client-side encryption or aren't encrypted. |
| unknown | integer<br />Format: int64 | False | The total number of objects that Amazon Macie doesn't have current encryption metadata for. Macie can't provide current data about the encryption settings for these objects. |

### ObjectLevelStatistics
<a name="datasources-s3-model-objectlevelstatistics"></a>

Provides information about the total storage size (in bytes) or number of objects that Amazon Macie can't analyze in one or more S3 buckets. In a `BucketMetadata` or `MatchingBucket` object, this data is for a specific bucket. In a `GetBucketStatisticsResponse` object, this data is aggregated for all the buckets in the query results. If versioning is enabled for a bucket, storage size values are based on the size of the latest version of each applicable object in the bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| fileType | integer<br />Format: int64 | False | The total storage size (in bytes) or number of objects that Amazon Macie can't analyze because the objects don't have a file name extension for a supported file or storage format. |
| storageClass | integer<br />Format: int64 | False | The total storage size (in bytes) or number of objects that Amazon Macie can't analyze because the objects use an unsupported storage class. |
| total | integer<br />Format: int64 | False | The total storage size (in bytes) or number of objects that Amazon Macie can't analyze because the objects use an unsupported storage class or don't have a file name extension for a supported file or storage format. |

### ReplicationDetails
<a name="datasources-s3-model-replicationdetails"></a>

Provides information about settings that define whether one or more objects in an S3 bucket are replicated to S3 buckets for other AWS accounts and, if so, which accounts.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| replicated | boolean | False | Specifies whether the bucket is configured to replicate one or more objects to any destination. |
| replicatedExternally | boolean | False | Specifies whether the bucket is configured to replicate one or more objects to a bucket for an AWS account that isn't part of your Amazon Macie organization. An *Amazon Macie organization* is a set of Macie accounts that are centrally managed as a group of related accounts through AWS Organizations or by Macie invitation. |
| replicationAccounts | Array of type string | False | An array of AWS account IDs, one for each AWS account that owns a bucket that the bucket is configured to replicate one or more objects to. |

### ResourceNotFoundException
<a name="datasources-s3-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="datasources-s3-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="datasources-s3-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="datasources-s3-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="datasources-s3-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeBuckets
<a name="DescribeBuckets-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/DescribeBuckets)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/DescribeBuckets)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/DescribeBuckets)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/DescribeBuckets)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/DescribeBuckets)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/DescribeBuckets)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/DescribeBuckets)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/DescribeBuckets)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/DescribeBuckets)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/DescribeBuckets)
