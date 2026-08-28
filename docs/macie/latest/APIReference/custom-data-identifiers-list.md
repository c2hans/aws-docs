---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/custom-data-identifiers-list.html
---

# Custom Data Identifier List
<a name="custom-data-identifiers-list"></a>

The Custom Data Identifier List resource represents the repository of custom data identifiers for your Amazon Macie account. A *custom data identifier* is a set of criteria that you define to detect sensitive data in a data source.

You can use this resource to retrieve a subset of information about the custom data identifiers for your account. To retrieve detailed information about the detection criteria and other settings for an individual custom data identifier, use the [Custom Data Identifier](custom-data-identifiers-id.md) resource.

## URI
<a name="custom-data-identifiers-list-url"></a>

`/custom-data-identifiers/list`

## HTTP methods
<a name="custom-data-identifiers-list-http-methods"></a>

### POST
<a name="custom-data-identifiers-listpost"></a>

**Operation ID:** `ListCustomDataIdentifiers`

Retrieves a subset of information about the custom data identifiers for an account.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListCustomDataIdentifiersResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="custom-data-identifiers-list-schemas"></a>

### Request bodies
<a name="custom-data-identifiers-list-request-examples"></a>

#### POST schema
<a name="custom-data-identifiers-list-request-body-post-example"></a>

```
{
  "maxResults": integer,
  "nextToken": "string"
}
```

### Response bodies
<a name="custom-data-identifiers-list-response-examples"></a>

#### ListCustomDataIdentifiersResponse schema
<a name="custom-data-identifiers-list-response-body-listcustomdataidentifiersresponse-example"></a>

```
{
  "items": [
    {
      "arn": "string",
      "createdAt": "string",
      "description": "string",
      "id": "string",
      "name": "string"
    }
  ],
  "nextToken": "string"
}
```

#### ValidationException schema
<a name="custom-data-identifiers-list-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="custom-data-identifiers-list-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="custom-data-identifiers-list-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="custom-data-identifiers-list-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="custom-data-identifiers-list-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="custom-data-identifiers-list-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="custom-data-identifiers-list-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="custom-data-identifiers-list-properties"></a>

### AccessDeniedException
<a name="custom-data-identifiers-list-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="custom-data-identifiers-list-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### CustomDataIdentifierSummary
<a name="custom-data-identifiers-list-model-customdataidentifiersummary"></a>

Provides information about a custom data identifier.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) of the custom data identifier. |
| createdAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the custom data identifier was created. |
| description | string | False | The custom description of the custom data identifier. |
| id | string | False | The unique identifier for the custom data identifier. |
| name | string | False | The custom name of the custom data identifier. |

### InternalServerException
<a name="custom-data-identifiers-list-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ListCustomDataIdentifiersRequest
<a name="custom-data-identifiers-list-model-listcustomdataidentifiersrequest"></a>

Specifies criteria for paginating the results of a request for information about custom data identifiers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| maxResults | integer<br />Format: int32 | False | The maximum number of items to include in each page of the response. |
| nextToken | string | False | The `nextToken` string that specifies which page of results to return in a paginated response. |

### ListCustomDataIdentifiersResponse
<a name="custom-data-identifiers-list-model-listcustomdataidentifiersresponse"></a>

Provides the results of a request for information about custom data identifiers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [CustomDataIdentifierSummary](#custom-data-identifiers-list-model-customdataidentifiersummary) | False | An array of objects, one for each custom data identifier. |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### ResourceNotFoundException
<a name="custom-data-identifiers-list-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="custom-data-identifiers-list-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="custom-data-identifiers-list-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="custom-data-identifiers-list-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="custom-data-identifiers-list-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListCustomDataIdentifiers
<a name="ListCustomDataIdentifiers-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/ListCustomDataIdentifiers)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/ListCustomDataIdentifiers)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/ListCustomDataIdentifiers)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/ListCustomDataIdentifiers)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/ListCustomDataIdentifiers)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/ListCustomDataIdentifiers)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/ListCustomDataIdentifiers)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/ListCustomDataIdentifiers)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/ListCustomDataIdentifiers)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/ListCustomDataIdentifiers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Macie. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query macie` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
