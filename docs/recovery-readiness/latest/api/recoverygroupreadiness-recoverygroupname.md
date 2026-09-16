---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroupreadiness-recoverygroupname.html
---

# GetRecoveryGroupReadinessSummary
<a name="recoverygroupreadiness-recoverygroupname"></a>

## URI
<a name="recoverygroupreadiness-recoverygroupname-url"></a>

`/recoverygroupreadiness/{{recoveryGroupName}}`

## HTTP methods
<a name="recoverygroupreadiness-recoverygroupname-http-methods"></a>

### GET
<a name="recoverygroupreadiness-recoverygroupnameget"></a>

**Operation ID:** `GetRecoveryGroupReadinessSummary`

Displays a summary of information about a recovery group's readiness status. Includes the readiness checks for resources in the recovery group and the readiness status of each one.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{recoveryGroupName}} | String | True | The name of a recovery group. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The token that identifies which batch of results you want to see. |
| maxResults | String | False | The number of objects that you want to return with this call. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetRecoveryGroupReadinessSummaryOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### OPTIONS
<a name="recoverygroupreadiness-recoverygroupnameoptions"></a>

Enable CORS by returning correct headers

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{recoveryGroupName}} | String | True | The name of a recovery group. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="recoverygroupreadiness-recoverygroupname-schemas"></a>

### Response bodies
<a name="recoverygroupreadiness-recoverygroupname-response-examples"></a>

#### GetRecoveryGroupReadinessSummaryOutput schema
<a name="recoverygroupreadiness-recoverygroupname-response-body-getrecoverygroupreadinesssummaryoutput-example"></a>

```
{
  "nextToken": "string",
  "readiness": enum,
  "readinessChecks": [
    {
      "readinessCheckName": "string",
      "readiness": enum
    }
  ]
}
```

## Properties
<a name="recoverygroupreadiness-recoverygroupname-properties"></a>

### GetRecoveryGroupReadinessSummaryOutput
<a name="recoverygroupreadiness-recoverygroupname-model-getrecoverygroupreadinesssummaryoutput"></a>

Result of a `GetReadinessRecoveryGroupSummary` operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | True | The token that identifies which batch of results you want to see. |
| readiness | [Readiness](#recoverygroupreadiness-recoverygroupname-model-readiness) | True | The readiness status at a recovery group level. |
| readinessChecks | Array of type [ReadinessCheckSummary](#recoverygroupreadiness-recoverygroupname-model-readinesschecksummary) | True | Summaries of the readiness checks for the recovery group. |

### Readiness
<a name="recoverygroupreadiness-recoverygroupname-model-readiness"></a>

The readiness status.
+ `READY`
+ `NOT_READY`
+ `UNKNOWN`
+ `NOT_AUTHORIZED`

### ReadinessCheckSummary
<a name="recoverygroupreadiness-recoverygroupname-model-readinesschecksummary"></a>

Summary of all readiness check statuses in a recovery group, paginated in `GetRecoveryGroupReadinessSummary` and `GetCellReadinessSummary`.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| readiness | [Readiness](#recoverygroupreadiness-recoverygroupname-model-readiness) | False | The readiness status of this readiness check. |
| readinessCheckName | string | False | The name of a readiness check. |

## See also
<a name="recoverygroupreadiness-recoverygroupname-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetRecoveryGroupReadinessSummary
<a name="GetRecoveryGroupReadinessSummary-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/GetRecoveryGroupReadinessSummary)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/GetRecoveryGroupReadinessSummary)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/GetRecoveryGroupReadinessSummary)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/GetRecoveryGroupReadinessSummary)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/GetRecoveryGroupReadinessSummary)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/GetRecoveryGroupReadinessSummary)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/GetRecoveryGroupReadinessSummary)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/GetRecoveryGroupReadinessSummary)
+ [AWS SDK for Python (Boto3)](/goto/boto3/aws-meridian-beta-2019-12-02/GetRecoveryGroupReadinessSummary)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/GetRecoveryGroupReadinessSummary)
