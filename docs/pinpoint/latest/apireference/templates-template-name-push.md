---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-push.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Push Notification Template
<a name="templates-template-name-push"></a>

A *push notification template* is a type of message template that contains content and settings that you can define, save, and reuse in messages that you send through a push notification channel for any of your Amazon Pinpoint applications. You can use push notification templates in push notifications that you send from campaigns, or to a limited audience as direct or test messages.

When you create a push notification template, you specify the content and settings that you want to reuse in various components of messages that are based on the template. These components, referred to as *template parts*, can be the message title, the message body, or both. This content can be static text or personalized content that you define by using the Handlebars template system and message variables. A template part can also be a channel-specific setting, such as a sound to play or an action to occur when a recipient interacts with a push notification that's based on the template. When you send a message that’s based on a template, Amazon Pinpoint populates the message with the content and settings that you defined in the template.

The Push Notification Template resource represents the repository of push notification templates that are associated with your Amazon Pinpoint account. You can use this resource to create, retrieve, update, or delete a message template for messages that you send through a push notification channel.

Amazon Pinpoint supports versioning for all types of message templates. When you use the Push Notification Template resource to work with a template, you can use supported parameters to specify whether your request applies to only a specific version of the template or to the overall template. For example, if you update a template, you can specify whether you want to save your updates as a new version of the template or save them to the latest existing version of the template. To retrieve information about all the versions of a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html) resource.

## URI
<a name="templates-template-name-push-url"></a>

`/v1/templates/{{template-name}}/push`

## HTTP methods
<a name="templates-template-name-push-http-methods"></a>

### GET
<a name="templates-template-name-pushget"></a>

**Operation ID:** `GetPushTemplate`

Retrieves the content and settings of a message template for messages that are sent through a push notification channel.

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
| version | String | False | The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html)resource.<br />If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.<br />If you don't specify a value for this parameter, Amazon Pinpoint does the following:  For a get operation, retrieves information about the active version of the template.   For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the `create-new-version` parameter isn't used or is set to `false`.   For a delete operation, deletes the template, including all versions of the template.   |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | PushNotificationTemplateResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### POST
<a name="templates-template-name-pushpost"></a>

**Operation ID:** `CreatePushTemplate`

Creates a message template for messages that are sent through a push notification channel.

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
| 201 | CreateTemplateMessageBody | The request succeeded and the specified resource was created. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 409 | MessageBody | The request failed due to a conflict with the current state of the specified resource (ConflictException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### PUT
<a name="templates-template-name-pushput"></a>

**Operation ID:** `UpdatePushTemplate`

Updates an existing message template for messages that are sent through a push notification channel.

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
| version | String | False | The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html)resource.<br />If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.<br />If you don't specify a value for this parameter, Amazon Pinpoint does the following:  For a get operation, retrieves information about the active version of the template.   For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the `create-new-version` parameter isn't used or is set to `false`.   For a delete operation, deletes the template, including all versions of the template.   |

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
<a name="templates-template-name-pushdelete"></a>

**Operation ID:** `DeletePushTemplate`

Deletes a message template for messages that were sent through a push notification channel.

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
| version | String | False | The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html)resource.<br />If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.<br />If you don't specify a value for this parameter, Amazon Pinpoint does the following:  For a get operation, retrieves information about the active version of the template.   For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the `create-new-version` parameter isn't used or is set to `false`.   For a delete operation, deletes the template, including all versions of the template.   |

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
<a name="templates-template-name-pushoptions"></a>

Retrieves information about the communication requirements and options that are available for the Push Notification Template resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{template-name}} | String | True | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (\_), or hyphens (-). Template names are case sensitive. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="templates-template-name-push-schemas"></a>

### Request bodies
<a name="templates-template-name-push-request-examples"></a>

#### POST schema
<a name="templates-template-name-push-request-body-post-example"></a>

```
{
  "TemplateDescription": "string",
  "DefaultSubstitutions": "string",
  "tags": {
  },
  "Default": {
    "Title": "string",
    "Body": "string",
    "Action": enum,
    "Sound": "string",
    "Url": "string"
  },
  "ADM": {
    "Title": "string",
    "Body": "string",
    "Action": enum,
    "Sound": "string",
    "Url": "string",
    "ImageUrl": "string",
    "ImageIconUrl": "string",
    "SmallImageIconUrl": "string",
    "RawContent": "string"
  },
  "GCM": {
    "Title": "string",
    "Body": "string",
    "Action": enum,
    "Sound": "string",
    "Url": "string",
    "ImageUrl": "string",
    "ImageIconUrl": "string",
    "SmallImageIconUrl": "string",
    "RawContent": "string"
  },
  "Baidu": {
    "Title": "string",
    "Body": "string",
    "Action": enum,
    "Sound": "string",
    "Url": "string",
    "ImageUrl": "string",
    "ImageIconUrl": "string",
    "SmallImageIconUrl": "string",
    "RawContent": "string"
  },
  "APNS": {
    "Title": "string",
    "Body": "string",
    "Action": enum,
    "Sound": "string",
    "Url": "string",
    "MediaUrl": "string",
    "RawContent": "string"
  },
  "RecommenderId": "string"
}
```

#### PUT schema
<a name="templates-template-name-push-request-body-put-example"></a>

```
{
  "TemplateDescription": "string",
  "DefaultSubstitutions": "string",
  "tags": {
  },
  "Default": {
    "Title": "string",
    "Body": "string",
    "Action": enum,
    "Sound": "string",
    "Url": "string"
  },
  "ADM": {
    "Title": "string",
    "Body": "string",
    "Action": enum,
    "Sound": "string",
    "Url": "string",
    "ImageUrl": "string",
    "ImageIconUrl": "string",
    "SmallImageIconUrl": "string",
    "RawContent": "string"
  },
  "GCM": {
    "Title": "string",
    "Body": "string",
    "Action": enum,
    "Sound": "string",
    "Url": "string",
    "ImageUrl": "string",
    "ImageIconUrl": "string",
    "SmallImageIconUrl": "string",
    "RawContent": "string"
  },
  "Baidu": {
    "Title": "string",
    "Body": "string",
    "Action": enum,
    "Sound": "string",
    "Url": "string",
    "ImageUrl": "string",
    "ImageIconUrl": "string",
    "SmallImageIconUrl": "string",
    "RawContent": "string"
  },
  "APNS": {
    "Title": "string",
    "Body": "string",
    "Action": enum,
    "Sound": "string",
    "Url": "string",
    "MediaUrl": "string",
    "RawContent": "string"
  },
  "RecommenderId": "string"
}
```

### Response bodies
<a name="templates-template-name-push-response-examples"></a>

#### PushNotificationTemplateResponse schema
<a name="templates-template-name-push-response-body-pushnotificationtemplateresponse-example"></a>

```
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
  "Arn": "string",
  "Default": {
    "Title": "string",
    "Body": "string",
    "Action": enum,
    "Sound": "string",
    "Url": "string"
  },
  "ADM": {
    "Title": "string",
    "Body": "string",
    "Action": enum,
    "Sound": "string",
    "Url": "string",
    "ImageUrl": "string",
    "ImageIconUrl": "string",
    "SmallImageIconUrl": "string",
    "RawContent": "string"
  },
  "GCM": {
    "Title": "string",
    "Body": "string",
    "Action": enum,
    "Sound": "string",
    "Url": "string",
    "ImageUrl": "string",
    "ImageIconUrl": "string",
    "SmallImageIconUrl": "string",
    "RawContent": "string"
  },
  "Baidu": {
    "Title": "string",
    "Body": "string",
    "Action": enum,
    "Sound": "string",
    "Url": "string",
    "ImageUrl": "string",
    "ImageIconUrl": "string",
    "SmallImageIconUrl": "string",
    "RawContent": "string"
  },
  "APNS": {
    "Title": "string",
    "Body": "string",
    "Action": enum,
    "Sound": "string",
    "Url": "string",
    "MediaUrl": "string",
    "RawContent": "string"
  },
  "RecommenderId": "string"
}
```

#### CreateTemplateMessageBody schema
<a name="templates-template-name-push-response-body-createtemplatemessagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string",
  "Arn": "string"
}
```

#### MessageBody schema
<a name="templates-template-name-push-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="templates-template-name-push-properties"></a>

### APNSPushNotificationTemplate
<a name="templates-template-name-push-model-apnspushnotificationtemplate"></a>

Specifies channel-specific content and settings for a message template that can be used in push notifications that are sent through the APNs (Apple Push Notification service) channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Action | string<br />Values: `OPEN_APP \| DEEP_LINK \| URL` | False | The action to occur if a recipient taps a push notification that's based on the message template. Valid values are:   `OPEN_APP` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.    `DEEP_LINK` – Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS platform.    `URL` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.   |
| Body | string | False | The message body to use in push notifications that are based on the message template. |
| MediaUrl | string | False | The URL of an image or video to display in push notifications that are based on the message template. |
| RawContent | string | False | The raw, JSON-formatted string to use as the payload for push notifications that are based on the message template. If specified, this value overrides all other content for the message template. |
| Sound | string | False | The key for the sound to play when the recipient receives a push notification that's based on the message template. The value for this key is the name of a sound file in your app's main bundle or the `Library/Sounds` folder in your app's data container. If the sound file can't be found or you specify `default` for the value, the system plays the default alert sound. |
| Title | string | False | The title to use in push notifications that are based on the message template. This title appears above the notification message on a recipient's device. |
| Url | string | False | The URL to open in the recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the `Action` property is `URL`. |

### AndroidPushNotificationTemplate
<a name="templates-template-name-push-model-androidpushnotificationtemplate"></a>

Specifies channel-specific content and settings for a message template that can be used in push notifications that are sent through the ADM (Amazon Device Messaging), Baidu (Baidu Cloud Push), or GCM (Firebase Cloud Messaging, formerly Google Cloud Messaging) channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Action | string<br />Values: `OPEN_APP \| DEEP_LINK \| URL` | False | The action to occur if a recipient taps a push notification that's based on the message template. Valid values are:   `OPEN_APP` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.    `DEEP_LINK` – Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform.    `URL` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.   |
| Body | string | False | The message body to use in a push notification that's based on the message template. |
| ImageIconUrl | string | False | The URL of the large icon image to display in the content view of a push notification that's based on the message template. |
| ImageUrl | string | False | The URL of an image to display in a push notification that's based on the message template. |
| RawContent | string | False | The raw, JSON-formatted string to use as the payload for a push notification that's based on the message template. If specified, this value overrides all other content for the message template. |
| SmallImageIconUrl | string | False | The URL of the small icon image to display in the status bar and the content view of a push notification that's based on the message template. |
| Sound | string | False | The sound to play when a recipient receives a push notification that's based on the message template. You can use the default stream or specify the file name of a sound resource that's bundled in your app. On an Android platform, the sound file must reside in `/res/raw/`. |
| Title | string | False | The title to use in a push notification that's based on the message template. This title appears above the notification message on a recipient's device. |
| Url | string | False | The URL to open in a recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the `Action` property is `URL`. |

### CreateTemplateMessageBody
<a name="templates-template-name-push-model-createtemplatemessagebody"></a>

Provides information about a request to create a message template.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Arn | string | False | The Amazon Resource Name (ARN) of the message template that was created. |
| Message | string | False | The message that's returned from the API for the request to create the message template. |
| RequestID | string | False | The unique identifier for the request to create the message template. |

### DefaultPushNotificationTemplate
<a name="templates-template-name-push-model-defaultpushnotificationtemplate"></a>

Specifies the default settings and content for a message template that can be used in messages that are sent through a push notification channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Action | string<br />Values: `OPEN_APP \| DEEP_LINK \| URL` | False | The action to occur if a recipient taps a push notification that's based on the message template. Valid values are:   `OPEN_APP` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.    `DEEP_LINK` – Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS and Android platforms.    `URL` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.   |
| Body | string | False | The message body to use in push notifications that are based on the message template. |
| Sound | string | False | The sound to play when a recipient receives a push notification that's based on the message template. You can use the default stream or specify the file name of a sound resource that's bundled in your app. On an Android platform, the sound file must reside in `/res/raw/`.<br />For an iOS platform, this value is the key for the name of a sound file in your app's main bundle or the `Library/Sounds` folder in your app's data container. If the sound file can't be found or you specify `default` for the value, the system plays the default alert sound. |
| Title | string | False | The title to use in push notifications that are based on the message template. This title appears above the notification message on a recipient's device. |
| Url | string | False | The URL to open in a recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the `Action` property is `URL`. |

### MessageBody
<a name="templates-template-name-push-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### PushNotificationTemplateRequest
<a name="templates-template-name-push-model-pushnotificationtemplaterequest"></a>

Specifies the content and settings for a message template that can be used in messages that are sent through a push notification channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ADM | [AndroidPushNotificationTemplate](#templates-template-name-push-model-androidpushnotificationtemplate) | False | The message template to use for the ADM (Amazon Device Messaging) channel. This message template overrides the default template for push notification channels (`DefaultPushNotificationTemplate`). |
| APNS | [APNSPushNotificationTemplate](#templates-template-name-push-model-apnspushnotificationtemplate) | False | The message template to use for the APNs (Apple Push Notification service) channel. This message template overrides the default template for push notification channels (`DefaultPushNotificationTemplate`). |
| Baidu | [AndroidPushNotificationTemplate](#templates-template-name-push-model-androidpushnotificationtemplate) | False | The message template to use for the Baidu (Baidu Cloud Push) channel. This message template overrides the default template for push notification channels (`DefaultPushNotificationTemplate`). |
| Default | [DefaultPushNotificationTemplate](#templates-template-name-push-model-defaultpushnotificationtemplate) | False | The default message template to use for push notification channels. |
| DefaultSubstitutions | string | False | A JSON object that specifies the default values to use for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message that's based on the template, you can override these defaults with message-specific and address-specific variables and values. |
| GCM | [AndroidPushNotificationTemplate](#templates-template-name-push-model-androidpushnotificationtemplate) | False | The message template to use for the GCM channel, which is used to send notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. This message template overrides the default template for push notification channels (`DefaultPushNotificationTemplate`). |
| RecommenderId | string | False | The unique identifier for the recommender model to use for the message template. Amazon Pinpoint uses this value to determine how to retrieve and process data from a recommender model when it sends messages that use the template, if the template contains message variables for recommendation data. |
| tags | object | False |  As of **22-05-2023** the tags attribute has been deprecated. After this date any value in the PUT UpdatePushTemplate tags attribute is not processed and an error code is not returned. The POST CreatePushTemplate tags attribute is processed. Use the [Tags](https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html) resource to add or modify tags. (Deprecated) A string-to-string map of key-value pairs that defines the tags to associate with the message template. Each tag consists of a required tag key and an associated tag value. |
| TemplateDescription | string | False | A custom description of the message template. |

### PushNotificationTemplateResponse
<a name="templates-template-name-push-model-pushnotificationtemplateresponse"></a>

Provides information about the content and settings for a message template that can be used in messages that are sent through a push notification channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ADM | [AndroidPushNotificationTemplate](#templates-template-name-push-model-androidpushnotificationtemplate) | False | The message template that's used for the ADM (Amazon Device Messaging) channel. This message template overrides the default template for push notification channels (`DefaultPushNotificationTemplate`). |
| APNS | [APNSPushNotificationTemplate](#templates-template-name-push-model-apnspushnotificationtemplate) | False | The message template that's used for the APNs (Apple Push Notification service) channel. This message template overrides the default template for push notification channels (`DefaultPushNotificationTemplate`). |
| Arn | string | False | The Amazon Resource Name (ARN) of the message template. |
| Baidu | [AndroidPushNotificationTemplate](#templates-template-name-push-model-androidpushnotificationtemplate) | False | The message template that's used for the Baidu (Baidu Cloud Push) channel. This message template overrides the default template for push notification channels (`DefaultPushNotificationTemplate`). |
| CreationDate | string | True | The date, in ISO 8601 format, when the message template was created. |
| Default | [DefaultPushNotificationTemplate](#templates-template-name-push-model-defaultpushnotificationtemplate) | False | The default message template that's used for push notification channels. |
| DefaultSubstitutions | string | False | The JSON object that specifies the default values that are used for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. |
| GCM | [AndroidPushNotificationTemplate](#templates-template-name-push-model-androidpushnotificationtemplate) | False | The message template that's used for the GCM channel, which is used to send notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. This message template overrides the default template for push notification channels (`DefaultPushNotificationTemplate`). |
| LastModifiedDate | string | True | The date, in ISO 8601 format, when the message template was last modified. |
| RecommenderId | string | False | The unique identifier for the recommender model that's used by the message template. |
| tags | object | False | A string-to-string map of key-value pairs that identifies the tags that are associated with the message template. Each tag consists of a required tag key and an associated tag value. |
| TemplateDescription | string | False | The custom description of the message template. |
| TemplateName | string | True | The name of the message template. |
| TemplateType | string<br />Values: `EMAIL \| SMS \| VOICE \| PUSH \| INAPP` | True | The type of channel that the message template is designed for. For a push notification template, this value is `PUSH`. |
| Version | string | False | The unique identifier, as an integer, for the active version of the message template, or the version of the template that you specified by using the `version` parameter in your request. |

## See also
<a name="templates-template-name-push-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetPushTemplate
<a name="GetPushTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetPushTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetPushTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetPushTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetPushTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetPushTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetPushTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetPushTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetPushTemplate)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetPushTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetPushTemplate)

### CreatePushTemplate
<a name="CreatePushTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/CreatePushTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/CreatePushTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/CreatePushTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/CreatePushTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/CreatePushTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/CreatePushTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/CreatePushTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/CreatePushTemplate)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/CreatePushTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/CreatePushTemplate)

### UpdatePushTemplate
<a name="UpdatePushTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/UpdatePushTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/UpdatePushTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/UpdatePushTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/UpdatePushTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/UpdatePushTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/UpdatePushTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/UpdatePushTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/UpdatePushTemplate)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/UpdatePushTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/UpdatePushTemplate)

### DeletePushTemplate
<a name="DeletePushTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/DeletePushTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/DeletePushTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/DeletePushTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/DeletePushTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/DeletePushTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/DeletePushTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/DeletePushTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/DeletePushTemplate)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/DeletePushTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/DeletePushTemplate)
