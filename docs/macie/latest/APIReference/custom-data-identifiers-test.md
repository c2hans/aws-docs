---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/custom-data-identifiers-test.html
---

# Custom Data Identifier Testing
<a name="custom-data-identifiers-test"></a>

The Custom Data Identifier Testing resource provides an environment for developing, testing, and refining detection criteria for a custom data identifier. A *custom data identifier* is a set of criteria that you define to detect sensitive data in a data source. By using custom data identifiers, you can detect sensitive data that reflects your particular scenarios, intellectual property, or proprietary data. You can supplement the managed data identifiers that Amazon Macie provides.

When you develop a custom data identifier, you specify a regular expression (*regex*) that defines a text pattern to match in a data source. You can also specify character sequences, such as words and phrases, and a proximity rule to refine the analysis of data. The character sequences can be: *keywords*, which are words or phrases that must be in proximity of text that matches the regex, or *ignore words*, which are words or phrases to exclude from results. For more information, see [Building custom data identifiers](https://docs.aws.amazon.com/macie/latest/user/custom-data-identifiers.html) in the *Amazon Macie User Guide*.

You can use the Custom Data Identifier Testing resource to develop, test, and refine detection criteria for a custom data identifier. Note that this resource doesn't create a persistent custom data identifier that you can later access and use in Macie. Instead, it provides a test environment that can help you optimize and refine detection criteria by using sample data. When you finish developing and testing the criteria, use the [Custom Data Identifier Creation](custom-data-identifiers.md) resource to create the custom data identifier.

## URI
<a name="custom-data-identifiers-test-url"></a>

`/custom-data-identifiers/test`

## HTTP methods
<a name="custom-data-identifiers-test-http-methods"></a>

### POST
<a name="custom-data-identifiers-testpost"></a>

**Operation ID:** `TestCustomDataIdentifier`

Tests criteria for a custom data identifier.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | TestCustomDataIdentifierResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="custom-data-identifiers-test-schemas"></a>

### Request bodies
<a name="custom-data-identifiers-test-request-examples"></a>

#### POST schema
<a name="custom-data-identifiers-test-request-body-post-example"></a>

```
{
  "ignoreWords": [
    "string"
  ],
  "keywords": [
    "string"
  ],
  "maximumMatchDistance": integer,
  "regex": "string",
  "sampleText": "string"
}
```

#### POST schema
<a name="custom-data-identifiers-test-request-body-post-example"></a>

```
{
  "ignoreWords": [
    "string"
  ],
  "keywords": [
    "string"
  ],
  "maximumMatchDistance": integer,
  "regex": "string",
  "sampleText": "string"
}
```

### Response bodies
<a name="custom-data-identifiers-test-response-examples"></a>

#### TestCustomDataIdentifierResponse schema
<a name="custom-data-identifiers-test-response-body-testcustomdataidentifierresponse-example"></a>

```
{
  "matchCount": integer
}
```

#### ValidationException schema
<a name="custom-data-identifiers-test-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="custom-data-identifiers-test-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="custom-data-identifiers-test-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="custom-data-identifiers-test-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="custom-data-identifiers-test-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="custom-data-identifiers-test-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="custom-data-identifiers-test-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="custom-data-identifiers-test-properties"></a>

### AccessDeniedException
<a name="custom-data-identifiers-test-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="custom-data-identifiers-test-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### InternalServerException
<a name="custom-data-identifiers-test-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="custom-data-identifiers-test-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="custom-data-identifiers-test-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### TestCustomDataIdentifierRequest
<a name="custom-data-identifiers-test-model-testcustomdataidentifierrequest"></a>

Specifies the detection criteria of a custom data identifier to test.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ignoreWords | Array of type string | False | An array that lists specific character sequences (*ignore words*) to exclude from results. If text matches the regular expression but it contains a string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4-90 UTF-8 characters. Ignore words are case sensitive. |
| keywords | Array of type string | False | An array that lists specific character sequences (*keywords*), one of which must precede and be within proximity (`maximumMatchDistance`) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3-90 UTF-8 characters. Keywords aren't case sensitive. |
| maximumMatchDistance | integer<br />Format: int32 | False | The maximum number of characters that can exist between the end of at least one complete character sequence specified by the `keywords` array and the end of text that matches the regular expression. If a complete keyword precedes all the text that matches the regular expression and the keyword is within the specified distance, Amazon Macie includes the result. The distance can be 1-300 characters. The default value is 50. |
| regex | string | True | The regular expression (*regex*) that defines the pattern to match. The expression can contain as many as 512 characters. |
| sampleText | string | True | The sample text to inspect by using the custom data identifier. The text can contain as many as 1,000 characters. |

### TestCustomDataIdentifierResponse
<a name="custom-data-identifiers-test-model-testcustomdataidentifierresponse"></a>

Provides test results for a custom data identifier.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| matchCount | integer<br />Format: int32 | False | The number of occurrences of sample text that matched the criteria specified by the custom data identifier. |

### ThrottlingException
<a name="custom-data-identifiers-test-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="custom-data-identifiers-test-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="custom-data-identifiers-test-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### TestCustomDataIdentifier
<a name="TestCustomDataIdentifier-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/TestCustomDataIdentifier)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/TestCustomDataIdentifier)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/TestCustomDataIdentifier)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/TestCustomDataIdentifier)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/TestCustomDataIdentifier)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/TestCustomDataIdentifier)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/TestCustomDataIdentifier)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/TestCustomDataIdentifier)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/TestCustomDataIdentifier)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/TestCustomDataIdentifier)
