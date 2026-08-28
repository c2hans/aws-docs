---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/reactnative-sdk.html
---

# ReactNative SDK
<a name="reactnative-sdk"></a>

 Clickstream React NativeSDK can help you easily collect in-app click stream data from mobile devices to your AWS environments through the data pipeline provisioned by this guidance.

The SDK relies on the [Clickstream Android SDK](android-sdk.md) and [Clickstream Swift SDK](swift-sdk.md). Therefore, React Native SDK also supports automatically collect common user events and attributes (e.g., session start, first open) . In addition, we've added easy-to-use APIs to simplify data collection in React Native apps.

**Platform Support **

**Android**: 4.1 (API level 16) and later

**iOS:** 13 and later

## Integrate the SDK
<a name="integrate-the-sdk-reactnative"></a>

 1. Include SDK

```
npm install @aws/clickstream-react-native
```

 After completion, you need to install the pod dependencies for iOS:

```
cd ios pod install;
```

2. Initialize the SDK

Copy your conﬁguration code from your clickstream guidance web console, and the conﬁguration code should be as follows. You can also manually add this code snippet and replace the values of appId and endpoint after you registered app to a data pipeline in the Clickstream Analytics guidance console

```
import { ClickstreamAnalytics } from '@aws/clickstream-react-native';

ClickstreamAnalytics.init({
    appId: 'your appId',
    endpoint: 'https://example.com/collect',
});
```

**Important**
Your appId and endpoint are already set up in it. We only need to initialize the SDK once after the application starts.
Make sure you call ClickstreamAnalytics.init() as early as possible in your application's life-cycle. And make sure the SDK is initialized when calling other APIs.
We can use const result = await ClickstreamAnalytics.init() to get the boolean value of the initialization result.

3. Start using.

**Record event **

Add the following code where you need to record event.

```
import { ClickstreamAnalytics } from'@aws/clickstream-react-native';

// record event with attributes
ClickstreamAnalytics.record({
  name: 'button_click',
  attributes: {
    event_category: 'shoes',
    currency: 'CNY',
    value: 279.9,
  },
});

// record event with name
ClickstreamAnalytics.record({name:'button_click'});
```

**Add global attributes**

1. Add global attributes when initializing the SDK.

   The following example code shows how to add traffic source fields as global attributes when initializing the SDK.

```
import { ClickstreamAnalytics, Attr } from '@aws/clickstream-react-native';

ClickstreamAnalytics.init({
   appId: "your appId",
   endpoint: "https://example.com/collect",
   globalAttributes:{
     [Attr.TRAFFIC_SOURCE_SOURCE]: 'amazon',
     [Attr.TRAFFIC_SOURCE_MEDIUM]: 'cpc',
     [Attr.TRAFFIC_SOURCE_CAMPAIGN]: 'summer_promotion',
     [Attr.TRAFFIC_SOURCE_CAMPAIGN_ID]: 'summer_promotion_01',
     [Attr.TRAFFIC_SOURCE_TERM]: 'running_shoes',
     [Attr.TRAFFIC_SOURCE_CONTENT]: 'banner_ad_1',
     [Attr.TRAFFIC_SOURCE_CLID]: 'amazon_ad_123',
     [Attr.TRAFFIC_SOURCE_CLID_PLATFORM]: 'amazon_ads',
     [Attr.APP_INSTALL_CHANNEL]: 'amazon_store',
   }
});
```

2. Add global attributes after initializing the SDK

```
import { ClickstreamAnalytics, Attr } from '@aws/clickstream-react-native';

ClickstreamAnalytics.setGlobalAttributes({
  [Attr.TRAFFIC_SOURCE_MEDIUM]: "Search engine",
  level: 10,
});
```

It is recommended to set global attributes after each SDK initialization, and global attributes will be included in all events that occur after it is set.

**Delete global attribute**

```
ClickstreamAnalytics.deleteGlobalAttributes(['level','_traffic_source_medium']);
```

**Login and logout**

```
import { ClickstreamAnalytics } from '@aws/clickstream-react-native';

// when user login success.
ClickstreamAnalytics.setUserId("userId");

// when user logout
ClickstreamAnalytics.setUserId(null);
```

**Add user attribute**

```
analytics.setUserAttributes({
  "userName":"carl",
  "userAge": 22
});
```

Current login user's attributes will be cached in disk, so the next time app launches you don't need to set all user's attribute again, of course you can use the same api ClickstreamAnalytics.setUserAttributes() to update the current user's attribute when it changes.

**Important**
If your application is already published and most users have already logged in, please manually set the user attributes once when integrating the Clickstream SDK for the ﬁrst time to ensure that subsequent events contain user attributes.

**Record event with items**

 You can add the following code to log an event with an item.

```
import { ClickstreamAnalytics, Item, Attr } from '@aws/clickstream-react-native';

const itemBook: Item = {
  id: '123',
  name: 'Nature',
  category: 'book',
  price: 99,
  book_publisher: "Nature Research",
};
ClickstreamAnalytics.record({
  name: 'view_item',
  attributes: {
    [Attr.VALUE]: 99,
    [Attr.CURRENCY]: 'USD',
    event_category: 'recommended',
  },
  items: [itemBook],
});
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
import { ClickstreamAnalytics } from '@aws/clickstream-react-native';

ClickstreamAnalytics.record({
  name: ClickstreamAnalytics.Event.SCREEN_VIEW,
  attributes: {
    [ClickstreamAnalytics.Attr.SCREEN_NAME]: 'HomeComponet',
    [ClickstreamAnalytics.Attr.SCREEN_UNIQUE_ID]: '123adf',
  },
});
```

**Record Screen Views for React Navigation **

Here's an example of globally logging React Native screen view events when using React Navigation 6.x

For other version of React Navigation, you can refer to official documentation: Screen tracking for analytics.

**Send event immediately**

```
import { ClickstreamAnalytics } from '@aws/clickstream-react-native';

ClickstreamAnalytics.flushEvents();
```

**Other configurations**

 In addition to the required appId and endpoint, you can configure other information to get more customized usage when initializing the SDK:

```
import { ClickstreamAnalytics } from '@aws/clickstream-react-native';

ClickstreamAnalytics.init({
  appId: 'your appId',
  endpoint: 'https://example.com/collect',
  isLogEvents: true,
  isCompressEvents: true,
  isTrackScreenViewEvents: false,
  isTrackUserEngagementEvents: true,
  isTrackAppExceptionEvents: true,
  sendEventsInterval: 15000,
  sessionTimeoutDuration: 1800000,
  authCookie: 'your auth cookie',
  globalAttributes: {
    _traffic_source_medium: 'Search engine',
  },
});
```

Here is an explanation of each option:

|  **Name**  |  **Required**  |  **Default value**  |  **Description**  |
| --- | --- | --- | --- |
|  appId  |  true  |  N/A  |  the app id of your application in control plane  |
|  endpoint  |  true  |  N/A  |  the endpoint path you will upload the event to Clickstream ingestion server  |
|  isLogEvents  |  false  |  false  |  whether to print out event json in console for debugging events  |
|  isCompressEvents  |  false  |  true  |  whether to compress event content by gzip when uploading events  |
|  isTrackScreenViewEvents  |  false  |  true  |  whether auto record screen view events in app  |
|  isTrackUserEngagementEvents  |  false  |  true  |  whether auto record user engagement events in app  |
|  isTrackAppExceptionEvents  |  false  |  false  |  whether auto track exception event in app  |
|  sendEventsInterval  |  false  |  10,000  |  event sending interval in milliseconds  |
| sessionTimeoutDuration  |  false  |  1,800,000  |  the duration for session timeout in milliseconds  |
|  authCookie  |  false  |  N/A |  your auth cookie for AWS application load balancer auth cookie  |
| globalAttributes | false | -- | the global attributes when initializing the SDK |

**Configuration update**

 You can update the default configuration after initializing the SDK. The following are additional configuration options that you can customize.

```
import { ClickstreamAnalytics } from '@aws/clickstream-react-native';

ClickstreamAnalytics.updateConfigure({
  appId: 'your appId',
  endpoint: 'https://example.com/collect',
  isLogEvents: true,
  authCookie: 'your auth cookie',
  isCompressEvents: true,
  isTrackScreenViewEvents: false,
  isTrackUserEngagementEvents: false,
  isTrackAppExceptionEvents: false,
});
```

**Disable SDK**

 You can disable the SDK in the scenario you need. After disabling the SDK, the SDK will not handle the logging and sending of any events. You can enable the SDK when you need to continue logging events.

```
import { ClickstreamAnalytics } from '@aws/clickstream-react-native';

// disable SDK
ClickstreamAnalytics.disable();

// enable SDK
ClickstreamAnalytics.enable();
```

**Debug events**

 You can complete the following steps to view the event raw JSON and debug your events.

1.  Enable the **isLogEvents** configuration when initializing the SDK.

   ```
   import { ClickstreamAnalytics } from '@aws/clickstream-react-native';

   ClickstreamAnalytics.init({
     appId: 'your appId',
     endpoint: 'https://example.com/collect',
     isLogEvents: true,
   });
   ```

1.  After configuring **isLogEvents:true,** when you record an event, you can see the event raw json in AndroidStudio Logcat or Xcode debug console by filter **EventRecorder.**

## Data format definition
<a name="data-format-definition-4"></a>

Refer to [Web SDK Data format ](web-sdk.md#data-format-definition-2)definition.

## Preset events
<a name="preset-events-4"></a>

 For Android, refer to [Android SDK preset events](android-sdk.md).

 For iOS, refer to [Swift SDK preset events](swift-sdk.md).

## Event attributes
<a name="event-attributes-7"></a>

 For Android, refer to [Android SDK event attributes](android-sdk.md).

 For iOS, refer to [Swift SDK event attributes](swift-sdk.md).

## Change log
<a name="change-log-4"></a>

 For more information, see [GitHub change log](https://github.com/awslabs/clickstream-flutter/releases).

 Native SDK version dependencies

|  **Flutter SDK Version**  |  **Android SDK Version**  |  **Swift SDK Version**  |
| --- | --- | --- |
|  0.1.0 \~ 0.2.0  |  0.12.0  |  0.11.0  |

**Sample project**

[Sample React Native Project](https://github.com/aws-samples/clickstream-sdk-samples/tree/main/react-native) for SDK integration.

## References
<a name="reference-link-4"></a>

 [*Source code*](https://github.com/awslabs/clickstream-flutter)

 [*Project issue*](https://github.com/awslabs/clickstream-flutter/issues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
