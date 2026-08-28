---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/jobs.html
---

# Classification Job Creation
<a name="jobs"></a>

The Classification Job Creation resource represents the collection of settings that define the scope and schedule for a classification job. A *classification job*, also referred to as a *sensitive data discovery job*, is a job that you create to analyze objects in Amazon Simple Storage Service (Amazon S3) general purpose buckets, and determine whether the objects contain sensitive data. To detect sensitive data, a job can use [managed data identifiers](managed-data-identifiers-list.md) that Amazon Macie provides, [custom data identifiers](custom-data-identifiers.md) that you define, or a combination of the two.

When you create a classification job, you can configure it to address specific scenarios. For example, you can use property- and tag-based conditions to perform targeted analysis of S3 buckets and objects that match specific criteria. You can also define a schedule for running the job on a recurring basis, such as every day or a specific day of each week or month. This can be helpful if you want to align your analysis with periodic updates to bucket objects or monitor buckets for the presence of sensitive data. In addition to these settings, you can configure a job to use one or more [allow lists](allow-lists.md). Allow lists define specific text or text patterns that you want Macie to ignore when it analyzes objects. You can create and use allow lists in all the AWS Regions where Macie is currently available except the Asia Pacific (Osaka) Region. For more information about creating and configuring jobs, see [Running sensitive data discovery jobs](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs.html) in the *Amazon Macie User Guide*.

You can use the Classification Job Creation resource to create and define the settings for a classification job. Note that you can't change any settings for a job after you create it. This helps to ensure that you have an immutable history of sensitive data findings and discovery results for data privacy and protection audits or investigations that you perform.

## URI
<a name="jobs-url"></a>

`/jobs`

## HTTP methods
<a name="jobs-http-methods"></a>

### POST
<a name="jobspost"></a>

**Operation ID:** `CreateClassificationJob`

Creates and defines the settings for a classification job.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateClassificationJobResponse | The request succeeded. The specified job was created. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="jobs-schemas"></a>

### Request bodies
<a name="jobs-request-examples"></a>

#### POST schema
<a name="jobs-request-body-post-example"></a>

```
{
  "allowListIds": [
    "string"
  ],
  "clientToken": "string",
  "customDataIdentifierIds": [
    "string"
  ],
  "description": "string",
  "initialRun": boolean,
  "jobType": enum,
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
  "tags": {
  }
}
```

### Response bodies
<a name="jobs-response-examples"></a>

#### CreateClassificationJobResponse schema
<a name="jobs-response-body-createclassificationjobresponse-example"></a>

```
{
  "jobArn": "string",
  "jobId": "string"
}
```

#### ValidationException schema
<a name="jobs-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="jobs-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="jobs-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="jobs-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="jobs-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="jobs-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="jobs-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="jobs-properties"></a>

### AccessDeniedException
<a name="jobs-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="jobs-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### CreateClassificationJobRequest
<a name="jobs-model-createclassificationjobrequest"></a>

Specifies the scope, schedule, and other settings for a classification job. You can't change any settings for a classification job after you create it. This helps to ensure that you have an immutable history of sensitive data findings and discovery results for data privacy and protection audits or investigations.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| allowListIds | Array of type string | False | An array of unique identifiers, one for each allow list for the job to use when it analyzes data. |
| clientToken | string | True | A unique, case-sensitive token that you provide to ensure the idempotency of the request. |
| customDataIdentifierIds | Array of type string | False | An array of unique identifiers, one for each custom data identifier for the job to use when it analyzes data. To use only managed data identifiers, don't specify a value for this property and specify a value other than `NONE` for the `managedDataIdentifierSelector` property. |
| description | string | False | A custom description of the job. The description can contain as many as 200 characters. |
| initialRun | boolean | False | For a recurring job, specifies whether to analyze all existing, eligible objects immediately after the job is created (`true`). To analyze only those objects that are created or changed after you create the job and before the job's first scheduled run, set this value to `false`.<br />If you configure the job to run only once, don't specify a value for this property. |
| jobType | [JobType](#jobs-model-jobtype) | True | The schedule for running the job. Valid values are:+   `ONE_TIME` - Run the job only once. If you specify this value, don't specify a value for the `scheduleFrequency` property. <br />+   `SCHEDULED` - Run the job on a daily, weekly, or monthly basis. If you specify this value, use the `scheduleFrequency` property to specify the recurrence pattern for the job.  |
| managedDataIdentifierIds | Array of type string | False | An array of unique identifiers, one for each managed data identifier for the job to include (use) or exclude (not use) when it analyzes data. Inclusion or exclusion depends on the managed data identifier selection type that you specify for the job (`managedDataIdentifierSelector`).<br />To retrieve a list of valid values for this property, use the `ListManagedDataIdentifiers` operation. |
| managedDataIdentifierSelector | [ManagedDataIdentifierSelector](#jobs-model-manageddataidentifierselector) | False | The selection type to apply when determining which managed data identifiers the job uses to analyze data. Valid values are:+  `ALL` - Use all managed data identifiers. If you specify this value, don't specify any values for the `managedDataIdentifierIds` property. <br />+  `EXCLUDE` - Use all managed data identifiers except the ones specified by the `managedDataIdentifierIds` property. <br />+  `INCLUDE` - Use only the managed data identifiers specified by the `managedDataIdentifierIds` property. <br />+  `NONE` - Don't use any managed data identifiers. If you specify this value, specify at least one value for the `customDataIdentifierIds` property and don't specify any values for the `managedDataIdentifierIds` property. <br />+  `RECOMMENDED` (default) - Use the recommended set of managed data identifiers. If you specify this value, don't specify any values for the `managedDataIdentifierIds` property. <br />If you don't specify a value for this property, the job uses the recommended set of managed data identifiers.<br />If the job is a recurring job and you specify `ALL` or `EXCLUDE`, each job run automatically uses new managed data identifiers that are released. If you don't specify a value for this property or you specify `RECOMMENDED` for a recurring job, each job run automatically uses all the managed data identifiers that are in the recommended set when the run starts.<br />To learn about individual managed data identifiers or determine which ones are in the recommended set, see [Using managed data identifiers](https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html) or [Recommended managed data identifiers](https://docs.aws.amazon.com/macie/latest/user/discovery-jobs-mdis-recommended.html) in the *Amazon Macie User Guide*. |
| name | string | True | A custom name for the job. The name can contain as many as 500 characters. |
| s3JobDefinition | [S3JobDefinition](#jobs-model-s3jobdefinition) | True | The S3 buckets that contain the objects to analyze, and the scope of that analysis. |
| samplingPercentage | integer<br />Format: int32 | False | The sampling depth, as a percentage, for the job to apply when processing objects. This value determines the percentage of eligible objects that the job analyzes. If this value is less than `100`, Amazon Macie selects the objects to analyze at random, up to the specified percentage, and analyzes all the data in those objects. |
| scheduleFrequency | [JobScheduleFrequency](#jobs-model-jobschedulefrequency) | False | The recurrence pattern for running the job. To run the job only once, don't specify a value for this property and set the value for the `jobType` property to `ONE_TIME`. |
| tags | [TagMap](#jobs-model-tagmap) | False | A map of key-value pairs that specifies the tags to associate with the job.<br />A job can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters. |

### CreateClassificationJobResponse
<a name="jobs-model-createclassificationjobresponse"></a>

Provides information about a classification job that was created in response to a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jobArn | string | False | The Amazon Resource Name (ARN) of the job. |
| jobId | string | False | The unique identifier for the job. |

### CriteriaBlockForJob
<a name="jobs-model-criteriablockforjob"></a>

Specifies one or more property- and tag-based conditions that define criteria for including or excluding S3 buckets from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| and | Array of type [CriteriaForJob](#jobs-model-criteriaforjob) | False | An array of conditions, one for each condition that determines which buckets to include or exclude from the job. If you specify more than one condition, Amazon Macie uses AND logic to join the conditions. |

### CriteriaForJob
<a name="jobs-model-criteriaforjob"></a>

Specifies a property- or tag-based condition that defines criteria for including or excluding S3 buckets from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| simpleCriterion | [SimpleCriterionForJob](#jobs-model-simplecriterionforjob) | False | A property-based condition that defines a property, operator, and one or more values for including or excluding buckets from the job. |
| tagCriterion | [TagCriterionForJob](#jobs-model-tagcriterionforjob) | False | A tag-based condition that defines an operator and tag keys, tag values, or tag key and value pairs for including or excluding buckets from the job. |

### DailySchedule
<a name="jobs-model-dailyschedule"></a>

Specifies that a classification job runs once a day, every day. This is an empty object.

### InternalServerException
<a name="jobs-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### JobComparator
<a name="jobs-model-jobcomparator"></a>

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
<a name="jobs-model-jobschedulefrequency"></a>

Specifies the recurrence pattern for running a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dailySchedule | [DailySchedule](#jobs-model-dailyschedule) | False | Specifies a daily recurrence pattern for running the job. |
| monthlySchedule | [MonthlySchedule](#jobs-model-monthlyschedule) | False | Specifies a monthly recurrence pattern for running the job. |
| weeklySchedule | [WeeklySchedule](#jobs-model-weeklyschedule) | False | Specifies a weekly recurrence pattern for running the job. |

### JobScopeTerm
<a name="jobs-model-jobscopeterm"></a>

Specifies a property- or tag-based condition that defines criteria for including or excluding S3 objects from a classification job. A `JobScopeTerm` object can contain only one `simpleScopeTerm` object or one `tagScopeTerm` object.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| simpleScopeTerm | [SimpleScopeTerm](#jobs-model-simplescopeterm) | False | A property-based condition that defines a property, operator, and one or more values for including or excluding objects from the job. |
| tagScopeTerm | [TagScopeTerm](#jobs-model-tagscopeterm) | False | A tag-based condition that defines the operator and tag keys or tag key and value pairs for including or excluding objects from the job. |

### JobScopingBlock
<a name="jobs-model-jobscopingblock"></a>

Specifies one or more property- and tag-based conditions that define criteria for including or excluding S3 objects from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| and | Array of type [JobScopeTerm](#jobs-model-jobscopeterm) | False | An array of conditions, one for each property- or tag-based condition that determines which objects to include or exclude from the job. If you specify more than one condition, Amazon Macie uses AND logic to join the conditions. |

### JobType
<a name="jobs-model-jobtype"></a>

The schedule for running a classification job. Valid values are:
+ `ONE_TIME`
+ `SCHEDULED`

### ManagedDataIdentifierSelector
<a name="jobs-model-manageddataidentifierselector"></a>

The selection type that determines which managed data identifiers a classification job uses to analyze data. Valid values are:
+ `ALL`
+ `EXCLUDE`
+ `INCLUDE`
+ `NONE`
+ `RECOMMENDED`

### MonthlySchedule
<a name="jobs-model-monthlyschedule"></a>

Specifies a monthly recurrence pattern for running a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dayOfMonth | integer<br />Format: int32 | False | The numeric day of the month when Amazon Macie runs the job. This value can be an integer from `1` through `31`.<br />If this value exceeds the number of days in a certain month, Macie doesn't run the job that month. Macie runs the job only during months that have the specified day. For example, if this value is `31` and a month has only 30 days, Macie doesn't run the job that month. To run the job every month, specify a value that's less than `29`. |

### ResourceNotFoundException
<a name="jobs-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### S3BucketCriteriaForJob
<a name="jobs-model-s3bucketcriteriaforjob"></a>

Specifies property- and tag-based conditions that define criteria for including or excluding S3 buckets from a classification job. Exclude conditions take precedence over include conditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| excludes | [CriteriaBlockForJob](#jobs-model-criteriablockforjob) | False | The property- and tag-based conditions that determine which buckets to exclude from the job. |
| includes | [CriteriaBlockForJob](#jobs-model-criteriablockforjob) | False | The property- and tag-based conditions that determine which buckets to include in the job. |

### S3BucketDefinitionForJob
<a name="jobs-model-s3bucketdefinitionforjob"></a>

Specifies an AWS account that owns S3 buckets for a classification job to analyze, and one or more specific buckets to analyze for that account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | True | The unique identifier for the AWS account that owns the buckets. |
| buckets | Array of type string | True | An array that lists the names of the buckets. |

### S3JobDefinition
<a name="jobs-model-s3jobdefinition"></a>

Specifies which S3 buckets contain the objects that a classification job analyzes, and the scope of that analysis. The bucket specification can be static (`bucketDefinitions`) or dynamic (`bucketCriteria`). If it's static, the job analyzes objects in the same predefined set of buckets each time the job runs. If it's dynamic, the job analyzes objects in any buckets that match the specified criteria each time the job starts to run.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucketCriteria | [S3BucketCriteriaForJob](#jobs-model-s3bucketcriteriaforjob) | False | The property- and tag-based conditions that determine which S3 buckets to include or exclude from the analysis. Each time the job runs, the job uses these criteria to determine which buckets contain objects to analyze. A job's definition can contain a `bucketCriteria` object or a `bucketDefinitions` array, not both. |
| bucketDefinitions | Array of type [S3BucketDefinitionForJob](#jobs-model-s3bucketdefinitionforjob) | False | An array of objects, one for each AWS account that owns specific S3 buckets to analyze. Each object specifies the account ID for an account and one or more buckets to analyze for that account. A job's definition can contain a `bucketDefinitions` array or a `bucketCriteria` object, not both. |
| scoping | [Scoping](#jobs-model-scoping) | False | The property- and tag-based conditions that determine which S3 objects to include or exclude from the analysis. Each time the job runs, the job uses these criteria to determine which objects to analyze. |

### ScopeFilterKey
<a name="jobs-model-scopefilterkey"></a>

The property to use in a condition that determines whether an S3 object is included or excluded from a classification job. Valid values are:
+ `OBJECT_EXTENSION`
+ `OBJECT_LAST_MODIFIED_DATE`
+ `OBJECT_SIZE`
+ `OBJECT_KEY`

### Scoping
<a name="jobs-model-scoping"></a>

Specifies one or more property- and tag-based conditions that define criteria for including or excluding S3 objects from a classification job. Exclude conditions take precedence over include conditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| excludes | [JobScopingBlock](#jobs-model-jobscopingblock) | False | The property- and tag-based conditions that determine which objects to exclude from the analysis. |
| includes | [JobScopingBlock](#jobs-model-jobscopingblock) | False | The property- and tag-based conditions that determine which objects to include in the analysis. |

### ServiceQuotaExceededException
<a name="jobs-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### SimpleCriterionForJob
<a name="jobs-model-simplecriterionforjob"></a>

Specifies a property-based condition that determines whether an S3 bucket is included or excluded from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| comparator | [JobComparator](#jobs-model-jobcomparator) | False | The operator to use in the condition. Valid values are `EQ` (equals) and `NE` (not equals). |
| key | [SimpleCriterionKeyForJob](#jobs-model-simplecriterionkeyforjob) | False | The property to use in the condition. |
| values | Array of type string | False | An array that lists one or more values to use in the condition. If you specify multiple values, Amazon Macie uses OR logic to join the values. Valid values for each supported property (`key`) are:+   `ACCOUNT_ID` - A string that represents the unique identifier for the AWS account that owns the bucket. <br />+   `S3_BUCKET_EFFECTIVE_PERMISSION` - A string that represents an enumerated value that Macie defines for the [BucketPublicAccess.effectivePermission](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketpublicaccess-effectivepermission) property of a bucket. <br />+   `S3_BUCKET_NAME` - A string that represents the name of a bucket. <br />+   `S3_BUCKET_SHARED_ACCESS` - A string that represents an enumerated value that Macie defines for the [BucketMetadata.sharedAccess](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketmetadata-sharedaccess) property of a bucket. <br />Values are case sensitive. Also, Macie doesn't support use of partial values or wildcard characters in these values. |

### SimpleCriterionKeyForJob
<a name="jobs-model-simplecriterionkeyforjob"></a>

The property to use in a condition that determines whether an S3 bucket is included or excluded from a classification job. Valid values are:
+ `ACCOUNT_ID`
+ `S3_BUCKET_NAME`
+ `S3_BUCKET_EFFECTIVE_PERMISSION`
+ `S3_BUCKET_SHARED_ACCESS`

### SimpleScopeTerm
<a name="jobs-model-simplescopeterm"></a>

Specifies a property-based condition that determines whether an S3 object is included or excluded from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| comparator | [JobComparator](#jobs-model-jobcomparator) | False | The operator to use in the condition. Valid values for each supported property (`key`) are:+   `OBJECT_EXTENSION` - `EQ` (equals) or `NE` (not equals) <br />+   `OBJECT_KEY` - `STARTS_WITH` <br />+   `OBJECT_LAST_MODIFIED_DATE` - `EQ` (equals), `GT` (greater than), `GTE` (greater than or equals), `LT` (less than), `LTE` (less than or equals), or `NE` (not equals) <br />+   `OBJECT_SIZE` - `EQ` (equals), `GT` (greater than), `GTE` (greater than or equals), `LT` (less than), `LTE` (less than or equals), or `NE` (not equals)  |
| key | [ScopeFilterKey](#jobs-model-scopefilterkey) | False | The object property to use in the condition. |
| values | Array of type string | False | An array that lists the values to use in the condition. If the value for the `key` property is `OBJECT_EXTENSION` or `OBJECT_KEY`, this array can specify multiple values and Amazon Macie uses OR logic to join the values. Otherwise, this array can specify only one value.<br />Valid values for each supported property (`key`) are:+   `OBJECT_EXTENSION` - A string that represents the file name extension of an object. For example: `docx` or `pdf`  <br />+   `OBJECT_KEY` - A string that represents the key prefix (folder name or path) of an object. For example: `logs` or `awslogs/eventlogs`. This value applies a condition to objects whose keys (names) begin with the specified value. <br />+   `OBJECT_LAST_MODIFIED_DATE` - The date and time (in UTC and extended ISO 8601 format) when an object was created or last changed, whichever is latest. For example: `2023-09-24T14:31:13Z`  <br />+   `OBJECT_SIZE` - An integer that represents the storage size (in bytes) of an object. <br />Macie doesn't support use of wildcard characters in these values. Also, string values are case sensitive. |

### TagCriterionForJob
<a name="jobs-model-tagcriterionforjob"></a>

Specifies a tag-based condition that determines whether an S3 bucket is included or excluded from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| comparator | [JobComparator](#jobs-model-jobcomparator) | False | The operator to use in the condition. Valid values are `EQ` (equals) and `NE` (not equals). |
| tagValues | Array of type [TagCriterionPairForJob](#jobs-model-tagcriterionpairforjob) | False | The tag keys, tag values, or tag key and value pairs to use in the condition. |

### TagCriterionPairForJob
<a name="jobs-model-tagcriterionpairforjob"></a>

Specifies a tag key, a tag value, or a tag key and value (as a pair) to use in a tag-based condition that determines whether an S3 bucket is included or excluded from a classification job. Tag keys and values are case sensitive. Also, Amazon Macie doesn't support use of partial values or wildcard characters in tag-based conditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| key | string | False | The value for the tag key to use in the condition. |
| value | string | False | The tag value to use in the condition. |

### TagMap
<a name="jobs-model-tagmap"></a>

A string-to-string map of key-value pairs that specifies the tags (keys and values) for an Amazon Macie resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### TagScopeTerm
<a name="jobs-model-tagscopeterm"></a>

Specifies a tag-based condition that determines whether an S3 object is included or excluded from a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| comparator | [JobComparator](#jobs-model-jobcomparator) | False | The operator to use in the condition. Valid values are `EQ` (equals) or `NE` (not equals). |
| key | string | False | The object property to use in the condition. The only valid value is `TAG`. |
| tagValues | Array of type [TagValuePair](#jobs-model-tagvaluepair) | False | The tag keys or tag key and value pairs to use in the condition. To specify only tag keys in a condition, specify the keys in this array and set the value for each associated tag value to an empty string. |
| target | [TagTarget](#jobs-model-tagtarget) | False | The type of object to apply the condition to. |

### TagTarget
<a name="jobs-model-tagtarget"></a>

The type of object to apply a tag-based condition to. Valid values are:
+ `S3_OBJECT`

### TagValuePair
<a name="jobs-model-tagvaluepair"></a>

Specifies a tag key or tag key and value pair to use in a tag-based condition that determines whether an S3 object is included or excluded from a classification job. Tag keys and values are case sensitive. Also, Amazon Macie doesn't support use of partial values or wildcard characters in tag-based conditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| key | string | False | The value for the tag key to use in the condition. |
| value | string | False | The tag value, associated with the specified tag key (`key`), to use in the condition. To specify only a tag key for a condition, specify the tag key for the `key` property and set this value to an empty string. |

### ThrottlingException
<a name="jobs-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="jobs-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### WeeklySchedule
<a name="jobs-model-weeklyschedule"></a>

Specifies a weekly recurrence pattern for running a classification job.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dayOfWeek | string<br />Values: `SUNDAY \| MONDAY \| TUESDAY \| WEDNESDAY \| THURSDAY \| FRIDAY \| SATURDAY` | False | The day of the week when Amazon Macie runs the job. |

## See also
<a name="jobs-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### CreateClassificationJob
<a name="CreateClassificationJob-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/CreateClassificationJob)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/CreateClassificationJob)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/CreateClassificationJob)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/CreateClassificationJob)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/CreateClassificationJob)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/CreateClassificationJob)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/CreateClassificationJob)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/CreateClassificationJob)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/CreateClassificationJob)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/CreateClassificationJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Macie. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query macie` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
