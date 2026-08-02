---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-journeys-journey-id-runs.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Journey Runs
<a name="apps-application-id-journeys-journey-id-runs"></a>

A *journey* is an automated workflow that performs a series of messaging activities for an Amazon Pinpoint application. A journey run represents each scheduled entry of endpoints into the journey. The journey run resource provides information about each journey run, including timing information and status.

Each journey run represents a single evaluation of a segment, so can include endpoints in different timezones. These endpoints may actually enter the journey at different times, depending on their timezones, but each are represented by the same journey run.

## URI
<a name="apps-application-id-journeys-journey-id-runs-url"></a>

`/v1/apps/{{application-id}}/journeys/{{journey-id}}/runs`

## HTTP methods
<a name="apps-application-id-journeys-journey-id-runs-http-methods"></a>

### GET
<a name="apps-application-id-journeys-journey-id-runsget"></a>

**Operation ID:** `GetJourneyRuns`

Provides information about the runs of a journey.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
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
| token | String | False | The `NextToken` string that specifies which page of results to return in a paginated response. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | JourneyRunsResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-journeys-journey-id-runsoptions"></a>

Retrieves information about the communication requirements and options that are available for the Journey Run resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{journey-id}} | String | True | The unique identifier for the journey. |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-journeys-journey-id-runs-schemas"></a>

### Response bodies
<a name="apps-application-id-journeys-journey-id-runs-response-examples"></a>

#### JourneyRunsResponse schema
<a name="apps-application-id-journeys-journey-id-runs-response-body-journeyrunsresponse-example"></a>

```
{
  "NextToken": "string",
  "Item": [
    {
      "RunId": "string",
      "CreationTime": "string",
      "LastUpdateTime": "string",
      "Status": enum
    }
  ]
}
```

#### MessageBody schema
<a name="apps-application-id-journeys-journey-id-runs-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-journeys-journey-id-runs-properties"></a>

### JourneyRunResponse
<a name="apps-application-id-journeys-journey-id-runs-model-journeyrunresponse"></a>

Provides information from a specified run of a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| CreationTime | string | True | The time when the journey run was created or scheduled, in ISO 8601 format. |
| LastUpdateTime | string | True | The last time the journey run was updated, in ISO 8601 format.. |
| RunId | string | True | The unique identifier for the run. |
| Status | string<br />Values: `SCHEDULED \| RUNNING \| COMPLETED \| CANCELLED` | True | The current status of the run. |

### JourneyRunsResponse
<a name="apps-application-id-journeys-journey-id-runs-model-journeyrunsresponse"></a>

Provides information from all runs of a journey.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Item | Array of type [JourneyRunResponse](#apps-application-id-journeys-journey-id-runs-model-journeyrunresponse) | True | An array of responses, one for each run of the journey |
| NextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### MessageBody
<a name="apps-application-id-journeys-journey-id-runs-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

## See also
<a name="apps-application-id-journeys-journey-id-runs-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetJourneyRuns
<a name="GetJourneyRuns-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetJourneyRuns)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetJourneyRuns)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetJourneyRuns)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetJourneyRuns)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetJourneyRuns)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetJourneyRuns)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetJourneyRuns)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetJourneyRuns)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetJourneyRuns)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetJourneyRuns)
