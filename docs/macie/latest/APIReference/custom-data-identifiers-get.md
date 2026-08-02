---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/custom-data-identifiers-get.html
---

# Custom Data Identifier Descriptions
<a name="custom-data-identifiers-get"></a>

The Custom Data Identifier Descriptions resource provides information about the custom data identifiers for your Amazon Macie account. A *custom data identifier* is a set of criteria that you define to detect sensitive data in a data source.

You can use this resource to retrieve a subset of information about one or more custom data identifiers for your account. To refine your request, you can use the supported request parameter to specify which custom data identifiers to retrieve information about. To retrieve detailed information about the detection criteria and other settings for an individual custom data identifier, use the [Custom Data Identifier](custom-data-identifiers-id.md) resource.

## URI
<a name="custom-data-identifiers-get-url"></a>

`/custom-data-identifiers/get`

## HTTP methods
<a name="custom-data-identifiers-get-http-methods"></a>

### POST
<a name="custom-data-identifiers-getpost"></a>

**Operation ID:** `BatchGetCustomDataIdentifiers`

Retrieves information about one or more custom data identifiers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | BatchGetCustomDataIdentifiersResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="custom-data-identifiers-get-schemas"></a>

### Request bodies
<a name="custom-data-identifiers-get-request-examples"></a>

#### POST schema
<a name="custom-data-identifiers-get-request-body-post-example"></a>

```
{
  "ids": [
    "string"
  ]
}
```

### Response bodies
<a name="custom-data-identifiers-get-response-examples"></a>

#### BatchGetCustomDataIdentifiersResponse schema
<a name="custom-data-identifiers-get-response-body-batchgetcustomdataidentifiersresponse-example"></a>

```
{
  "customDataIdentifiers": [
    {
      "arn": "string",
      "createdAt": "string",
      "deleted": boolean,
      "description": "string",
      "id": "string",
      "name": "string"
    }
  ],
  "notFoundIdentifierIds": [
    "string"
  ]
}
```

#### ValidationException schema
<a name="custom-data-identifiers-get-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="custom-data-identifiers-get-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="custom-data-identifiers-get-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="custom-data-identifiers-get-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="custom-data-identifiers-get-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="custom-data-identifiers-get-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="custom-data-identifiers-get-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="custom-data-identifiers-get-properties"></a>

### AccessDeniedException
<a name="custom-data-identifiers-get-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### BatchGetCustomDataIdentifierSummary
<a name="custom-data-identifiers-get-model-batchgetcustomdataidentifiersummary"></a>

Provides information about a custom data identifier.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) of the custom data identifier. |
| createdAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the custom data identifier was created. |
| deleted | boolean | False | Specifies whether the custom data identifier was deleted. If you delete a custom data identifier, Amazon Macie doesn't delete it permanently. Instead, Macie soft deletes the identifier. |
| description | string | False | The custom description of the custom data identifier. |
| id | string | False | The unique identifier for the custom data identifier. |
| name | string | False | The custom name of the custom data identifier. |

### BatchGetCustomDataIdentifiersRequest
<a name="custom-data-identifiers-get-model-batchgetcustomdataidentifiersrequest"></a>

Specifies one or more custom data identifiers to retrieve information about.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ids | Array of type string | False | An array of custom data identifier IDs, one for each custom data identifier to retrieve information about. |

### BatchGetCustomDataIdentifiersResponse
<a name="custom-data-identifiers-get-model-batchgetcustomdataidentifiersresponse"></a>

Provides information about one or more custom data identifiers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| customDataIdentifiers | Array of type [BatchGetCustomDataIdentifierSummary](#custom-data-identifiers-get-model-batchgetcustomdataidentifiersummary) | False | An array of objects, one for each custom data identifier that matches the criteria specified in the request. |
| notFoundIdentifierIds | Array of type string | False | An array of custom data identifier IDs, one for each custom data identifier that was specified in the request but doesn't correlate to an existing custom data identifier. |

### ConflictException
<a name="custom-data-identifiers-get-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### InternalServerException
<a name="custom-data-identifiers-get-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="custom-data-identifiers-get-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="custom-data-identifiers-get-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="custom-data-identifiers-get-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="custom-data-identifiers-get-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="custom-data-identifiers-get-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### BatchGetCustomDataIdentifiers
<a name="BatchGetCustomDataIdentifiers-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/BatchGetCustomDataIdentifiers)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/BatchGetCustomDataIdentifiers)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/BatchGetCustomDataIdentifiers)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/BatchGetCustomDataIdentifiers)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/BatchGetCustomDataIdentifiers)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/BatchGetCustomDataIdentifiers)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/BatchGetCustomDataIdentifiers)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/BatchGetCustomDataIdentifiers)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/BatchGetCustomDataIdentifiers)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/BatchGetCustomDataIdentifiers)
