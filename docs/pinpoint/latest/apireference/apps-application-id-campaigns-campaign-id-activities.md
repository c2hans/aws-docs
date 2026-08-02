---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id-activities.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Campaign Activities
<a name="apps-application-id-campaigns-campaign-id-activities"></a>

A *campaign* represents a messaging initiative that engages a specific segment of users for an Amazon Pinpoint application. The Campaign Activities resource provides information about the activities that were performed by a campaign, such as the time during which the campaign ran and the number of endpoints that the campaign delivered messages to.

You can use this resource to retrieve information about the activities that were performed by a specific campaign.

## URI
<a name="apps-application-id-campaigns-campaign-id-activities-url"></a>

`/v1/apps/{{application-id}}/campaigns/{{campaign-id}}/activities`

## HTTP methods
<a name="apps-application-id-campaigns-campaign-id-activities-http-methods"></a>

### GET
<a name="apps-application-id-campaigns-campaign-id-activitiesget"></a>

**Operation ID:** `GetCampaignActivities`

Retrieves information about all the activities for a campaign.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |
| {{campaign-id}} | String | True | The unique identifier for the campaign. |

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
| 200 | ActivitiesResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-campaigns-campaign-id-activitiesoptions"></a>

Retrieves information about the communication requirements and options that are available for the Campaign Activities resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{campaign-id}} | String | True | The unique identifier for the campaign. |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-campaigns-campaign-id-activities-schemas"></a>

### Response bodies
<a name="apps-application-id-campaigns-campaign-id-activities-response-examples"></a>

#### ActivitiesResponse schema
<a name="apps-application-id-campaigns-campaign-id-activities-response-body-activitiesresponse-example"></a>

```
{
  "NextToken": "string",
  "Item": [
    {
      "Id": "string",
      "ApplicationId": "string",
      "CampaignId": "string",
      "TreatmentId": "string",
      "State": "string",
      "Result": "string",
      "ScheduledStart": "string",
      "Start": "string",
      "End": "string",
      "SuccessfulEndpointCount": integer,
      "TotalEndpointCount": integer,
      "TimezonesTotalCount": integer,
      "TimezonesCompletedCount": integer,
      "ExecutionMetrics": {
      }
    }
  ]
}
```

#### MessageBody schema
<a name="apps-application-id-campaigns-campaign-id-activities-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-campaigns-campaign-id-activities-properties"></a>

### ActivitiesResponse
<a name="apps-application-id-campaigns-campaign-id-activities-model-activitiesresponse"></a>

Provides information about the activities that were performed by a campaign.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Item | Array of type [ActivityResponse](#apps-application-id-campaigns-campaign-id-activities-model-activityresponse) | True | An array of responses, one for each activity that was performed by the campaign. |
| NextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### ActivityResponse
<a name="apps-application-id-campaigns-campaign-id-activities-model-activityresponse"></a>

Provides information about an activity that was performed by a campaign.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | True | The unique identifier for the application that the campaign applies to. |
| CampaignId | string | True | The unique identifier for the campaign that the activity applies to. |
| End | string | False | The actual time, in ISO 8601 format, when the activity was marked `CANCELLED` or `COMPLETED`. |
| ExecutionMetrics | object | False | A JSON object that contains metrics relating to the campaign execution for this campaign activity. For information about the structure and contents of the results, see [Standard Amazon Pinpoint analytics metrics](https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html) in the *Amazon Pinpoint Developer Guide*. |
| Id | string | True | The unique identifier for the activity. |
| Result | string | False | Specifies whether the activity succeeded. Possible values are `SUCCESS` and `FAIL`. |
| ScheduledStart | string | False | The scheduled start time, in ISO 8601 format, for the activity. |
| Start | string | False | The actual start time, in ISO 8601 format, of the activity. |
| State | string | False | The current status of the activity. Possible values are: `PENDING`, `INITIALIZING`, `RUNNING`, `PAUSED`, `CANCELLED`, and `COMPLETED`. |
| SuccessfulEndpointCount | integer | False | The total number of endpoints that the campaign successfully delivered messages to. |
| TimezonesCompletedCount | integer | False | The total number of time zones that were completed. |
| TimezonesTotalCount | integer | False | The total number of unique time zones that are in the segment for the campaign. |
| TotalEndpointCount | integer | False | The total number of endpoints that the campaign attempted to deliver messages to. |
| TreatmentId | string | False | The unique identifier for the campaign treatment that the activity applies to. A treatment is a variation of a campaign that's used for A/B testing of a campaign. |

### MessageBody
<a name="apps-application-id-campaigns-campaign-id-activities-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

## See also
<a name="apps-application-id-campaigns-campaign-id-activities-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetCampaignActivities
<a name="GetCampaignActivities-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetCampaignActivities)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetCampaignActivities)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetCampaignActivities)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetCampaignActivities)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetCampaignActivities)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetCampaignActivities)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetCampaignActivities)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetCampaignActivities)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetCampaignActivities)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetCampaignActivities)
