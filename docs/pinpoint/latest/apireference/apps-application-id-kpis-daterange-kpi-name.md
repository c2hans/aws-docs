---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-kpis-daterange-kpi-name.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Application Metrics
<a name="apps-application-id-kpis-daterange-kpi-name"></a>

An *application metric* is a measurable value, also referred to as a *key performance indicator (KPI)*, that can help you monitor and assess trends related to user engagement, campaign outreach, and more for an application. For example, you can use an application metric to see a breakdown of the number of campaign messages that were opened by recipients for each campaign that's associated with an Amazon Pinpoint application. Amazon Pinpoint automatically collects, aggregates, and stores this data for all of your applications. If you integrated a mobile app with Amazon Pinpoint by using an AWS Mobile SDK, Amazon Pinpoint extends this support to include additional metrics, such as a breakdown of the percentage of push notifications that were opened by recipients of each campaign. For information about integrating a mobile app, see [Integrating Amazon Pinpoint with Your Application](https://docs.aws.amazon.com/pinpoint/latest/developerguide/integrate.html) in the *Amazon Pinpoint Developer Guide*.

The Application Metrics resource represents a collection of standard metrics that apply to an Amazon Pinpoint application. As part of the Amazon Pinpoint Analytics APIs, this resource provides you with programmatic access to pre-aggregated data for each of these metrics. For a list of application metrics that are currently supported, see the [Amazon Pinpoint Developer Guide](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html).

You can use the Application Metrics resource to retrieve pre-aggregated data for a standard metric that applies to an application.

## URI
<a name="apps-application-id-kpis-daterange-kpi-name-url"></a>

`/v1/apps/{{application-id}}/kpis/daterange/{{kpi-name}}`

## HTTP methods
<a name="apps-application-id-kpis-daterange-kpi-name-http-methods"></a>

### GET
<a name="apps-application-id-kpis-daterange-kpi-nameget"></a>

**Operation ID:** `GetApplicationDateRangeKpi`

Retrieves (queries) pre-aggregated data for a standard metric that applies to an application.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |
| {{kpi-name}} | String | True | The name of the metric, also referred to as a *key performance indicator (KPI)*, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are `email-open-rate` and `successful-delivery-rate`. For a list of valid values, see the [Amazon Pinpoint Developer Guide](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html). |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| next-token | String | False | The `` string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics. |
| end-time | String | False | The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: `2019-07-26T20:00:00Z` for 8:00 PM UTC July 26, 2019. |
| start-time | String | False | The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: `2019-07-19T20:00:00Z` for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day. |
| page-size | String | False | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ApplicationDateRangeKpiResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-kpis-daterange-kpi-nameoptions"></a>

Retrieves information about the communication requirements and options that are available for the Application Metrics resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |
| {{kpi-name}} | String | True | The name of the metric, also referred to as a *key performance indicator (KPI)*, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are `email-open-rate` and `successful-delivery-rate`. For a list of valid values, see the [Amazon Pinpoint Developer Guide](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html). |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-kpis-daterange-kpi-name-schemas"></a>

### Response bodies
<a name="apps-application-id-kpis-daterange-kpi-name-response-examples"></a>

#### ApplicationDateRangeKpiResponse schema
<a name="apps-application-id-kpis-daterange-kpi-name-response-body-applicationdaterangekpiresponse-example"></a>

```
{
  "KpiName": "string",
  "KpiResult": {
    "Rows": [
      {
        "GroupedBys": [
          {
            "Key": "string",
            "Value": "string",
            "Type": "string"
          }
        ],
        "Values": [
          {
            "Key": "string",
            "Value": "string",
            "Type": "string"
          }
        ]
      }
    ]
  },
  "NextToken": "string",
  "ApplicationId": "string",
  "StartTime": "string",
  "EndTime": "string"
}
```

#### MessageBody schema
<a name="apps-application-id-kpis-daterange-kpi-name-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-kpis-daterange-kpi-name-properties"></a>

### ApplicationDateRangeKpiResponse
<a name="apps-application-id-kpis-daterange-kpi-name-model-applicationdaterangekpiresponse"></a>

Provides the results of a query that retrieved the data for a standard metric that applies to an application, and provides information about that query.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | True | The unique identifier for the application that the metric applies to. |
| EndTime | string | True | The last date and time of the date range that was used to filter the query results, in extended ISO 8601 format. The date range is inclusive. |
| KpiName | string | True | The name of the metric, also referred to as a *key performance indicator (KPI)*, that the data was retrieved for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. For a list of possible values, see the [Amazon Pinpoint Developer Guide](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html). |
| KpiResult | [BaseKpiResult](#apps-application-id-kpis-daterange-kpi-name-model-basekpiresult) | True | An array of objects that contains the results of the query. Each object contains the value for the metric and metadata about that value. |
| NextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null for the Application Metrics resource because the resource returns all results in a single page. |
| StartTime | string | True | The first date and time of the date range that was used to filter the query results, in extended ISO 8601 format. The date range is inclusive. |

### BaseKpiResult
<a name="apps-application-id-kpis-daterange-kpi-name-model-basekpiresult"></a>

Provides the results of a query that retrieved the data for a standard metric that applies to an application, campaign, or journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Rows | Array of type [ResultRow](#apps-application-id-kpis-daterange-kpi-name-model-resultrow) | True | An array of objects that provides the results of a query that retrieved the data for a standard metric that applies to an application, campaign, or journey. |

### MessageBody
<a name="apps-application-id-kpis-daterange-kpi-name-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### ResultRow
<a name="apps-application-id-kpis-daterange-kpi-name-model-resultrow"></a>

Provides the results of a query that retrieved the data for a standard metric that applies to an application, campaign, or journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| GroupedBys | Array of type [ResultRowValue](#apps-application-id-kpis-daterange-kpi-name-model-resultrowvalue) | True | An array of objects that defines the field and field values that were used to group data in a result set that contains multiple results. This value is null if the data in a result set isn’t grouped. |
| Values | Array of type [ResultRowValue](#apps-application-id-kpis-daterange-kpi-name-model-resultrowvalue) | True | An array of objects that provides pre-aggregated values for a standard metric that applies to an application, campaign, or journey. |

### ResultRowValue
<a name="apps-application-id-kpis-daterange-kpi-name-model-resultrowvalue"></a>

Provides a single value and metadata about that value as part of an array of query results for a standard metric that applies to an application, campaign, or journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Key | string | True | The friendly name of the metric whose value is specified by the `Value` property. |
| Type | string | True | The data type of the value specified by the `Value` property. |
| Value | string | True | In a `Values` object, the value for the metric that the query retrieved data for. In a `GroupedBys` object, the value for the field that was used to group data in a result set that contains multiple results (`Values` objects). |

## See also
<a name="apps-application-id-kpis-daterange-kpi-name-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetApplicationDateRangeKpi
<a name="GetApplicationDateRangeKpi-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetApplicationDateRangeKpi)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetApplicationDateRangeKpi)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetApplicationDateRangeKpi)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetApplicationDateRangeKpi)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetApplicationDateRangeKpi)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetApplicationDateRangeKpi)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetApplicationDateRangeKpi)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetApplicationDateRangeKpi)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetApplicationDateRangeKpi)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetApplicationDateRangeKpi)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
