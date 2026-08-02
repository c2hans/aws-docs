---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/flutter-sdk.html
---

# Flutter SDK
<a name="flutter-sdk"></a>

## Introduction
<a name="introduction-3"></a>

 Clickstream Flutter SDK can help you easily collect in-app click stream data from mobile devices to your AWS environments through the data pipeline provisioned by this guidance.

 The SDK relies on the [Clickstream Android SDK](android-sdk.md) and [Clickstream Swift SDK](swift-sdk.md). Therefore, Flutter SDK also supports automatically collecting common user events and attributes (for example, session start, first open). In addition, we've added easy-to-use APIs to simplify data collection in Flutter apps.

### Platform Support
<a name="platform-support-2"></a>

 **Android**: 4.1 (API level 16) and later

 **iOS**: 13 and later

## Integrate the SDK
<a name="integrate-the-sdk-3"></a>

1. Include SDK

   ```
   flutter pub add clickstream_analytics
   ```

    After completion, rebuild your Flutter application.

   ```
   flutter run
   ```

1. Initialize the SDK

   Copy your conﬁguration code from your clickstream guidance web console, and the conﬁguration code should be as follows. You can also manually add this code snippet and replace the values of appId and endpoint after you registered app to a data pipeline in the Clickstream Analytics guidance console.

   ```
   import 'package:clickstream_analytics/clickstream_analytics.dart';

   final analytics = ClickstreamAnalytics();
   analytics.init(
   appId: "your appId",
   endpoint: "https://example.com/collect"
   );
   ```
**Important**
 Your appId and endpoint are already set up.
 We only need to initialize the SDK once after the application starts. It is recommended to do it in the main function of your App.
 We can use bool result = await analytics.init() to get the boolean value of the initialization result.

1. Start using

   **Record event**

    Add the following code where you need to record event.

   ```
   import 'package:clickstream_analytics/clickstream_analytics.dart';

   final analytics = ClickstreamAnalytics();

   // record event with attributes
   analytics.record(name: 'button_click', attributes: {
     "event_category": "shoes",
     "currency": "CNY",
     "value": 279.9
   });

   // record event with name
   analytics.record(name: "button_click");
   ```

   **Add global attributes**

   1. Add global attributes when initializing the SDK.

      The following example code shows how to add traffic source fields as global attributes when initializing the SDK.

      ```
      analytics.init({
        appId: "your appId",
        endpoint: "https://example.com/collect",
        globalAttributes: {
          Attr.TRAFFIC_SOURCE_SOURCE: "amazon",
          Attr.TRAFFIC_SOURCE_MEDIUM: "cpc",
          Attr.TRAFFIC_SOURCE_CAMPAIGN: "summer_promotion",
          Attr.TRAFFIC_SOURCE_CAMPAIGN_ID: "summer_promotion_01",
          Attr.TRAFFIC_SOURCE_TERM: "running_shoes",
          Attr.TRAFFIC_SOURCE_CONTENT: "banner_ad_1",
          Attr.TRAFFIC_SOURCE_CLID: "amazon_ad_123",
          Attr.TRAFFIC_SOURCE_CLID_PLATFORM: "amazon_ads",
          Attr.APP_INSTALL_CHANNEL: "amazon_store"
        }
      });
      ```

   1. Add global attributes after initializing the SDK.

   ```
   analytics.addGlobalAttributes({
     Attr.TRAFFIC_SOURCE_MEDIUM: "Search engine",
     "level": 10
   });
   ```

   It is recommended to set global attributes after each SDK initialization, and global attributes will be included in all events that occur after it is set.

   **Delete global attributes**

   ```
   analytics.deleteGlobalAttributes(["level"]);
   ```

   **Login and logout**

   ```
   // when user login success.
   analytics.setUserId("userId");

   // when user logout
   analytics.setUserId(null);
   ```

   **Add user attributes**

   ```
   analytics.setUserAttributes({
     "userName":"carl",
     "userAge": 22
   });
   ```

   Current login user's attributes will be cached in disk, so the next time app launches you don't need to set all user's attribute again, of course you can use the same api analytics.setUserAttributes() to update the current user's attribute when it changes.

**Important**
If your application is already published and most users have already logged in, please manually set the user attributes once when integrating the Clickstream SDK for the ﬁrst time to ensure that subsequent events contain user attributes.

**Record event with items**

 You can add the following code to log an event with an item, and you can add custom item attribute in the attributes Map. In addition to the preset attributes, an item can add up to 10 custom attributes.

```
var itemBook = ClickstreamItem(
    id: "123",
    name: "Nature",
    category: "book",
    price: 99,
    attributes: {
      "book_publisher": "Nature Research"
    }
);

analytics.record(
    name: "view_item",
    attributes: {
        Attr.VALUE: 99,
        Attr.CURRENCY: "USD",
        "event_category": "recommended"
    },
    items: [itemBook]
);
```

 For logging more attributes in an item, please refer to [item attributes.](web-sdk.md#get-started)

**Important**
Only pipelines from version 1.1.0 can handle items with custom attribute.
**item id **is a required attribute. If not set, the item will be discarded.

**Record Screen View events manually **

By default, SDK will automatically track the **preset \_screen\_view** event when Android Activity triggers **onResume** or iOS **ViewController** triggers **viewDidAppear**.

You can also manually record screen view events whether automatic screen view tracking is enabled, add the following code to record a screen view event with two attributes:
+ **SCREEN\_NAME** Required. Your screen's name.
+ **SCREEN\_UNIQUE\_ID **Optional. Set the id of your Widget. If you do not set, the SDK will set a default value based on the hashcode of the current Activity or **ViewController**.

```
analytics.recordScreenView(
  screenName: 'Main',
  screenUniqueId: '123adf',
  attributes: { ... }
);
```

**Other configurations**

 In addition to the required appId and endpoint, you can configure other information to get more customized usage when initializing the SDK:

```
final analytics = ClickstreamAnalytics(); analytics.init(
appId: "your appId",
endpoint: "https://example.com/collect", isLogEvents: false,
isCompressEvents: false, sendEventsInterval: 10000, isTrackScreenViewEvents: true, isTrackUserEngagementEvents: true, isTrackAppExceptionEvents: false, authCookie: "your auth cookie", sessionTimeoutDuration: 1800000,
globalAttributes: {
    "_traffic_source_medium": "Search engine",
  }
);
```

Here is an explanation of each option:

|  **Name**  |  **Required**  |  **Default value**  |  **Description**  |
| --- | --- | --- | --- |
|  appId  |  true  |  N/A  |  the app id of your application in control plane  |
|  endpoint  |  true  |  N/A  |  the endpoint path you will upload the event to Clickstream ingestion server  |
|  isLogEvents  |  false  |  false  |  whether to print out event json in console for debugging events  |
|  isCompressEvents  |  false  |  true  |  whether to compress event content by gzip when uploading events  |
|  sendEventsInterval  |  false  |  10,000  |  event sending interval in milliseconds  |
|  isTrackScreenViewEvents  |  false  |  true  |  whether auto record screen view events in app  |
|  isTrackUserEngagementEvents  |  false  |  true  |  whether auto record user engagement events in app  |
|  isTrackAppExceptionEvents  |  false  |  false  |  whether auto track exception event in app  |
|  authCookie  |  false  |  N/A |  your auth cookie for AWS application load balancer auth cookie  |
| sessionTimeoutDuration  |  false  |  1,800,000  |  the duration for session timeout in milliseconds  |
| globalAttributes | false | -- | the global attributes when initializing the SDK |

**Configuration update**

 You can update the default configuration after initializing the SDK. The following are additional configuration options that you can customize.

```
final analytics = ClickstreamAnalytics();
analytics.updateConfigure(
     appId: "your appId",
     endpoint: "https://example.com/collect",
     isLogEvents: true,
     isCompressEvents: false,
     isTrackScreenViewEvents: false
     isTrackUserEngagementEvents: false,
     isTrackAppExceptionEvents:
     false, authCookie: "test cookie");
```

**Send event immediately**

```
final analytics = ClickstreamAnalytics();
analytics.flushEvents();
```

**Disable SDK**

 You can disable the SDK in the scenario you need. After disabling the SDK, the SDK will not handle the logging and sending of any events. You can enable the SDK when you need to continue logging events.

```
final analytics = ClickstreamAnalytics();

// disable SDK
ClickstreamAnalytics.disable();

// enable SDK
ClickstreamAnalytics.enable();
```

**Debug events**

 You can complete the following steps to view the event raw JSON and debug your events.

1.  Using **analytics.updateConﬁgure()** API and set the **isLogEvents** attributes with **true **in debug mode, for example:

   ```
   // log the event in debug mode.
   analytics.updateConfigure(isLogEvents: true);
   ```

1.  Integrate the SDK and launch your app.

   1. For Android application logs, we can see the logs directly in the terminal window. You can also use ﬁlters in the Android Studio **Logcat** window to view logs.

   1. For iOS application logs, launch it via Xcode and open the log panel to see it.

1. Input **EventRecorder** to the ﬁlter, and you will see the JSON content of all events recorded by Clickstream Flutter SDK.

## Data format definition
<a name="data-format-definition-3"></a>

### Data types
<a name="data-types-123"></a>

Clickstream Flutter SDK supports the following data types.

|  **Data type**  |  **Range**  |  **Example**  |
| --- | --- | --- |
| int | -9223372036854775808 ～ 9223372036854775807 | 12 |
| double | 5e-324 \~ 1.79e\+308 | 3.14 |
| bool | true, false | true |
| String | max 1024 characters | "Clickstream" |

### Naming rules
<a name="naming-rules-123"></a>

1. The event name and attribute name cannot start with a number, and must contain only uppercase and lowercase letters, numbers, and underscores. In case of an invalid attribute name or user attribute name, it will discard the attribute and record error.

1. Do not use `_` as a preﬁx in an event name or attribute name. The `_` preﬁx is reserved for the guidance.

1. The event name and attribute name are case-sensitive, so `Add_to_cart` and `add_to_cart` will be recognized as two diﬀerent event names.

### Event and attribute limitation
<a name="event-and-attribute-limitation-123"></a>

To improve the eﬃciency of querying and analysis, we apply limits to event data as follows:

| Name | Suggestion | Hard limit | Strategy | Error code |
| --- | --- | --- | --- | --- |
| Event name invalid | N/A | N/A | discard event, print log, and record \_clickstream\_errorevent | 1001 |
| Length of event name | under 25 characters | 50 characters | discard event, print log, and record \_clickstream\_errorevent | 1002 |
| Length of event attribute name | under 25 characters | 50 characters | discard the attribute, print log, and record error in event attribute | 2001 |
| Attribute name invalid | N/A | N/A | discard the attribute, print log, and record error in event attribute | 2002 |
| Length of event attribute value | under 100 characters | 1024 characters | discard the attribute, print log, and record error in event attribute | 2003 |
| Event attribute per event | under 50 attributes | 500 event attributes | discard the attribute, print log, and record error in event attribute | 2004 |
| User attribute number | under 25 attributes | 100 user attributes | discard event, print log, and record \_clickstream\_errorevent | 3001 |
| Length of User attribute name | under 25 characters | 50 characters | discard event, print log, and record \_clickstream\_errorevent | 3002 |
| User attribute name invalid | N/A | N/A | discard event, print log, and record \_clickstream\_errorevent | 3003 |
| Length of User attribute value | under 50 characters | 256 characters | discard event, print log, and record \_clickstream\_errorevent | 3004 |
| Item number in one event | under 50 items | 100 items | discard the attribute, print log, and record error in event attribute | 4001 |
| Length of item attribute value | under 100 characters | 256 characters | discard the attribute, print log, and record error in event attribute | 4002 |
| Custom item attribute number in one item | under 10 custom attributes | 10 custom attributes | discard the attribute, print log, and record error in event attribute | 4003 |
| Length of item attribute name | under 25 characters | 50 characters | discard the attribute, print log, and record error in event attribute | 4004 |
| Item attribute name invalid | N/A | N/A | discard the attribute, print log, and record error in event attribute | 4005 |

**Important**
The character limits are the same for single-width character languages (e.g., English) and double-width character languages (e.g., Chinese).
The limit of event attribute per event include preset attributes.
If the attribute or user attribute with the same name is added more than twice, the latest value will apply.
All errors that exceed the limit will be recorded \_error\_code and \_error\_message these two attribute in the event attributes.

## Preset events
<a name="preset-events-3"></a>

 For Android, refer to [Android SDK preset events](android-sdk.md).

 For iOS, refer to [Swift SDK preset events](swift-sdk.md).

## Event attributes
<a name="event-attributes-6"></a>

 For Android, refer to [Android SDK event attributes](android-sdk.md).

 For iOS, refer to [Swift SDK event attributes](swift-sdk.md).

## Change log
<a name="change-log-3"></a>

 For more information, see [GitHub change log](https://github.com/awslabs/clickstream-flutter/releases).

 Native SDK version dependencies

|  **Flutter SDK Version**  |  **Android SDK Version**  |  **Swift SDK Version**  |
| --- | --- | --- |
|  0.3.0 \~ 0.4.0  |  0.12.0  |  0.11.0  |
|  0.2.0 |  0.10.0 |  0.9.1 |
|  0.1.0 |  0.9.0 |  0.8.0 |

## References
<a name="reference-link-3"></a>

 [https://github.com/awslabs/clickstream-flutter](https://github.com/awslabs/clickstream-flutter)

 [https://github.com/awslabs/clickstream-flutter/issues](https://github.com/awslabs/clickstream-flutter/issues)
