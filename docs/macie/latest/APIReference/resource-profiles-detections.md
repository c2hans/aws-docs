---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/resource-profiles-detections.html
---

# Resource Sensitivity Profile - Detections
<a name="resource-profiles-detections"></a>

The Resource Sensitivity Profile Detections resource provides information about the types and amount of sensitive data that Amazon Macie has found in individual Amazon Simple Storage Service (Amazon S3) buckets for your account. If you're the Macie administrator for an organization, this includes S3 buckets that your member accounts own.

For each S3 bucket, the information includes an inventory of the types of sensitive data that Macie has found and the number of occurrences of each type. It also includes details about the custom data identifier or managed data identifier that detected each type. The information captures the results of automated sensitive data discovery activities that Macie has performed for an S3 bucket. For more information, see [Performing automated sensitive data discovery](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd.html) in the *Amazon Macie User Guide*.

This resource also provides access to the sensitivity scoring settings for individual S3 buckets. By default, Macie calculates a bucket's sensitivity score based partly on the amount of sensitive data that Macie has found in a bucket. If you're a Macie administrator or you have a standalone Macie account, you can optionally adjust these calculations by excluding (*suppressing*) or including specific types of sensitive data in a bucket's score.

You can use the Resource Sensitivity Profile Detections resource to retrieve information about the types and amount of sensitive data that Macie has found in an S3 bucket. If you're a Macie administrator or you have a standalone Macie account, you can also use this resource to adjust the sensitivity scoring settings for a bucket.

To use this resource, you must first enable automated sensitive data discovery. To enable it for an organization or a standalone account, use the [Configuration](automated-discovery-configuration.md) resource for automated sensitive data discovery. To enable it for a member account in an organization, use the [Accounts](automated-discovery-accounts.md) resource for automated sensitive data discovery.

## URI
<a name="resource-profiles-detections-url"></a>

`/resource-profiles/detections`

## HTTP methods
<a name="resource-profiles-detections-http-methods"></a>

### GET
<a name="resource-profiles-detectionsget"></a>

**Operation ID:** `ListResourceProfileDetections`

Retrieves information about the types and amount of sensitive data that Amazon Macie found in an S3 bucket.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| resourceArn | String | True | The Amazon Resource Name (ARN) of the S3 bucket that the request applies to. |
| nextToken | String | False | The `nextToken` string that specifies which page of results to return in a paginated response. |
| maxResults | String | False | The maximum number of items to include in each page of a paginated response. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListResourceProfileDetectionsResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### PATCH
<a name="resource-profiles-detectionspatch"></a>

**Operation ID:** `UpdateResourceProfileDetections`

Updates the sensitivity scoring settings for an S3 bucket.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| resourceArn | String | True | The Amazon Resource Name (ARN) of the S3 bucket that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Empty Schema | The request succeeded. The settings were updated and there isn't any content to include in the body of the response (No Content). |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="resource-profiles-detections-schemas"></a>

### Request bodies
<a name="resource-profiles-detections-request-examples"></a>

#### PATCH schema
<a name="resource-profiles-detections-request-body-patch-example"></a>

```
{
  "suppressDataIdentifiers": [
    {
      "id": "string",
      "type": enum
    }
  ]
}
```

### Response bodies
<a name="resource-profiles-detections-response-examples"></a>

#### ListResourceProfileDetectionsResponse schema
<a name="resource-profiles-detections-response-body-listresourceprofiledetectionsresponse-example"></a>

```
{
  "detections": [
    {
      "arn": "string",
      "count": integer,
      "id": "string",
      "name": "string",
      "suppressed": boolean,
      "type": enum
    }
  ],
  "nextToken": "string"
}
```

#### Empty Schema schema
<a name="resource-profiles-detections-response-body-empty-example"></a>

```
{
}
```

#### ValidationException schema
<a name="resource-profiles-detections-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="resource-profiles-detections-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="resource-profiles-detections-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="resource-profiles-detections-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="resource-profiles-detections-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="resource-profiles-detections-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="resource-profiles-detections-properties"></a>

### AccessDeniedException
<a name="resource-profiles-detections-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### DataIdentifierType
<a name="resource-profiles-detections-model-dataidentifiertype"></a>

The type of data identifier that detected a specific type of sensitive data in an S3 bucket. Possible values are:
+ `CUSTOM`
+ `MANAGED`

### Detection
<a name="resource-profiles-detections-model-detection"></a>

Provides information about a type of sensitive data that Amazon Macie found in an S3 bucket while performing automated sensitive data discovery for an account. The information also specifies the custom or managed data identifier that detected the data. This information is available only if automated sensitive data discovery has been enabled for the account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | If the sensitive data was detected by a custom data identifier, the Amazon Resource Name (ARN) of the custom data identifier that detected the data. Otherwise, this value is null. |
| count | integer<br />Format: int64 | False | The total number of occurrences of the sensitive data. |
| id | string | False | The unique identifier for the custom data identifier or managed data identifier that detected the sensitive data. For additional details about a specified managed data identifier, see [Using managed data identifiers](https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html) in the *Amazon Macie User Guide*. |
| name | string | False | The name of the custom data identifier or managed data identifier that detected the sensitive data. For a managed data identifier, this value is the same as the unique identifier (`id`). |
| suppressed | boolean | False | Specifies whether occurrences of this type of sensitive data are excluded (`true`) or included (`false`) in the bucket's sensitivity score, if the score is calculated by Amazon Macie. |
| type | [DataIdentifierType](#resource-profiles-detections-model-dataidentifiertype) | False | The type of data identifier that detected the sensitive data. Possible values are: `CUSTOM`, for a custom data identifier; and, `MANAGED`, for a managed data identifier. |

### Empty
<a name="resource-profiles-detections-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### InternalServerException
<a name="resource-profiles-detections-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ListResourceProfileDetectionsResponse
<a name="resource-profiles-detections-model-listresourceprofiledetectionsresponse"></a>

Provides information about the types and amount of sensitive data that Amazon Macie found in an S3 bucket while performing automated sensitive data discovery for an account. This information is available only if automated sensitive data discovery has been enabled for the account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| detections | Array of type [Detection](#resource-profiles-detections-model-detection) | True | An array of objects, one for each type of sensitive data that Amazon Macie found in the bucket. Each object reports the number of occurrences of the specified type and provides information about the custom data identifier or managed data identifier that detected the data. |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### ResourceNotFoundException
<a name="resource-profiles-detections-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="resource-profiles-detections-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### SuppressDataIdentifier
<a name="resource-profiles-detections-model-suppressdataidentifier"></a>

Specifies a custom data identifier or managed data identifier that detected a type of sensitive data to exclude from an S3 bucket's sensitivity score.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | The unique identifier for the custom data identifier or managed data identifier that detected the type of sensitive data to exclude from the score. |
| type | [DataIdentifierType](#resource-profiles-detections-model-dataidentifiertype) | False | The type of data identifier that detected the sensitive data. Possible values are: `CUSTOM`, for a custom data identifier; and, `MANAGED`, for a managed data identifier. |

### ThrottlingException
<a name="resource-profiles-detections-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UpdateResourceProfileDetectionsRequest
<a name="resource-profiles-detections-model-updateresourceprofiledetectionsrequest"></a>

Updates the sensitivity scoring settings for an S3 bucket that Amazon Macie monitors and analyzes for an account. The settings specify types of sensitive data to exclude from the sensitivity score that Macie calculates for the bucket. To update the settings, automated sensitive data discovery must be enabled for the account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| suppressDataIdentifiers | Array of type [SuppressDataIdentifier](#resource-profiles-detections-model-suppressdataidentifier) | False | An array of objects, one for each custom data identifier or managed data identifier that detected a type of sensitive data to exclude from the bucket's score. To include all sensitive data types in the score, don't specify any values for this array. |

### ValidationException
<a name="resource-profiles-detections-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="resource-profiles-detections-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListResourceProfileDetections
<a name="ListResourceProfileDetections-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/ListResourceProfileDetections)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/ListResourceProfileDetections)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/ListResourceProfileDetections)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/ListResourceProfileDetections)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/ListResourceProfileDetections)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/ListResourceProfileDetections)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/ListResourceProfileDetections)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/ListResourceProfileDetections)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/ListResourceProfileDetections)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/ListResourceProfileDetections)

### UpdateResourceProfileDetections
<a name="UpdateResourceProfileDetections-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/UpdateResourceProfileDetections)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/UpdateResourceProfileDetections)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/UpdateResourceProfileDetections)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/UpdateResourceProfileDetections)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/UpdateResourceProfileDetections)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/UpdateResourceProfileDetections)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/UpdateResourceProfileDetections)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/UpdateResourceProfileDetections)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/UpdateResourceProfileDetections)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/UpdateResourceProfileDetections)
