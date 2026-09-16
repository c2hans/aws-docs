---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/custom-data-identifiers.html
---

# Custom Data Identifier Creation
<a name="custom-data-identifiers"></a>

A *custom data identifier* is a set of criteria that you define to detect sensitive data in a data source. The criteria consist of a regular expression (*regex*) that defines a text pattern to match and, optionally, character sequences and a proximity rule that refine the analysis of data. The character sequences can be: *keywords*, which are words or phrases that must be in proximity of text that matches the regex, or *ignore words*, which are words or phrases to exclude from results. By using custom data identifiers, you can detect sensitive data that reflects your particular scenarios, intellectual property, or proprietary data. You can supplement the managed data identifiers that Amazon Macie provides.

In addition to detection criteria, you can optionally specify severity levels for findings that a custom data identifier produces. Each severity level is based on the number of occurrences of text that match the custom data identifier's detection criteria. If you don't specify any severity levels for a custom data identifier, Macie automatically assigns the *Medium* severity to all findings that the custom data identifier produces. For more information, see [Building custom data identifiers](https://docs.aws.amazon.com/macie/latest/user/custom-data-identifiers.html) in the *Amazon Macie User Guide*.

You can use the Custom Data Identifier Creation resource to create a new custom data identifier. Note that you can't change a custom data identifier after you create it. This helps to ensure that you have an immutable history of sensitive data findings and discovery results for data privacy and protection audits or investigations. To test and refine a custom data identifier before you create it, use the [Custom Data Identifier Testing](custom-data-identifiers-test.md) resource.

## URI
<a name="custom-data-identifiers-url"></a>

`/custom-data-identifiers`

## HTTP methods
<a name="custom-data-identifiers-http-methods"></a>

### POST
<a name="custom-data-identifierspost"></a>

**Operation ID:** `CreateCustomDataIdentifier`

Creates and defines the criteria and other settings for a custom data identifier.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateCustomDataIdentifierResponse | The request succeeded. The specified custom data identifier was created. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="custom-data-identifiers-schemas"></a>

### Request bodies
<a name="custom-data-identifiers-request-examples"></a>

#### POST schema
<a name="custom-data-identifiers-request-body-post-example"></a>

```
{
  "clientToken": "string",
  "description": "string",
  "ignoreWords": [
    "string"
  ],
  "keywords": [
    "string"
  ],
  "maximumMatchDistance": integer,
  "name": "string",
  "regex": "string",
  "severityLevels": [
    {
      "occurrencesThreshold": integer,
      "severity": enum
    }
  ],
  "tags": {
  }
}
```

### Response bodies
<a name="custom-data-identifiers-response-examples"></a>

#### CreateCustomDataIdentifierResponse schema
<a name="custom-data-identifiers-response-body-createcustomdataidentifierresponse-example"></a>

```
{
  "customDataIdentifierId": "string"
}
```

#### ValidationException schema
<a name="custom-data-identifiers-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="custom-data-identifiers-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="custom-data-identifiers-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="custom-data-identifiers-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="custom-data-identifiers-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="custom-data-identifiers-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="custom-data-identifiers-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="custom-data-identifiers-properties"></a>

### AccessDeniedException
<a name="custom-data-identifiers-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="custom-data-identifiers-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### CreateCustomDataIdentifierRequest
<a name="custom-data-identifiers-model-createcustomdataidentifierrequest"></a>

Specifies the detection criteria and other settings for a custom data identifier. You can't change a custom data identifier after you create it. This helps to ensure that you have an immutable history of sensitive data findings and discovery results for data privacy and protection audits or investigations.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientToken | string | False | A unique, case-sensitive token that you provide to ensure the idempotency of the request. |
| description | string | False | A custom description of the custom data identifier. The description can contain as many as 512 characters.<br />We strongly recommend that you avoid including any sensitive data in the description of a custom data identifier. Other users of your account might be able to access this description, depending on the actions that they're allowed to perform in Amazon Macie. |
| ignoreWords | Array of type string | False | An array that lists specific character sequences (*ignore words*) to exclude from results. If text matches the regular expression but it contains a string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4-90 UTF-8 characters. Ignore words are case sensitive. |
| keywords | Array of type string | False | An array that lists specific character sequences (*keywords*), one of which must precede and be within proximity (`maximumMatchDistance`) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3-90 UTF-8 characters. Keywords aren't case sensitive. |
| maximumMatchDistance | integer<br />Format: int32 | False | The maximum number of characters that can exist between the end of at least one complete character sequence specified by the `keywords` array and the end of text that matches the regular expression. If a complete keyword precedes all the text that matches the regular expression and the keyword is within the specified distance, Amazon Macie includes the result. The distance can be 1-300 characters. The default value is 50. |
| name | string | True | A custom name for the custom data identifier. The name can contain as many as 128 characters.<br />We strongly recommend that you avoid including any sensitive data in the name of a custom data identifier. Other users of your account might be able to access this name, depending on the actions that they're allowed to perform in Amazon Macie. |
| regex | string | True | The regular expression (*regex*) that defines the pattern to match. The expression can contain as many as 512 characters. |
| severityLevels | Array of type [SeverityLevel](#custom-data-identifiers-model-severitylevel) | False | The severity to assign to findings that the custom data identifier produces, based on the number of occurrences of text that match the identifier's detection criteria. You can specify as many as three objects in this array, one for each severity: `LOW`, `MEDIUM`, or `HIGH`. If you specify more than one, the occurrences thresholds must be in ascending order by severity, moving from `LOW` to `HIGH`. For example, `1` for `LOW`, `50` for `MEDIUM`, and `100` for `HIGH`. If an S3 object contains fewer occurrences than the lowest specified threshold, Amazon Macie doesn't create a finding.<br />If you don't specify any values for this array, Macie creates findings for S3 objects that contain at least one occurrence of text that matches the detection criteria, and assigns the `MEDIUM` severity to the findings. |
| tags | [TagMap](#custom-data-identifiers-model-tagmap) | False | A map of key-value pairs that specifies the tags to associate with the custom data identifier.<br />A custom data identifier can have a maximum of 50 tags. Each tag consists of a tag key and an associated tag value. The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters. |

### CreateCustomDataIdentifierResponse
<a name="custom-data-identifiers-model-createcustomdataidentifierresponse"></a>

Provides information about a custom data identifier that was created in response to a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| customDataIdentifierId | string | False | The unique identifier for the custom data identifier that was created. |

### DataIdentifierSeverity
<a name="custom-data-identifiers-model-dataidentifierseverity"></a>

The severity of a finding, ranging from `LOW`, for least severe, to `HIGH`, for most severe. Valid values are:
+ `LOW`
+ `MEDIUM`
+ `HIGH`

### InternalServerException
<a name="custom-data-identifiers-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="custom-data-identifiers-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="custom-data-identifiers-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### SeverityLevel
<a name="custom-data-identifiers-model-severitylevel"></a>

Specifies a severity level for findings that a custom data identifier produces. A severity level determines which severity is assigned to the findings, based on the number of occurrences of text that match the identifier's detection criteria.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| occurrencesThreshold | integer<br />Format: int64 | True | The minimum number of occurrences of text that must match the custom data identifier's detection criteria in order to produce a finding with the specified severity (`severity`). |
| severity | [DataIdentifierSeverity](#custom-data-identifiers-model-dataidentifierseverity) | True | The severity to assign to a finding if the number of occurrences is greater than or equal to the specified threshold (`occurrencesThreshold`) and, if applicable, less than the threshold for the next consecutive severity level moving from `LOW` to `HIGH`. |

### TagMap
<a name="custom-data-identifiers-model-tagmap"></a>

A string-to-string map of key-value pairs that specifies the tags (keys and values) for an Amazon Macie resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### ThrottlingException
<a name="custom-data-identifiers-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="custom-data-identifiers-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="custom-data-identifiers-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### CreateCustomDataIdentifier
<a name="CreateCustomDataIdentifier-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/CreateCustomDataIdentifier)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/CreateCustomDataIdentifier)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/CreateCustomDataIdentifier)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/CreateCustomDataIdentifier)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/CreateCustomDataIdentifier)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/CreateCustomDataIdentifier)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/CreateCustomDataIdentifier)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/CreateCustomDataIdentifier)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/CreateCustomDataIdentifier)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/CreateCustomDataIdentifier)
