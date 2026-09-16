---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Messages
<a name="apps-application-id-messages"></a>

The Messages resource represents a *direct message*, which is a one-time message that you send directly to a limited audience without creating a campaign. You can send a direct message to as many as 100 recipients. The message can be a push notification for users of your mobile app, an SMS message, an email message, or a voice message.

When you send a direct message, Amazon Pinpoint delivers it immediately. You can't schedule the delivery of direct messages. In addition, you can't send a direct message to a segment. If you want to schedule a message to be sent at a certain time or you want to send a message to a segment, you should create a campaign rather than sending a direct message.

While sending transactional template-based messages using the Amazon Pinpoint API, CLI or SDK, you need to make sure that values are provided for all the template variable either at request time or as default values with the template. Messages failing to render due to missing attribute value will not be received successfully.

You can use the Messages resource to send a direct message.

## URI
<a name="apps-application-id-messages-url"></a>

`/v1/apps/{{application-id}}/messages`

## HTTP methods
<a name="apps-application-id-messages-http-methods"></a>

### POST
<a name="apps-application-id-messagespost"></a>

**Operation ID:** `SendMessages`

Creates and sends a direct message.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | MessageResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-messagesoptions"></a>

Retrieves information about the communication requirements and options that are available for the Messages resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-messages-schemas"></a>

### Request bodies
<a name="apps-application-id-messages-request-examples"></a>

#### POST schema
<a name="apps-application-id-messages-request-body-post-example"></a>

```
{
  "TraceId": "string",
  "Context": {
  },
  "MessageConfiguration": {
    "DefaultMessage": {
      "Body": "string",
      "Substitutions": {
      }
    },
    "DefaultPushNotificationMessage": {
      "Body": "string",
      "Substitutions": {
      },
      "Title": "string",
      "Action": enum,
      "Url": "string",
      "SilentPush": boolean,
      "Data": {
      }
    },
    "APNSMessage": {
      "Body": "string",
      "Substitutions": {
      },
      "Title": "string",
      "Action": enum,
      "Url": "string",
      "SilentPush": boolean,
      "Data": {
      },
      "MediaUrl": "string",
      "Sound": "string",
      "Badge": integer,
      "Category": "string",
      "ThreadId": "string",
      "RawContent": "string",
      "PreferredAuthenticationMethod": "string",
      "TimeToLive": integer,
      "Priority": "string",
      "CollapseId": "string",
      "APNSPushType": "string"
    },
    "GCMMessage": {
      "Body": "string",
      "Substitutions": {
      },
      "Title": "string",
      "Action": enum,
      "Url": "string",
      "SilentPush": boolean,
      "Data": {
      },
      "IconReference": "string",
      "Sound": "string",
      "ImageUrl": "string",
      "ImageIconUrl": "string",
      "SmallImageIconUrl": "string",
      "RawContent": "string",
      "CollapseKey": "string",
      "RestrictedPackageName": "string",
      "TimeToLive": integer,
      "Priority": "string",
      "PreferredAuthenticationMethod": "string"
    },
    "BaiduMessage": {
      "Body": "string",
      "Substitutions": {
      },
      "Title": "string",
      "Action": enum,
      "Url": "string",
      "SilentPush": boolean,
      "Data": {
      },
      "IconReference": "string",
      "Sound": "string",
      "ImageUrl": "string",
      "ImageIconUrl": "string",
      "SmallImageIconUrl": "string",
      "RawContent": "string",
      "TimeToLive": integer
    },
    "ADMMessage": {
      "Body": "string",
      "Substitutions": {
      },
      "Title": "string",
      "Action": enum,
      "Url": "string",
      "SilentPush": boolean,
      "Data": {
      },
      "IconReference": "string",
      "Sound": "string",
      "ImageUrl": "string",
      "ImageIconUrl": "string",
      "SmallImageIconUrl": "string",
      "RawContent": "string",
      "ConsolidationKey": "string",
      "ExpiresAfter": "string",
      "MD5": "string"
    },
    "EmailMessage": {
      "Body": "string",
      "Substitutions": {
      },
      "FromAddress": "string",
      "FeedbackForwardingAddress": "string",
      "ReplyToAddresses": [
        "string"
      ],
      "SimpleEmail": {
        "Subject": {
          "Data": "string",
          "Charset": "string"
        },
        "TextPart": {
          "Data": "string",
          "Charset": "string"
        },
        "HtmlPart": {
          "Data": "string",
          "Charset": "string"
        },
        "Headers": [
          {
            "Name": "string",
            "Value": "string"
          }
        ]
      },
      "RawEmail": {
        "Data": "string"
      }
    },
    "SMSMessage": {
      "Body": "string",
      "Substitutions": {
      },
      "SenderId": "string",
      "MessageType": enum,
      "Keyword": "string",
      "OriginationNumber": "string",
      "EntityId": "string",
      "TemplateId": "string",
      "MediaUrl": "string"
    },
    "VoiceMessage": {
      "Body": "string",
      "Substitutions": {
      },
      "LanguageCode": "string",
      "VoiceId": "string",
      "OriginationNumber": "string"
    }
  },
  "TemplateConfiguration": {
    "SMSTemplate": {
      "Name": "string",
      "Version": "string"
    },
    "EmailTemplate": {
      "Name": "string",
      "Version": "string"
    },
    "PushTemplate": {
      "Name": "string",
      "Version": "string"
    },
    "VoiceTemplate": {
      "Name": "string",
      "Version": "string"
    },
    "InAppTemplate": {
      "Name": "string",
      "Version": "string"
    }
  },
  "Addresses": {
  },
  "Endpoints": {
  }
}
```

### Response bodies
<a name="apps-application-id-messages-response-examples"></a>

#### MessageResponse schema
<a name="apps-application-id-messages-response-body-messageresponse-example"></a>

```
{
  "ApplicationId": "string",
  "RequestId": "string",
  "Result": {
  },
  "EndpointResult": {
  }
}
```

#### MessageBody schema
<a name="apps-application-id-messages-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-messages-properties"></a>

### ADMMessage
<a name="apps-application-id-messages-model-admmessage"></a>

Specifies the settings for a one-time message that's sent directly to an endpoint through the ADM (Amazon Device Messaging) channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Action | string<br />Values: `OPEN_APP \| DEEP_LINK \| URL` | False | The action to occur if the recipient taps the push notification. Valid values are:+   `OPEN_APP` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action. <br />+   `DEEP_LINK` – Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform. <br />+   `URL` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.  |
| Body | string | False | The body of the notification message. |
| ConsolidationKey | string | False | An arbitrary string that indicates that multiple messages are logically the same and that Amazon Device Messaging (ADM) can drop previously enqueued messages in favor of this message. |
| Data | object | False | The JSON data payload to use for the push notification, if the notification is a silent push notification. This payload is added to the `data.pinpoint.jsonBody` object of the notification. |
| ExpiresAfter | string | False | The amount of time, in seconds, that ADM should store the message if the recipient's device is offline. Amazon Pinpoint specifies this value in the `expiresAfter` parameter when it sends the notification message to ADM. |
| IconReference | string | False | The icon image name of the asset saved in your app. |
| ImageIconUrl | string | False | The URL of the large icon image to display in the content view of the push notification. |
| ImageUrl | string | False | The URL of an image to display in the push notification. |
| MD5 | string | False | The base64-encoded, MD5 checksum of the value specified by the `Data` property. ADM uses the `MD5` value to verify the integrity of the data. |
| RawContent | string | False | The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message. |
| SilentPush | boolean | False | Specifies whether the notification is a silent push notification, which is a push notification that doesn't display on a recipient's device. Silent push notifications can be used for cases such as updating an app's configuration or supporting phone home functionality. |
| SmallImageIconUrl | string | False | The URL of the small icon image to display in the status bar and the content view of the push notification. |
| Sound | string | False | The sound to play when the recipient receives the push notification. You can use the default stream or specify the file name of a sound resource that's bundled in your app. On an Android platform, the sound file must reside in `/res/raw/`. |
| Substitutions | object | False | The default message variables to use in the notification message. You can override the default variables with individual address variables. |
| Title | string | False | The title to display above the notification message on the recipient's device. |
| Url | string | False | The URL to open in the recipient's default mobile browser, if a recipient taps the push notification and the value of the `Action` property is `URL`. |

### APNSMessage
<a name="apps-application-id-messages-model-apnsmessage"></a>

Specifies the settings for a one-time message that's sent directly to an endpoint through the APNs (Apple Push Notification service) channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Action | string<br />Values: `OPEN_APP \| DEEP_LINK \| URL` | False | The action to occur if the recipient taps the push notification. Valid values are:+   `OPEN_APP` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action. <br />+   `DEEP_LINK` – Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS platform. <br />+   `URL` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.  |
| APNSPushType | string | False | The type of push notification to send. Valid values are:+   `alert` – For a standard notification that's displayed on recipients' devices and prompts a recipient to interact with the notification. <br />+   `background` – For a silent notification that delivers content in the background and isn't displayed on recipients' devices. <br />+   `complication` – For a notification that contains update information for an app’s complication timeline. <br />+   `fileprovider` – For a notification that signals changes to a File Provider extension. <br />+   `mdm` – For a notification that tells managed devices to contact the MDM server. <br />+   `voip` – For a notification that provides information about an incoming VoIP call. <br />Amazon Pinpoint specifies this value in the `apns-push-type` request header when it sends the notification message to APNs. If you don't specify a value for this property, Amazon Pinpoint sets the value to `alert` or `background` automatically, based on the value that you specify for the `SilentPush` or `RawContent` property of the message.<br />For more information about the `apns-push-type` request header, see [Sending Notification Requests to APNs](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns) on the Apple Developer website. |
| Badge | integer | False | The key that indicates whether and how to modify the badge of your app's icon when the recipient receives the push notification. If this key isn't included in the dictionary, the badge doesn't change. To remove the badge, set this value to `0`. |
| Body | string | False | The body of the notification message. |
| Category | string | False | The key that indicates the notification type for the push notification. This key is a value that's defined by the `identifier` property of one of your app's registered categories. |
| CollapseId | string | False | An arbitrary identifier that, if assigned to multiple messages, APNs uses to coalesce the messages into a single push notification instead of delivering each message individually. This value can't exceed 64 bytes.<br />Amazon Pinpoint specifies this value in the `apns-collapse-id` request header when it sends the notification message to APNs. |
| Data | object | False | The JSON payload to use for a silent push notification. This payload is added to the `data.pinpoint.jsonBody` object of the notification. |
| MediaUrl | string | False | The URL of an image or video to display in the push notification. |
| PreferredAuthenticationMethod | string | False | The authentication method that you want Amazon Pinpoint to use when authenticating with APNs, `CERTIFICATE` or `TOKEN`. |
| Priority | string | False | The priority of the push notification. Valid values are:+   `5` – Low priority, the notification might be delayed, delivered as part of a group, or throttled. <br />+   `10` – High priority, the notification is sent immediately. This is the default value. A high priority notification should trigger an alert, play a sound, or badge your app's icon on the recipient's device. <br />Amazon Pinpoint specifies this value in the `apns-priority` request header when it sends the notification message to APNs.<br />The equivalent values for Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), are `normal`, for `5`, and `high`, for `10`. If you specify an FCM value for this property, Amazon Pinpoint accepts and converts the value to the corresponding APNs value. |
| RawContent | string | False | The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message. For an example of the RawContent property, see [Schema sample: RawContent object for a push notification](https://docs.aws.amazon.com/pinpoint/latest/apireference/samples-rawcontent-object.html). If you specify the raw content of an APNs push notification, the message payload has to include the `content-available` key. The value of the `content-available` key has to be an integer, and can only be `0` or `1`. If you're sending a standard notification, set the value of `content-available` to `0`. If you're sending a silent (background) notification, set the value of `content-available` to `1`. Additionally, silent notification payloads can't include the `alert`, `badge`, or `sound` keys. For more information, see [Generating a Remote Notification](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/generating_a_remote_notification) and [Pushing Background Updates to Your App](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) on the Apple Developer website. <br />If you want to send a push notification to users of the Safari web browser on a macOS laptop or desktop computer, you must specify the raw message payload. Also, the raw message payload must include a `url-args` array within the `aps` object. The `url-args` array is required in order to send push notifications to the Safari web browser. However, it is acceptable for the array to contain a single, empty element. For more information about Safari push notifications, see [Configuring Safari Push Notifications](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html) on the Apple Developer website.  |
| SilentPush | boolean | False | Specifies whether the notification is a silent push notification. A silent (or background) push notification isn't displayed on recipients' devices. You can use silent push notifications to make small updates to your app, or to display messages in an in-app message center.<br />Amazon Pinpoint uses this property to determine the correct value for the `apns-push-type` request header when it sends the notification message to APNs. If you specify a value of `true` for this property, Amazon Pinpoint sets the value for the `apns-push-type` header field to `background`. If you specify the raw content of an APNs push notification, the message payload has to include the `content-available` key. For silent (background) notifications, set the value of `content-available` to `1`. Additionally, the message payload for a silent notification can't include the `alert`, `badge`, or `sound` keys. For more information, see [Generating a Remote Notification](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/generating_a_remote_notification) and [Pushing Background Updates to Your App](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app) on the Apple Developer website. <br />Apple has indicated that they will throttle "excessive" background notifications based on current traffic volumes. To prevent your notifications being throttled, Apple recommends that you send no more than 3 silent push notifications to each recipient per hour.  |
| Sound | string | False | The key for the sound to play when the recipient receives the push notification. The value for this key is the name of a sound file in your app's main bundle or the `Library/Sounds` folder in your app's data container. If the sound file can't be found or you specify `default` for the value, the system plays the default alert sound. |
| Substitutions | object | False | The default message variables to use in the notification message. You can override these default variables with individual address variables. |
| ThreadId | string | False | The key that represents your app-specific identifier for grouping notifications. If you provide a Notification Content app extension, you can use this value to group your notifications together. |
| TimeToLive | integer | False | The amount of time, in seconds, that APNs should store and attempt to deliver the push notification, if the service is unable to deliver the notification the first time. If this value is `0`, APNs treats the notification as if it expires immediately and the service doesn't store or try to deliver the notification again.<br />Amazon Pinpoint specifies this value in the `apns-expiration` request header when it sends the notification message to APNs. |
| Title | string | False | The title to display above the notification message on the recipient's device. |
| Url | string | False | The URL to open in the recipient's default mobile browser, if a recipient taps the push notification and the value of the `Action` property is `URL`. |

### AddressConfiguration
<a name="apps-application-id-messages-model-addressconfiguration"></a>

Specifies address-based configuration settings for a message that's sent directly to an endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| BodyOverride | string | False | The message body to use instead of the default message body. This value overrides the default message body. |
| ChannelType | string<br />Values: `PUSH \| GCM \| APNS \| APNS_SANDBOX \| APNS_VOIP \| APNS_VOIP_SANDBOX \| ADM \| SMS \| VOICE \| EMAIL \| BAIDU \| CUSTOM \| IN_APP` | False | The channel to use when sending the message. |
| Context | object | False | An object that maps custom attributes to attributes for the address and is attached to the message. Attribute names are case sensitive.<br />For a push notification, this payload is added to the `data.pinpoint` object. For an email or text message, this payload is added to email/SMS delivery receipt event attributes. |
| RawContent | string | False | The raw, JSON-formatted string to use as the payload for the message. If specified, this value overrides all other values for the message. |
| Substitutions | object | False | A map of the message variables to merge with the variables specified by properties of the `DefaultMessage` object. The variables specified in this map take precedence over all other variables. |
| TitleOverride | string | False | The message title to use instead of the default message title. This value overrides the default message title. |

### BaiduMessage
<a name="apps-application-id-messages-model-baidumessage"></a>

Specifies the settings for a one-time message that's sent directly to an endpoint through the Baidu (Baidu Cloud Push) channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Action | string<br />Values: `OPEN_APP \| DEEP_LINK \| URL` | False | The action to occur if the recipient taps the push notification. Valid values are:+   `OPEN_APP` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action. <br />+   `DEEP_LINK` – Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform. <br />+   `URL` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.  |
| Body | string | False | The body of the notification message. |
| Data | object | False | The JSON data payload to use for the push notification, if the notification is a silent push notification. This payload is added to the `data.pinpoint.jsonBody` object of the notification. |
| IconReference | string | False | The icon image name of the asset saved in your app. |
| ImageIconUrl | string | False | The URL of the large icon image to display in the content view of the push notification. |
| ImageUrl | string | False | The URL of an image to display in the push notification. |
| RawContent | string | False | The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message. |
| SilentPush | boolean | False | Specifies whether the notification is a silent push notification, which is a push notification that doesn't display on a recipient's device. Silent push notifications can be used for cases such as updating an app's configuration or supporting phone home functionality. |
| SmallImageIconUrl | string | False | The URL of the small icon image to display in the status bar and the content view of the push notification. |
| Sound | string | False | The sound to play when the recipient receives the push notification. You can use the default stream or specify the file name of a sound resource that's bundled in your app. On an Android platform, the sound file must reside in `/res/raw/`. |
| Substitutions | object | False | The default message variables to use in the notification message. You can override the default variables with individual address variables. |
| TimeToLive | integer | False | The amount of time, in seconds, that the Baidu Cloud Push service should store the message if the recipient's device is offline. The default value and maximum supported time is 604,800 seconds (7 days). |
| Title | string | False | The title to display above the notification message on the recipient's device. |
| Url | string | False | The URL to open in the recipient's default mobile browser, if a recipient taps the push notification and the value of the `Action` property is `URL`. |

### DefaultMessage
<a name="apps-application-id-messages-model-defaultmessage"></a>

Specifies the default message for all channels.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Body | string | False | The default body of the message. |
| Substitutions | object | False | The default message variables to use in the message. You can override these default variables with individual address variables. |

### DefaultPushNotificationMessage
<a name="apps-application-id-messages-model-defaultpushnotificationmessage"></a>

Specifies the default settings and content for a push notification that's sent directly to an endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Action | string<br />Values: `OPEN_APP \| DEEP_LINK \| URL` | False | The default action to occur if a recipient taps the push notification. Valid values are:+   `OPEN_APP` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action. <br />+   `DEEP_LINK` – Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS and Android platforms. <br />+   `URL` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.  |
| Body | string | False | The default body of the notification message. |
| Data | object | False | The JSON data payload to use for the default push notification, if the notification is a silent push notification. This payload is added to the `data.pinpoint.jsonBody` object of the notification. |
| SilentPush | boolean | False | Specifies whether the default notification is a silent push notification, which is a push notification that doesn't display on a recipient's device. Silent push notifications can be used for cases such as updating an app's configuration or delivering messages to an in-app notification center. |
| Substitutions | object | False | The default message variables to use in the notification message. You can override the default variables with individual address variables. |
| Title | string | False | The default title to display above the notification message on a recipient's device. |
| Url | string | False | The default URL to open in a recipient's default mobile browser, if a recipient taps the push notification and the value of the `Action` property is `URL`. |

### DirectMessageConfiguration
<a name="apps-application-id-messages-model-directmessageconfiguration"></a>

Specifies the settings and content for the default message and any default messages that you tailored for specific channels.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ADMMessage | [ADMMessage](#apps-application-id-messages-model-admmessage) | False | The default push notification message for the ADM (Amazon Device Messaging) channel. This message overrides the default push notification message (`DefaultPushNotificationMessage`). |
| APNSMessage | [APNSMessage](#apps-application-id-messages-model-apnsmessage) | False | The default push notification message for the APNs (Apple Push Notification service) channel. This message overrides the default push notification message (`DefaultPushNotificationMessage`). |
| BaiduMessage | [BaiduMessage](#apps-application-id-messages-model-baidumessage) | False | The default push notification message for the Baidu (Baidu Cloud Push) channel. This message overrides the default push notification message (`DefaultPushNotificationMessage`). |
| DefaultMessage | [DefaultMessage](#apps-application-id-messages-model-defaultmessage) | False | The default message for all channels. |
| DefaultPushNotificationMessage | [DefaultPushNotificationMessage](#apps-application-id-messages-model-defaultpushnotificationmessage) | False | The default push notification message for all push notification channels. |
| EmailMessage | [EmailMessage](#apps-application-id-messages-model-emailmessage) | False | The default message for the email channel. This message overrides the default message (`DefaultMessage`). |
| GCMMessage | [GCMMessage](#apps-application-id-messages-model-gcmmessage) | False | The default push notification message for the GCM channel, which is used to send notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. This message overrides the default push notification message (`DefaultPushNotificationMessage`). |
| SMSMessage | [SMSMessage](#apps-application-id-messages-model-smsmessage) | False | The default message for the SMS channel. This message overrides the default message (`DefaultMessage`). |
| VoiceMessage | [VoiceMessage](#apps-application-id-messages-model-voicemessage) | False | The default message for the voice channel. This message overrides the default message (`DefaultMessage`). |

### EmailMessage
<a name="apps-application-id-messages-model-emailmessage"></a>

Specifies the default settings and content for a one-time email message that's sent directly to an endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Body | string | False | The body of the email message. |
| FeedbackForwardingAddress | string | False | The email address to forward bounces and complaints to, if feedback forwarding is enabled. |
| FromAddress | string | False | The verified email address to send the email message from. The default value is the `FromAddress` specified for the email channel. |
| RawEmail | [RawEmail](#apps-application-id-messages-model-rawemail) | False | The email message, represented as a raw MIME message. |
| ReplyToAddresses | Array of type string | False | The reply-to email address(es) for the email message. If a recipient replies to the email, each reply-to address receives the reply. |
| SimpleEmail | [SimpleEmail](#apps-application-id-messages-model-simpleemail) | False | The email message, composed of a subject, a text part, and an HTML part. |
| Substitutions | object | False | The default message variables to use in the email message. You can override the default variables with individual address variables. |

### EndpointMessageResult
<a name="apps-application-id-messages-model-endpointmessageresult"></a>

Provides information about the delivery status and results of sending a message directly to an endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Address | string | False | The endpoint address that the message was delivered to. |
| DeliveryStatus | string<br />Values: `SUCCESSFUL \| THROTTLED \| TEMPORARY_FAILURE \| PERMANENT_FAILURE \| UNKNOWN_FAILURE \| OPT_OUT \| DUPLICATE` | True | The delivery status of the message. Possible values are:+   `DUPLICATE` – The endpoint address is a duplicate of another endpoint address. Amazon Pinpoint won't attempt to send the message again. <br />+   `OPT_OUT` – The SendMessages API does not honor the endpoint OPT\_OUT status.  <br />+   `PERMANENT_FAILURE` – An error occurred when delivering the message to the endpoint. Amazon Pinpoint won't attempt to send the message again. <br />+   `SUCCESSFUL` – The message was successfully delivered to the endpoint. <br />+   `TEMPORARY_FAILURE` – A temporary error occurred. Amazon Pinpoint won't attempt to send the message again. <br />+   `THROTTLED` – Amazon Pinpoint throttled the operation to send the message to the endpoint. <br />+   `UNKNOWN_FAILURE` – An unknown error occurred.  |
| MessageId | string | False | The unique identifier for the message that was sent. |
| StatusCode | integer | True | The downstream service status code for delivering the message. |
| StatusMessage | string | False | The status message for delivering the message. |
| UpdatedToken | string | False | For push notifications that are sent through the GCM channel, specifies whether the endpoint's device registration token was updated as part of delivering the message. |

### EndpointSendConfiguration
<a name="apps-application-id-messages-model-endpointsendconfiguration"></a>

Specifies the content, including message variables and attributes, to use in a message that's sent directly to an endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| BodyOverride | string | False | The body of the message. If specified, this value overrides the default message body. |
| Context | object | False | A map of custom attributes to attach to the message for the address. Attribute names are case sensitive.<br />For a push notification, this payload is added to the `data.pinpoint` object. For an email or text message, this payload is added to email/SMS delivery receipt event attributes. |
| RawContent | string | False | The raw, JSON-formatted string to use as the payload for the message. If specified, this value overrides all other values for the message. |
| Substitutions | object | False | A map of the message variables to merge with the variables specified for the default message (`DefaultMessage.Substitutions`). The variables specified in this map take precedence over all other variables. |
| TitleOverride | string | False | The title or subject line of the message. If specified, this value overrides the default message title or subject line. |

### GCMMessage
<a name="apps-application-id-messages-model-gcmmessage"></a>

Specifies the settings for a one-time message that's sent directly to an endpoint through the GCM channel. The GCM channel enables Amazon Pinpoint to send messages to the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Action | string<br />Values: `OPEN_APP \| DEEP_LINK \| URL` | False | The action to occur if the recipient taps the push notification. Valid values are:+   `OPEN_APP` – Your app opens or it becomes the foreground app if it was sent to the background. This is the default action. <br />+   `DEEP_LINK` – Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform. This is a legacy FCM key and cannot be used with FCMV1. You can use RawContent with deep link in the payload. For more information, see [Using Google Firebase Cloud Messaging (FCM) v1 payloads](https://docs.aws.amazon.com/sns/latest/dg/sns-fcm-v1-payloads.html). <br />+   `URL` – The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.  |
| Body | string | False | The body of the notification message. |
| CollapseKey | string | False | An arbitrary string that identifies a group of messages that can be collapsed to ensure that only the last message is sent when delivery can resume. This helps avoid sending too many instances of the same messages when the recipient's device comes online again or becomes active.<br />Amazon Pinpoint specifies this value in the Firebase Cloud Messaging (FCM) `collapse_key` parameter when it sends the notification message to FCM. |
| Data | object | False | The JSON data payload to use for the push notification, if the notification is a silent push notification. This payload is added to the `data.pinpoint.jsonBody` object of the notification. |
| IconReference | string | False | The icon image name of the asset saved in your app. |
| ImageIconUrl | string | False | The URL of the large icon image to display in the content view of the push notification. |
| ImageUrl | string | False | The URL of an image to display in the push notification. |
| PreferredAuthenticationMethod | string | False | The preferred authentication method, with valid values "KEY" or "TOKEN". If a value isn't provided then the **DefaultAuthenticationMethod** is used. |
| Priority | string | False | The priority of the push notification. Valid values are:+   `normal` – The notification might be delayed. Delivery is optimized for battery usage on the recipient's device. Use this value unless immediate delivery is required. <br />+   `high` – The notification is sent immediately and might wake a sleeping device. <br />Amazon Pinpoint specifies this value in the FCM `priority` parameter when it sends the notification message to FCM.<br />The equivalent values for Apple Push Notification service (APNs) are `5`, for `normal`, and `10`, for `high`. If you specify an APNs value for this property, Amazon Pinpoint accepts and converts the value to the corresponding FCM value. |
| RawContent | string | False | The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message. For an example of the RawContent property, see [Schema sample: RawContent object for a push notification](https://docs.aws.amazon.com/pinpoint/latest/apireference/samples-rawcontent-object.html). |
| RestrictedPackageName | string | False | The package name of the application where registration tokens must match in order for the recipient to receive the message. |
| SilentPush | boolean | False | Specifies whether the notification is a silent push notification, which is a push notification that doesn't display on a recipient's device. Silent push notifications can be used for cases such as updating an app's configuration or supporting phone home functionality. |
| SmallImageIconUrl | string | False | The URL of the small icon image to display in the status bar and the content view of the push notification. |
| Sound | string | False | The sound to play when the recipient receives the push notification. You can use the default stream or specify the file name of a sound resource that's bundled in your app. On an Android platform, the sound file must reside in `/res/raw/`. |
| Substitutions | object | False | The default message variables to use in the notification message. You can override the default variables with individual address variables. |
| TimeToLive | integer | False | The amount of time, in seconds, that FCM should store and attempt to deliver the push notification, if the service is unable to deliver the notification the first time. If you don't specify this value, FCM defaults to the maximum value, which is 2,419,200 seconds (28 days).<br />Amazon Pinpoint specifies this value in the FCM `time_to_live` parameter when it sends the notification message to FCM. |
| Title | string | False | The title to display above the notification message on the recipient's device. |
| Url | string | False | The URL to open in the recipient's default mobile browser, if a recipient taps the push notification and the value of the `Action` property is `URL`. |

### MessageBody
<a name="apps-application-id-messages-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### MessageHeader
<a name="apps-application-id-messages-model-messageheader"></a>

Contains the name and value pair of an message header to add to your email. You can have up to 15 MessageHeaders. A header can contain information such as the sender, receiver, route, or timestamp.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Name | string | False | The name of the message header. The header name can contain up to 126 characters. |
| Value | string | False | The value of the message header. The header value can contain up to 870 characters, including the length of any rendered attributes. For example if you add the `{CreationDate}` attribute, it renders as `YYYY-MM-DDTHH:MM:SS.SSSZ` and is 24 characters in length. |

### MessageRequest
<a name="apps-application-id-messages-model-messagerequest"></a>

Specifies the configuration and other settings for a message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Addresses | object | False | A map of key-value pairs, where each key is an address and each value is an [AddressConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-addressconfiguration) object. An address can be a push notification token, a phone number, or an email address. You can use an [AddressConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-addressconfiguration) object to tailor the message for an address by specifying settings such as content overrides and message variables. |
| Context | object | False | A map of custom attributes to attach to the message. For a push notification, this payload is added to the `data.pinpoint` object. For an email or text message, this payload is added to email/SMS delivery receipt event attributes. |
| Endpoints | object | False | A map of key-value pairs, where each key is an endpoint ID and each value is an [EndpointSendConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-endpointsendconfiguration) object. You can use an [EndpointSendConfiguration](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-messages.html#apps-application-id-messages-model-endpointsendconfiguration) object to tailor the message for an endpoint by specifying settings such as content overrides and message variables. |
| MessageConfiguration | [DirectMessageConfiguration](#apps-application-id-messages-model-directmessageconfiguration) | False | The settings and content for the default message and any default messages that you defined for specific channels. |
| TemplateConfiguration | [TemplateConfiguration](#apps-application-id-messages-model-templateconfiguration) | False | The message template to use for the message. |
| TraceId | string | False | The unique identifier for tracing the message. This identifier is visible in message events. |

### MessageResponse
<a name="apps-application-id-messages-model-messageresponse"></a>

Provides information about the results of a request to send a message to an endpoint address.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | True | The unique identifier for the application that was used to send the message. |
| EndpointResult | object | False | A map that contains a multipart response for each address that the message was sent to. In the map, the endpoint ID is the key and the result is the value. |
| RequestId | string | False | The identifier for the original request that the message was delivered for. |
| Result | object | False | A map that contains a multipart response for each address (email address, phone number, or push notification token) that the message was sent to. In the map, the address is the key and the result is the value. |

### MessageResult
<a name="apps-application-id-messages-model-messageresult"></a>

Provides information about the results of sending a message directly to an endpoint address.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| DeliveryStatus | string<br />Values: `SUCCESSFUL \| THROTTLED \| TEMPORARY_FAILURE \| PERMANENT_FAILURE \| UNKNOWN_FAILURE \| OPT_OUT \| DUPLICATE` | True | The delivery status of the message. Possible values are:+   `DUPLICATE` – The endpoint address is a duplicate of another endpoint address. Amazon Pinpoint won't attempt to send the message again. <br />+   `OPT_OUT` – The SendMessages API does not honor the OPT\_OUT attribute when sending to endpoints and therefore will not use the OPT\_OUT message status. <br />+   `PERMANENT_FAILURE` – An error occurred when delivering the message to the endpoint address. Amazon Pinpoint won't attempt to send the message again. <br />+   `SUCCESSFUL` – The message was successfully delivered to the endpoint address. <br />+   `TEMPORARY_FAILURE` – A temporary error occurred. Amazon Pinpoint won't attempt to send the message again. <br />+   `THROTTLED` – Amazon Pinpoint throttled the operation to send the message to the endpoint address. <br />+   `UNKNOWN_FAILURE` – An unknown error occurred.  |
| MessageId | string | False | The unique identifier for the message that was sent. |
| StatusCode | integer | True | The downstream service status code for delivering the message. |
| StatusMessage | string | False | The status message for delivering the message. |
| UpdatedToken | string | False | For push notifications that are sent through the GCM channel, specifies whether the endpoint's device registration token was updated as part of delivering the message. |

### RawEmail
<a name="apps-application-id-messages-model-rawemail"></a>

Specifies the contents of an email message, represented as a raw MIME message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Data | string | False | The email message, represented as a raw MIME message. The entire message must be base64 encoded. |

### SMSMessage
<a name="apps-application-id-messages-model-smsmessage"></a>

Specifies the default settings for a one-time SMS message that's sent directly to an endpoint.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Body | string | False | The body of the SMS message. |
| EntityId | string | False | A registered Entity ID (currently only used when sending messages to recipients in India). |
| Keyword | string | False | The SMS program name that you provided to AWS Support when you requested your dedicated number. |
| MediaUrl | string | False | This field is reserved for future use. |
| MessageType | string<br />Values: `TRANSACTIONAL \| PROMOTIONAL` | False | The SMS message type. Valid values are `TRANSACTIONAL` (for messages that are critical or time-sensitive, such as a one-time passwords) and `PROMOTIONAL` (for messsages that aren't critical or time-sensitive, such as marketing messages). |
| OriginationNumber | string | False | The number to send the SMS message from. The phone number that you specify must exist in your Amazon Pinpoint account—you can't pass an arbitrary phone number. If you want to use a sender ID to send your message, omit this parameter and use `SenderId` instead. |
| SenderId | string | False | The alphabetic Sender ID to display as the sender of the message on a recipient's device. Support for sender IDs varies by country. To specify a phone number as the sender, omit this parameter and use `OriginationNumber` instead. For more information about support for Sender ID by country, see the [Amazon Pinpoint User Guide](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-countries.html). |
| Substitutions | object | False | The message variables to use in the SMS message. You can override the default variables with individual address variables. |
| TemplateId | string | False | A registered Template ID (currently only used when sending messages to recipients in India). |

### SimpleEmail
<a name="apps-application-id-messages-model-simpleemail"></a>

Specifies the contents of an email message, composed of a subject, a text part, and an HTML part.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Headers | Array of type [MessageHeader](#apps-application-id-messages-model-messageheader) | False | List of Headers for the email. |
| HtmlPart | [SimpleEmailPart](#apps-application-id-messages-model-simpleemailpart) | False | The body of the email message, in HTML format. We recommend using HTML format for email clients that render HTML content. You can include links, formatted text, and more in an HTML message. |
| Subject | [SimpleEmailPart](#apps-application-id-messages-model-simpleemailpart) | False | The subject line, or title, of the email. |
| TextPart | [SimpleEmailPart](#apps-application-id-messages-model-simpleemailpart) | False | The body of the email message, in plain text format. We recommend using plain text format for email clients that don't render HTML content and clients that are connected to high-latency networks, such as mobile devices. |

### SimpleEmailPart
<a name="apps-application-id-messages-model-simpleemailpart"></a>

Specifies the subject or body of an email message, represented as textual email data and the applicable character set.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Charset | string | False | The applicable character set for the message content. |
| Data | string | False | The textual data of the message content. |

### Template
<a name="apps-application-id-messages-model-template"></a>

Specifies the name and version of the message template to use for the message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Name | string | False | The name of the message template to use for the message. If specified, this value must match the name of an existing message template. |
| Version | string | False | The unique identifier for the version of the message template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html) resource.<br />If you don't specify a value for this property, Amazon Pinpoint uses the *active version* of the template. The *active version* is typically the version of a template that's been most recently reviewed and approved for use, depending on your workflow. It isn't necessarily the latest version of a template. |

### TemplateConfiguration
<a name="apps-application-id-messages-model-templateconfiguration"></a>

Specifies the message template to use for the message, for each type of channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| EmailTemplate | [Template](#apps-application-id-messages-model-template) | False | The email template to use for the message. |
| InAppTemplate | [Template](#apps-application-id-messages-model-template) | False | The InApp template to use for the message. The InApp template object is not supported for SendMessages. |
| PushTemplate | [Template](#apps-application-id-messages-model-template) | False | The push notification template to use for the message. |
| SMSTemplate | [Template](#apps-application-id-messages-model-template) | False | The SMS template to use for the message. |
| VoiceTemplate | [Template](#apps-application-id-messages-model-template) | False | The voice template to use for the message. This object isn't supported for campaigns. |

### VoiceMessage
<a name="apps-application-id-messages-model-voicemessage"></a>

Specifies the settings for a one-time voice message that's sent directly to an endpoint through the voice channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Body | string | False | The text of the script to use for the voice message. |
| LanguageCode | string | False | The code for the language to use when synthesizing the text of the message script. For a list of supported languages and the code for each one, see the [Amazon Polly Developer Guide](https://docs.aws.amazon.com/polly/latest/dg/what-is.html). |
| OriginationNumber | string | False | The phone number, in E.164 format, to send the voice message from. This value should be one of the dedicated long codes that's assigned to your AWS account. |
| Substitutions | object | False | The default message variables to use in the voice message. You can override the default variables with individual address variables. |
| VoiceId | string | False | The name of the voice to use when delivering the message. For a list of supported voices, see the [Amazon Polly Developer Guide](https://docs.aws.amazon.com/polly/latest/dg/what-is.html). |

## See also
<a name="apps-application-id-messages-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### SendMessages
<a name="SendMessages-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/SendMessages)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/SendMessages)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/SendMessages)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/SendMessages)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/SendMessages)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/SendMessages)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/SendMessages)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/SendMessages)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/SendMessages)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/SendMessages)
