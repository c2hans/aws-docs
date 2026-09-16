---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks.html
---

# ListReadinessChecks, CreateReadinessCheck
<a name="readinesschecks"></a>

## URI
<a name="readinesschecks-url"></a>

`/readinesschecks`

## HTTP methods
<a name="readinesschecks-http-methods"></a>

### GET
<a name="readinesschecksget"></a>

**Operation ID:** `ListReadinessChecks`

Lists the readiness checks for an account.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The token that identifies which batch of results you want to see. |
| maxResults | String | False | The number of objects that you want to return with this call. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListReadinessChecksResult | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### POST
<a name="readinesscheckspost"></a>

**Operation ID:** `CreateReadinessCheck`

Creates a readiness check in an account. A readiness check monitors a resource set in your application, such as a set of Amazon Aurora instances, that Application Recovery Controller is auditing recovery readiness for. The audits run once every minute on every resource that's associated with a readiness check.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ReadinessCheckOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 409 | None | 409 response - Conflict exception. You might be using a predefined variable. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### OPTIONS
<a name="readinesschecksoptions"></a>

Enables CORS by returning correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="readinesschecks-schemas"></a>

### Request bodies
<a name="readinesschecks-request-examples"></a>

#### POST schema
<a name="readinesschecks-request-body-post-example"></a>

```
{
  "readinessCheckName": "string",
  "resourceSetName": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="readinesschecks-response-examples"></a>

#### ListReadinessChecksResult schema
<a name="readinesschecks-response-body-listreadinesschecksresult-example"></a>

```
{
  "nextToken": "string",
  "readinessChecks": [
    {
      "resourceSet": "string",
      "readinessCheckName": "string",
      "readinessCheckArn": "string",
      "tags": {
      }
    }
  ]
}
```

#### ReadinessCheckOutput schema
<a name="readinesschecks-response-body-readinesscheckoutput-example"></a>

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
<a name="readinesschecks-properties"></a>

### ListReadinessChecksResult
<a name="readinesschecks-model-listreadinesschecksresult"></a>

The result of a successful `ListReadinessChecks` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | The token that identifies which batch of results you want to see. |
| readinessChecks | Array of type [ReadinessCheckOutput](#readinesschecks-model-readinesscheckoutput) | False | A list of readiness checks associated with the account. |

### ReadinessCheckCreateParameters
<a name="readinesschecks-model-readinesscheckcreateparameters"></a>

Parameters used to create or update a readiness check.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| readinessCheckName | string | True | The name of the readiness check to create. |
| resourceSetName | string | True | The name of the resource set to check. |
| tags | [Tags](#readinesschecks-model-tags) | False |  |

### ReadinessCheckOutput
<a name="readinesschecks-model-readinesscheckoutput"></a>

A readiness check.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| readinessCheckArn | string<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) associated with a readiness check. |
| readinessCheckName | string<br />Pattern: `\A[a-zA-Z0-9_]+\z`<br />MaxLength: 64 | False | Name of a readiness check. |
| resourceSet | string<br />Pattern: `\A[a-zA-Z0-9_]+\z`<br />MaxLength: 64 | True | Name of the resource set to be checked. |
| tags | [Tags](#readinesschecks-model-tags) | False |  |

### Tags
<a name="readinesschecks-model-tags"></a>

A collection of tags associated with a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="readinesschecks-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListReadinessChecks
<a name="ListReadinessChecks-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/ListReadinessChecks)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/ListReadinessChecks)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/ListReadinessChecks)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/ListReadinessChecks)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/ListReadinessChecks)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/ListReadinessChecks)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/ListReadinessChecks)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/ListReadinessChecks)
+ [AWS SDK for Python (Boto3)](/goto/boto3/aws-meridian-beta-2019-12-02/ListReadinessChecks)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/ListReadinessChecks)

### CreateReadinessCheck
<a name="CreateReadinessCheck-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/CreateReadinessCheck)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/CreateReadinessCheck)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/CreateReadinessCheck)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/CreateReadinessCheck)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/CreateReadinessCheck)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/CreateReadinessCheck)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/CreateReadinessCheck)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/CreateReadinessCheck)
+ [AWS SDK for Python (Boto3)](/goto/boto3/aws-meridian-beta-2019-12-02/CreateReadinessCheck)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/CreateReadinessCheck)
