---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/cellreadiness-cellname.html
---

# GetCellReadinessSummary
<a name="cellreadiness-cellname"></a>

## URI
<a name="cellreadiness-cellname-url"></a>

`/cellreadiness/{{cellName}}`

## HTTP methods
<a name="cellreadiness-cellname-http-methods"></a>

### GET
<a name="cellreadiness-cellnameget"></a>

**Operation ID:** `GetCellReadinessSummary`

Gets readiness for a cell. Aggregates the readiness of all the resources that are associated with the cell into a single value.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{cellName}} | String | True | The name of the cell. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The token that identifies which batch of results you want to see. |
| maxResults | String | False | The number of objects that you want to return with this call. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetCellReadinessSummaryOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### OPTIONS
<a name="cellreadiness-cellnameoptions"></a>

Enable CORS by returning correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{cellName}} | String | True | The name of the cell. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="cellreadiness-cellname-schemas"></a>

### Response bodies
<a name="cellreadiness-cellname-response-examples"></a>

#### GetCellReadinessSummaryOutput schema
<a name="cellreadiness-cellname-response-body-getcellreadinesssummaryoutput-example"></a>

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
<a name="cellreadiness-cellname-properties"></a>

### GetCellReadinessSummaryOutput
<a name="cellreadiness-cellname-model-getcellreadinesssummaryoutput"></a>

Result of a `GetReadinessCellSummary` operation

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | True | The token that identifies which batch of results you want to see. |
| readiness | [Readiness](#cellreadiness-cellname-model-readiness) | True | The readiness at a cell level. |
| readinessChecks | Array of type [ReadinessCheckSummary](#cellreadiness-cellname-model-readinesschecksummary) | True | Summaries for the readiness checks that make up the cell. |

### Readiness
<a name="cellreadiness-cellname-model-readiness"></a>

The readiness status.
+ `READY`
+ `NOT_READY`
+ `UNKNOWN`
+ `NOT_AUTHORIZED`

### ReadinessCheckSummary
<a name="cellreadiness-cellname-model-readinesschecksummary"></a>

Summary of all readiness check statuses in a recovery group, paginated in `GetRecoveryGroupReadinessSummary` and `GetCellReadinessSummary`.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| readiness | [Readiness](#cellreadiness-cellname-model-readiness) | False | The readiness status of this readiness check. |
| readinessCheckName | string | False | The name of a readiness check. |

## See also
<a name="cellreadiness-cellname-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetCellReadinessSummary
<a name="GetCellReadinessSummary-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/GetCellReadinessSummary)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/GetCellReadinessSummary)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/GetCellReadinessSummary)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/GetCellReadinessSummary)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/GetCellReadinessSummary)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/GetCellReadinessSummary)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/GetCellReadinessSummary)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/GetCellReadinessSummary)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/GetCellReadinessSummary)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/GetCellReadinessSummary)
