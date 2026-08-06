---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-inapp.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# In-App Template
<a name="templates-template-name-inapp"></a>

An *in-app messaging template* is a type of message template that contains content and settings that you can define, save, and reuse in messages that you send to users of your applications.

When you create an in-app messaging template, you specify the layout of the message and the content contained in the message. You can also change the color and position of the message text, add buttons to the message, and add images to the message.

The In-App Template resource represents the repository of in-app messaging templates that are associated with your Amazon Pinpoint account. You can use this resource to create, retrieve, update, or delete a message template for messages that you send through the in-app messaging channel.

Amazon Pinpoint supports versioning for all types of message templates. When you use the In-App Template resource to work with a template, you can use supported parameters to specify whether your request applies to only a specific version of the template or to the overall template. For example, if you update a template, you can specify whether you want to save your updates as a new version of the template or save them to the latest existing version of the template. To retrieve information about all the versions of a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html) resource.

## URI
<a name="templates-template-name-inapp-url"></a>

`/v1/templates/{{template-name}}/inapp`

## HTTP methods
<a name="templates-template-name-inapp-http-methods"></a>

### GET
<a name="templates-template-name-inappget"></a>

**Operation ID:** `GetInAppTemplate`

Retrieves the content and configuration of an in-app message template.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{template-name}} | String | True | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (\_), or hyphens (-). Template names are case sensitive. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| version | String | False | The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html)resource.<br />If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.<br />If you don't specify a value for this parameter, Amazon Pinpoint does the following:+  For a get operation, retrieves information about the active version of the template. <br />+  For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the `create-new-version` parameter isn't used or is set to `false`. <br />+  For a delete operation, deletes the template, including all versions of the template.  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | InAppTemplateResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### POST
<a name="templates-template-name-inapppost"></a>

**Operation ID:** `CreateInAppTemplate`

Creates a new in-app message template.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{template-name}} | String | True | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (\_), or hyphens (-). Template names are case sensitive. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | TemplateCreateMessageBody | The request succeeded and the specified resource was created. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 409 | MessageBody | The request failed due to a conflict with the current state of the specified resource (ConflictException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### PUT
<a name="templates-template-name-inappput"></a>

**Operation ID:** `UpdateInAppTemplate`

Updates an existing in-app message template.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{template-name}} | String | True | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (\_), or hyphens (-). Template names are case sensitive. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| create-new-version | String | False | Specifies whether to save the updates as a new version of the message template. Valid values are: `true`, save the updates as a new version; and, `false`, save the updates to (overwrite) the latest existing version of the template.<br />If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of `true` for this parameter, don't specify a value for the `version` parameter. Otherwise, an error will occur. |
| version | String | False | The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html)resource.<br />If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.<br />If you don't specify a value for this parameter, Amazon Pinpoint does the following:+  For a get operation, retrieves information about the active version of the template. <br />+  For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the `create-new-version` parameter isn't used or is set to `false`. <br />+  For a delete operation, deletes the template, including all versions of the template.  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 202 | MessageBody | The request was accepted for processing. Processing may not be complete. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### DELETE
<a name="templates-template-name-inappdelete"></a>

**Operation ID:** `DeleteInAppTemplate`

Deletes an existing in-app message template.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{template-name}} | String | True | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (\_), or hyphens (-). Template names are case sensitive. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| version | String | False | The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html)resource.<br />If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.<br />If you don't specify a value for this parameter, Amazon Pinpoint does the following:+  For a get operation, retrieves information about the active version of the template. <br />+  For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the `create-new-version` parameter isn't used or is set to `false`. <br />+  For a delete operation, deletes the template, including all versions of the template.  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 202 | MessageBody | The request was accepted for processing. Processing may not be complete. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="templates-template-name-inappoptions"></a>

Retrieves information about the communication requirements and options that are available for the In-App Template resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{template-name}} | String | True | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (\_), or hyphens (-). Template names are case sensitive. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="templates-template-name-inapp-schemas"></a>

### Request bodies
<a name="templates-template-name-inapp-request-examples"></a>

#### POST schema
<a name="templates-template-name-inapp-request-body-post-example"></a>

```
{
  "tags": {
  },
  "TemplateDescription": "string",
  "Layout": enum,
  "Content": [
    {
      "HeaderConfig": {
        "Header": "string",
        "TextColor": "string",
        "Alignment": enum
      },
      "BackgroundColor": "string",
      "BodyConfig": {
        "Body": "string",
        "TextColor": "string",
        "Alignment": enum
      },
      "ImageUrl": "string",
      "PrimaryBtn": {
        "DefaultConfig": {
          "Text": "string",
          "ButtonAction": enum,
          "Link": "string",
          "TextColor": "string",
          "BackgroundColor": "string",
          "BorderRadius": integer
        },
        "Web": {
          "ButtonAction": enum,
          "Link": "string"
        },
        "IOS": {
          "ButtonAction": enum,
          "Link": "string"
        },
        "Android": {
          "ButtonAction": enum,
          "Link": "string"
        }
      },
      "SecondaryBtn": {
        "DefaultConfig": {
          "Text": "string",
          "ButtonAction": enum,
          "Link": "string",
          "TextColor": "string",
          "BackgroundColor": "string",
          "BorderRadius": integer
        },
        "Web": {
          "ButtonAction": enum,
          "Link": "string"
        },
        "IOS": {
          "ButtonAction": enum,
          "Link": "string"
        },
        "Android": {
          "ButtonAction": enum,
          "Link": "string"
        }
      }
    }
  ],
  "CustomConfig": {
  }
}
```

#### PUT schema
<a name="templates-template-name-inapp-request-body-put-example"></a>

```
{
  "tags": {
  },
  "TemplateDescription": "string",
  "Layout": enum,
  "Content": [
    {
      "HeaderConfig": {
        "Header": "string",
        "TextColor": "string",
        "Alignment": enum
      },
      "BackgroundColor": "string",
      "BodyConfig": {
        "Body": "string",
        "TextColor": "string",
        "Alignment": enum
      },
      "ImageUrl": "string",
      "PrimaryBtn": {
        "DefaultConfig": {
          "Text": "string",
          "ButtonAction": enum,
          "Link": "string",
          "TextColor": "string",
          "BackgroundColor": "string",
          "BorderRadius": integer
        },
        "Web": {
          "ButtonAction": enum,
          "Link": "string"
        },
        "IOS": {
          "ButtonAction": enum,
          "Link": "string"
        },
        "Android": {
          "ButtonAction": enum,
          "Link": "string"
        }
      },
      "SecondaryBtn": {
        "DefaultConfig": {
          "Text": "string",
          "ButtonAction": enum,
          "Link": "string",
          "TextColor": "string",
          "BackgroundColor": "string",
          "BorderRadius": integer
        },
        "Web": {
          "ButtonAction": enum,
          "Link": "string"
        },
        "IOS": {
          "ButtonAction": enum,
          "Link": "string"
        },
        "Android": {
          "ButtonAction": enum,
          "Link": "string"
        }
      }
    }
  ],
  "CustomConfig": {
  }
}
```

### Response bodies
<a name="templates-template-name-inapp-response-examples"></a>

#### InAppTemplateResponse schema
<a name="templates-template-name-inapp-response-body-inapptemplateresponse-example"></a>

```
{
  "CreationDate": "string",
  "LastModifiedDate": "string",
  "TemplateType": enum,
  "TemplateName": "string",
  "TemplateDescription": "string",
  "Version": "string",
  "tags": {
  },
  "Arn": "string",
  "Layout": enum,
  "Content": [
    {
      "HeaderConfig": {
        "Header": "string",
        "TextColor": "string",
        "Alignment": enum
      },
      "BackgroundColor": "string",
      "BodyConfig": {
        "Body": "string",
        "TextColor": "string",
        "Alignment": enum
      },
      "ImageUrl": "string",
      "PrimaryBtn": {
        "DefaultConfig": {
          "Text": "string",
          "ButtonAction": enum,
          "Link": "string",
          "TextColor": "string",
          "BackgroundColor": "string",
          "BorderRadius": integer
        },
        "Web": {
          "ButtonAction": enum,
          "Link": "string"
        },
        "IOS": {
          "ButtonAction": enum,
          "Link": "string"
        },
        "Android": {
          "ButtonAction": enum,
          "Link": "string"
        }
      },
      "SecondaryBtn": {
        "DefaultConfig": {
          "Text": "string",
          "ButtonAction": enum,
          "Link": "string",
          "TextColor": "string",
          "BackgroundColor": "string",
          "BorderRadius": integer
        },
        "Web": {
          "ButtonAction": enum,
          "Link": "string"
        },
        "IOS": {
          "ButtonAction": enum,
          "Link": "string"
        },
        "Android": {
          "ButtonAction": enum,
          "Link": "string"
        }
      }
    }
  ],
  "CustomConfig": {
  }
}
```

#### TemplateCreateMessageBody schema
<a name="templates-template-name-inapp-response-body-templatecreatemessagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string",
  "Arn": "string"
}
```

#### MessageBody schema
<a name="templates-template-name-inapp-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="templates-template-name-inapp-properties"></a>

### DefaultButtonConfiguration
<a name="templates-template-name-inapp-model-defaultbuttonconfiguration"></a>

Information about the default behavior for a button that appears in an in-app message. You can optionally add button configurations that specifically apply to iOS, Android, or web browser users.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| BackgroundColor | string | False | The background color of a button, expressed as a string consisting of a hex color code (such as "\#000000" for black). |
| BorderRadius | integer | False | The border radius of a button. |
| ButtonAction | string<br />Values: `LINK \| DEEP_LINK \| CLOSE` | True | The action that occurs when a recipient chooses a button in an in-app message. You can specify one of the following:+  `LINK` – A link to a web destination. <br />+  `DEEP_LINK` – A link to a specific page in an application. <br />+  `CLOSE` – Dismisses the message.  |
| Link | string | False | The destination (such as a URL) for a button. |
| Text | string | True | The text that appears on a button in an in-app message. |
| TextColor | string | False | The color of the body text in a button, expressed as a string consisting of a hex color code (such as "\#000000" for black). |

### InAppMessageBodyConfig
<a name="templates-template-name-inapp-model-inappmessagebodyconfig"></a>

Configuration information related to the main body text of an in-app message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Alignment | string<br />Values: `LEFT \| CENTER \| RIGHT` | True | The text alignment of the main body text of the message. |
| Body | string | True | The main body text of the message. |
| TextColor | string | False | The color of the body text, expressed as a string consisting of a hex color code (such as "\#000000" for black). |

### InAppMessageButton
<a name="templates-template-name-inapp-model-inappmessagebutton"></a>

Configuration information for a button that appears in an in-app message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Android | [OverrideButtonConfiguration](#templates-template-name-inapp-model-overridebuttonconfiguration) | False | An object that defines the default behavior for a button in in-app messages sent to Android. |
| DefaultConfig | [DefaultButtonConfiguration](#templates-template-name-inapp-model-defaultbuttonconfiguration) | False | An object that defines the default behavior for a button in an in-app message. |
| IOS | [OverrideButtonConfiguration](#templates-template-name-inapp-model-overridebuttonconfiguration) | False | An object that defines the default behavior for a button in in-app messages sent to iOS devices. |
| Web | [OverrideButtonConfiguration](#templates-template-name-inapp-model-overridebuttonconfiguration) | False | An object that defines the default behavior for a button in in-app messages for web applications. |

### InAppMessageContent
<a name="templates-template-name-inapp-model-inappmessagecontent"></a>

Configuration information related to an in-app message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| BackgroundColor | string | False | The background color for an in-app message banner, expressed as a string consisting of a hex color code (such as "\#000000" for black). |
| BodyConfig | [InAppMessageBodyConfig](#templates-template-name-inapp-model-inappmessagebodyconfig) | False | An object that contains configuration information about the header or title text of the in-app message. |
| HeaderConfig | [InAppMessageHeaderConfig](#templates-template-name-inapp-model-inappmessageheaderconfig) | False | An object that contains configuration information about the header or title text of the in-app message. |
| ImageUrl | string | False | The URL of the image that appears on an in-app message banner. |
| PrimaryBtn | [InAppMessageButton](#templates-template-name-inapp-model-inappmessagebutton) | False | An object that contains configuration information about the primary button in an in-app message. |
| SecondaryBtn | [InAppMessageButton](#templates-template-name-inapp-model-inappmessagebutton) | False | An object that contains configuration information about the secondary button in an in-app message. |

### InAppMessageHeaderConfig
<a name="templates-template-name-inapp-model-inappmessageheaderconfig"></a>

Configuration information related to the message header for an in-app message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Alignment | string<br />Values: `LEFT \| CENTER \| RIGHT` | True | The text alignment of the title of the message. |
| Header | string | True | The text that appears in the header or title of the message. |
| TextColor | string | False | The color of the body text, expressed as a string consisting of a hex color code (such as "\#000000" for black). |

### InAppTemplateRequest
<a name="templates-template-name-inapp-model-inapptemplaterequest"></a>

Specifies the content and settings for a message template that can be used to send in-app messages.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Content | Array of type [InAppMessageContent](#templates-template-name-inapp-model-inappmessagecontent) | False | An object that contains information about the content of an in-app message, including its title and body text, text colors, background colors, images, buttons, and behaviors. |
| CustomConfig | object | False | Information about the custom data that is included in an in-app messaging payload. |
| Layout | string<br />Values: `BOTTOM_BANNER \| TOP_BANNER \| OVERLAYS \| MOBILE_FEED \| MIDDLE_BANNER \| CAROUSEL` | False | A string that determines the appearance of the in-app message. You can specify one of the following:+  `BOTTOM_BANNER` – a message that appears as a banner at the bottom of the page. <br />+  `TOP_BANNER` – a message that appears as a banner at the top of the page. <br />+  `OVERLAYS` – a message that covers entire screen. <br />+  `MOBILE_FEED` – a message that appears in a window in front of the page. <br />+  `MIDDLE_BANNER` – a message that appears as a banner in the middle of the page. <br />+  `CAROUSEL` – a scrollable layout of up to five unique messages.  |
| tags | object | False |  As of **22-05-2023** the tags attribute has been deprecated. After this date any value in the PUT UpdateInAppTemplate tags attribute is not processed and an error code is not returned. The POST CreateInAppTemplate tags attribute is processed. Use the [Tags](https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html) resource to add or modify tags. (Deprecated) A string-to-string map of key-value pairs that defines the tags to associate with the message template. Each tag consists of a required tag key and an associated tag value. |
| TemplateDescription | string | False | An optional description of the in-app template. |

### InAppTemplateResponse
<a name="templates-template-name-inapp-model-inapptemplateresponse"></a>

Provides information about the content and settings for an in-app message template.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Arn | string | False | The Amazon Resource Name (ARN) of the message template. |
| Content | Array of type [InAppMessageContent](#templates-template-name-inapp-model-inappmessagecontent) | False | An array that contains configurtion information about the message, including title and body text, text colors, background colors, image URLs, and button configurations. |
| CreationDate | string | True | The date, in ISO 8601 format, when the message template was created. |
| CustomConfig | object | False | An object that contains custom data (in the form of key-value pairs) that is included in the in-app messaging payload. |
| LastModifiedDate | string | True | The date, in ISO 8601 format, when the message template was last modified. |
| Layout | string<br />Values: `BOTTOM_BANNER \| TOP_BANNER \| OVERLAYS \| MOBILE_FEED \| MIDDLE_BANNER \| CAROUSEL` | False | A string that determines the appearance of the in-app message. You can specify one of the following:+  `BOTTOM_BANNER` – a message that appears as a banner at the bottom of the page. <br />+  `TOP_BANNER` – a message that appears as a banner at the top of the page. <br />+  `OVERLAYS` – a message that covers entire screen. <br />+  `MOBILE_FEED` – a message that appears in a window in front of the page. <br />+  `MIDDLE_BANNER` – a message that appears as a banner in the middle of the page. <br />+  `CAROUSEL` – a scrollable layout of up to five unique messages.  |
| tags | object | False | A string-to-string map of key-value pairs that identifies the tags that are associated with the message template. Each tag consists of a required tag key and an associated tag value.  |
| TemplateDescription | string | False | A description of the message template. |
| TemplateName | string | True | The name of the in-app message template. |
| TemplateType | string<br />Values: `EMAIL \| SMS \| VOICE \| PUSH \| INAPP` | True | The type of channel that the message template is designed for. For an in-app message template, this value is `INAPP`.  |
| Version | string | False | The unique identifier, shown as an integer, of the active version of the message template, or the version of the template that you specified by using the version parameter in your request. |

### MessageBody
<a name="templates-template-name-inapp-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### OverrideButtonConfiguration
<a name="templates-template-name-inapp-model-overridebuttonconfiguration"></a>

Configuration information related to the configuration of a button with settings that are specific to a certain device type.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ButtonAction | string<br />Values: `LINK \| DEEP_LINK \| CLOSE` | False | The action that occurs when a recipient chooses a button in an in-app message. You can specify one of the following:+  `LINK` – A link to a web destination. <br />+  `DEEP_LINK` – A link to a specific page in an application. <br />+  `CLOSE` – Dismisses the message.  |
| Link | string | False | The destination (such as a URL) for a button. |

### TemplateCreateMessageBody
<a name="templates-template-name-inapp-model-templatecreatemessagebody"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Arn | string | False |  |
| Message | string | False |  |
| RequestID | string | False |  |

## See also
<a name="templates-template-name-inapp-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetInAppTemplate
<a name="GetInAppTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetInAppTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetInAppTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetInAppTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetInAppTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetInAppTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetInAppTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetInAppTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetInAppTemplate)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetInAppTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetInAppTemplate)

### CreateInAppTemplate
<a name="CreateInAppTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/CreateInAppTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/CreateInAppTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/CreateInAppTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/CreateInAppTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/CreateInAppTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/CreateInAppTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/CreateInAppTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/CreateInAppTemplate)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/CreateInAppTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/CreateInAppTemplate)

### UpdateInAppTemplate
<a name="UpdateInAppTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/UpdateInAppTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/UpdateInAppTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/UpdateInAppTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/UpdateInAppTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/UpdateInAppTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/UpdateInAppTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/UpdateInAppTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/UpdateInAppTemplate)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/UpdateInAppTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/UpdateInAppTemplate)

### DeleteInAppTemplate
<a name="DeleteInAppTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/DeleteInAppTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/DeleteInAppTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/DeleteInAppTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/DeleteInAppTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/DeleteInAppTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/DeleteInAppTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/DeleteInAppTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/DeleteInAppTemplate)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/DeleteInAppTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/DeleteInAppTemplate)
