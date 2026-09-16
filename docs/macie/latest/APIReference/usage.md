---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/usage.html
---

# Usage Totals
<a name="usage"></a>

The Usage Totals resource provides aggregated usage data for your Amazon Macie account. The data can provide insight into the estimated cost of using Macie to monitor and analyze your Amazon Simple Storage Service (Amazon S3) data. If you're currently participating in a 30-day free trial, the applicable cost estimates can help you understand what your usage costs might be after the trial ends. For information about how Macie calculates this data for your account, see [Forecasting and monitoring costs](https://docs.aws.amazon.com/macie/latest/user/account-mgmt-costs.html) in the *Amazon Macie User Guide*.

You can use the Usage Totals resource to retrieve (query) aggregated usage data for your Macie account for the preceding 30 days or the current calendar month to date. If you're the Macie administrator for an organization, the data reports cumulative usage for all the accounts in your organization. To query additional usage-related data or build a custom query for a select set of accounts, use the [Usage Statistics](usage-statistics.md) resource.

## URI
<a name="usage-url"></a>

`/usage`

## HTTP methods
<a name="usage-http-methods"></a>

### GET
<a name="usageget"></a>

**Operation ID:** `GetUsageTotals`

Retrieves (queries) aggregated usage data for an account.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| timeRange | String | False | The inclusive time period to retrieve the data for. Valid values are: `MONTH_TO_DATE`, for the current calendar month to date; and, `PAST_30_DAYS`, for the preceding 30 days. If you don't specify a value for this parameter, Amazon Macie provides aggregated usage data for the preceding 30 days. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetUsageTotalsResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="usage-schemas"></a>

### Response bodies
<a name="usage-response-examples"></a>

#### GetUsageTotalsResponse schema
<a name="usage-response-body-getusagetotalsresponse-example"></a>

```
{
  "timeRange": enum,
  "usageTotals": [
    {
      "currency": enum,
      "estimatedCost": "string",
      "type": enum
    }
  ]
}
```

#### ValidationException schema
<a name="usage-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="usage-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="usage-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="usage-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="usage-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="usage-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="usage-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="usage-properties"></a>

### AccessDeniedException
<a name="usage-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="usage-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Currency
<a name="usage-model-currency"></a>

The type of currency that the data for an Amazon Macie usage metric is reported in. Possible values are:
+ `USD`

### GetUsageTotalsResponse
<a name="usage-model-getusagetotalsresponse"></a>

Provides the results of a query that retrieved aggregated usage data for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| timeRange | [TimeRange](#usage-model-timerange) | False | The inclusive time period that the usage data applies to. Possible values are: `MONTH_TO_DATE`, for the current calendar month to date; and, `PAST_30_DAYS`, for the preceding 30 days. |
| usageTotals | Array of type [UsageTotal](#usage-model-usagetotal) | False | An array of objects that contains the results of the query. Each object contains the data for a specific usage metric. |

### InternalServerException
<a name="usage-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="usage-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceQuotaExceededException
<a name="usage-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="usage-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### TimeRange
<a name="usage-model-timerange"></a>

An inclusive time period that Amazon Macie usage data applies to. Possible values are:
+ `MONTH_TO_DATE`
+ `PAST_30_DAYS`

### UsageTotal
<a name="usage-model-usagetotal"></a>

Provides aggregated data for an Amazon Macie usage metric. The value for the metric reports estimated usage data for an account for the preceding 30 days or the current calendar month to date, depending on the time period (`timeRange`) specified in the request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| currency | [Currency](#usage-model-currency) | False | The type of currency that the value for the metric (`estimatedCost`) is reported in. |
| estimatedCost | string | False | The estimated value for the metric. |
| type | [UsageType](#usage-model-usagetype) | False | The name of the metric. Possible values are: `AUTOMATED_OBJECT_MONITORING`, to monitor S3 objects for automated sensitive data discovery; `AUTOMATED_SENSITIVE_DATA_DISCOVERY`, to analyze S3 objects for automated sensitive data discovery; `DATA_INVENTORY_EVALUATION`, to monitor S3 buckets; and, `SENSITIVE_DATA_DISCOVERY`, to run classification jobs. |

### UsageType
<a name="usage-model-usagetype"></a>

The name of an Amazon Macie usage metric for an account. Possible values are:
+ `DATA_INVENTORY_EVALUATION`
+ `SENSITIVE_DATA_DISCOVERY`
+ `AUTOMATED_SENSITIVE_DATA_DISCOVERY`
+ `AUTOMATED_OBJECT_MONITORING`

### ValidationException
<a name="usage-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="usage-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetUsageTotals
<a name="GetUsageTotals-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetUsageTotals)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetUsageTotals)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetUsageTotals)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetUsageTotals)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetUsageTotals)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetUsageTotals)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetUsageTotals)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetUsageTotals)
+ [AWS SDK for Python (Boto3)](/goto/boto3/macie2-2020-01-01/GetUsageTotals)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetUsageTotals)
