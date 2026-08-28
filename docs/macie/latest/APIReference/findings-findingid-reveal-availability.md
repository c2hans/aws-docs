---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/findings-findingid-reveal-availability.html
---

# Findings - Reveal Sensitive Data Occurrences Availability
<a name="findings-findingid-reveal-availability"></a>

The Reveal Sensitive Data Occurrences Availability resource provides an environment for determining whether you can retrieve sample occurrences of sensitive data that Amazon Macie reported in a finding. You can use this resource in all the AWS Regions where Macie is currently available except the Asia Pacific (Osaka) and Israel (Tel Aviv) Regions.

To retrieve sensitive data samples for a finding, the finding must meet all the following criteria:
+ Include one or more `occurrences` objects that indicate the location of specific occurrences of sensitive data in the affected Amazon Simple Storage Service (Amazon S3) object.
+ Specify the location of a valid, corresponding sensitive data discovery result in the `classificationDetails.detailedResultsLocation` field.
+ Specify one of the following values in the `mimeType` field: `application/avro`, `application/gzip`, `application/json`, `application/parquet`, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`, `application/zip`, `text/csv`, `text/plain`, or `text/tab-separated-values`.

For additional requirements, see [Retrieving sensitive data samples with findings](https://docs.aws.amazon.com/macie/latest/user/findings-retrieve-sd.html) in the *Amazon Macie User Guide*.

By using the Reveal Sensitive Data Occurrences Availability resource, you can determine whether you can retrieve sample occurrences of sensitive data for a particular finding. To use this resource, you have to specify the unique identifier for the finding that your request applies to. To find this identifier, you can use the [Finding List](findings.md) resource. If samples are available for a finding, use the [Reveal Sensitive Data Occurrences](findings-findingid-reveal.md) resource to retrieve the samples.

Before you can use this resource, you have to configure and enable Macie to retrieve sensitive data samples for findings. To do this, use the [Reveal Sensitive Data Occurrences Configuration](reveal-configuration.md) resource.

## URI
<a name="findings-findingid-reveal-availability-url"></a>

`/findings/{{findingId}}/reveal/availability`

## HTTP methods
<a name="findings-findingid-reveal-availability-http-methods"></a>

### GET
<a name="findings-findingid-reveal-availabilityget"></a>

**Operation ID:** `GetSensitiveDataOccurrencesAvailability`

Checks whether occurrences of sensitive data can be retrieved for a finding.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{findingId}} | String | True | The unique identifier for the finding. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetSensitiveDataOccurrencesAvailabilityResponse | The request succeeded. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="findings-findingid-reveal-availability-schemas"></a>

### Response bodies
<a name="findings-findingid-reveal-availability-response-examples"></a>

#### GetSensitiveDataOccurrencesAvailabilityResponse schema
<a name="findings-findingid-reveal-availability-response-body-getsensitivedataoccurrencesavailabilityresponse-example"></a>

```
{
  "code": enum,
  "reasons": [
    enum
  ]
}
```

#### AccessDeniedException schema
<a name="findings-findingid-reveal-availability-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="findings-findingid-reveal-availability-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="findings-findingid-reveal-availability-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="findings-findingid-reveal-availability-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="findings-findingid-reveal-availability-properties"></a>

### AccessDeniedException
<a name="findings-findingid-reveal-availability-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### AvailabilityCode
<a name="findings-findingid-reveal-availability-model-availabilitycode"></a>

Specifies whether occurrences of sensitive data can be retrieved for a finding. Possible values are:
+ `AVAILABLE`
+ `UNAVAILABLE`

### GetSensitiveDataOccurrencesAvailabilityResponse
<a name="findings-findingid-reveal-availability-model-getsensitivedataoccurrencesavailabilityresponse"></a>

Provides information about whether occurrences of sensitive data can be retrieved for a finding and, if not, why the data can't be retrieved.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| code | [AvailabilityCode](#findings-findingid-reveal-availability-model-availabilitycode) | True | Specifies whether occurrences of sensitive data can be retrieved for the finding. Possible values are: `AVAILABLE`, the sensitive data can be retrieved; and, `UNAVAILABLE`, the sensitive data can't be retrieved. If this value is `UNAVAILABLE`, the `reasons` array indicates why the data can't be retrieved. |
| reasons | Array of type [UnavailabilityReasonCode](#findings-findingid-reveal-availability-model-unavailabilityreasoncode)<br />MinItems: 0 | True | Specifies why occurrences of sensitive data can't be retrieved for the finding. Possible values are:+  `ACCOUNT_NOT_IN_ORGANIZATION` - The affected account isn't currently part of your organization. Or the account is part of your organization but Macie isn't currently enabled for the account. You're not allowed to access the affected S3 object by using Macie. <br />+  `INVALID_CLASSIFICATION_RESULT` - There isn't a corresponding sensitive data discovery result for the finding. Or the corresponding sensitive data discovery result isn't available in the current AWS Region, is malformed or corrupted, or uses an unsupported storage format. Macie can't verify the location of the sensitive data to retrieve. <br />+  `INVALID_RESULT_SIGNATURE` - The corresponding sensitive data discovery result is stored in an S3 object that wasn't signed by Macie. Macie can't verify the integrity and authenticity of the sensitive data discovery result. Therefore, Macie can't verify the location of the sensitive data to retrieve. <br />+  `MEMBER_ROLE_TOO_PERMISSIVE` - The trust or permissions policy for the IAM role in the affected member account doesn't meet Macie requirements for restricting access to the role. Or the role's trust policy doesn't specify the correct external ID for your organization. Macie can't assume the role to retrieve the sensitive data. <br />+  `MISSING_GET_MEMBER_PERMISSION` - You're not allowed to retrieve information about the association between your account and the affected account. Macie can't determine whether you're allowed to access the affected S3 object as the delegated Macie administrator for the affected account. <br />+  `OBJECT_EXCEEDS_SIZE_QUOTA` - The storage size of the affected S3 object exceeds the size quota for retrieving occurrences of sensitive data from this type of file. <br />+  `OBJECT_UNAVAILABLE` - The affected S3 object isn't available. The object was renamed, moved, deleted, or changed after Macie created the finding. Or the object is encrypted with an AWS KMS key that isn't available. For example, the key is disabled, is scheduled for deletion, or was deleted. <br />+  `RESULT_NOT_SIGNED` - The corresponding sensitive data discovery result is stored in an S3 object that hasn't been signed. Macie can't verify the integrity and authenticity of the sensitive data discovery result. Therefore, Macie can't verify the location of the sensitive data to retrieve. <br />+  `ROLE_TOO_PERMISSIVE` - Your account is configured to retrieve occurrences of sensitive data by using an IAM role whose trust or permissions policy doesn't meet Macie requirements for restricting access to the role. Macie can't assume the role to retrieve the sensitive data. <br />+  `UNSUPPORTED_FINDING_TYPE` - The specified finding isn't a sensitive data finding. <br />+  `UNSUPPORTED_OBJECT_TYPE` - The affected S3 object uses a file or storage format that Macie doesn't support for retrieving occurrences of sensitive data. <br />This value is null if sensitive data can be retrieved for the finding. |

### InternalServerException
<a name="findings-findingid-reveal-availability-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="findings-findingid-reveal-availability-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="findings-findingid-reveal-availability-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### UnavailabilityReasonCode
<a name="findings-findingid-reveal-availability-model-unavailabilityreasoncode"></a>

Specifies why occurrences of sensitive data can't be retrieved for a finding. Possible values are:
+ `OBJECT_EXCEEDS_SIZE_QUOTA`
+ `UNSUPPORTED_OBJECT_TYPE`
+ `UNSUPPORTED_FINDING_TYPE`
+ `INVALID_CLASSIFICATION_RESULT`
+ `OBJECT_UNAVAILABLE`
+ `ACCOUNT_NOT_IN_ORGANIZATION`
+ `MISSING_GET_MEMBER_PERMISSION`
+ `ROLE_TOO_PERMISSIVE`
+ `MEMBER_ROLE_TOO_PERMISSIVE`
+ `INVALID_RESULT_SIGNATURE`
+ `RESULT_NOT_SIGNED`

## See also
<a name="findings-findingid-reveal-availability-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetSensitiveDataOccurrencesAvailability
<a name="GetSensitiveDataOccurrencesAvailability-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetSensitiveDataOccurrencesAvailability)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetSensitiveDataOccurrencesAvailability)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetSensitiveDataOccurrencesAvailability)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetSensitiveDataOccurrencesAvailability)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetSensitiveDataOccurrencesAvailability)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetSensitiveDataOccurrencesAvailability)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetSensitiveDataOccurrencesAvailability)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetSensitiveDataOccurrencesAvailability)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/GetSensitiveDataOccurrencesAvailability)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetSensitiveDataOccurrencesAvailability)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Macie. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query macie` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
