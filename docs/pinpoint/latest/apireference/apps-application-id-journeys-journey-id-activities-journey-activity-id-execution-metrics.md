---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Journey Activity Execution Metrics
<a name="apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics"></a>

A *journey activity execution metric* is a measurable value, also referred to as a *key performance indicator (KPI)*, that can help you assess the status of participants in a journey activity. For example, you can use this type of metric to determine how many participants started and completed an activity. Amazon Pinpoint automatically collects, aggregates, and stores this data for all of your journey activities.

The Journey Activity Execution Metrics resource represents a collection of standard execution metrics that apply to an individual journey activity. As part of the Amazon Pinpoint Analytics APIs, this resource provides you with programmatic access to pre-aggregated data for each of these metrics. For a list of metrics that are currently supported, see the [Amazon Pinpoint Developer Guide](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html).

You can use the Journey Activity Execution Metrics resource to retrieve pre-aggregated data for standard execution metrics that apply to a journey activity.

## URI
<a name="apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics-url"></a>

`/v1/apps/{{application-id}}/journeys/{{journey-id}}/activities/{{journey-activity-id}}/execution-metrics`

## HTTP methods
<a name="apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics-http-methods"></a>

### GET
<a name="apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metricsget"></a>

**Operation ID:** `GetJourneyExecutionActivityMetrics`

Retrieves (queries) pre-aggregated data for a standard execution metric that applies to a journey activity.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{journey-activity-id}} | String | True | The unique identifier for the journey activity. |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |
| {{journey-id}} | String | True | The unique identifier for the journey. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| page-size | String | False | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. |
| next-token | String | False | The `` string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | JourneyExecutionActivityMetricsResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metricsoptions"></a>

Retrieves information about the communication requirements and options that are available for the Journey Activity Execution Metrics resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{journey-activity-id}} | String | True | The unique identifier for the journey activity. |
| {{journey-id}} | String | True | The unique identifier for the journey. |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics-schemas"></a>

### Response bodies
<a name="apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics-response-examples"></a>

#### JourneyExecutionActivityMetricsResponse schema
<a name="apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics-response-body-journeyexecutionactivitymetricsresponse-example"></a>

```
{
  "ApplicationId": "string",
  "JourneyId": "string",
  "JourneyActivityId": "string",
  "ActivityType": "string",
  "LastEvaluatedTime": "string",
  "Metrics": {
  }
}
```

#### MessageBody schema
<a name="apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics-properties"></a>

### JourneyExecutionActivityMetricsResponse
<a name="apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics-model-journeyexecutionactivitymetricsresponse"></a>

Provides the results of a query that retrieved the data for a standard execution metric that applies to a journey activity, and provides information about that query.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ActivityType | string | True | The type of activity that the metric applies to. Possible values are:   `CONDITIONAL_SPLIT` – For a yes/no split activity, which is an activity that sends participants down one of two paths in a journey.    `HOLDOUT` – For a holdout activity, which is an activity that stops a journey for a specified percentage of participants.    `MESSAGE` – For an email activity, which is an activity that sends an email message to participants.    `MULTI_CONDITIONAL_SPLIT` – For a multivariate split activity, which is an activity that sends participants down one of as many as five paths in a journey.    `RANDOM_SPLIT` – For a random split activity, which is an activity that sends specified percentages of participants down one of as many as five paths in a journey.    `WAIT` – For a wait activity, which is an activity that waits for a certain amount of time or until a specific date and time before moving participants to the next activity in a journey.   |
| ApplicationId | string | True | The unique identifier for the application that the metric applies to. |
| JourneyActivityId | string | True | The unique identifier for the activity that the metric applies to. |
| JourneyId | string | True | The unique identifier for the journey that the metric applies to. |
| LastEvaluatedTime | string | True | The date and time, in ISO 8601 format, when Amazon Pinpoint last evaluated the execution status of the activity and updated the data for the metric. |
| Metrics | object | True | A JSON object that contains the results of the query. The results vary depending on the type of activity (`ActivityType`). For information about the structure and contents of the results, see the [Amazon Pinpoint Developer Guide](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html). |

### MessageBody
<a name="apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

## See also
<a name="apps-application-id-journeys-journey-id-activities-journey-activity-id-execution-metrics-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetJourneyExecutionActivityMetrics
<a name="GetJourneyExecutionActivityMetrics-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetJourneyExecutionActivityMetrics)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetJourneyExecutionActivityMetrics)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetJourneyExecutionActivityMetrics)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetJourneyExecutionActivityMetrics)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetJourneyExecutionActivityMetrics)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetJourneyExecutionActivityMetrics)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetJourneyExecutionActivityMetrics)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetJourneyExecutionActivityMetrics)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetJourneyExecutionActivityMetrics)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetJourneyExecutionActivityMetrics)
