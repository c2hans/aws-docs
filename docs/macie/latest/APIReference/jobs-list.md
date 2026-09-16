---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/jobs-list.html
---

# Classification Job List
<a name="jobs-list"></a>

The Classification Job List resource provides a subset of information about the classification jobs for your Amazon Macie account. A *classification job*, also referred to as a *sensitive data discovery job*, is a job that you create to analyze objects in Amazon Simple Storage Service (Amazon S3) general purpose buckets, and determine whether the objects contain sensitive data.

You can use this resource to retrieve a subset of information about your classification jobs. To customize and refine your request, you can use the supported parameters to specify how to filter, sort, and paginate the results. To retrieve additional information about a particular classification job, use the [Classification Job](jobs-jobid.md) resource.

## URI
<a name="jobs-list-url"></a>

`/jobs/list`

## HTTP methods
<a name="jobs-list-http-methods"></a>

### POST
<a name="jobs-listpost"></a>

**Operation ID:** `ListClassificationJobs`

Retrieves a subset of information about one or more classification jobs.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListClassificationJobsResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="jobs-list-schemas"></a>

### Request bodies
<a name="jobs-list-request-examples"></a>

#### POST schema
<a name="jobs-list-request-body-post-example"></a>

```
{
  "filterCriteria": {
    "excludes": [
      {
        "comparator": enum,
        "key": enum,
        "values": [
          "string"
        ]
      }
    ],
    "includes": [
      {
        "comparator": enum,
        "key": enum,
        "values": [
          "string"
        ]
      }
    ]
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
<a name="jobs-list-response-examples"></a>

#### ListClassificationJobsResponse schema
<a name="jobs-list-response-body-listclassificationjobsresponse-example"></a>

```
{
  "items": [
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
      "bucketDefinitions": [
        {
          "accountId": "string",
          "buckets": [
            "string"
          ]
        }
      ],
      "createdAt": "string",
      "jobId": "string",
      "jobStatus": enum,
      "jobType": enum,
      "lastRunErrorStatus": {
        "code": enum
      },
      "name": "string",
      "userPausedDetails": {
        "jobExpiresAt": "string",
        "jobImminentExpirationHealthEventArn": "string",
        "jobPausedAt": "string"
      }
    }
  ],
  "nextToken": "string"
}
```

#### ValidationException schema
<a name="jobs-list-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="jobs-list-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="jobs-list-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="jobs-list-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="jobs-list-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="jobs-list-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="jobs-list-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="jobs-list-properties"></a>

### AccessDeniedException
<a name="jobs-list-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="jobs-list-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### CriteriaBlockForJob
<a name="jobs-list-model-criteriablockforjob"></a>

Specifies one or more property- and tag-based conditions that define criteria for including or excluding S3 buckets from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| and | Array of type [CriteriaForJob](#jobs-list-model-criteriaforjob) | False | An array of conditions, one for each condition that determines which buckets to include or exclude from the job. If you specify more than one condition, Amazon Macie uses AND logic to join the conditions. |

### CriteriaForJob
<a name="jobs-list-model-criteriaforjob"></a>

Specifies a property- or tag-based condition that defines criteria for including or excluding S3 buckets from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| simpleCriterion | [SimpleCriterionForJob](#jobs-list-model-simplecriterionforjob) | False | A property-based condition that defines a property, operator, and one or more values for including or excluding buckets from the job. |
| tagCriterion | [TagCriterionForJob](#jobs-list-model-tagcriterionforjob) | False | A tag-based condition that defines an operator and tag keys, tag values, or tag key and value pairs for including or excluding buckets from the job. |

### InternalServerException
<a name="jobs-list-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### JobComparator
<a name="jobs-list-model-jobcomparator"></a>

The operator to use in a condition. Depending on the type of condition, possible values are:
+ `EQ`
+ `GT`
+ `GTE`
+ `LT`
+ `LTE`
+ `NE`
+ `CONTAINS`
+ `STARTS_WITH`

### JobStatus
<a name="jobs-list-model-jobstatus"></a>

The status of a classification job. Possible values are:
+ `RUNNING`
+ `PAUSED`
+ `CANCELLED`
+ `COMPLETE`
+ `IDLE`
+ `USER_PAUSED`

### JobSummary
<a name="jobs-list-model-jobsummary"></a>

Provides information about a classification job, including the current status of the job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketCriteria | [S3BucketCriteriaForJob](#jobs-list-model-s3bucketcriteriaforjob) | False | The property- and tag-based conditions that determine which S3 buckets are included or excluded from the job's analysis. Each time the job runs, the job uses these criteria to determine which buckets to analyze. A job's definition can contain a `bucketCriteria` object or a `bucketDefinitions` array, not both. |
| bucketDefinitions | Array of type [S3BucketDefinitionForJob](#jobs-list-model-s3bucketdefinitionforjob) | False | An array of objects, one for each AWS account that owns specific S3 buckets for the job to analyze. Each object specifies the account ID for an account and one or more buckets to analyze for that account. A job's definition can contain a `bucketDefinitions` array or a `bucketCriteria` object, not both. |
| createdAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the job was created. |
| jobId | string | False | The unique identifier for the job. |
| jobStatus | [JobStatus](#jobs-list-model-jobstatus) | False | The current status of the job. Possible values are:+   `CANCELLED` - You cancelled the job or, if it's a one-time job, you paused the job and didn't resume it within 30 days. <br />+   `COMPLETE` - For a one-time job, Amazon Macie finished processing the data specified for the job. This value doesn't apply to recurring jobs. <br />+   `IDLE` - For a recurring job, the previous scheduled run is complete and the next scheduled run is pending. This value doesn't apply to one-time jobs. <br />+   `PAUSED` - Macie started running the job but additional processing would exceed the monthly sensitive data discovery quota for your account or one or more member accounts that the job analyzes data for. <br />+   `RUNNING` - For a one-time job, the job is in progress. For a recurring job, a scheduled run is in progress. <br />+   `USER_PAUSED` - You paused the job. If you paused the job while it had a status of `RUNNING` and you don't resume it within 30 days of pausing it, the job or job run will expire and be cancelled, depending on the job's type. To check the expiration date, refer to the `UserPausedDetails.jobExpiresAt` property.  |
| jobType | [JobType](#jobs-list-model-jobtype) | False | The schedule for running the job. Possible values are:+   `ONE_TIME` - The job runs only once. <br />+   `SCHEDULED` - The job runs on a daily, weekly, or monthly basis.  |
| lastRunErrorStatus | [LastRunErrorStatus](#jobs-list-model-lastrunerrorstatus) | False | Specifies whether any account- or bucket-level access errors occurred when the job ran. For a recurring job, this value indicates the error status of the job's most recent run. |
| name | string | False | The custom name of the job. |
| userPausedDetails | [UserPausedDetails](#jobs-list-model-userpauseddetails) | False | If the current status of the job is `USER_PAUSED`, specifies when the job was paused and when the job or job run will expire and be cancelled if it isn't resumed. This value is present only if the value for `jobStatus` is `USER_PAUSED`. |

### JobType
<a name="jobs-list-model-jobtype"></a>

The schedule for running a classification job. Valid values are:
+ `ONE_TIME`
+ `SCHEDULED`

### LastRunErrorStatus
<a name="jobs-list-model-lastrunerrorstatus"></a>

Specifies whether any account- or bucket-level access errors occurred when a classification job ran. For information about using logging data to investigate these errors, see [Monitoring sensitive data discovery jobs](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-monitor-cw-logs.html) in the *Amazon Macie User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| code | [LastRunErrorStatusCode](#jobs-list-model-lastrunerrorstatuscode) | False | Specifies whether any account- or bucket-level access errors occurred when the job ran. For a recurring job, this value indicates the error status of the job's most recent run. Possible values are:+   `ERROR` - One or more errors occurred. Amazon Macie didn't process all the data specified for the job. <br />+   `NONE` - No errors occurred. Macie processed all the data specified for the job.  |

### LastRunErrorStatusCode
<a name="jobs-list-model-lastrunerrorstatuscode"></a>

Specifies whether any account- or bucket-level access errors occurred during the run of a one-time classification job or the most recent run of a recurring classification job. Possible values are:
+ `NONE`
+ `ERROR`

### ListClassificationJobsRequest
<a name="jobs-list-model-listclassificationjobsrequest"></a>

Specifies criteria for filtering, sorting, and paginating the results of a request for information about classification jobs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| filterCriteria | [ListJobsFilterCriteria](#jobs-list-model-listjobsfiltercriteria) | False | The criteria to use to filter the results. |
| maxResults | integer<br />Format: int32 | False | The maximum number of items to include in each page of the response. |
| nextToken | string | False | The `nextToken` string that specifies which page of results to return in a paginated response. |
| sortCriteria | [ListJobsSortCriteria](#jobs-list-model-listjobssortcriteria) | False | The criteria to use to sort the results. |

### ListClassificationJobsResponse
<a name="jobs-list-model-listclassificationjobsresponse"></a>

Provides the results of a request for information about one or more classification jobs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [JobSummary](#jobs-list-model-jobsummary) | False | An array of objects, one for each job that matches the filter criteria specified in the request. |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### ListJobsFilterCriteria
<a name="jobs-list-model-listjobsfiltercriteria"></a>

Specifies criteria for filtering the results of a request for information about classification jobs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| excludes | Array of type [ListJobsFilterTerm](#jobs-list-model-listjobsfilterterm) | False | An array of objects, one for each condition that determines which jobs to exclude from the results.  |
| includes | Array of type [ListJobsFilterTerm](#jobs-list-model-listjobsfilterterm) | False | An array of objects, one for each condition that determines which jobs to include in the results.  |

### ListJobsFilterKey
<a name="jobs-list-model-listjobsfilterkey"></a>

The property to use to filter the results. Valid values are:
+ `jobType`
+ `jobStatus`
+ `createdAt`
+ `name`

### ListJobsFilterTerm
<a name="jobs-list-model-listjobsfilterterm"></a>

Specifies a condition that filters the results of a request for information about classification jobs. Each condition consists of a property, an operator, and one or more values.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| comparator | [JobComparator](#jobs-list-model-jobcomparator) | False | The operator to use to filter the results. |
| key | [ListJobsFilterKey](#jobs-list-model-listjobsfilterkey) | False | The property to use to filter the results. |
| values | Array of type string | False | An array that lists one or more values to use to filter the results. |

### ListJobsSortAttributeName
<a name="jobs-list-model-listjobssortattributename"></a>

The property to sort the results by. Valid values are:
+ `createdAt`
+ `jobStatus`
+ `name`
+ `jobType`

### ListJobsSortCriteria
<a name="jobs-list-model-listjobssortcriteria"></a>

Specifies criteria for sorting the results of a request for information about classification jobs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| attributeName | [ListJobsSortAttributeName](#jobs-list-model-listjobssortattributename) | False | The property to sort the results by. |
| orderBy | string<br />Values: `ASC \| DESC` | False | The sort order to apply to the results, based on the value for the property specified by the `attributeName` property. Valid values are: `ASC`, sort the results in ascending order; and, `DESC`, sort the results in descending order. |

### ResourceNotFoundException
<a name="jobs-list-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### S3BucketCriteriaForJob
<a name="jobs-list-model-s3bucketcriteriaforjob"></a>

Specifies property- and tag-based conditions that define criteria for including or excluding S3 buckets from a classification job. Exclude conditions take precedence over include conditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| excludes | [CriteriaBlockForJob](#jobs-list-model-criteriablockforjob) | False | The property- and tag-based conditions that determine which buckets to exclude from the job. |
| includes | [CriteriaBlockForJob](#jobs-list-model-criteriablockforjob) | False | The property- and tag-based conditions that determine which buckets to include in the job. |

### S3BucketDefinitionForJob
<a name="jobs-list-model-s3bucketdefinitionforjob"></a>

Specifies an AWS account that owns S3 buckets for a classification job to analyze, and one or more specific buckets to analyze for that account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | True | The unique identifier for the AWS account that owns the buckets. |
| buckets | Array of type string | True | An array that lists the names of the buckets. |

### ServiceQuotaExceededException
<a name="jobs-list-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### SimpleCriterionForJob
<a name="jobs-list-model-simplecriterionforjob"></a>

Specifies a property-based condition that determines whether an S3 bucket is included or excluded from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| comparator | [JobComparator](#jobs-list-model-jobcomparator) | False | The operator to use in the condition. Valid values are `EQ` (equals) and `NE` (not equals). |
| key | [SimpleCriterionKeyForJob](#jobs-list-model-simplecriterionkeyforjob) | False | The property to use in the condition. |
| values | Array of type string | False | An array that lists one or more values to use in the condition. If you specify multiple values, Amazon Macie uses OR logic to join the values. Valid values for each supported property (`key`) are:+   `ACCOUNT_ID` - A string that represents the unique identifier for the AWS account that owns the bucket. <br />+   `S3_BUCKET_EFFECTIVE_PERMISSION` - A string that represents an enumerated value that Macie defines for the [BucketPublicAccess.effectivePermission](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketpublicaccess-effectivepermission) property of a bucket. <br />+   `S3_BUCKET_NAME` - A string that represents the name of a bucket. <br />+   `S3_BUCKET_SHARED_ACCESS` - A string that represents an enumerated value that Macie defines for the [BucketMetadata.sharedAccess](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketmetadata-sharedaccess) property of a bucket. <br />Values are case sensitive. Also, Macie doesn't support use of partial values or wildcard characters in these values. |

### SimpleCriterionKeyForJob
<a name="jobs-list-model-simplecriterionkeyforjob"></a>

The property to use in a condition that determines whether an S3 bucket is included or excluded from a classification job. Valid values are:
+ `ACCOUNT_ID`
+ `S3_BUCKET_NAME`
+ `S3_BUCKET_EFFECTIVE_PERMISSION`
+ `S3_BUCKET_SHARED_ACCESS`

### TagCriterionForJob
<a name="jobs-list-model-tagcriterionforjob"></a>

Specifies a tag-based condition that determines whether an S3 bucket is included or excluded from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| comparator | [JobComparator](#jobs-list-model-jobcomparator) | False | The operator to use in the condition. Valid values are `EQ` (equals) and `NE` (not equals). |
| tagValues | Array of type [TagCriterionPairForJob](#jobs-list-model-tagcriterionpairforjob) | False | The tag keys, tag values, or tag key and value pairs to use in the condition. |

### TagCriterionPairForJob
<a name="jobs-list-model-tagcriterionpairforjob"></a>

Specifies a tag key, a tag value, or a tag key and value (as a pair) to use in a tag-based condition that determines whether an S3 bucket is included or excluded from a classification job. Tag keys and values are case sensitive. Also, Amazon Macie doesn't support use of partial values or wildcard characters in tag-based conditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| key | string | False | The value for the tag key to use in the condition. |
| value | string | False | The tag value to use in the condition. |

### ThrottlingException
<a name="jobs-list-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UserPausedDetails
<a name="jobs-list-model-userpauseddetails"></a>

Provides information about when a classification job was paused. For a one-time job, this object also specifies when the job will expire and be cancelled if it isn't resumed. For a recurring job, this object also specifies when the paused job run will expire and be cancelled if it isn't resumed. This object is present only if a job's current status (`jobStatus`) is `USER_PAUSED`. The information in this object applies only to a job that was paused while it had a status of `RUNNING`.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jobExpiresAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the job or job run will expire and be cancelled if you don't resume it first. |
| jobImminentExpirationHealthEventArn | string | False | The Amazon Resource Name (ARN) of the AWS Health event that Amazon Macie sent to notify you of the job or job run's pending expiration and cancellation. This value is null if a job has been paused for less than 23 days. |
| jobPausedAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when you paused the job. |

### ValidationException
<a name="jobs-list-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="jobs-list-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListClassificationJobs
<a name="ListClassificationJobs-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/ListClassificationJobs)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/ListClassificationJobs)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/ListClassificationJobs)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/ListClassificationJobs)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/ListClassificationJobs)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/ListClassificationJobs)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/ListClassificationJobs)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/ListClassificationJobs)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/ListClassificationJobs)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/ListClassificationJobs)
