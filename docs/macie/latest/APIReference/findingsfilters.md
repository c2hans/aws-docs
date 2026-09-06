---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/findingsfilters.html
---

# Findings Filters
<a name="findingsfilters"></a>

The Findings Filters resource represents the repository of filters that you create and save to review, analyze, and manage findings. A *findings filter*, also referred to as a *filter*, is a set of criteria that specifies which findings to include in the results of a query for findings. A findings filter can also perform specific actions on findings that match the filter's criteria. For example, you can configure a filter to suppress (automatically archive) findings that match the filter's criteria. For more information about creating and using filters, see [Filtering findings](https://docs.aws.amazon.com/macie/latest/user/findings-filter-overview.html) in the *Amazon Macie User Guide*.

You can use the Findings Filters resource to create a new filter or retrieve information about all the existing filters for your Amazon Macie account. To update, delete, or retrieve detailed information about an individual filter, use the [Findings Filter](findingsfilters-id.md) resource.

## URI
<a name="findingsfilters-url"></a>

`/findingsfilters`

## HTTP methods
<a name="findingsfilters-http-methods"></a>

### GET
<a name="findingsfiltersget"></a>

**Operation ID:** `ListFindingsFilters`

Retrieves a subset of information about all the findings filters for an account.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The `nextToken` string that specifies which page of results to return in a paginated response. |
| maxResults | String | False | The maximum number of items to include in each page of a paginated response. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListFindingsFiltersResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### POST
<a name="findingsfilterspost"></a>

**Operation ID:** `CreateFindingsFilter`

Creates and defines the criteria and other settings for a findings filter.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateFindingsFilterResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="findingsfilters-schemas"></a>

### Request bodies
<a name="findingsfilters-request-examples"></a>

#### POST schema
<a name="findingsfilters-request-body-post-example"></a>

```
{
  "action": enum,
  "clientToken": "string",
  "description": "string",
  "findingCriteria": {
    "criterion": {
    }
  },
  "name": "string",
  "position": integer,
  "tags": {
  }
}
```

### Response bodies
<a name="findingsfilters-response-examples"></a>

#### ListFindingsFiltersResponse schema
<a name="findingsfilters-response-body-listfindingsfiltersresponse-example"></a>

```
{
  "findingsFilterListItems": [
    {
      "action": enum,
      "arn": "string",
      "id": "string",
      "name": "string",
      "tags": {
      }
    }
  ],
  "nextToken": "string"
}
```

#### CreateFindingsFilterResponse schema
<a name="findingsfilters-response-body-createfindingsfilterresponse-example"></a>

```
{
  "arn": "string",
  "id": "string"
}
```

#### ValidationException schema
<a name="findingsfilters-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="findingsfilters-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="findingsfilters-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="findingsfilters-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="findingsfilters-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="findingsfilters-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="findingsfilters-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="findingsfilters-properties"></a>

### AccessDeniedException
<a name="findingsfilters-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="findingsfilters-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### CreateFindingsFilterRequest
<a name="findingsfilters-model-createfindingsfilterrequest"></a>

Specifies the criteria and other settings for a new findings filter.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| action | [FindingsFilterAction](#findingsfilters-model-findingsfilteraction) | True | The action to perform on findings that match the filter criteria (`findingCriteria`). Valid values are: `ARCHIVE`, suppress (automatically archive) the findings; and, `NOOP`, don't perform any action on the findings. |
| clientToken | string | False | A unique, case-sensitive token that you provide to ensure the idempotency of the request. |
| description | string | False | A custom description of the filter. The description can contain as many as 512 characters.<br />We strongly recommend that you avoid including any sensitive data in the description of a filter. Other users of your account might be able to see this description, depending on the actions that they're allowed to perform in Amazon Macie. |
| findingCriteria | [FindingCriteria](#findingsfilters-model-findingcriteria) | True | The criteria to use to filter findings. |
| name | string | True | A custom name for the filter. The name must contain at least 3 characters and can contain as many as 64 characters.<br />We strongly recommend that you avoid including any sensitive data in the name of a filter. Other users of your account might be able to see this name, depending on the actions that they're allowed to perform in Amazon Macie. |
| position | integer<br />Format: int32 | False | The position of the filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings. |
| tags | [TagMap](#findingsfilters-model-tagmap) | False | A map of key-value pairs that specifies the tags to associate with the filter.<br />A findings filter can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters. |

### CreateFindingsFilterResponse
<a name="findingsfilters-model-createfindingsfilterresponse"></a>

Provides information about a findings filter that was created in response to a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) of the filter that was created. |
| id | string | False | The unique identifier for the filter that was created. |

### Criterion
<a name="findingsfilters-model-criterion"></a>

Specifies a condition that defines a property, operator, and one or more values to filter the results of a query for findings. The number of values depends on the property and operator specified by the condition. For information about defining filter conditions, see [Fundamentals of filtering findings](https://docs.aws.amazon.com/macie/latest/user/findings-filter-basics.html) in the *Amazon Macie User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | object | False |  |

### CriterionAdditionalProperties
<a name="findingsfilters-model-criterionadditionalproperties"></a>

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
<a name="findingsfilters-model-findingcriteria"></a>

Specifies, as a map, one or more property-based conditions that filter the results of a query for findings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| criterion | [Criterion](#findingsfilters-model-criterion) | False | A condition that specifies the property, operator, and one or more values to use to filter the results. |

### FindingsFilterAction
<a name="findingsfilters-model-findingsfilteraction"></a>

The action to perform on findings that match the filter criteria. To suppress (automatically archive) findings that match the criteria, set this value to `ARCHIVE`. Valid values are:
+ `ARCHIVE`
+ `NOOP`

### FindingsFilterListItem
<a name="findingsfilters-model-findingsfilterlistitem"></a>

Provides information about a findings filter.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| action | [FindingsFilterAction](#findingsfilters-model-findingsfilteraction) | False | The action that's performed on findings that match the filter criteria. Possible values are: `ARCHIVE`, suppress (automatically archive) the findings; and, `NOOP`, don't perform any action on the findings. |
| arn | string | False | The Amazon Resource Name (ARN) of the filter. |
| id | string | False | The unique identifier for the filter. |
| name | string | False | The custom name of the filter. |
| tags | [TagMap](#findingsfilters-model-tagmap) | False | A map of key-value pairs that specifies which tags (keys and values) are associated with the filter. |

### InternalServerException
<a name="findingsfilters-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ListFindingsFiltersResponse
<a name="findingsfilters-model-listfindingsfiltersresponse"></a>

Provides information about all the findings filters for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| findingsFilterListItems | Array of type [FindingsFilterListItem](#findingsfilters-model-findingsfilterlistitem) | False | An array of objects, one for each filter that's associated with the account. |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### ResourceNotFoundException
<a name="findingsfilters-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="findingsfilters-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### TagMap
<a name="findingsfilters-model-tagmap"></a>

A string-to-string map of key-value pairs that specifies the tags (keys and values) for an Amazon Macie resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### ThrottlingException
<a name="findingsfilters-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="findingsfilters-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="findingsfilters-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListFindingsFilters
<a name="ListFindingsFilters-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/ListFindingsFilters)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/ListFindingsFilters)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/ListFindingsFilters)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/ListFindingsFilters)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/ListFindingsFilters)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/ListFindingsFilters)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/ListFindingsFilters)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/ListFindingsFilters)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/ListFindingsFilters)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/ListFindingsFilters)

### CreateFindingsFilter
<a name="CreateFindingsFilter-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/CreateFindingsFilter)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/CreateFindingsFilter)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/CreateFindingsFilter)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/CreateFindingsFilter)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/CreateFindingsFilter)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/CreateFindingsFilter)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/CreateFindingsFilter)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/CreateFindingsFilter)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/CreateFindingsFilter)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/CreateFindingsFilter)
