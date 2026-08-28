---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Apps
<a name="apps"></a>

An *app* represents an Amazon Pinpoint application, also referred to as a *project*, in which you define an audience and you engage this audience with tailored messages. For example, you can use an application to send push notifications to users of your iOS or Android app, send email to newsletter subscribers, or send SMS messages to your customers' mobile phones.

After you create an application, you can define your audience by registering endpoints and defining segments. To engage your audience, define campaigns or write direct messages, and send your messages by using any supported channel, including channels for mobile push notifications, email, SMS, and voice. You can then monitor application analytics by creating an event stream, which streams data for message deliveries and events that your app reports to Amazon Pinpoint. Analytics are also provided on the Amazon Pinpoint console.

You can use the Apps resource to create a new application or retrieve information about all of your existing applications. To delete an application, use the [App](apps-application-id.md) resource and send a DELETE request to the `/apps/{{application-id}} ` URI.

## URI
<a name="apps-url"></a>

`/v1/apps`

## HTTP methods
<a name="apps-http-methods"></a>

### GET
<a name="appsget"></a>

**Operation ID:** `GetApps`

Retrieves information about all the applications that are associated with your Amazon Pinpoint account.

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| token | String | False | The `NextToken` string that specifies which page of results to return in a paginated response. |
| page-size | String | False | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ApplicationsResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### POST
<a name="appspost"></a>

**Operation ID:** `CreateApp`

Creates an application.

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | ApplicationResponse | The request succeeded and the specified resource was created. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="appsoptions"></a>

Retrieves information about the communication requirements and options that are available for the Apps resource.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-schemas"></a>

### Request bodies
<a name="apps-request-examples"></a>

#### POST schema
<a name="apps-request-body-post-example"></a>

```
{
  "Name": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="apps-response-examples"></a>

#### ApplicationsResponse schema
<a name="apps-response-body-applicationsresponse-example"></a>

```
{
  "NextToken": "string",
  "Item": [
    {
      "Name": "string",
      "Id": "string",
      "Arn": "string",
      "CreationDate": "string",
      "tags": {
      }
    }
  ]
}
```

#### ApplicationResponse schema
<a name="apps-response-body-applicationresponse-example"></a>

```
{
  "Name": "string",
  "Id": "string",
  "Arn": "string",
  "CreationDate": "string",
  "tags": {
  }
}
```

#### MessageBody schema
<a name="apps-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-properties"></a>

### ApplicationResponse
<a name="apps-model-applicationresponse"></a>

Provides information about an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Arn | string | True | The Amazon Resource Name (ARN) of the application. |
| CreationDate | string | False | The creation date for the application. |
| Id | string | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |
| Name | string | True | The display name of the application. This name is displayed as the **Project name** on the Amazon Pinpoint console. |
| tags | object | False | A string-to-string map of key-value pairs that identifies the tags that are associated with the application. Each tag consists of a required tag key and an associated tag value. |

### ApplicationsResponse
<a name="apps-model-applicationsresponse"></a>

Provides information about all of your applications.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Item | Array of type [ApplicationResponse](#apps-model-applicationresponse) | False | An array of responses, one for each application that was returned. |
| NextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

### CreateApplicationRequest
<a name="apps-model-createapplicationrequest"></a>

Specifies the display name of an application and the tags to associate with the application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Name | string | True | The display name of the application. This name is displayed as the **Project name** on the Amazon Pinpoint console. |
| tags | object | False | A string-to-string map of key-value pairs that defines the tags to associate with the application. Each tag consists of a required tag key and an associated tag value. |

### MessageBody
<a name="apps-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

## See also
<a name="apps-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetApps
<a name="GetApps-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetApps)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetApps)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetApps)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetApps)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetApps)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetApps)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetApps)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetApps)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetApps)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetApps)

### CreateApp
<a name="CreateApp-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/CreateApp)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/CreateApp)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/CreateApp)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/CreateApp)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/CreateApp)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/CreateApp)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/CreateApp)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/CreateApp)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/CreateApp)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/CreateApp)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
