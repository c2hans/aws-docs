---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/findings-statistics.html
---

# Finding Statistics
<a name="findings-statistics"></a>

The Finding Statistics resource provides aggregated statistical data about the findings for your Amazon Macie account. This primarily includes data about the total number of findings, grouped by a key value such as severity, finding type, or affected resource. The data is available for all the findings that Macie stores for your account.

You can use the Finding Statistics resource to retrieve (query) aggregated statistical data about findings for your account. To customize and refine your query, you can use the supported parameters to specify how to filter, group, and sort the query results. For more information about filter options, see [Filtering findings](https://docs.aws.amazon.com/macie/latest/user/findings-filter-overview.html) in the *Amazon Macie User Guide*.

## URI
<a name="findings-statistics-url"></a>

`/findings/statistics`

## HTTP methods
<a name="findings-statistics-http-methods"></a>

### POST
<a name="findings-statisticspost"></a>

**Operation ID:** `GetFindingStatistics`

Retrieves (queries) aggregated statistical data about findings.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetFindingStatisticsResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="findings-statistics-schemas"></a>

### Request bodies
<a name="findings-statistics-request-examples"></a>

#### POST schema
<a name="findings-statistics-request-body-post-example"></a>

```
{
  "findingCriteria": {
    "criterion": {
    }
  },
  "groupBy": enum,
  "size": integer,
  "sortCriteria": {
    "attributeName": enum,
    "orderBy": enum
  }
}
```

### Response bodies
<a name="findings-statistics-response-examples"></a>

#### GetFindingStatisticsResponse schema
<a name="findings-statistics-response-body-getfindingstatisticsresponse-example"></a>

```
{
  "countsByGroup": [
    {
      "count": integer,
      "groupKey": "string"
    }
  ]
}
```

#### ValidationException schema
<a name="findings-statistics-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="findings-statistics-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="findings-statistics-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="findings-statistics-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="findings-statistics-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="findings-statistics-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="findings-statistics-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="findings-statistics-properties"></a>

### AccessDeniedException
<a name="findings-statistics-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="findings-statistics-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Criterion
<a name="findings-statistics-model-criterion"></a>

Specifies a condition that defines a property, operator, and one or more values to filter the results of a query for findings. The number of values depends on the property and operator specified by the condition. For information about defining filter conditions, see [Fundamentals of filtering findings](https://docs.aws.amazon.com/macie/latest/user/findings-filter-basics.html) in the *Amazon Macie User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | object | False |  |

### CriterionAdditionalProperties
<a name="findings-statistics-model-criterionadditionalproperties"></a>

Specifies the operator to use in a property-based condition that filters the results of a query for findings. For detailed information and examples of each operator, see [Fundamentals of filtering findings](https://docs.aws.amazon.com/macie/latest/user/findings-filter-basics.html) in the *Amazon Macie User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| eq | Array of type string | False | The value for the property matches (equals) the specified value. If you specify multiple values, Macie uses OR logic to join the values. |
| eqExactMatch | Array of type string | False | The value for the property exclusively matches (equals an exact match for) all the specified values. If you specify multiple values, Amazon Macie uses AND logic to join the values.<br />You can use this operator with the following properties: `customDataIdentifiers.detections.arn`, `customDataIdentifiers.detections.name`, `resourcesAffected.s3Bucket.tags.key`, `resourcesAffected.s3Bucket.tags.value`, `resourcesAffected.s3Object.tags.key`, `resourcesAffected.s3Object.tags.value`, `sensitiveData.category`, and `sensitiveData.detections.type`. |
| gt | integer<br />Format: int64 | False | The value for the property is greater than the specified value. |
| gte | integer<br />Format: int64 | False | The value for the property is greater than or equal to the specified value. |
| lt | integer<br />Format: int64 | False | The value for the property is less than the specified value. |
| lte | integer<br />Format: int64 | False | The value for the property is less than or equal to the specified value. |
| neq | Array of type string | False | The value for the property doesn't match (doesn't equal) the specified value. If you specify multiple values, Macie uses OR logic to join the values. |

### FindingCriteria
<a name="findings-statistics-model-findingcriteria"></a>

Specifies, as a map, one or more property-based conditions that filter the results of a query for findings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| criterion | [Criterion](#findings-statistics-model-criterion) | False | A condition that specifies the property, operator, and one or more values to use to filter the results. |

### FindingStatisticsSortAttributeName
<a name="findings-statistics-model-findingstatisticssortattributename"></a>

The grouping to sort the results by. Valid values are:
+ `groupKey`
+ `count`

### FindingStatisticsSortCriteria
<a name="findings-statistics-model-findingstatisticssortcriteria"></a>

Specifies criteria for sorting the results of a query that retrieves aggregated statistical data about findings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| attributeName | [FindingStatisticsSortAttributeName](#findings-statistics-model-findingstatisticssortattributename) | False | The grouping to sort the results by. Valid values are: `count`, sort the results by the number of findings in each group of results; and, `groupKey`, sort the results by the name of each group of results. |
| orderBy | string<br />Values: `ASC \| DESC` | False | The sort order to apply to the results, based on the value for the property specified by the `attributeName` property. Valid values are: `ASC`, sort the results in ascending order; and, `DESC`, sort the results in descending order. |

### GetFindingStatisticsRequest
<a name="findings-statistics-model-getfindingstatisticsrequest"></a>

Specifies criteria for filtering, grouping, sorting, and paginating the results of a query that retrieves aggregated statistical data about findings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| findingCriteria | [FindingCriteria](#findings-statistics-model-findingcriteria) | False | The criteria to use to filter the query results. |
| groupBy | string<br />Values: `resourcesAffected.s3Bucket.name \| type \| classificationDetails.jobId \| severity.description` | True | The finding property to use to group the query results. Valid values are:   `classificationDetails.jobId` - The unique identifier for the classification job that produced the finding.    `resourcesAffected.s3Bucket.name` - The name of the S3 bucket that the finding applies to.    `severity.description` - The severity level of the finding, such as `High` or `Medium`.    `type` - The type of finding, such as `Policy:IAMUser/S3BucketPublic` and `SensitiveData:S3Object/Personal`.   |
| size | integer<br />Format: int32 | False | The maximum number of items to include in each page of the response. |
| sortCriteria | [FindingStatisticsSortCriteria](#findings-statistics-model-findingstatisticssortcriteria) | False | The criteria to use to sort the query results. |

### GetFindingStatisticsResponse
<a name="findings-statistics-model-getfindingstatisticsresponse"></a>

Provides the results of a query that retrieved aggregated statistical data about findings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| countsByGroup | Array of type [GroupCount](#findings-statistics-model-groupcount) | False | An array of objects, one for each group of findings that matches the filter criteria specified in the request. |

### GroupCount
<a name="findings-statistics-model-groupcount"></a>

Provides a group of results for a query that retrieved aggregated statistical data about findings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| count | integer<br />Format: int64 | False | The total number of findings in the group of query results. |
| groupKey | string | False | The name of the property that defines the group in the query results, as specified by the `groupBy` property in the query request. |

### InternalServerException
<a name="findings-statistics-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="findings-statistics-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="findings-statistics-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="findings-statistics-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="findings-statistics-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="findings-statistics-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetFindingStatistics
<a name="GetFindingStatistics-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetFindingStatistics)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetFindingStatistics)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetFindingStatistics)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetFindingStatistics)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetFindingStatistics)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetFindingStatistics)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetFindingStatistics)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetFindingStatistics)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/GetFindingStatistics)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetFindingStatistics)
