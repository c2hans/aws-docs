---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/resource-profiles.html
---

# Resource Sensitivity Profile
<a name="resource-profiles"></a>

The Resource Sensitivity Profile resource provides statistical data for sensitive data discovery metrics that apply to individual Amazon Simple Storage Service (Amazon S3) buckets for your account. If you're the Amazon Macie administrator for an organization, this includes S3 buckets that your member accounts own.

For each S3 bucket, the data includes metrics such as:
+ The number of objects that Amazon Macie has analyzed.
+ The number of objects that Macie has found sensitive data in.
+ The number of occurrences of sensitive data that Macie has found.

The data captures the results of automated sensitive data discovery activities that Macie has performed for an S3 bucket. For more information, see [Performing automated sensitive data discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd.html) in the *Amazon Macie User Guide*.

This resource also provides access to the sensitivity score for individual S3 buckets. By default, Macie calculates this score based on the intersection of two primary dimensions: the amount of data that Macie has analyzed in a bucket, and the amount of sensitive data that Macie has found in a bucket. If you're a Macie administrator or you have a standalone Macie account, you can optionally override the calculated score for a bucket. You can assign the maximum score (`100`), which also applies the *Sensitive* label to the bucket. If you override the calculated score, Macie continues to perform automated sensitive data discovery for the bucket. However, later analyses don't affect the bucket's score.

You can use the Resource Sensitivity Profile resource to retrieve (query) sensitive data discovery statistics and the sensitivity score for an S3 bucket. If you're a Macie administrator or you have a standalone Macie account, you can also use this resource to change the sensitivity score for a bucket.

To use this resource, you must first enable automated sensitive data discovery. To enable it for an organization or a standalone account, use the [Configuration](automated-discovery-configuration.md) resource for automated sensitive data discovery. To enable it for a member account in an organization, use the [Accounts](automated-discovery-accounts.md) resource for automated sensitive data discovery.

## URI
<a name="resource-profiles-url"></a>

`/resource-profiles`

## HTTP methods
<a name="resource-profiles-http-methods"></a>

### GET
<a name="resource-profilesget"></a>

**Operation ID:** `GetResourceProfile`

Retrieves (queries) sensitive data discovery statistics and the sensitivity score for an S3 bucket.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| resourceArn | String | True | The Amazon Resource Name (ARN) of the S3 bucket that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetResourceProfileResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### PATCH
<a name="resource-profilespatch"></a>

**Operation ID:** `UpdateResourceProfile`

Updates the sensitivity score for an S3 bucket.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| resourceArn | String | True | The Amazon Resource Name (ARN) of the S3 bucket that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Empty Schema | The request succeeded. The S3 bucket's sensitivity score was updated and there isn't any content to include in the body of the response (No Content). |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="resource-profiles-schemas"></a>

### Request bodies
<a name="resource-profiles-request-examples"></a>

#### PATCH schema
<a name="resource-profiles-request-body-patch-example"></a>

```
{
  "sensitivityScoreOverride": integer
}
```

### Response bodies
<a name="resource-profiles-response-examples"></a>

#### GetResourceProfileResponse schema
<a name="resource-profiles-response-body-getresourceprofileresponse-example"></a>

```
{
  "profileUpdatedAt": "string",
  "sensitivityScore": integer,
  "sensitivityScoreOverridden": boolean,
  "statistics": {
    "totalBytesClassified": integer,
    "totalDetections": integer,
    "totalDetectionsSuppressed": integer,
    "totalItemsClassified": integer,
    "totalItemsSensitive": integer,
    "totalItemsSkipped": integer,
    "totalItemsSkippedInvalidEncryption": integer,
    "totalItemsSkippedInvalidKms": integer,
    "totalItemsSkippedPermissionDenied": integer
  }
}
```

#### Empty Schema schema
<a name="resource-profiles-response-body-empty-example"></a>

```
{
}
```

#### ValidationException schema
<a name="resource-profiles-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="resource-profiles-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="resource-profiles-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="resource-profiles-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="resource-profiles-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="resource-profiles-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="resource-profiles-properties"></a>

### AccessDeniedException
<a name="resource-profiles-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Empty
<a name="resource-profiles-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### GetResourceProfileResponse
<a name="resource-profiles-model-getresourceprofileresponse"></a>

Provides sensitive data discovery statistics and the sensitivity score for an S3 bucket that Amazon Macie monitors and analyzes for an account. This data is available only if automated sensitive data discovery has been enabled for the account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| profileUpdatedAt | string<br />Format: date-time | True | The date and time, in UTC and extended ISO 8601 format, when Amazon Macie most recently recalculated sensitive data discovery statistics and details for the bucket. If the bucket's sensitivity score is calculated automatically, this includes the score. |
| sensitivityScore | integer<br />Format: int32 | True | The current sensitivity score for the bucket, ranging from `-1` (classification error) to `100` (sensitive). By default, this score is calculated automatically based on the amount of data that Amazon Macie has analyzed in the bucket and the amount of sensitive data that Macie has found in the bucket. |
| sensitivityScoreOverridden | boolean | False | Specifies whether the bucket's current sensitivity score was set manually. If this value is `true`, the score was manually changed to `100`. If this value is `false`, the score was calculated automatically by Amazon Macie. |
| statistics | [ResourceStatistics](#resource-profiles-model-resourcestatistics) | True | The sensitive data discovery statistics for the bucket. The statistics capture the results of automated sensitive data discovery activities that Amazon Macie has performed for the bucket. |

### InternalServerException
<a name="resource-profiles-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="resource-profiles-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceStatistics
<a name="resource-profiles-model-resourcestatistics"></a>

Provides statistical data for sensitive data discovery metrics that apply to an S3 bucket that Amazon Macie monitors and analyzes for an account, if automated sensitive data discovery has been enabled for the account. The data captures the results of automated sensitive data discovery activities that Macie has performed for the bucket.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| totalBytesClassified | integer<br />Format: int64 | False | The total amount of data, in bytes, that Amazon Macie has analyzed in the bucket. |
| totalDetections | integer<br />Format: int64 | False | The total number of occurrences of sensitive data that Amazon Macie has found in the bucket's objects. This includes occurrences that are currently suppressed by the sensitivity scoring settings for the bucket (`totalDetectionsSuppressed`). |
| totalDetectionsSuppressed | integer<br />Format: int64 | False | The total number of occurrences of sensitive data that are currently suppressed by the sensitivity scoring settings for the bucket. These represent occurrences of sensitive data that Amazon Macie found in the bucket's objects, but the occurrences were manually suppressed. By default, suppressed occurrences are excluded from the bucket's sensitivity score. |
| totalItemsClassified | integer<br />Format: int64 | False | The total number of objects that Amazon Macie has analyzed in the bucket. |
| totalItemsSensitive | integer<br />Format: int64 | False | The total number of the bucket's objects that Amazon Macie has found sensitive data in. |
| totalItemsSkipped | integer<br />Format: int64 | False | The total number of objects that Amazon Macie wasn't able to analyze in the bucket due to an object-level issue or error. For example, an object is a malformed file. This value includes objects that Macie wasn't able to analyze for reasons reported by other statistics in the `ResourceStatistics` object. |
| totalItemsSkippedInvalidEncryption | integer<br />Format: int64 | False | The total number of objects that Amazon Macie wasn't able to analyze in the bucket because the objects are encrypted with a key that Macie can't access. The objects use server-side encryption with customer-provided keys (SSE-C). |
| totalItemsSkippedInvalidKms | integer<br />Format: int64 | False | The total number of objects that Amazon Macie wasn't able to analyze in the bucket because the objects are encrypted with AWS KMS keys that were disabled, are scheduled for deletion, or were deleted. |
| totalItemsSkippedPermissionDenied | integer<br />Format: int64 | False | The total number of objects that Amazon Macie wasn't able to analyze in the bucket due to the permissions settings for the objects or the permissions settings for the keys that were used to encrypt the objects. |

### ServiceQuotaExceededException
<a name="resource-profiles-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="resource-profiles-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UpdateResourceProfileRequest
<a name="resource-profiles-model-updateresourceprofilerequest"></a>

Specifies a new sensitivity score for an S3 bucket that Amazon Macie monitors and analyzes for an account. To update the score, automated sensitive data discovery must be enabled for the account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sensitivityScoreOverride | integer<br />Format: int32 | False | The new sensitivity score for the bucket. Valid values are: `100`, assign the maximum score and apply the *Sensitive* label to the bucket; and, null (empty), assign a score that Amazon Macie calculates automatically after you submit the request. |

### ValidationException
<a name="resource-profiles-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="resource-profiles-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetResourceProfile
<a name="GetResourceProfile-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetResourceProfile)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetResourceProfile)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetResourceProfile)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetResourceProfile)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetResourceProfile)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetResourceProfile)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetResourceProfile)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetResourceProfile)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/GetResourceProfile)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetResourceProfile)

### UpdateResourceProfile
<a name="UpdateResourceProfile-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/UpdateResourceProfile)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/UpdateResourceProfile)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/UpdateResourceProfile)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/UpdateResourceProfile)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/UpdateResourceProfile)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/UpdateResourceProfile)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/UpdateResourceProfile)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/UpdateResourceProfile)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/UpdateResourceProfile)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/UpdateResourceProfile)
