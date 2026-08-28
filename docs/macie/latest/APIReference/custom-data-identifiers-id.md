---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/custom-data-identifiers-id.html
---

# Custom Data Identifier
<a name="custom-data-identifiers-id"></a>

The Custom Data Identifier resource provides access to the repository of custom data identifiers for your Amazon Macie account. A *custom data identifier* is a set of criteria that you define to detect sensitive data in a data source. The criteria consist of a regular expression (*regex*) that defines a text pattern to match and, optionally, character sequences and a proximity rule that refine the analysis of data. In addition to detection criteria, you can optionally define severity levels for findings that a custom data identifier produces. Severity levels are based on the number of occurrences of text that match the custom data identifier's detection criteria. For more information, see [Building custom data identifiers](https://docs.aws.amazon.com/macie/latest/user/custom-data-identifiers.html) in the *Amazon Macie User Guide*.

You can use this resource to retrieve detailed information about the detection criteria and other settings for a custom data identifier. You can also use this resource to delete a custom data identifier. If you delete a custom data identifier, Macie soft deletes it. This means that a record of the custom data identifier remains for your account, but it's marked as deleted. If a custom data identifier has this status, you can't configure new classification jobs to use it or add it to your settings for automated sensitive data discovery. In addition, you can't access it by using the Amazon Macie console. You can, however, retrieve its details programmatically.

If you delete a custom data identifier that you configured classification jobs or automated sensitive data discovery to use, the jobs and automated discovery will continue to use it. This means that sensitive data findings, statistics, and other types of results will continue to report text that matches the identifier's criteria. To prevent this, do the following before you delete the custom data identifier:
+ Remove it from your settings for automated sensitive data discovery. To remove it, use the [Sensitivity Inspection Template](templates-sensitivity-inspections-id.md) resource.
+ Identify existing jobs that use it and are scheduled to run in the future. You can cancel these jobs. Then create copies of the jobs and adjust their settings to exclude the custom data identifier. To cancel a job or retrieve its settings, use the [Classification Job](jobs-jobid.md) resource.

To use the Custom Data Identifier resource, you have to specify the unique identifier for the custom data identifier that your request applies to. To find this identifier, use the [Custom Data Identifier List](custom-data-identifiers-list.md) resource.

## URI
<a name="custom-data-identifiers-id-url"></a>

`/custom-data-identifiers/{{id}}`

## HTTP methods
<a name="custom-data-identifiers-id-http-methods"></a>

### DELETE
<a name="custom-data-identifiers-iddelete"></a>

**Operation ID:** `DeleteCustomDataIdentifier`

Soft deletes a custom data identifier.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Empty Schema | The request succeeded. The specified custom data identifier was deleted and there isn't any content to include in the body of the response (No Content). |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

### GET
<a name="custom-data-identifiers-idget"></a>

**Operation ID:** `GetCustomDataIdentifier`

Retrieves the criteria and other settings for a custom data identifier.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{id}} | String | True | The unique identifier for the Amazon Macie resource that the request applies to. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetCustomDataIdentifierResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="custom-data-identifiers-id-schemas"></a>

### Response bodies
<a name="custom-data-identifiers-id-response-examples"></a>

#### Empty Schema schema
<a name="custom-data-identifiers-id-response-body-empty-example"></a>

```
{
}
```

#### GetCustomDataIdentifierResponse schema
<a name="custom-data-identifiers-id-response-body-getcustomdataidentifierresponse-example"></a>

```
{
  "arn": "string",
  "createdAt": "string",
  "deleted": boolean,
  "description": "string",
  "id": "string",
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

#### ValidationException schema
<a name="custom-data-identifiers-id-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="custom-data-identifiers-id-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="custom-data-identifiers-id-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="custom-data-identifiers-id-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="custom-data-identifiers-id-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="custom-data-identifiers-id-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="custom-data-identifiers-id-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="custom-data-identifiers-id-properties"></a>

### AccessDeniedException
<a name="custom-data-identifiers-id-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="custom-data-identifiers-id-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### DataIdentifierSeverity
<a name="custom-data-identifiers-id-model-dataidentifierseverity"></a>

The severity of a finding, ranging from `LOW`, for least severe, to `HIGH`, for most severe. Valid values are:
+ `LOW`
+ `MEDIUM`
+ `HIGH`

### Empty
<a name="custom-data-identifiers-id-model-empty"></a>

The request succeeded and there isn't any content to include in the body of the response (No Content).

### GetCustomDataIdentifierResponse
<a name="custom-data-identifiers-id-model-getcustomdataidentifierresponse"></a>

Provides information about the detection criteria and other settings for a custom data identifier.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | The Amazon Resource Name (ARN) of the custom data identifier. |
| createdAt | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the custom data identifier was created. |
| deleted | boolean | False | Specifies whether the custom data identifier was deleted. If you delete a custom data identifier, Amazon Macie doesn't delete it permanently. Instead, Macie soft deletes the identifier. |
| description | string | False | The custom description of the custom data identifier. |
| id | string | False | The unique identifier for the custom data identifier. |
| ignoreWords | Array of type string | False | An array that lists specific character sequences (*ignore words*) to exclude from results. If text matches the regular expression but it contains a string in this array, Amazon Macie ignores it. Ignore words are case sensitive. |
| keywords | Array of type string | False | An array that lists specific character sequences (*keywords*), one of which must precede and be within proximity (`maximumMatchDistance`) of the regular expression to match. Keywords aren't case sensitive. |
| maximumMatchDistance | integer<br />Format: int32 | False | The maximum number of characters that can exist between the end of at least one complete character sequence specified by the `keywords` array and the end of text that matches the regular expression. If a complete keyword precedes all the text that matches the regular expression and the keyword is within the specified distance, Amazon Macie includes the result. Otherwise, Macie excludes the result. |
| name | string | False | The custom name of the custom data identifier. |
| regex | string | False | The regular expression (*regex*) that defines the pattern to match. |
| severityLevels | Array of type [SeverityLevel](#custom-data-identifiers-id-model-severitylevel) | False | Specifies the severity that's assigned to findings that the custom data identifier produces, based on the number of occurrences of text that match the identifier's detection criteria. By default, Amazon Macie creates findings for S3 objects that contain at least one occurrence of text that matches the detection criteria, and assigns the `MEDIUM` severity to the findings. |
| tags | [TagMap](#custom-data-identifiers-id-model-tagmap) | False | A map of key-value pairs that identifies the tags (keys and values) that are associated with the custom data identifier. |

### InternalServerException
<a name="custom-data-identifiers-id-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="custom-data-identifiers-id-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="custom-data-identifiers-id-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### SeverityLevel
<a name="custom-data-identifiers-id-model-severitylevel"></a>

Specifies a severity level for findings that a custom data identifier produces. A severity level determines which severity is assigned to the findings, based on the number of occurrences of text that match the identifier's detection criteria.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| occurrencesThreshold | integer<br />Format: int64 | True | The minimum number of occurrences of text that must match the custom data identifier's detection criteria in order to produce a finding with the specified severity (`severity`). |
| severity | [DataIdentifierSeverity](#custom-data-identifiers-id-model-dataidentifierseverity) | True | The severity to assign to a finding if the number of occurrences is greater than or equal to the specified threshold (`occurrencesThreshold`) and, if applicable, less than the threshold for the next consecutive severity level moving from `LOW` to `HIGH`. |

### TagMap
<a name="custom-data-identifiers-id-model-tagmap"></a>

A string-to-string map of key-value pairs that specifies the tags (keys and values) for an Amazon Macie resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### ThrottlingException
<a name="custom-data-identifiers-id-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ValidationException
<a name="custom-data-identifiers-id-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="custom-data-identifiers-id-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteCustomDataIdentifier
<a name="DeleteCustomDataIdentifier-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/DeleteCustomDataIdentifier)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/DeleteCustomDataIdentifier)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/DeleteCustomDataIdentifier)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/DeleteCustomDataIdentifier)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/DeleteCustomDataIdentifier)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/DeleteCustomDataIdentifier)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/DeleteCustomDataIdentifier)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/DeleteCustomDataIdentifier)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/DeleteCustomDataIdentifier)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/DeleteCustomDataIdentifier)

### GetCustomDataIdentifier
<a name="GetCustomDataIdentifier-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetCustomDataIdentifier)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetCustomDataIdentifier)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetCustomDataIdentifier)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetCustomDataIdentifier)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetCustomDataIdentifier)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetCustomDataIdentifier)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetCustomDataIdentifier)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetCustomDataIdentifier)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/GetCustomDataIdentifier)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetCustomDataIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Macie. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query macie` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
