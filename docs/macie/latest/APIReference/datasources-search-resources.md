---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/datasources-search-resources.html
---

# Data Sources - Search
<a name="datasources-search-resources"></a>

The Search Data Sources resource provides statistical data and other information about AWS resources that Amazon Macie monitors and analyzes for your account. The information includes quantitative breakdowns that indicate how much data Macie can analyze to detect sensitive data in a resource, and whether and when that analysis occurred. The data is available for all the AWS resources that Macie monitors and analyzes for your account. If you're the Macie administrator for an organization, this includes resources that your member accounts own.

Note that complete data is available for a resource only if Macie can retrieve and process information about the resource. If permissions settings, an error, or a quota prevents Macie from retrieving and processing the information, statistical data and other information about the resource is limited. Macie can provide only a subset of the information, such as the name of the resource and the account ID for the AWS account that owns the resource.

In addition to querying data about resources, you can use the Search Data Sources resource to build, test, and refine runtime criteria for new classification jobs. These criteria can determine which Amazon Simple Storage Service (Amazon S3) general purpose buckets a job analyzes when it runs. For existing classification jobs, you can use this resource to create a snapshot of the S3 general purpose buckets that currently match the criteria. This is because the `SearchResourcesBucketCriteria` structure for this resource is the same as the `S3BucketCriteriaForJob` structure for classification jobs. The exception is the `automatedDiscoveryMonitoringStatus` field. Jobs don't support use of that field in runtime criteria. To learn more about specifying runtime criteria for jobs, see [Scope options for jobs](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-scope.html) in the *Amazon Macie User Guide*.

You can use the Search Data Sources resource to query (retrieve) statistical data and other information about AWS resources that Macie monitors and analyzes for your account. To customize and refine your query, use the supported parameters to specify how to filter, sort, and paginate the results. You can also use this resource to build and test S3 bucket criteria for classification jobs.

## URI
<a name="datasources-search-resources-url"></a>

`/datasources/search-resources`

## HTTP methods
<a name="datasources-search-resources-http-methods"></a>

### POST
<a name="datasources-search-resourcespost"></a>

**Operation ID:** `SearchResources`

Retrieves (queries) statistical data and other information about AWS resources that Amazon Macie monitors and analyzes for an account.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | SearchResourcesResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="datasources-search-resources-schemas"></a>

### Request bodies
<a name="datasources-search-resources-request-examples"></a>

#### POST schema
<a name="datasources-search-resources-request-body-post-example"></a>

```
{
  "bucketCriteria": {
    "excludes": {
      "and": [
        {
          "simpleCriterion": {
            "comparator": enum,
            "key": enum,
            "values": [
              "string"
            ]
          },
          "tagCriterion": {
            "comparator": enum,
            "tagValues": [
              {
                "key": "string",
                "value": "string"
              }
            ]
          }
        }
      ]
    },
    "includes": {
      "and": [
        {
          "simpleCriterion": {
            "comparator": enum,
            "key": enum,
            "values": [
              "string"
            ]
          },
          "tagCriterion": {
            "comparator": enum,
            "tagValues": [
              {
                "key": "string",
                "value": "string"
              }
            ]
          }
        }
      ]
    }
  },
  "maxResults": integer,
  "nextToken": "string",
  "sortCriteria": {
    "attributeName": enum,
    "orderBy": enum
  }
}
```

### Response bodies
<a name="datasources-search-resources-response-examples"></a>

#### SearchResourcesResponse schema
<a name="datasources-search-resources-response-body-searchresourcesresponse-example"></a>

```
{
  "matchingResources": [
    {
      "matchingBucket": {
        "accountId": "string",
        "automatedDiscoveryMonitoringStatus": enum,
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
        "objectCount": integer,
        "objectCountByEncryptionType": {
          "customerManaged": integer,
          "kmsManaged": integer,
          "s3Managed": integer,
          "unencrypted": integer,
          "unknown": integer
        },
        "sensitivityScore": integer,
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
    }
  ],
  "nextToken": "string"
}
```

#### ValidationException schema
<a name="datasources-search-resources-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="datasources-search-resources-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="datasources-search-resources-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="datasources-search-resources-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="datasources-search-resources-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="datasources-search-resources-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="datasources-search-resources-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="datasources-search-resources-properties"></a>

### AccessDeniedException
<a name="datasources-search-resources-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### AutomatedDiscoveryMonitoringStatus
<a name="datasources-search-resources-model-automateddiscoverymonitoringstatus"></a>

Specifies whether automated sensitive data discovery is currently configured to analyze objects in an S3 bucket. Possible values are:
+ `MONITORED`
+ `NOT_MONITORED`

### BucketMetadataErrorCode
<a name="datasources-search-resources-model-bucketmetadataerrorcode"></a>

The code for an error or issue that prevented Amazon Macie from retrieving and processing information about an S3 bucket and the bucket's objects.
+ `ACCESS_DENIED`
+ `BUCKET_COUNT_EXCEEDS_QUOTA`

### ConflictException
<a name="datasources-search-resources-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### InternalServerException
<a name="datasources-search-resources-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### JobDetails
<a name="datasources-search-resources-model-jobdetails"></a>

Specifies whether any one-time or recurring classification jobs are configured to analyze objects in an S3 bucket, and, if so, the details of the job that ran most recently.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| isDefinedInJob | string<br />Values: `TRUE \| FALSE \| UNKNOWN` | False | Specifies whether any one-time or recurring jobs are configured to analyze objects in the bucket. Possible values are:+   `TRUE` - The bucket is explicitly included in the bucket definition (`S3BucketDefinitionForJob`) for one or more jobs and at least one of those jobs has a status other than `CANCELLED`. Or the bucket matched the bucket criteria (`S3BucketCriteriaForJob`) for at least one job that previously ran. <br />+   `FALSE` - The bucket isn't explicitly included in the bucket definition (`S3BucketDefinitionForJob`) for any jobs, all the jobs that explicitly include the bucket in their bucket definitions have a status of `CANCELLED`, or the bucket didn't match the bucket criteria (`S3BucketCriteriaForJob`) for any jobs that previously ran. <br />+   `UNKNOWN` - An exception occurred when Amazon Macie attempted to retrieve job data for the bucket.  |
| isMonitoredByJob | string<br />Values: `TRUE \| FALSE \| UNKNOWN` | False | Specifies whether any recurring jobs are configured to analyze objects in the bucket. Possible values are:+   `TRUE` - The bucket is explicitly included in the bucket definition (`S3BucketDefinitionForJob`) for one or more recurring jobs or the bucket matches the bucket criteria (`S3BucketCriteriaForJob`) for one or more recurring jobs. At least one of those jobs has a status other than `CANCELLED`. <br />+   `FALSE` - The bucket isn't explicitly included in the bucket definition (`S3BucketDefinitionForJob`) for any recurring jobs, the bucket doesn't match the bucket criteria (`S3BucketCriteriaForJob`) for any recurring jobs, or all the recurring jobs that are configured to analyze data in the bucket have a status of `CANCELLED`. <br />+   `UNKNOWN` - An exception occurred when Amazon Macie attempted to retrieve job data for the bucket.  |
| lastJobId | string | False | The unique identifier for the job that ran most recently and is configured to analyze objects in the bucket, either the latest run of a recurring job or the only run of a one-time job.<br />This value is typically null if the value for the `isDefinedInJob` property is `FALSE` or `UNKNOWN`. |
| lastJobRunTime | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the job (`lastJobId`) started. If the job is a recurring job, this value indicates when the most recent run started.<br />This value is typically null if the value for the `isDefinedInJob` property is `FALSE` or `UNKNOWN`. |

### MatchingBucket
<a name="datasources-search-resources-model-matchingbucket"></a>

Provides statistical data and other information about an S3 bucket that Amazon Macie monitors and analyzes for your account. By default, object count and storage size values include data for object parts that are the result of incomplete multipart uploads. For more information, see [How Macie monitors Amazon S3 data security](https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-how-it-works.html) in the *Amazon Macie User Guide*.

If an error or issue prevents Macie from retrieving and processing information about the bucket or the bucket's objects, the value for many of these properties is null. Key exceptions are `accountId` and `bucketName`. To identify the cause, refer to the `errorCode` and `errorMessage` values.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The unique identifier for the AWS account that owns the bucket. |
| automatedDiscoveryMonitoringStatus | [AutomatedDiscoveryMonitoringStatus](#datasources-search-resources-model-automateddiscoverymonitoringstatus) | False | Specifies whether automated sensitive data discovery is currently configured to analyze objects in the bucket. Possible values are: `MONITORED`, the bucket is included in analyses; and, `NOT_MONITORED`, the bucket is excluded from analyses. If automated sensitive data discovery is disabled for your account, this value is `NOT_MONITORED`. |
| bucketName | string | False | The name of the bucket. |
| classifiableObjectCount | integer<br />Format: int64 | False | The total number of objects that Amazon Macie can analyze in the bucket. These objects use a supported storage class and have a file name extension for a supported file or storage format. |
| classifiableSizeInBytes | integer<br />Format: int64 | False | The total storage size, in bytes, of the objects that Amazon Macie can analyze in the bucket. These objects use a supported storage class and have a file name extension for a supported file or storage format.<br />If versioning is enabled for the bucket, Macie calculates this value based on the size of the latest version of each applicable object in the bucket. This value doesn't reflect the storage size of all versions of each applicable object in the bucket. |
| errorCode | [BucketMetadataErrorCode](#datasources-search-resources-model-bucketmetadataerrorcode) | False | The code for an error or issue that prevented Amazon Macie from retrieving and processing information about the bucket and the bucket's objects. Possible values are:+  `ACCESS_DENIED` - Macie doesn't have permission to retrieve the information. For example, the bucket has a restrictive bucket policy and Amazon S3 denied the request. <br />+  `BUCKET_COUNT_EXCEEDS_QUOTA` - Retrieving and processing the information would exceed the quota for the number of buckets that Macie monitors for an account (10,000). <br />If this value is null, Macie was able to retrieve and process the information. |
| errorMessage | string | False | A brief description of the error or issue (`errorCode`) that prevented Amazon Macie from retrieving and processing information about the bucket and the bucket's objects. This value is null if Macie was able to retrieve and process the information. |
| jobDetails | [JobDetails](#datasources-search-resources-model-jobdetails) | False | Specifies whether any one-time or recurring classification jobs are configured to analyze objects in the bucket, and, if so, the details of the job that ran most recently. |
| lastAutomatedDiscoveryTime | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when Amazon Macie most recently analyzed objects in the bucket while performing automated sensitive data discovery. This value is null if this analysis hasn't occurred. |
| objectCount | integer<br />Format: int64 | False | The total number of objects in the bucket. |
| objectCountByEncryptionType | [ObjectCountByEncryptionType](#datasources-search-resources-model-objectcountbyencryptiontype) | False | The total number of objects in the bucket, grouped by server-side encryption type. This includes a grouping that reports the total number of objects that aren't encrypted or use client-side encryption. |
| sensitivityScore | integer<br />Format: int32 | False | The sensitivity score for the bucket, ranging from `-1` (classification error) to `100` (sensitive).<br />If automated sensitive data discovery has never been enabled for your account or it's been disabled for your organization or standalone account for more than 30 days, possible values are: `1`, the bucket is empty; or, `50`, the bucket stores objects but it's been excluded from recent analyses. |
| sizeInBytes | integer<br />Format: int64 | False | The total storage size, in bytes, of the bucket.<br />If versioning is enabled for the bucket, Amazon Macie calculates this value based on the size of the latest version of each object in the bucket. This value doesn't reflect the storage size of all versions of each object in the bucket. |
| sizeInBytesCompressed | integer<br />Format: int64 | False | The total storage size, in bytes, of the objects that are compressed (.gz, .gzip, .zip) files in the bucket.<br />If versioning is enabled for the bucket, Amazon Macie calculates this value based on the size of the latest version of each applicable object in the bucket. This value doesn't reflect the storage size of all versions of each applicable object in the bucket. |
| unclassifiableObjectCount | [ObjectLevelStatistics](#datasources-search-resources-model-objectlevelstatistics) | False | The total number of objects that Amazon Macie can't analyze in the bucket. These objects don't use a supported storage class or don't have a file name extension for a supported file or storage format. |
| unclassifiableObjectSizeInBytes | [ObjectLevelStatistics](#datasources-search-resources-model-objectlevelstatistics) | False | The total storage size, in bytes, of the objects that Amazon Macie can't analyze in the bucket. These objects don't use a supported storage class or don't have a file name extension for a supported file or storage format. |

### MatchingResource
<a name="datasources-search-resources-model-matchingresource"></a>

Provides statistical data and other information about an AWS resource that Amazon Macie monitors and analyzes for your account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| matchingBucket | [MatchingBucket](#datasources-search-resources-model-matchingbucket) | False | The details of an S3 bucket that Amazon Macie monitors and analyzes for your account. |

### ObjectCountByEncryptionType
<a name="datasources-search-resources-model-objectcountbyencryptiontype"></a>

Provides information about the number of objects that are in an S3 bucket and use certain types of server-side encryption, use client-side encryption, or aren't encrypted.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| customerManaged | integer<br />Format: int64 | False | The total number of objects that are encrypted with customer-provided keys. The objects use server-side encryption with customer-provided keys (SSE-C). |
| kmsManaged | integer<br />Format: int64 | False | The total number of objects that are encrypted with AWS KMS keys, either AWS managed keys or customer managed keys. The objects use dual-layer server-side encryption or server-side encryption with AWS KMS keys (DSSE-KMS or SSE-KMS). |
| s3Managed | integer<br />Format: int64 | False | The total number of objects that are encrypted with Amazon S3 managed keys. The objects use server-side encryption with Amazon S3 managed keys (SSE-S3). |
| unencrypted | integer<br />Format: int64 | False | The total number of objects that use client-side encryption or aren't encrypted. |
| unknown | integer<br />Format: int64 | False | The total number of objects that Amazon Macie doesn't have current encryption metadata for. Macie can't provide current data about the encryption settings for these objects. |

### ObjectLevelStatistics
<a name="datasources-search-resources-model-objectlevelstatistics"></a>

Provides information about the total storage size (in bytes) or number of objects that Amazon Macie can't analyze in one or more S3 buckets. In a `BucketMetadata` or `MatchingBucket` object, this data is for a specific bucket. In a `GetBucketStatisticsResponse` object, this data is aggregated for all the buckets in the query results. If versioning is enabled for a bucket, storage size values are based on the size of the latest version of each applicable object in the bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| fileType | integer<br />Format: int64 | False | The total storage size (in bytes) or number of objects that Amazon Macie can't analyze because the objects don't have a file name extension for a supported file or storage format. |
| storageClass | integer<br />Format: int64 | False | The total storage size (in bytes) or number of objects that Amazon Macie can't analyze because the objects use an unsupported storage class. |
| total | integer<br />Format: int64 | False | The total storage size (in bytes) or number of objects that Amazon Macie can't analyze because the objects use an unsupported storage class or don't have a file name extension for a supported file or storage format. |

### ResourceNotFoundException
<a name="datasources-search-resources-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### SearchResourcesBucketCriteria
<a name="datasources-search-resources-model-searchresourcesbucketcriteria"></a>

Specifies property- and tag-based conditions that define filter criteria for including or excluding S3 buckets from the query results. Exclude conditions take precedence over include conditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| excludes | [SearchResourcesCriteriaBlock](#datasources-search-resources-model-searchresourcescriteriablock) | False | The property- and tag-based conditions that determine which buckets to exclude from the results. |
| includes | [SearchResourcesCriteriaBlock](#datasources-search-resources-model-searchresourcescriteriablock) | False | The property- and tag-based conditions that determine which buckets to include in the results. |

### SearchResourcesComparator
<a name="datasources-search-resources-model-searchresourcescomparator"></a>

The operator to use in a condition that filters the results of a query. Valid values are:
+ `EQ`
+ `NE`

### SearchResourcesCriteria
<a name="datasources-search-resources-model-searchresourcescriteria"></a>

Specifies a property- or tag-based filter condition for including or excluding AWS resources from the query results.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| simpleCriterion | [SearchResourcesSimpleCriterion](#datasources-search-resources-model-searchresourcessimplecriterion) | False | A property-based condition that defines a property, operator, and one or more values for including or excluding resources from the results. |
| tagCriterion | [SearchResourcesTagCriterion](#datasources-search-resources-model-searchresourcestagcriterion) | False | A tag-based condition that defines an operator and tag keys, tag values, or tag key and value pairs for including or excluding resources from the results. |

### SearchResourcesCriteriaBlock
<a name="datasources-search-resources-model-searchresourcescriteriablock"></a>

Specifies property- and tag-based conditions that define filter criteria for including or excluding AWS resources from the query results.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| and | Array of type [SearchResourcesCriteria](#datasources-search-resources-model-searchresourcescriteria) | False | An array of objects, one for each property- or tag-based condition that includes or excludes resources from the query results. If you specify more than one condition, Amazon Macie uses AND logic to join the conditions. |

### SearchResourcesRequest
<a name="datasources-search-resources-model-searchresourcesrequest"></a>

Specifies criteria for filtering, sorting, and paginating the results of a query for statistical data and other information about AWS resources that Amazon Macie monitors and analyzes for your account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketCriteria | [SearchResourcesBucketCriteria](#datasources-search-resources-model-searchresourcesbucketcriteria) | False | The filter conditions that determine which S3 buckets to include or exclude from the query results. |
| maxResults | integer<br />Format: int32 | False | The maximum number of items to include in each page of the response. The default value is 50. |
| nextToken | string | False | The `nextToken` string that specifies which page of results to return in a paginated response. |
| sortCriteria | [SearchResourcesSortCriteria](#datasources-search-resources-model-searchresourcessortcriteria) | False | The criteria to use to sort the results. |

### SearchResourcesResponse
<a name="datasources-search-resources-model-searchresourcesresponse"></a>

Provides the results of a query that retrieved statistical data and other information about AWS resources that Amazon Macie monitors and analyzes for your account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| matchingResources | Array of type [MatchingResource](#datasources-search-resources-model-matchingresource) | False | An array of objects, one for each resource that matches the filter criteria specified in the request. |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### SearchResourcesSimpleCriterion
<a name="datasources-search-resources-model-searchresourcessimplecriterion"></a>

Specifies a property-based filter condition that determines which AWS resources are included or excluded from the query results.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| comparator | [SearchResourcesComparator](#datasources-search-resources-model-searchresourcescomparator) | False | The operator to use in the condition. Valid values are `EQ` (equals) and `NE` (not equals). |
| key | [SearchResourcesSimpleCriterionKey](#datasources-search-resources-model-searchresourcessimplecriterionkey) | False | The property to use in the condition. |
| values | Array of type string | False | An array that lists one or more values to use in the condition. If you specify multiple values, Amazon Macie uses OR logic to join the values. Valid values for each supported property (`key`) are:+   `ACCOUNT_ID` - A string that represents the unique identifier for the AWS account that owns the resource. <br />+  `AUTOMATED_DISCOVERY_MONITORING_STATUS` - A string that represents an enumerated value that Macie defines for the [BucketMetadata.automatedDiscoveryMonitoringStatus](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketmetadata-automateddiscoverymonitoringstatus) property of an S3 bucket. <br />+   `S3_BUCKET_EFFECTIVE_PERMISSION` - A string that represents an enumerated value that Macie defines for the [BucketPublicAccess.effectivePermission](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketpublicaccess-effectivepermission) property of an S3 bucket. <br />+   `S3_BUCKET_NAME` - A string that represents the name of an S3 bucket. <br />+   `S3_BUCKET_SHARED_ACCESS` - A string that represents an enumerated value that Macie defines for the [BucketMetadata.sharedAccess](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketmetadata-sharedaccess) property of an S3 bucket. <br />Values are case sensitive. Also, Macie doesn't support use of partial values or wildcard characters in values. |

### SearchResourcesSimpleCriterionKey
<a name="datasources-search-resources-model-searchresourcessimplecriterionkey"></a>

The property to use in a condition that filters the query results. Valid values are:
+ `ACCOUNT_ID`
+ `S3_BUCKET_NAME`
+ `S3_BUCKET_EFFECTIVE_PERMISSION`
+ `S3_BUCKET_SHARED_ACCESS`
+ `AUTOMATED_DISCOVERY_MONITORING_STATUS`

### SearchResourcesSortAttributeName
<a name="datasources-search-resources-model-searchresourcessortattributename"></a>

The property to sort the query results by. Valid values are:
+ `ACCOUNT_ID`
+ `RESOURCE_NAME`
+ `S3_CLASSIFIABLE_OBJECT_COUNT`
+ `S3_CLASSIFIABLE_SIZE_IN_BYTES`

### SearchResourcesSortCriteria
<a name="datasources-search-resources-model-searchresourcessortcriteria"></a>

Specifies criteria for sorting the results of a query for information about AWS resources that Amazon Macie monitors and analyzes.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| attributeName | [SearchResourcesSortAttributeName](#datasources-search-resources-model-searchresourcessortattributename) | False | The property to sort the results by. |
| orderBy | string<br />Values: `ASC \| DESC` | False | The sort order to apply to the results, based on the value for the property specified by the `attributeName` property. Valid values are: `ASC`, sort the results in ascending order; and, `DESC`, sort the results in descending order. |

### SearchResourcesTagCriterion
<a name="datasources-search-resources-model-searchresourcestagcriterion"></a>

Specifies a tag-based filter condition that determines which AWS resources are included or excluded from the query results.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| comparator | [SearchResourcesComparator](#datasources-search-resources-model-searchresourcescomparator) | False | The operator to use in the condition. Valid values are `EQ` (equals) and `NE` (not equals). |
| tagValues | Array of type [SearchResourcesTagCriterionPair](#datasources-search-resources-model-searchresourcestagcriterionpair) | False | The tag keys, tag values, or tag key and value pairs to use in the condition. |

### SearchResourcesTagCriterionPair
<a name="datasources-search-resources-model-searchresourcestagcriterionpair"></a>

Specifies a tag key, a tag value, or a tag key and value (as a pair) to use in a tag-based filter condition for a query. Tag keys and values are case sensitive. Also, Amazon Macie doesn't support use of partial values or wildcard characters in tag-based filter conditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| key | string | False | The value for the tag key to use in the condition. |
| value | string | False | The tag value to use in the condition. |

### ServiceQuotaExceededException
<a name="datasources-search-resources-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="datasources-search-resources-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="datasources-search-resources-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="datasources-search-resources-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### SearchResources
<a name="SearchResources-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/SearchResources)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/SearchResources)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/SearchResources)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/SearchResources)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/SearchResources)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/SearchResources)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/SearchResources)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/SearchResources)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/SearchResources)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/SearchResources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Macie. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query macie` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
