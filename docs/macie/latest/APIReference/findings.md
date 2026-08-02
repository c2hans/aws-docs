---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/findings.html
---

# Finding List
<a name="findings"></a>

The Finding List resource provides a subset of information about the findings for your Amazon Macie account. A *finding* is a detailed report of a potential issue with the security or privacy of an Amazon Simple Storage Service (Amazon S3) general purpose bucket or sensitive data in an S3 object.

This resource doesn't provide access to all the data for a finding. Instead, it provides only a subset of metadata, primarily the unique identifier for a finding. To retrieve all the data for one or more findings, use the [Findings](findings-describe.md) resource.

You can use the Finding List resource to retrieve a subset of information about one or more findings for your account. To customize and refine your query, you can use the supported parameters to specify how to filter, sort, and paginate the results. For more information about filter options, see [Filtering findings](https://docs.aws.amazon.com/macie/latest/user/findings-filter-overview.html) in the *Amazon Macie User Guide*.

## URI
<a name="findings-url"></a>

`/findings`

## HTTP methods
<a name="findings-http-methods"></a>

### POST
<a name="findingspost"></a>

**Operation ID:** `ListFindings`

Retrieves a subset of information about one or more findings.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListFindingsResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="findings-schemas"></a>

### Request bodies
<a name="findings-request-examples"></a>

#### POST schema
<a name="findings-request-body-post-example"></a>

```
{
  "findingCriteria": {
    "criterion": {
    }
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
<a name="findings-response-examples"></a>

#### ListFindingsResponse schema
<a name="findings-response-body-listfindingsresponse-example"></a>

```
{
  "findingIds": [
    "string"
  ],
  "nextToken": "string"
}
```

#### ValidationException schema
<a name="findings-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="findings-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="findings-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="findings-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="findings-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="findings-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="findings-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="findings-properties"></a>

### AccessDeniedException
<a name="findings-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="findings-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Criterion
<a name="findings-model-criterion"></a>

Specifies a condition that defines a property, operator, and one or more values to filter the results of a query for findings. The number of values depends on the property and operator specified by the condition. For information about defining filter conditions, see [Fundamentals of filtering findings](https://docs.aws.amazon.com/macie/latest/user/findings-filter-basics.html) in the *Amazon Macie User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | object | False |  |

### CriterionAdditionalProperties
<a name="findings-model-criterionadditionalproperties"></a>

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
<a name="findings-model-findingcriteria"></a>

Specifies, as a map, one or more property-based conditions that filter the results of a query for findings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| criterion | [Criterion](#findings-model-criterion) | False | A condition that specifies the property, operator, and one or more values to use to filter the results. |

### InternalServerException
<a name="findings-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ListFindingsRequest
<a name="findings-model-listfindingsrequest"></a>

Specifies criteria for filtering, sorting, and paginating the results of a request for information about findings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| findingCriteria | [FindingCriteria](#findings-model-findingcriteria) | False | The criteria to use to filter the results. |
| maxResults | integer<br />Format: int32 | False | The maximum number of items to include in each page of the response. |
| nextToken | string | False | The `nextToken` string that specifies which page of results to return in a paginated response. |
| sortCriteria | [SortCriteria](#findings-model-sortcriteria) | False | The criteria to use to sort the results. |

### ListFindingsResponse
<a name="findings-model-listfindingsresponse"></a>

Provides the results of a request for information about one or more findings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| findingIds | Array of type string | False | An array of strings, where each string is the unique identifier for a finding that matches the filter criteria specified in the request. |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### ResourceNotFoundException
<a name="findings-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="findings-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### SortCriteria
<a name="findings-model-sortcriteria"></a>

Specifies criteria for sorting the results of a request for findings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| attributeName | string | False | The name of the property to sort the results by. Valid values are: `count`, `createdAt`, `policyDetails.action.apiCallDetails.firstSeen`, `policyDetails.action.apiCallDetails.lastSeen`, `resourcesAffected`, `severity.score`, `type`, and `updatedAt`. |
| orderBy | string<br />Values: `ASC \| DESC` | False | The sort order to apply to the results, based on the value for the property specified by the `attributeName` property. Valid values are: `ASC`, sort the results in ascending order; and, `DESC`, sort the results in descending order. |

### ThrottlingException
<a name="findings-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="findings-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="findings-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListFindings
<a name="ListFindings-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/ListFindings)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/ListFindings)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/ListFindings)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/ListFindings)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/ListFindings)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/ListFindings)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/ListFindings)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/ListFindings)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/ListFindings)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/ListFindings)
