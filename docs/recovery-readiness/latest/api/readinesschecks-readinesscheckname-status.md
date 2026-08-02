---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/readinesschecks-readinesscheckname-status.html
---

# GetReadinessCheckStatus
<a name="readinesschecks-readinesscheckname-status"></a>

## URI
<a name="readinesschecks-readinesscheckname-status-url"></a>

`/readinesschecks/{{readinessCheckName}}/status`

## HTTP methods
<a name="readinesschecks-readinesscheckname-status-http-methods"></a>

### GET
<a name="readinesschecks-readinesscheckname-statusget"></a>

**Operation ID:** `GetReadinessCheckStatus`

Gets the readiness status for an individual readiness check. To see the overall readiness status for a recovery group, that considers the readiness status for all the readiness checks in a recovery group, use `GetRecoveryGroupReadinessSummary`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{readinessCheckName}} | String | True | Name of a readiness check. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The token that identifies which batch of results you want to see. |
| maxResults | String | False | The number of objects that you want to return with this call. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetReadinessCheckStatusOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### OPTIONS
<a name="readinesschecks-readinesscheckname-statusoptions"></a>

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
<a name="readinesschecks-readinesscheckname-status-schemas"></a>

### Response bodies
<a name="readinesschecks-readinesscheckname-status-response-examples"></a>

#### GetReadinessCheckStatusOutput schema
<a name="readinesschecks-readinesscheckname-status-response-body-getreadinesscheckstatusoutput-example"></a>

```
{
  "nextToken": "string",
  "readiness": enum,
  "messages": [
    {
      "messageText": "string"
    }
  ],
  "resources": [
    {
      "componentId": "string",
      "readiness": enum,
      "resourceArn": "string",
      "lastCheckedTimestamp": "string"
    }
  ]
}
```

## Properties
<a name="readinesschecks-readinesscheckname-status-properties"></a>

### GetReadinessCheckStatusOutput
<a name="readinesschecks-readinesscheckname-status-model-getreadinesscheckstatusoutput"></a>

Result of a `GetReadinessCheckStatus` operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| messages | Array of type [Message](#readinesschecks-readinesscheckname-status-model-message) | True | Top level messages for readiness check status |
| nextToken | string | True | The token that identifies which batch of results you want to see. |
| readiness | [Readiness](#readinesschecks-readinesscheckname-status-model-readiness) | True | The readiness at rule level. |
| resources | Array of type [ResourceResult](#readinesschecks-readinesscheckname-status-model-resourceresult) | True | Summary of the readiness of resources. |

### Message
<a name="readinesschecks-readinesscheckname-status-model-message"></a>

Information relating to readiness check status.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| messageText | string | False | The text of a readiness check message. |

### Readiness
<a name="readinesschecks-readinesscheckname-status-model-readiness"></a>

The readiness status.
+ `READY`
+ `NOT_READY`
+ `UNKNOWN`
+ `NOT_AUTHORIZED`

### ResourceResult
<a name="readinesschecks-readinesscheckname-status-model-resourceresult"></a>

The result of a successful `Resource` request, with status for an individual resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| componentId | string | False | The component id of the resource. |
| lastCheckedTimestamp | string | True | The time (UTC) that the resource was last checked for readiness, in ISO-8601 format. |
| readiness | [Readiness](#readinesschecks-readinesscheckname-status-model-readiness) | True | The readiness of a resource. |
| resourceArn | string | False | The Amazon Resource Name (ARN) of the resource. |

## See also
<a name="readinesschecks-readinesscheckname-status-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetReadinessCheckStatus
<a name="GetReadinessCheckStatus-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/GetReadinessCheckStatus)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/GetReadinessCheckStatus)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/GetReadinessCheckStatus)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/GetReadinessCheckStatus)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/GetReadinessCheckStatus)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/GetReadinessCheckStatus)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/GetReadinessCheckStatus)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/GetReadinessCheckStatus)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/GetReadinessCheckStatus)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/GetReadinessCheckStatus)
