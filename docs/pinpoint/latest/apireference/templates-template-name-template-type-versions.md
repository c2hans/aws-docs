---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Template Versions
<a name="templates-template-name-template-type-versions"></a>

A *message template* is a set of content and settings that you can define, save, and reuse in email messages, push notifications, SMS text messages, and voice messages for any of your Amazon Pinpoint applications. To help you develop and maintain templates, Amazon Pinpoint supports versioning for all types of message templates.

Each time you update a template, Amazon Pinpoint automatically saves your changes to (overwrites) the latest existing version of the template, unless you choose to create a new version of the template. Each version of a template is a snapshot of the template that you can use in a message.

The Template Versions resource provides information about all the versions of a specific message template. This information includes the unique identifier, creation and modification dates, and settings for each version of the template.

You can use the Template Versions resource to retrieve information about all the versions of a specific message template.

## URI
<a name="templates-template-name-template-type-versions-url"></a>

`/v1/templates/{{template-name}}/{{template-type}}/versions`

## HTTP methods
<a name="templates-template-name-template-type-versions-http-methods"></a>

### GET
<a name="templates-template-name-template-type-versionsget"></a>

**Operation ID:** `ListTemplateVersions`

Retrieves information about all the versions of a specific message template.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{template-name}} | String | True | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (\_), or hyphens (-). Template names are case sensitive. |
| {{template-type}} | String | True | The type of channel that the message template is designed for. Valid values are: `EMAIL`, `PUSH`, `SMS`, and `VOICE`. |

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
| 200 | TemplateVersionsResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="templates-template-name-template-type-versionsoptions"></a>

Retrieves information about the communication requirements and options that are available for the Template Versions resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{template-name}} | String | True | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (\_), or hyphens (-). Template names are case sensitive. |
| {{template-type}} | String | True | The type of channel that the message template is designed for. Valid values are: `EMAIL`, `PUSH`, `SMS`, and `VOICE`. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="templates-template-name-template-type-versions-schemas"></a>

### Response bodies
<a name="templates-template-name-template-type-versions-response-examples"></a>

#### TemplateVersionsResponse schema
<a name="templates-template-name-template-type-versions-response-body-templateversionsresponse-example"></a>

```
{
  "RequestID": "string",
  "Message": "string",
  "Item": [
    {
      "TemplateName": "string",
      "TemplateType": "string",
      "CreationDate": "string",
      "LastModifiedDate": "string",
      "TemplateDescription": "string",
      "DefaultSubstitutions": "string",
      "Version": "string"
    }
  ],
  "NextToken": "string"
}
```

#### MessageBody schema
<a name="templates-template-name-template-type-versions-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="templates-template-name-template-type-versions-properties"></a>

### MessageBody
<a name="templates-template-name-template-type-versions-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### TemplateVersionResponse
<a name="templates-template-name-template-type-versions-model-templateversionresponse"></a>

Provides information about a specific version of a message template.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| CreationDate | string | True | The date, in ISO 8601 format, when the version of the message template was created. |
| DefaultSubstitutions | string | False | A JSON object that specifies the default values that are used for message variables in the version of the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. |
| LastModifiedDate | string | True | The date, in ISO 8601 format, when the version of the message template was last modified. |
| TemplateDescription | string | False | The custom description of the version of the message template. |
| TemplateName | string | True | The name of the message template. |
| TemplateType | string | True | The type of channel that the message template is designed for. Possible values are: `EMAIL`, `PUSH`, `SMS`, `INAPP`, and `VOICE`. |
| Version | string | False | The unique identifier for the version of the message template. This value is an integer that Amazon Pinpoint automatically increments and assigns to each new version of a template. |

### TemplateVersionsResponse
<a name="templates-template-name-template-type-versions-model-templateversionsresponse"></a>

Provides information about all the versions of a specific message template.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Item | Array of type [TemplateVersionResponse](#templates-template-name-template-type-versions-model-templateversionresponse) | True | An array of responses, one for each version of the message template. |
| Message | string | False | The message that's returned from the API for the request to retrieve information about all the versions of the message template. |
| NextToken | string | False | The string to use in a subsequent request to get the next page of results in a paginated response. This value is null if there are no additional pages. |
| RequestID | string | False | The unique identifier for the request to retrieve information about all the versions of the message template. |

## See also
<a name="templates-template-name-template-type-versions-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListTemplateVersions
<a name="ListTemplateVersions-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/ListTemplateVersions)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/ListTemplateVersions)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/ListTemplateVersions)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/ListTemplateVersions)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/ListTemplateVersions)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/ListTemplateVersions)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/ListTemplateVersions)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/ListTemplateVersions)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/ListTemplateVersions)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/ListTemplateVersions)
