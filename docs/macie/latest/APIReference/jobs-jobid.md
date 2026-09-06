---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/jobs-jobid.html
---

# Classification Job
<a name="jobs-jobid"></a>

The Classification Job resource provides detailed information about individual classification jobs for your Amazon Macie account. It also provides access to the status of each job. A *classification job*, also referred to as a *sensitive data discovery job*, is a job that you create to analyze objects in Amazon Simple Storage Service (Amazon S3) general purpose buckets, and determine whether the objects contain sensitive data. For more information, see [Running sensitive data discovery jobs](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs.html) in the *Amazon Macie User Guide*.

You can use this resource to pause, resume, or cancel a classification job, or retrieve detailed information about a classification job. To retrieve information about more than one classification job, use the [Classification Job List](jobs-list.md) resource.

## URI
<a name="jobs-jobid-url"></a>

`/jobs/{{jobId}}`

## HTTP methods
<a name="jobs-jobid-http-methods"></a>

### GET
<a name="jobs-jobidget"></a>

**Operation ID:** `DescribeClassificationJob`

Retrieves the status and settings for a classification job.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{jobId}} | String | True | The unique identifier for the classification job. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DescribeClassificationJobResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### PATCH
<a name="jobs-jobidpatch"></a>

**Operation ID:** `UpdateClassificationJob`

Changes the status of a classification job.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{jobId}} | String | True | The unique identifier for the classification job. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Empty Schema | The request succeeded. The job's status was changed and there isn't any content to include in the body of the response (No Content). |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="jobs-jobid-schemas"></a>

### Request bodies
<a name="jobs-jobid-request-examples"></a>

#### PATCH schema
<a name="jobs-jobid-request-body-patch-example"></a>

```
{
  "jobStatus": enum
}
```

### Response bodies
<a name="jobs-jobid-response-examples"></a>

#### DescribeClassificationJobResponse schema
<a name="jobs-jobid-response-body-describeclassificationjobresponse-example"></a>

```
{
  "allowListIds": [
    "string"
  ],
  "clientToken": "string",
  "createdAt": "string",
  "customDataIdentifierIds": [
    "string"
  ],
  "description": "string",
  "initialRun": boolean,
  "jobArn": "string",
  "jobId": "string",
  "jobStatus": enum,
  "jobType": enum,
  "lastRunErrorStatus": {
    "code": enum
  },
  "lastRunTime": "string",
  "managedDataIdentifierIds": [
    "string"
  ],
  "managedDataIdentifierSelector": enum,
  "name": "string",
  "s3JobDefinition": {
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
    "scoping": {
      "excludes": {
        "and": [
          {
            "simpleScopeTerm": {
              "comparator": enum,
              "key": enum,
              "values": [
                "string"
              ]
            },
            "tagScopeTerm": {
              "comparator": enum,
              "key": "string",
              "tagValues": [
                {
                  "key": "string",
                  "value": "string"
                }
              ],
              "target": enum
            }
          }
        ]
      },
      "includes": {
        "and": [
          {
            "simpleScopeTerm": {
              "comparator": enum,
              "key": enum,
              "values": [
                "string"
              ]
            },
            "tagScopeTerm": {
              "comparator": enum,
              "key": "string",
              "tagValues": [
                {
                  "key": "string",
                  "value": "string"
                }
              ],
              "target": enum
            }
          }
        ]
      }
    }
  },
  "samplingPercentage": integer,
  "scheduleFrequency": {
    "dailySchedule": {
    },
    "monthlySchedule": {
      "dayOfMonth": integer
    },
    "weeklySchedule": {
      "dayOfWeek": enum
    }
  },
  "statistics": {
    "approximateNumberOfObjectsToProcess": number,
    "numberOfRuns": number
  },
  "tags": {
  },
  "userPausedDetails": {
    "jobExpiresAt": "string",
    "jobImminentExpirationHealthEventArn": "string",
    "jobPausedAt": "string"
  }
}
```

#### Empty Schema schema
<a name="jobs-jobid-response-body-empty-example"></a>

```
{
}
```

#### ValidationException schema
<a name="jobs-jobid-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="jobs-jobid-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="jobs-jobid-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="jobs-jobid-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="jobs-jobid-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="jobs-jobid-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="jobs-jobid-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="jobs-jobid-properties"></a>

### AccessDeniedException
<a name="jobs-jobid-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="jobs-jobid-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### CriteriaBlockForJob
<a name="jobs-jobid-model-criteriablockforjob"></a>

Specifies one or more property- and tag-based conditions that define criteria for including or excluding S3 buckets from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| and | Array of type [CriteriaForJob](#jobs-jobid-model-criteriaforjob) | False | An array of conditions, one for each condition that determines which buckets to include or exclude from the job. If you specify more than one condition, Amazon Macie uses AND logic to join the conditions. |

### CriteriaForJob
<a name="jobs-jobid-model-criteriaforjob"></a>

Specifies a property- or tag-based condition that defines criteria for including or excluding S3 buckets from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| simpleCriterion | [SimpleCriterionForJob](#jobs-jobid-model-simplecriterionforjob) | False | A property-based condition that defines a property, operator, and one or more values for including or excluding buckets from the job. |
| tagCriterion | [TagCriterionForJob](#jobs-jobid-model-tagcriterionforjob) | False | A tag-based condition that defines an operator and tag keys, tag values, or tag key and value pairs for including or excluding buckets from the job. |

### DailySchedule
<a name="jobs-jobid-model-dailyschedule"></a>

Specifies that a classification job runs once a day, every day. This is an empty object.

### DescribeClassificationJobResponse
<a name="jobs-jobid-model-describeclassificationjobresponse"></a>

Provides information about a classification job, including the current configuration settings and status of the job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| allowListIds | Array of type string | False | An array of unique identifiers, one for each allow list that the job is configured to use when it analyzes data. |
| clientToken | string | False | The token that was provided to ensure the idempotency of the request to create the job. |
| createdAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the job was created. |
| customDataIdentifierIds | Array of type string | False | An array of unique identifiers, one for each custom data identifier that the job is configured to use when it analyzes data. This value is null if the job is configured to use only managed data identifiers to analyze data. |
| description | string | False | The custom description of the job. |
| initialRun | boolean | False | For a recurring job, specifies whether you configured the job to analyze all existing, eligible objects immediately after the job was created (`true`). If you configured the job to analyze only those objects that were created or changed after the job was created and before the job's first scheduled run, this value is `false`. This value is also `false` for a one-time job. |
| jobArn | string | False | The Amazon Resource Name (ARN) of the job. |
| jobId | string | False | The unique identifier for the job. |
| jobStatus | [JobStatus](#jobs-jobid-model-jobstatus) | False | The current status of the job. Possible values are:+   `CANCELLED` - You cancelled the job or, if it's a one-time job, you paused the job and didn't resume it within 30 days. <br />+   `COMPLETE` - For a one-time job, Amazon Macie finished processing the data specified for the job. This value doesn't apply to recurring jobs. <br />+   `IDLE` - For a recurring job, the previous scheduled run is complete and the next scheduled run is pending. This value doesn't apply to one-time jobs. <br />+   `PAUSED` - Macie started running the job but additional processing would exceed the monthly sensitive data discovery quota for your account or one or more member accounts that the job analyzes data for. <br />+   `RUNNING` - For a one-time job, the job is in progress. For a recurring job, a scheduled run is in progress. <br />+   `USER_PAUSED` - You paused the job. If you paused the job while it had a status of `RUNNING` and you don't resume it within 30 days of pausing it, the job or job run will expire and be cancelled, depending on the job's type. To check the expiration date, refer to the `UserPausedDetails.jobExpiresAt` property.  |
| jobType | [JobType](#jobs-jobid-model-jobtype) | False | The schedule for running the job. Possible values are:+   `ONE_TIME` - The job runs only once. <br />+   `SCHEDULED` - The job runs on a daily, weekly, or monthly basis. The `scheduleFrequency` property indicates the recurrence pattern for the job.  |
| lastRunErrorStatus | [LastRunErrorStatus](#jobs-jobid-model-lastrunerrorstatus) | False | Specifies whether any account- or bucket-level access errors occurred when the job ran. For a recurring job, this value indicates the error status of the job's most recent run. |
| lastRunTime | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the job started. If the job is a recurring job, this value indicates when the most recent run started or, if the job hasn't run yet, when the job was created. |
| managedDataIdentifierIds | Array of type string | False | An array of unique identifiers, one for each managed data identifier that the job is explicitly configured to include (use) or exclude (not use) when it analyzes data. Inclusion or exclusion depends on the managed data identifier selection type specified for the job (`managedDataIdentifierSelector`).<br />This value is null if the job's managed data identifier selection type is `ALL`, `NONE`, or `RECOMMENDED`. |
| managedDataIdentifierSelector | [ManagedDataIdentifierSelector](#jobs-jobid-model-manageddataidentifierselector) | False | The selection type that determines which managed data identifiers the job uses when it analyzes data. Possible values are:+  `ALL` - Use all managed data identifiers. <br />+  `EXCLUDE` - Use all managed data identifiers except the ones specified by the `managedDataIdentifierIds` property. <br />+  `INCLUDE` - Use only the managed data identifiers specified by the `managedDataIdentifierIds` property. <br />+  `NONE` - Don't use any managed data identifiers. Use only custom data identifiers (`customDataIdentifierIds`). <br />+  `RECOMMENDED` (default) - Use the recommended set of managed data identifiers. <br />If this value is null, the job uses the recommended set of managed data identifiers.<br />If the job is a recurring job and this value is `ALL` or `EXCLUDE`, each job run automatically uses new managed data identifiers that are released. If this value is null or `RECOMMENDED` for a recurring job, each job run uses all the managed data identifiers that are in the recommended set when the run starts.<br />To learn about individual managed data identifiers or determine which ones are in the recommended set, see [Using managed data identifiers](https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html) or [Recommended managed data identifiers](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-mdis-recommended.html) in the *Amazon Macie User Guide*. |
| name | string | False | The custom name of the job. |
| s3JobDefinition | [S3JobDefinition](#jobs-jobid-model-s3jobdefinition) | False | The S3 buckets that contain the objects to analyze, and the scope of that analysis. |
| samplingPercentage | integer<br />Format: int32 | False | The sampling depth, as a percentage, that determines the percentage of eligible objects that the job analyzes. |
| scheduleFrequency | [JobScheduleFrequency](#jobs-jobid-model-jobschedulefrequency) | False | The recurrence pattern for running the job. This value is null if the job is configured to run only once. |
| statistics | [Statistics](#jobs-jobid-model-statistics) | False | The number of times that the job has run and processing statistics for the job's current run. |
| tags | [TagMap](#jobs-jobid-model-tagmap) | False | A map of key-value pairs that specifies which tags (keys and values) are associated with the job. |
| userPausedDetails | [UserPausedDetails](#jobs-jobid-model-userpauseddetails) | False | If the current status of the job is `USER_PAUSED`, specifies when the job was paused and when the job or job run will expire and be cancelled if it isn't resumed. This value is present only if the value for `jobStatus` is `USER_PAUSED`. |

### Empty
<a name="jobs-jobid-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### InternalServerException
<a name="jobs-jobid-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### JobComparator
<a name="jobs-jobid-model-jobcomparator"></a>

The operator to use in a condition. Depending on the type of condition, possible values are:
+ `EQ`
+ `GT`
+ `GTE`
+ `LT`
+ `LTE`
+ `NE`
+ `CONTAINS`
+ `STARTS_WITH`

### JobScheduleFrequency
<a name="jobs-jobid-model-jobschedulefrequency"></a>

Specifies the recurrence pattern for running a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dailySchedule | [DailySchedule](#jobs-jobid-model-dailyschedule) | False | Specifies a daily recurrence pattern for running the job. |
| monthlySchedule | [MonthlySchedule](#jobs-jobid-model-monthlyschedule) | False | Specifies a monthly recurrence pattern for running the job. |
| weeklySchedule | [WeeklySchedule](#jobs-jobid-model-weeklyschedule) | False | Specifies a weekly recurrence pattern for running the job. |

### JobScopeTerm
<a name="jobs-jobid-model-jobscopeterm"></a>

Specifies a property- or tag-based condition that defines criteria for including or excluding S3 objects from a classification job. A `JobScopeTerm` object can contain only one `simpleScopeTerm` object or one `tagScopeTerm` object.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| simpleScopeTerm | [SimpleScopeTerm](#jobs-jobid-model-simplescopeterm) | False | A property-based condition that defines a property, operator, and one or more values for including or excluding objects from the job. |
| tagScopeTerm | [TagScopeTerm](#jobs-jobid-model-tagscopeterm) | False | A tag-based condition that defines the operator and tag keys or tag key and value pairs for including or excluding objects from the job. |

### JobScopingBlock
<a name="jobs-jobid-model-jobscopingblock"></a>

Specifies one or more property- and tag-based conditions that define criteria for including or excluding S3 objects from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| and | Array of type [JobScopeTerm](#jobs-jobid-model-jobscopeterm) | False | An array of conditions, one for each property- or tag-based condition that determines which objects to include or exclude from the job. If you specify more than one condition, Amazon Macie uses AND logic to join the conditions. |

### JobStatus
<a name="jobs-jobid-model-jobstatus"></a>

The status of a classification job. Possible values are:
+ `RUNNING`
+ `PAUSED`
+ `CANCELLED`
+ `COMPLETE`
+ `IDLE`
+ `USER_PAUSED`

### JobType
<a name="jobs-jobid-model-jobtype"></a>

The schedule for running a classification job. Valid values are:
+ `ONE_TIME`
+ `SCHEDULED`

### LastRunErrorStatus
<a name="jobs-jobid-model-lastrunerrorstatus"></a>

Specifies whether any account- or bucket-level access errors occurred when a classification job ran. For information about using logging data to investigate these errors, see [Monitoring sensitive data discovery jobs](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-monitor-cw-logs.html) in the *Amazon Macie User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| code | [LastRunErrorStatusCode](#jobs-jobid-model-lastrunerrorstatuscode) | False | Specifies whether any account- or bucket-level access errors occurred when the job ran. For a recurring job, this value indicates the error status of the job's most recent run. Possible values are:+   `ERROR` - One or more errors occurred. Amazon Macie didn't process all the data specified for the job. <br />+   `NONE` - No errors occurred. Macie processed all the data specified for the job.  |

### LastRunErrorStatusCode
<a name="jobs-jobid-model-lastrunerrorstatuscode"></a>

Specifies whether any account- or bucket-level access errors occurred during the run of a one-time classification job or the most recent run of a recurring classification job. Possible values are:
+ `NONE`
+ `ERROR`

### ManagedDataIdentifierSelector
<a name="jobs-jobid-model-manageddataidentifierselector"></a>

The selection type that determines which managed data identifiers a classification job uses to analyze data. Valid values are:
+ `ALL`
+ `EXCLUDE`
+ `INCLUDE`
+ `NONE`
+ `RECOMMENDED`

### MonthlySchedule
<a name="jobs-jobid-model-monthlyschedule"></a>

Specifies a monthly recurrence pattern for running a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dayOfMonth | integer<br />Format: int32 | False | The numeric day of the month when Amazon Macie runs the job. This value can be an integer from `1` through `31`.<br />If this value exceeds the number of days in a certain month, Macie doesn't run the job that month. Macie runs the job only during months that have the specified day. For example, if this value is `31` and a month has only 30 days, Macie doesn't run the job that month. To run the job every month, specify a value that's less than `29`. |

### ResourceNotFoundException
<a name="jobs-jobid-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### S3BucketCriteriaForJob
<a name="jobs-jobid-model-s3bucketcriteriaforjob"></a>

Specifies property- and tag-based conditions that define criteria for including or excluding S3 buckets from a classification job. Exclude conditions take precedence over include conditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| excludes | [CriteriaBlockForJob](#jobs-jobid-model-criteriablockforjob) | False | The property- and tag-based conditions that determine which buckets to exclude from the job. |
| includes | [CriteriaBlockForJob](#jobs-jobid-model-criteriablockforjob) | False | The property- and tag-based conditions that determine which buckets to include in the job. |

### S3BucketDefinitionForJob
<a name="jobs-jobid-model-s3bucketdefinitionforjob"></a>

Specifies an AWS account that owns S3 buckets for a classification job to analyze, and one or more specific buckets to analyze for that account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | True | The unique identifier for the AWS account that owns the buckets. |
| buckets | Array of type string | True | An array that lists the names of the buckets. |

### S3JobDefinition
<a name="jobs-jobid-model-s3jobdefinition"></a>

Specifies which S3 buckets contain the objects that a classification job analyzes, and the scope of that analysis. The bucket specification can be static (`bucketDefinitions`) or dynamic (`bucketCriteria`). If it's static, the job analyzes objects in the same predefined set of buckets each time the job runs. If it's dynamic, the job analyzes objects in any buckets that match the specified criteria each time the job starts to run.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketCriteria | [S3BucketCriteriaForJob](#jobs-jobid-model-s3bucketcriteriaforjob) | False | The property- and tag-based conditions that determine which S3 buckets to include or exclude from the analysis. Each time the job runs, the job uses these criteria to determine which buckets contain objects to analyze. A job's definition can contain a `bucketCriteria` object or a `bucketDefinitions` array, not both. |
| bucketDefinitions | Array of type [S3BucketDefinitionForJob](#jobs-jobid-model-s3bucketdefinitionforjob) | False | An array of objects, one for each AWS account that owns specific S3 buckets to analyze. Each object specifies the account ID for an account and one or more buckets to analyze for that account. A job's definition can contain a `bucketDefinitions` array or a `bucketCriteria` object, not both. |
| scoping | [Scoping](#jobs-jobid-model-scoping) | False | The property- and tag-based conditions that determine which S3 objects to include or exclude from the analysis. Each time the job runs, the job uses these criteria to determine which objects to analyze. |

### ScopeFilterKey
<a name="jobs-jobid-model-scopefilterkey"></a>

The property to use in a condition that determines whether an S3 object is included or excluded from a classification job. Valid values are:
+ `OBJECT_EXTENSION`
+ `OBJECT_LAST_MODIFIED_DATE`
+ `OBJECT_SIZE`
+ `OBJECT_KEY`

### Scoping
<a name="jobs-jobid-model-scoping"></a>

Specifies one or more property- and tag-based conditions that define criteria for including or excluding S3 objects from a classification job. Exclude conditions take precedence over include conditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| excludes | [JobScopingBlock](#jobs-jobid-model-jobscopingblock) | False | The property- and tag-based conditions that determine which objects to exclude from the analysis. |
| includes | [JobScopingBlock](#jobs-jobid-model-jobscopingblock) | False | The property- and tag-based conditions that determine which objects to include in the analysis. |

### ServiceQuotaExceededException
<a name="jobs-jobid-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### SimpleCriterionForJob
<a name="jobs-jobid-model-simplecriterionforjob"></a>

Specifies a property-based condition that determines whether an S3 bucket is included or excluded from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| comparator | [JobComparator](#jobs-jobid-model-jobcomparator) | False | The operator to use in the condition. Valid values are `EQ` (equals) and `NE` (not equals). |
| key | [SimpleCriterionKeyForJob](#jobs-jobid-model-simplecriterionkeyforjob) | False | The property to use in the condition. |
| values | Array of type string | False | An array that lists one or more values to use in the condition. If you specify multiple values, Amazon Macie uses OR logic to join the values. Valid values for each supported property (`key`) are:+   `ACCOUNT_ID` - A string that represents the unique identifier for the AWS account that owns the bucket. <br />+   `S3_BUCKET_EFFECTIVE_PERMISSION` - A string that represents an enumerated value that Macie defines for the [BucketPublicAccess.effectivePermission](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketpublicaccess-effectivepermission) property of a bucket. <br />+   `S3_BUCKET_NAME` - A string that represents the name of a bucket. <br />+   `S3_BUCKET_SHARED_ACCESS` - A string that represents an enumerated value that Macie defines for the [BucketMetadata.sharedAccess](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketmetadata-sharedaccess) property of a bucket. <br />Values are case sensitive. Also, Macie doesn't support use of partial values or wildcard characters in these values. |

### SimpleCriterionKeyForJob
<a name="jobs-jobid-model-simplecriterionkeyforjob"></a>

The property to use in a condition that determines whether an S3 bucket is included or excluded from a classification job. Valid values are:
+ `ACCOUNT_ID`
+ `S3_BUCKET_NAME`
+ `S3_BUCKET_EFFECTIVE_PERMISSION`
+ `S3_BUCKET_SHARED_ACCESS`

### SimpleScopeTerm
<a name="jobs-jobid-model-simplescopeterm"></a>

Specifies a property-based condition that determines whether an S3 object is included or excluded from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| comparator | [JobComparator](#jobs-jobid-model-jobcomparator) | False | The operator to use in the condition. Valid values for each supported property (`key`) are:+   `OBJECT_EXTENSION` - `EQ` (equals) or `NE` (not equals) <br />+   `OBJECT_KEY` - `STARTS_WITH` <br />+   `OBJECT_LAST_MODIFIED_DATE` - `EQ` (equals), `GT` (greater than), `GTE` (greater than or equals), `LT` (less than), `LTE` (less than or equals), or `NE` (not equals) <br />+   `OBJECT_SIZE` - `EQ` (equals), `GT` (greater than), `GTE` (greater than or equals), `LT` (less than), `LTE` (less than or equals), or `NE` (not equals)  |
| key | [ScopeFilterKey](#jobs-jobid-model-scopefilterkey) | False | The object property to use in the condition. |
| values | Array of type string | False | An array that lists the values to use in the condition. If the value for the `key` property is `OBJECT_EXTENSION` or `OBJECT_KEY`, this array can specify multiple values and Amazon Macie uses OR logic to join the values. Otherwise, this array can specify only one value.<br />Valid values for each supported property (`key`) are:+   `OBJECT_EXTENSION` - A string that represents the file name extension of an object. For example: `docx` or `pdf`  <br />+   `OBJECT_KEY` - A string that represents the key prefix (folder name or path) of an object. For example: `logs` or `awslogs/eventlogs`. This value applies a condition to objects whose keys (names) begin with the specified value. <br />+   `OBJECT_LAST_MODIFIED_DATE` - The date and time (in UTC and extended ISO 8601 format) when an object was created or last changed, whichever is latest. For example: `2023-09-24T14:31:13Z`  <br />+   `OBJECT_SIZE` - An integer that represents the storage size (in bytes) of an object. <br />Macie doesn't support use of wildcard characters in these values. Also, string values are case sensitive. |

### Statistics
<a name="jobs-jobid-model-statistics"></a>

Provides processing statistics for a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| approximateNumberOfObjectsToProcess | number | False | The approximate number of objects that the job has yet to process during its current run. |
| numberOfRuns | number | False | The number of times that the job has run. |

### TagCriterionForJob
<a name="jobs-jobid-model-tagcriterionforjob"></a>

Specifies a tag-based condition that determines whether an S3 bucket is included or excluded from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| comparator | [JobComparator](#jobs-jobid-model-jobcomparator) | False | The operator to use in the condition. Valid values are `EQ` (equals) and `NE` (not equals). |
| tagValues | Array of type [TagCriterionPairForJob](#jobs-jobid-model-tagcriterionpairforjob) | False | The tag keys, tag values, or tag key and value pairs to use in the condition. |

### TagCriterionPairForJob
<a name="jobs-jobid-model-tagcriterionpairforjob"></a>

Specifies a tag key, a tag value, or a tag key and value (as a pair) to use in a tag-based condition that determines whether an S3 bucket is included or excluded from a classification job. Tag keys and values are case sensitive. Also, Amazon Macie doesn't support use of partial values or wildcard characters in tag-based conditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| key | string | False | The value for the tag key to use in the condition. |
| value | string | False | The tag value to use in the condition. |

### TagMap
<a name="jobs-jobid-model-tagmap"></a>

A string-to-string map of key-value pairs that specifies the tags (keys and values) for an Amazon Macie resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### TagScopeTerm
<a name="jobs-jobid-model-tagscopeterm"></a>

Specifies a tag-based condition that determines whether an S3 object is included or excluded from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| comparator | [JobComparator](#jobs-jobid-model-jobcomparator) | False | The operator to use in the condition. Valid values are `EQ` (equals) or `NE` (not equals). |
| key | string | False | The object property to use in the condition. The only valid value is `TAG`. |
| tagValues | Array of type [TagValuePair](#jobs-jobid-model-tagvaluepair) | False | The tag keys or tag key and value pairs to use in the condition. To specify only tag keys in a condition, specify the keys in this array and set the value for each associated tag value to an empty string. |
| target | [TagTarget](#jobs-jobid-model-tagtarget) | False | The type of object to apply the condition to. |

### TagTarget
<a name="jobs-jobid-model-tagtarget"></a>

The type of object to apply a tag-based condition to. Valid values are:
+ `S3_OBJECT`

### TagValuePair
<a name="jobs-jobid-model-tagvaluepair"></a>

Specifies a tag key or tag key and value pair to use in a tag-based condition that determines whether an S3 object is included or excluded from a classification job. Tag keys and values are case sensitive. Also, Amazon Macie doesn't support use of partial values or wildcard characters in tag-based conditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| key | string | False | The value for the tag key to use in the condition. |
| value | string | False | The tag value, associated with the specified tag key (`key`), to use in the condition. To specify only a tag key for a condition, specify the tag key for the `key` property and set this value to an empty string. |

### ThrottlingException
<a name="jobs-jobid-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UpdateClassificationJobRequest
<a name="jobs-jobid-model-updateclassificationjobrequest"></a>

Changes the status of a classification job. For more information about pausing, resuming, or cancelling jobs, see [Changing the status of a job](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-status-change.html) in the *Amazon Macie User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jobStatus | [JobStatus](#jobs-jobid-model-jobstatus) | True | The new status for the job. Valid values are:+   `CANCELLED` - Stops the job permanently and cancels it. This value is valid only if the job's current status is `IDLE`, `PAUSED`, `RUNNING`, or `USER_PAUSED`. <br />If you specify this value and the job's current status is `RUNNING`, Amazon Macie immediately begins to stop all processing tasks for the job. You can't resume or restart a job after you cancel it. <br />+   `RUNNING` - Resumes the job. This value is valid only if the job's current status is `USER_PAUSED`. <br />If you paused the job while it was actively running and you specify this value less than 30 days after you paused the job, Macie immediately resumes processing from the point where you paused the job. Otherwise, Macie resumes the job according to the schedule and other settings for the job. <br />+   `USER_PAUSED` - Pauses the job temporarily. This value is valid only if the job's current status is `IDLE`, `PAUSED`, or `RUNNING`. If you specify this value and the job's current status is `RUNNING`, Macie immediately begins to pause all processing tasks for the job. <br />If you pause a one-time job and you don't resume it within 30 days, the job expires and Macie cancels the job. If you pause a recurring job when its status is `RUNNING` and you don't resume it within 30 days, the job run expires and Macie cancels the run. To check the expiration date, refer to the `UserPausedDetails.jobExpiresAt` property.  |

### UserPausedDetails
<a name="jobs-jobid-model-userpauseddetails"></a>

Provides information about when a classification job was paused. For a one-time job, this object also specifies when the job will expire and be cancelled if it isn't resumed. For a recurring job, this object also specifies when the paused job run will expire and be cancelled if it isn't resumed. This object is present only if a job's current status (`jobStatus`) is `USER_PAUSED`. The information in this object applies only to a job that was paused while it had a status of `RUNNING`.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jobExpiresAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the job or job run will expire and be cancelled if you don't resume it first. |
| jobImminentExpirationHealthEventArn | string | False | The Amazon Resource Name (ARN) of the AWS Health event that Amazon Macie sent to notify you of the job or job run's pending expiration and cancellation. This value is null if a job has been paused for less than 23 days. |
| jobPausedAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when you paused the job. |

### ValidationException
<a name="jobs-jobid-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### WeeklySchedule
<a name="jobs-jobid-model-weeklyschedule"></a>

Specifies a weekly recurrence pattern for running a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dayOfWeek | string<br />Values: `SUNDAY \| MONDAY \| TUESDAY \| WEDNESDAY \| THURSDAY \| FRIDAY \| SATURDAY` | False | The day of the week when Amazon Macie runs the job. |

## See also
<a name="jobs-jobid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeClassificationJob
<a name="DescribeClassificationJob-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/DescribeClassificationJob)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/DescribeClassificationJob)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/DescribeClassificationJob)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/DescribeClassificationJob)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/DescribeClassificationJob)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/DescribeClassificationJob)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/DescribeClassificationJob)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/DescribeClassificationJob)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/DescribeClassificationJob)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/DescribeClassificationJob)

### UpdateClassificationJob
<a name="UpdateClassificationJob-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/UpdateClassificationJob)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/UpdateClassificationJob)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/UpdateClassificationJob)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/UpdateClassificationJob)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/UpdateClassificationJob)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/UpdateClassificationJob)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/UpdateClassificationJob)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/UpdateClassificationJob)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/UpdateClassificationJob)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/UpdateClassificationJob)
