---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname.html
---

# GetReadinessCheck, UpdateReadinessCheck, DeleteReadinessCheck
<a name="readinesschecks-readinesscheckname"></a>

## URI
<a name="readinesschecks-readinesscheckname-url"></a>

`/readinesschecks/{{readinessCheckName}}`

## HTTP methods
<a name="readinesschecks-readinesscheckname-http-methods"></a>

### GET
<a name="readinesschecks-readinesschecknameget"></a>

**Operation ID:** `GetReadinessCheck`

Gets details about a readiness check.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{readinessCheckName}} | String | True | Name of a readiness check. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ReadinessCheckOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### PUT
<a name="readinesschecks-readinesschecknameput"></a>

**Operation ID:** `UpdateReadinessCheck`

Updates a readiness check.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{readinessCheckName}} | String | True | Name of a readiness check. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ReadinessCheckOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### DELETE
<a name="readinesschecks-readinesschecknamedelete"></a>

**Operation ID:** `DeleteReadinessCheck`

Deletes a readiness check.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{readinessCheckName}} | String | True | Name of a readiness check. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | 204 response - Successful deletion |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### OPTIONS
<a name="readinesschecks-readinesschecknameoptions"></a>

Enables CORS by returning correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{readinessCheckName}} | String | True | Name of a readiness check. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="readinesschecks-readinesscheckname-schemas"></a>

### Request bodies
<a name="readinesschecks-readinesscheckname-request-examples"></a>

#### PUT schema
<a name="readinesschecks-readinesscheckname-request-body-put-example"></a>

```
{
  "resourceSetName": "string"
}
```

### Response bodies
<a name="readinesschecks-readinesscheckname-response-examples"></a>

#### ReadinessCheckOutput schema
<a name="readinesschecks-readinesscheckname-response-body-readinesscheckoutput-example"></a>

```
{
  "resourceSet": "string",
  "readinessCheckName": "string",
  "readinessCheckArn": "string",
  "tags": {
  }
}
```

## Properties
<a name="readinesschecks-readinesscheckname-properties"></a>

### ReadinessCheckOutput
<a name="readinesschecks-readinesscheckname-model-readinesscheckoutput"></a>

A readiness check.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| readinessCheckArn | string<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) associated with a readiness check. |
| readinessCheckName | string<br />Pattern: `\A[a-zA-Z0-9_]+\z`<br />MaxLength: 64 | False | Name of a readiness check. |
| resourceSet | string<br />Pattern: `\A[a-zA-Z0-9_]+\z`<br />MaxLength: 64 | True | Name of the resource set to be checked. |
| tags | [Tags](#readinesschecks-readinesscheckname-model-tags) | False |  |

### ReadinessCheckUpdateParameters
<a name="readinesschecks-readinesscheckname-model-readinesscheckupdateparameters"></a>

Parameter used to create or update a readiness check.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resourceSetName | string | True | The name of the resource set to be checked. |

### Tags
<a name="readinesschecks-readinesscheckname-model-tags"></a>

A collection of tags associated with a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="readinesschecks-readinesscheckname-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetReadinessCheck
<a name="GetReadinessCheck-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/GetReadinessCheck)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/GetReadinessCheck)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/GetReadinessCheck)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/GetReadinessCheck)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/GetReadinessCheck)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/GetReadinessCheck)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/GetReadinessCheck)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/GetReadinessCheck)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/GetReadinessCheck)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/GetReadinessCheck)

### UpdateReadinessCheck
<a name="UpdateReadinessCheck-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/UpdateReadinessCheck)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/UpdateReadinessCheck)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/UpdateReadinessCheck)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/UpdateReadinessCheck)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/UpdateReadinessCheck)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/UpdateReadinessCheck)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/UpdateReadinessCheck)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/UpdateReadinessCheck)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/UpdateReadinessCheck)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/UpdateReadinessCheck)

### DeleteReadinessCheck
<a name="DeleteReadinessCheck-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/DeleteReadinessCheck)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/DeleteReadinessCheck)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/DeleteReadinessCheck)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/DeleteReadinessCheck)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/DeleteReadinessCheck)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/DeleteReadinessCheck)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/DeleteReadinessCheck)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/DeleteReadinessCheck)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/DeleteReadinessCheck)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/DeleteReadinessCheck)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-readiness` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
