---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/templates.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Templates
<a name="templates"></a>

A *message template* is a set of content and settings that you can define, save, and reuse in email messages, push notifications, SMS text messages, and voice messages for any of your Amazon Pinpoint applications.

When you create a message template, you specify the content and settings that you want to reuse in various components of messages that are based on the template. These components, referred to as *template parts*, can be the message title or subject, the message body, or both, depending on the message type. A template part can also be a channel-specific setting, such as an image to display or a sound to play when a recipient receives a message that's based on the template. When you send a message that’s based on a template, Amazon Pinpoint populates the message with the content and settings that you defined in the template.

The Templates resource represents the repository of message templates that are associated with your Amazon Pinpoint account. You can use this resource to retrieve information about all the message templates that are associated with your account. To retrieve information about versions of a specific message template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html) resource.

## URI
<a name="templates-url"></a>

`/v1/templates`

## HTTP methods
<a name="templates-http-methods"></a>

### GET
<a name="templatesget"></a>

**Operation ID:** `ListTemplates`

Retrieves information about all the message templates that are associated with your Amazon Pinpoint account.

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| page-size | String | False | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. |
| next-token | String | False | The `` string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics. |
| prefix | String | False | The substring to match in the names of the message templates to include in the results. If you specify this value, Amazon Pinpoint returns only those templates whose names begin with the value that you specify. |
| template-type | String | False | The type of message template to include in the results. Valid values are: `EMAIL`, `PUSH`, `SMS`, and `VOICE`. To include all types of templates in the results, don't include this parameter in your request. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | TemplatesResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 409 | MessageBody | The request failed due to a conflict with the current state of the specified resource (ConflictException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="templatesoptions"></a>

Retrieves information about the communication requirements and options that are available for the Templates resource.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="templates-schemas"></a>

### Response bodies
<a name="templates-response-examples"></a>

#### TemplatesResponse schema
<a name="templates-response-body-templatesresponse-example"></a>

```
{
  "Item": [
    {
      "CreationDate": "string",
      "LastModifiedDate": "string",
      "TemplateType": enum,
      "TemplateName": "string",
      "TemplateDescription": "string",
      "DefaultSubstitutions": "string",
      "Version": "string",
      "tags": {
      },
      "Arn": "string"
    }
  ],
  "NextToken": "string"
}
```

#### MessageBody schema
<a name="templates-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="templates-properties"></a>

### MessageBody
<a name="templates-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### TemplateResponse
<a name="templates-model-templateresponse"></a>

Provides information about a message template that's associated with your Amazon Pinpoint account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Arn | string | False | The Amazon Resource Name (ARN) of the message template. This value isn't included in a `TemplateResponse` object. To retrieve the ARN of a template, use the `GetEmailTemplate`, `GetPushTemplate`, `GetSmsTemplate`, or `GetVoiceTemplate` operation, depending on the type of template that you want to retrieve the ARN for. |
| CreationDate | string | True | The date, in ISO 8601 format, when the message template was created. |
| DefaultSubstitutions | string | False | The JSON object that specifies the default values that are used for message variables in the message template. This object isn't included in a `TemplateResponse` object. To retrieve this object for a template, use the `GetEmailTemplate`, `GetPushTemplate`, `GetSmsTemplate`, or `GetVoiceTemplate` operation, depending on the type of template that you want to retrieve the object for. |
| LastModifiedDate | string | True | The date, in ISO 8601 format, when the message template was last modified. |
| tags | object | False | A map of key-value pairs that identifies the tags that are associated with the message template. This object isn't included in a `TemplateResponse` object. To retrieve this object for a template, use the `GetEmailTemplate`, `GetPushTemplate`, `GetSmsTemplate`, or `GetVoiceTemplate` operation, depending on the type of template that you want to retrieve the object for. |
| TemplateDescription | string | False | The custom description of the message template. This value isn't included in a `TemplateResponse` object. To retrieve the description of a template, use the `GetEmailTemplate`, `GetPushTemplate`, `GetSmsTemplate`, or `GetVoiceTemplate` operation, depending on the type of template that you want to retrieve the description for. |
| TemplateName | string | True | The name of the message template. |
| TemplateType | string<br />Values: `EMAIL \| SMS \| VOICE \| PUSH \| INAPP` | True | The type of channel that the message template is designed for. Possible values are: `EMAIL`, `PUSH`, `SMS`, `INAPP`, and `VOICE`. |
| Version | string | False | The unique identifier, as an integer, for the active version of the message template. |

### TemplatesResponse
<a name="templates-model-templatesresponse"></a>

Provides information about all the message templates that are associated with your Amazon Pinpoint account.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Item | Array of type [TemplateResponse](#templates-model-templateresponse) | True | An array of responses, one for each message template that's associated with your Amazon Pinpoint account and meets any filter criteria that you specified in the request. |
| NextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |

## See also
<a name="templates-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListTemplates
<a name="ListTemplates-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/ListTemplates)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/ListTemplates)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/ListTemplates)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/ListTemplates)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/ListTemplates)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/ListTemplates)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/ListTemplates)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/ListTemplates)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/ListTemplates)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/ListTemplates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
