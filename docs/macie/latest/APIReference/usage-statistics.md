---
source_url: https://docs.aws.amazon.com/macie/latest/APIReference/usage-statistics.html
---

# Usage Statistics
<a name="usage-statistics"></a>

The Usage Statistics resource provides information about current quotas and usage statistics for your Amazon Macie account. This includes metrics that report the estimated cost of using Macie to perform specific types of tasks, and current account quotas for those tasks. The data can help you track your use of the service and determine whether to adjust your quotas or use of the service. For information about how Macie calculates usage statistics and data for your account, see [Forecasting and monitoring costs](https://docs.aws.amazon.com/macie/latest/user/account-mgmt-costs.html) in the *Amazon Macie User Guide*.

If you're participating in a 30-day free trial, the applicable cost estimates are based on your use of Macie thus far during the trial. They can help you understand what your usage costs might be after the trial ends. This resource also provides information about when each trial started for your account.

You can use the Usage Statistics resource to retrieve (query) aggregated data for usage metrics that apply to your Macie account and the quotas that correspond to those metrics. If you're the Macie administrator for an organization, this resource provides a breakdown of quota, usage, and free-trial data for individual member accounts in your organization.

To customize your query, you can use supported parameters to filter and sort the data. You can also specify a time range for the data. The time range can be the preceding 30 days or the current calendar month to date.

## URI
<a name="usage-statistics-url"></a>

`/usage/statistics`

## HTTP methods
<a name="usage-statistics-http-methods"></a>

### POST
<a name="usage-statisticspost"></a>

**Operation ID:** `GetUsageStatistics`

Retrieves (queries) quotas and aggregated usage data for one or more accounts.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetUsageStatisticsResponse | The request succeeded. |
| 400 | ValidationException | The request failed because the input doesn't satisfy the constraints specified by the service. |
| 402 | ServiceQuotaExceededException | The request failed because fulfilling the request would exceed one or more service quotas for your account. |
| 403 | AccessDeniedException | The request was denied because you don't have sufficient access to the specified resource. |
| 404 | ResourceNotFoundException | The request failed because the specified resource wasn't found. |
| 409 | ConflictException | The request failed because it conflicts with the current state of the specified resource. |
| 429 | ThrottlingException | The request failed because you sent too many requests during a certain amount of time. |
| 500 | InternalServerException | The request failed due to an unknown internal server error, exception, or failure. |

## Schemas
<a name="usage-statistics-schemas"></a>

### Request bodies
<a name="usage-statistics-request-examples"></a>

#### POST schema
<a name="usage-statistics-request-body-post-example"></a>

```
{
  "filterBy": [
    {
      "comparator": enum,
      "key": enum,
      "values": [
        "string"
      ]
    }
  ],
  "maxResults": integer,
  "nextToken": "string",
  "sortBy": {
    "key": enum,
    "orderBy": enum
  },
  "timeRange": enum
}
```

### Response bodies
<a name="usage-statistics-response-examples"></a>

#### GetUsageStatisticsResponse schema
<a name="usage-statistics-response-body-getusagestatisticsresponse-example"></a>

```
{
  "nextToken": "string",
  "records": [
    {
      "accountId": "string",
      "automatedDiscoveryFreeTrialStartDate": "string",
      "freeTrialStartDate": "string",
      "usage": [
        {
          "currency": enum,
          "estimatedCost": "string",
          "serviceLimit": {
            "isServiceLimited": boolean,
            "unit": enum,
            "value": integer
          },
          "type": enum
        }
      ]
    }
  ],
  "timeRange": enum
}
```

#### ValidationException schema
<a name="usage-statistics-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="usage-statistics-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="usage-statistics-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="usage-statistics-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="usage-statistics-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="usage-statistics-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="usage-statistics-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="usage-statistics-properties"></a>

### AccessDeniedException
<a name="usage-statistics-model-accessdeniedexception"></a>

Provides information about an error that occurred due to insufficient access to a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ConflictException
<a name="usage-statistics-model-conflictexception"></a>

Provides information about an error that occurred due to a versioning conflict for a specified resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### Currency
<a name="usage-statistics-model-currency"></a>

The type of currency that the data for an Amazon Macie usage metric is reported in. Possible values are:
+ `USD`

### GetUsageStatisticsRequest
<a name="usage-statistics-model-getusagestatisticsrequest"></a>

Specifies criteria for filtering, sorting, and paginating the results of a query for quotas and aggregated usage data for one or more Amazon Macie accounts.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| filterBy | Array of type [UsageStatisticsFilter](#usage-statistics-model-usagestatisticsfilter) | False | An array of objects, one for each condition to use to filter the query results. If you specify more than one condition, Amazon Macie uses an AND operator to join the conditions. |
| maxResults | integer<br />Format: int32 | False | The maximum number of items to include in each page of the response. |
| nextToken | string | False | The `nextToken` string that specifies which page of results to return in a paginated response. |
| sortBy | [UsageStatisticsSortBy](#usage-statistics-model-usagestatisticssortby) | False | The criteria to use to sort the query results. |
| timeRange | [TimeRange](#usage-statistics-model-timerange) | False | The inclusive time period to query usage data for. Valid values are: `MONTH_TO_DATE`, for the current calendar month to date; and, `PAST_30_DAYS`, for the preceding 30 days. If you don't specify a value, Amazon Macie provides usage data for the preceding 30 days. |

### GetUsageStatisticsResponse
<a name="usage-statistics-model-getusagestatisticsresponse"></a>

Provides the results of a query that retrieved quotas and aggregated usage data for one or more Amazon Macie accounts.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |
| records | Array of type [UsageRecord](#usage-statistics-model-usagerecord) | False | An array of objects that contains the results of the query. Each object contains the data for an account that matches the filter criteria specified in the request. |
| timeRange | [TimeRange](#usage-statistics-model-timerange) | False | The inclusive time period that the usage data applies to. Possible values are: `MONTH_TO_DATE`, for the current calendar month to date; and, `PAST_30_DAYS`, for the preceding 30 days. |

### InternalServerException
<a name="usage-statistics-model-internalserverexception"></a>

Provides information about an error that occurred due to an unknown internal server error, exception, or failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ResourceNotFoundException
<a name="usage-statistics-model-resourcenotfoundexception"></a>

Provides information about an error that occurred because a specified resource wasn't found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ServiceLimit
<a name="usage-statistics-model-servicelimit"></a>

Specifies a current quota for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| isServiceLimited | boolean | False | Specifies whether the account has met the quota that corresponds to the metric specified by the `UsageByAccount.type` field in the response. |
| unit | string<br />Values: `TERABYTES` | False | The unit of measurement for the value specified by the `value` field. |
| value | integer<br />Format: int64 | False | The value for the metric specified by the `UsageByAccount.type` field in the response. |

### ServiceQuotaExceededException
<a name="usage-statistics-model-servicequotaexceededexception"></a>

Provides information about an error that occurred due to one or more service quotas for an account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### ThrottlingException
<a name="usage-statistics-model-throttlingexception"></a>

Provides information about an error that occurred because too many requests were sent during a certain amount of time.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

### TimeRange
<a name="usage-statistics-model-timerange"></a>

An inclusive time period that Amazon Macie usage data applies to. Possible values are:
+ `MONTH_TO_DATE`
+ `PAST_30_DAYS`

### UsageByAccount
<a name="usage-statistics-model-usagebyaccount"></a>

Provides data for a specific usage metric and the corresponding quota for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| currency | [Currency](#usage-statistics-model-currency) | False | The type of currency that the value for the metric (`estimatedCost`) is reported in. |
| estimatedCost | string | False | The estimated value for the metric. |
| serviceLimit | [ServiceLimit](#usage-statistics-model-servicelimit) | False | The current value for the quota that corresponds to the metric specified by the `type` field. |
| type | [UsageType](#usage-statistics-model-usagetype) | False | The name of the metric. Possible values are: `AUTOMATED_OBJECT_MONITORING`, to monitor S3 objects for automated sensitive data discovery; `AUTOMATED_SENSITIVE_DATA_DISCOVERY`, to analyze S3 objects for automated sensitive data discovery; `DATA_INVENTORY_EVALUATION`, to monitor S3 buckets; and, `SENSITIVE_DATA_DISCOVERY`, to run classification jobs. |

### UsageRecord
<a name="usage-statistics-model-usagerecord"></a>

Provides quota and aggregated usage data for an Amazon Macie account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accountId | string | False | The unique identifier for the AWS account that the data applies to. |
| automatedDiscoveryFreeTrialStartDate | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the free trial of automated sensitive data discovery started for the account. This value is null if automated sensitive data discovery hasn't been enabled for the account. |
| freeTrialStartDate | string<br />Format: date-time | False | The date and time, in UTC and extended ISO 8601 format, when the Amazon Macie free trial started for the account. |
| usage | Array of type [UsageByAccount](#usage-statistics-model-usagebyaccount) | False | An array of objects that contains usage data and quotas for the account. Each object contains the data for a specific usage metric and the corresponding quota. |

### UsageStatisticsFilter
<a name="usage-statistics-model-usagestatisticsfilter"></a>

Specifies a condition for filtering the results of a query for quota and usage data for one or more Amazon Macie accounts.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| comparator | [UsageStatisticsFilterComparator](#usage-statistics-model-usagestatisticsfiltercomparator) | False | The operator to use in the condition. If the value for the `key` property is `accountId`, this value must be `CONTAINS`. If the value for the `key` property is any other supported field, this value can be `EQ`, `GT`, `GTE`, `LT`, `LTE`, or `NE`. |
| key | [UsageStatisticsFilterKey](#usage-statistics-model-usagestatisticsfilterkey) | False | The field to use in the condition. |
| values | Array of type string | False | An array that lists values to use in the condition, based on the value for the field specified by the `key` property. If the value for the `key` property is `accountId`, this array can specify multiple values. Otherwise, this array can specify only one value.<br />Valid values for each supported field are:+   `accountId` - The unique identifier for an AWS account. <br />+   `freeTrialStartDate` - The date and time, in UTC and extended ISO 8601 format, when the Amazon Macie free trial started for an account. <br />+   `serviceLimit` - A Boolean (`true` or `false`) value that indicates whether an account has reached its monthly quota. <br />+   `total` - A string that represents the current estimated cost for an account.  |

### UsageStatisticsFilterComparator
<a name="usage-statistics-model-usagestatisticsfiltercomparator"></a>

The operator to use in a condition that filters the results of a query for Amazon Macie account quotas and usage data. Valid values are:
+ `GT`
+ `GTE`
+ `LT`
+ `LTE`
+ `EQ`
+ `NE`
+ `CONTAINS`

### UsageStatisticsFilterKey
<a name="usage-statistics-model-usagestatisticsfilterkey"></a>

The field to use in a condition that filters the results of a query for Amazon Macie account quotas and usage data. Valid values are:
+ `accountId`
+ `serviceLimit`
+ `freeTrialStartDate`
+ `total`

### UsageStatisticsSortBy
<a name="usage-statistics-model-usagestatisticssortby"></a>

Specifies criteria for sorting the results of a query for Amazon Macie account quotas and usage data.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| key | [UsageStatisticsSortKey](#usage-statistics-model-usagestatisticssortkey) | False | The field to sort the results by. |
| orderBy | string<br />Values: `ASC \| DESC` | False | The sort order to apply to the results, based on the value for the field specified by the `key` property. Valid values are: `ASC`, sort the results in ascending order; and, `DESC`, sort the results in descending order. |

### UsageStatisticsSortKey
<a name="usage-statistics-model-usagestatisticssortkey"></a>

The field to use to sort the results of a query for Amazon Macie account quotas and usage data. Valid values are:
+ `accountId`
+ `total`
+ `serviceLimitValue`
+ `freeTrialStartDate`

### UsageType
<a name="usage-statistics-model-usagetype"></a>

The name of an Amazon Macie usage metric for an account. Possible values are:
+ `DATA_INVENTORY_EVALUATION`
+ `SENSITIVE_DATA_DISCOVERY`
+ `AUTOMATED_SENSITIVE_DATA_DISCOVERY`
+ `AUTOMATED_OBJECT_MONITORING`

### ValidationException
<a name="usage-statistics-model-validationexception"></a>

Provides information about an error that occurred due to a syntax error in a request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The explanation of the error that occurred. |

## See also
<a name="usage-statistics-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetUsageStatistics
<a name="GetUsageStatistics-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/macie2-2020-01-01/GetUsageStatistics)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/macie2-2020-01-01/GetUsageStatistics)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/macie2-2020-01-01/GetUsageStatistics)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/macie2-2020-01-01/GetUsageStatistics)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/macie2-2020-01-01/GetUsageStatistics)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/macie2-2020-01-01/GetUsageStatistics)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/macie2-2020-01-01/GetUsageStatistics)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/macie2-2020-01-01/GetUsageStatistics)
+ [AWS SDK for Python](/goto/boto3/macie2-2020-01-01/GetUsageStatistics)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/macie2-2020-01-01/GetUsageStatistics)
