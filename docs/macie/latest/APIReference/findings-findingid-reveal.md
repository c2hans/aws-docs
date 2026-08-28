---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/findings-findingid-reveal.html
---

# Findings - Reveal Sensitive Data Occurrences
<a name="findings-findingid-reveal"></a>

The Reveal Sensitive Data Occurrences resource provides options for retrieving sample occurrences of sensitive data that Amazon Macie reported in a finding. The samples can help you verify the nature of the sensitive data that Macie found. You can also use them to tailor your investigation of the affected Amazon Simple Storage Service (Amazon S3) object or bucket. You can retrieve sensitive data samples in all the AWS Regions where Macie is currently available except the Asia Pacific (Osaka) and Israel (Tel Aviv) Regions.

When you retrieve sensitive data samples, you specify the unique identifier for a particular sensitive data finding. Macie then uses location data in the corresponding sensitive data discovery result to locate and extract sample occurrences of sensitive data from the affected S3 object. Macie encrypts the extracted data with an AWS Key Management Service (AWS KMS) key that you specify, temporarily stores the encrypted data in a cache, and returns the data in your results. Soon after extraction and encryption, Macie permanently deletes the data from the cache unless additional retention is temporarily required to resolve an operational issue.

To retrieve sensitive data samples for a finding, the finding must meet all the following criteria:
+ Include one or more `occurrences` objects that indicate the location of specific occurrences of sensitive data in the affected S3 object.
+ Specify the location of a valid, corresponding sensitive data discovery result in the `classificationDetails.detailedResultsLocation` field.
+ Specify one of the following values in the `mimeType` field: `application/avro`, `application/gzip`, `application/json`, `application/parquet`, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`, `application/zip`, `text/csv`, `text/plain`, or `text/tab-separated-values`.

For additional requirements, see [Retrieving sensitive data samples with findings](https://docs.aws.amazon.com/macie/latest/user/findings-retrieve-sd.html) in the *Amazon Macie User Guide*.

By using the Reveal Sensitive Data Occurrences resource, you can retrieve sample occurrences of sensitive data that Macie reported in a particular finding. When you use this resource, you have to specify the unique identifier for the finding that your request applies to. To find this identifier, you can use the [Finding List](findings.md) resource.

Before you can use this resource, you have to configure and enable Macie to retrieve sensitive data samples for findings. To do this, use the [Reveal Sensitive Data Occurrences Configuration](reveal-configuration.md) resource.

## URI
<a name="findings-findingid-reveal-url"></a>

`/findings/{{findingId}}/reveal`

## HTTP methods
<a name="findings-findingid-reveal-http-methods"></a>

### GET
<a name="findings-findingid-revealget"></a>

**Operation ID:** `GetSensitiveDataOccurrences`

Retrieves occurrences of sensitive data reported by a finding.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{findingId}} | String | True | The unique identifier for the finding. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetSensitiveDataOccurrencesResponse | The request succeeded. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 422 | UnprocessableEntityException | The request failed because it contains instructions that Amazon Macie can't process (Unprocessable Entity). |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="findings-findingid-reveal-schemas"></a>

### Response bodies
<a name="findings-findingid-reveal-response-examples"></a>

#### GetSensitiveDataOccurrencesResponse schema
<a name="findings-findingid-reveal-response-body-getsensitivedataoccurrencesresponse-example"></a>

```
{
  "error": "string",
  "sensitiveDataOccurrences": {
  },
  "status": enum
}
```

#### ServiceQuotaExceededException schema
<a name="findings-findingid-reveal-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="findings-findingid-reveal-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="findings-findingid-reveal-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### UnprocessableEntityException schema
<a name="findings-findingid-reveal-response-body-unprocessableentityexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="findings-findingid-reveal-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="findings-findingid-reveal-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="findings-findingid-reveal-properties"></a>

### AccessDeniedException
<a name="findings-findingid-reveal-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### DetectedDataDetails
<a name="findings-findingid-reveal-model-detecteddatadetails"></a>

Specifies 1-10 occurrences of a specific type of sensitive data reported by a finding.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| value | string<br />Format: password<br />MinLength: 1<br />MaxLength: 128 | True | An occurrence of the specified type of sensitive data. Each occurrence contains 1-128 characters. |

### GetSensitiveDataOccurrencesResponse
<a name="findings-findingid-reveal-model-getsensitivedataoccurrencesresponse"></a>

Provides the results of a request to retrieve occurrences of sensitive data reported by a finding.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| error | string | False | If an error occurred when Amazon Macie attempted to retrieve occurrences of sensitive data reported by the finding, a description of the error that occurred. This value is null if the status (`status`) of the request is `PROCESSING` or `SUCCESS`. |
| sensitiveDataOccurrences | [SensitiveDataOccurrences](#findings-findingid-reveal-model-sensitivedataoccurrences) | False | A map that specifies 1-100 types of sensitive data reported by the finding and, for each type, 1-10 occurrences of sensitive data. |
| status | [RevealRequestStatus](#findings-findingid-reveal-model-revealrequeststatus) | False | The status of the request to retrieve occurrences of sensitive data reported by the finding. Possible values are:+  `ERROR` - An error occurred when Amazon Macie attempted to locate, retrieve, or encrypt the sensitive data. The `error` value indicates the nature of the error that occurred. <br />+  `PROCESSING` - Macie is processing the request. <br />+  `SUCCESS` - Macie successfully located, retrieved, and encrypted the sensitive data.  |

### InternalServerException
<a name="findings-findingid-reveal-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="findings-findingid-reveal-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### RevealRequestStatus
<a name="findings-findingid-reveal-model-revealrequeststatus"></a>

The status of a request to retrieve occurrences of sensitive data reported by a finding. Possible values are:
+ `SUCCESS`
+ `PROCESSING`
+ `ERROR`

### SensitiveDataOccurrences
<a name="findings-findingid-reveal-model-sensitivedataoccurrences"></a>

Specifies a type of sensitive data reported by a finding and provides occurrences of the specified type of sensitive data.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | array | False | An array of DetectedDataDetails objects. Each object specifies 1-10 occurrences of a specified type of sensitive data. |

### ServiceQuotaExceededException
<a name="findings-findingid-reveal-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="findings-findingid-reveal-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UnprocessableEntityException
<a name="findings-findingid-reveal-model-unprocessableentityexception"></a>

Provides information about an error that occurred due to an unprocessable entity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True | The type of error that occurred and prevented Amazon Macie from retrieving occurrences of sensitive data reported by the finding. Possible values are:+  `ACCOUNT_NOT_IN_ORGANIZATION` - The affected account isn't currently part of your organization. Or the account is part of your organization but Macie isn't currently enabled for the account. You're not allowed to access the affected S3 object by using Macie. <br />+  `INVALID_CLASSIFICATION_RESULT` - There isn't a corresponding sensitive data discovery result for the finding. Or the corresponding sensitive data discovery result isn't available in the current AWS Region, is malformed or corrupted, or uses an unsupported storage format. Macie can't verify the location of the sensitive data to retrieve. <br />+  `INVALID_RESULT_SIGNATURE` - The corresponding sensitive data discovery result is stored in an S3 object that wasn't signed by Macie. Macie can't verify the integrity and authenticity of the sensitive data discovery result. Therefore, Macie can't verify the location of the sensitive data to retrieve. <br />+  `MEMBER_ROLE_TOO_PERMISSIVE` - The trust or permissions policy for the IAM role in the affected member account doesn't meet Macie requirements for restricting access to the role. Or the role's trust policy doesn't specify the correct external ID for your organization. Macie can't assume the role to retrieve the sensitive data. <br />+  `MISSING_GET_MEMBER_PERMISSION` - You're not allowed to retrieve information about the association between your account and the affected account. Macie can't determine whether you're allowed to access the affected S3 object as the delegated Macie administrator for the affected account. <br />+  `OBJECT_EXCEEDS_SIZE_QUOTA` - The storage size of the affected S3 object exceeds the size quota for retrieving occurrences of sensitive data from this type of file. <br />+  `OBJECT_UNAVAILABLE` - The affected S3 object isn't available. The object was renamed, moved, deleted, or changed after Macie created the finding. Or the object is encrypted with an AWS KMS key that isn't available. For example, the key is disabled, is scheduled for deletion, or was deleted. <br />+  `RESULT_NOT_SIGNED` - The corresponding sensitive data discovery result is stored in an S3 object that hasn't been signed. Macie can't verify the integrity and authenticity of the sensitive data discovery result. Therefore, Macie can't verify the location of the sensitive data to retrieve. <br />+  `ROLE_TOO_PERMISSIVE` - Your account is configured to retrieve occurrences of sensitive data by using an IAM role whose trust or permissions policy doesn't meet Macie requirements for restricting access to the role. Macie can't assume the role to retrieve the sensitive data. <br />+  `UNSUPPORTED_FINDING_TYPE` - The specified finding isn't a sensitive data finding. <br />+  `UNSUPPORTED_OBJECT_TYPE` - The affected S3 object uses a file or storage format that Macie doesn't support for retrieving occurrences of sensitive data.  |

## See also
<a name="findings-findingid-reveal-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetSensitiveDataOccurrences
<a name="GetSensitiveDataOccurrences-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetSensitiveDataOccurrences)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetSensitiveDataOccurrences)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetSensitiveDataOccurrences)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetSensitiveDataOccurrences)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetSensitiveDataOccurrences)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetSensitiveDataOccurrences)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetSensitiveDataOccurrences)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetSensitiveDataOccurrences)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/GetSensitiveDataOccurrences)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetSensitiveDataOccurrences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Macie. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query macie` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
