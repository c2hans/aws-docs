---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/findingsfilters-id.html
---

# Findings Filter
<a name="findingsfilters-id"></a>

The Findings Filter resource represents an individual filter that you created and saved to review, analyze, and manage findings. A *findings filter*, also referred to as a *filter*, is a set of criteria that specifies which findings to include in the results of a query for findings. A findings filter can also perform specific actions on findings that match the filter's criteria. For example, you can configure a filter to suppress (automatically archive) findings that match the filter's criteria. For more information about creating and using filters, see [Filtering findings](https://docs.aws.amazon.com/macie/latest/user/findings-filter-overview.html) in the *Amazon Macie User Guide*.

You can use the Findings Filter resource to update, delete, or retrieve detailed information about a findings filter. To create a new filter, use the [Findings Filters](findingsfilters.md) resource.

## URI
<a name="findingsfilters-id-url"></a>

`/findingsfilters/{{id}}`

## HTTP methods
<a name="findingsfilters-id-http-methods"></a>

### DELETE
<a name="findingsfilters-iddelete"></a>

**Operation ID:** `DeleteFindingsFilter`

Deletes a findings filter.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Empty Schema | The request succeeded. The specified findings filter was deleted and there isn't any content to include in the body of the response (No Content). |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### GET
<a name="findingsfilters-idget"></a>

**Operation ID:** `GetFindingsFilter`

Retrieves the criteria and other settings for a findings filter.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetFindingsFilterResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### PATCH
<a name="findingsfilters-idpatch"></a>

**Operation ID:** `UpdateFindingsFilter`

Updates the criteria and other settings for a findings filter.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateFindingsFilterResponse | The request succeeded. The specified findings filter was updated. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="findingsfilters-id-schemas"></a>

### Request bodies
<a name="findingsfilters-id-request-examples"></a>

#### PATCH schema
<a name="findingsfilters-id-request-body-patch-example"></a>

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
  "position": integer
}
```

### Response bodies
<a name="findingsfilters-id-response-examples"></a>

#### Empty Schema schema
<a name="findingsfilters-id-response-body-empty-example"></a>

```
{
}
```

#### GetFindingsFilterResponse schema
<a name="findingsfilters-id-response-body-getfindingsfilterresponse-example"></a>

```
{
  "action": enum,
  "arn": "string",
  "description": "string",
  "findingCriteria": {
    "criterion": {
    }
  },
  "id": "string",
  "name": "string",
  "position": integer,
  "tags": {
  }
}
```

#### UpdateFindingsFilterResponse schema
<a name="findingsfilters-id-response-body-updatefindingsfilterresponse-example"></a>

```
{
  "arn": "string",
  "id": "string"
}
```

#### ValidationException schema
<a name="findingsfilters-id-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="findingsfilters-id-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="findingsfilters-id-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="findingsfilters-id-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="findingsfilters-id-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="findingsfilters-id-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="findingsfilters-id-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="findingsfilters-id-properties"></a>

### AccessDeniedException
<a name="findingsfilters-id-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="findingsfilters-id-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Criterion
<a name="findingsfilters-id-model-criterion"></a>

Specifies a condition that defines a property, operator, and one or more values to filter the results of a query for findings. The number of values depends on the property and operator specified by the condition. For information about defining filter conditions, see [Fundamentals of filtering findings](https://docs.aws.amazon.com/macie/latest/user/findings-filter-basics.html) in the *Amazon Macie User Guide*.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | object | False |  |

### CriterionAdditionalProperties
<a name="findingsfilters-id-model-criterionadditionalproperties"></a>

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

### Empty
<a name="findingsfilters-id-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### FindingCriteria
<a name="findingsfilters-id-model-findingcriteria"></a>

Specifies, as a map, one or more property-based conditions that filter the results of a query for findings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| criterion | [Criterion](#findingsfilters-id-model-criterion) | False | A condition that specifies the property, operator, and one or more values to use to filter the results. |

### FindingsFilterAction
<a name="findingsfilters-id-model-findingsfilteraction"></a>

The action to perform on findings that match the filter criteria. To suppress (automatically archive) findings that match the criteria, set this value to `ARCHIVE`. Valid values are:
+ `ARCHIVE`
+ `NOOP`

### GetFindingsFilterResponse
<a name="findingsfilters-id-model-getfindingsfilterresponse"></a>

Provides information about the criteria and other settings for a findings filter.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| action | [FindingsFilterAction](#findingsfilters-id-model-findingsfilteraction) | False | The action that's performed on findings that match the filter criteria (`findingCriteria`). Possible values are: `ARCHIVE`, suppress (automatically archive) the findings; and, `NOOP`, don't perform any action on the findings. |
| arn | string | False | The Amazon Resource Name (ARN) of the filter. |
| description | string | False | The custom description of the filter. |
| findingCriteria | [FindingCriteria](#findingsfilters-id-model-findingcriteria) | False | The criteria that's used to filter findings. |
| id | string | False | The unique identifier for the filter. |
| name | string | False | The custom name of the filter. |
| position | integer<br />Format: int32 | False | The position of the filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings. |
| tags | [TagMap](#findingsfilters-id-model-tagmap) | False | A map of key-value pairs that specifies which tags (keys and values) are associated with the filter. |

### InternalServerException
<a name="findingsfilters-id-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="findingsfilters-id-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="findingsfilters-id-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### TagMap
<a name="findingsfilters-id-model-tagmap"></a>

A string-to-string map of key-value pairs that specifies the tags (keys and values) for an Amazon Macie resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### ThrottlingException
<a name="findingsfilters-id-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UpdateFindingsFilterRequest
<a name="findingsfilters-id-model-updatefindingsfilterrequest"></a>

Specifies the criteria and other settings for a findings filter.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| action | [FindingsFilterAction](#findingsfilters-id-model-findingsfilteraction) | False | The action to perform on findings that match the filter criteria (`findingCriteria`). Valid values are: `ARCHIVE`, suppress (automatically archive) the findings; and, `NOOP`, don't perform any action on the findings. |
| clientToken | string | False | A unique, case-sensitive token that you provide to ensure the idempotency of the request. |
| description | string | False | A custom description of the filter. The description can contain as many as 512 characters.<br />We strongly recommend that you avoid including any sensitive data in the description of a filter. Other users of your account might be able to see this description, depending on the actions that they're allowed to perform in Amazon Macie. |
| findingCriteria | [FindingCriteria](#findingsfilters-id-model-findingcriteria) | False | The criteria to use to filter findings. |
| name | string | False | A custom name for the filter. The name must contain at least 3 characters and can contain as many as 64 characters.<br />We strongly recommend that you avoid including any sensitive data in the name of a filter. Other users of your account might be able to see this name, depending on the actions that they're allowed to perform in Amazon Macie. |
| position | integer<br />Format: int32 | False | The position of the filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings. |

### UpdateFindingsFilterResponse
<a name="findingsfilters-id-model-updatefindingsfilterresponse"></a>

Provides information about a findings filter that was updated in response to a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) of the filter that was updated. |
| id | string | False | The unique identifier for the filter that was updated. |

### ValidationException
<a name="findingsfilters-id-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="findingsfilters-id-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteFindingsFilter
<a name="DeleteFindingsFilter-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/DeleteFindingsFilter)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/DeleteFindingsFilter)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/DeleteFindingsFilter)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/DeleteFindingsFilter)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/DeleteFindingsFilter)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/DeleteFindingsFilter)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/DeleteFindingsFilter)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/DeleteFindingsFilter)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/DeleteFindingsFilter)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/DeleteFindingsFilter)

### GetFindingsFilter
<a name="GetFindingsFilter-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetFindingsFilter)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetFindingsFilter)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetFindingsFilter)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetFindingsFilter)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetFindingsFilter)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetFindingsFilter)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetFindingsFilter)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetFindingsFilter)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/GetFindingsFilter)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetFindingsFilter)

### UpdateFindingsFilter
<a name="UpdateFindingsFilter-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/UpdateFindingsFilter)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/UpdateFindingsFilter)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/UpdateFindingsFilter)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/UpdateFindingsFilter)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/UpdateFindingsFilter)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/UpdateFindingsFilter)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/UpdateFindingsFilter)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/UpdateFindingsFilter)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/UpdateFindingsFilter)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/UpdateFindingsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Macie. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query macie` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
