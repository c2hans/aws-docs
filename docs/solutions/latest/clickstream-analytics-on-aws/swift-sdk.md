---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/swift-sdk.html
---

# Swift SDK
<a name="swift-sdk"></a>

## Introduction
<a name="introduction-1"></a>

Clickstream Swift SDK can help you easily collect in-app click stream data from iOS devices to your AWS environments through the data pipeline provisioned by this guidance.

 The SDK is based on the Amplify for Swift Core Library and developed according to the Amplify Swift SDK plug-in specification. In addition, the SDK is equipped with features that automatically collect common user events and attributes (for example, screen view, first open) to simplify data collection for users.

### Platform Support
<a name="platform-support-1"></a>

 Clickstream Swift SDK supports iOS 13\+.

 Clickstream Swift SDK requires Xcode 13.4 or higher to build.

## Integrate the SDK
<a name="integrate-the-sdk-1"></a>

### 1 Add Package
<a name="add-package"></a>

 The guidance uses Swift Package Manager to distribute Clickstream Swift SDK. Open your project in Xcode and select **File** > **Add Packages**.

![Xcode File menu with Add Packages option highlighted.](https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/add-packages.png)

1.  Copy the Clickstream Swift SDK GitHub repository URL and paste it into the search bar.

   ```
   https://github.com/awslabs/clickstream-swift
   ```

1.  Check the rules for the version of the SDK that you want Swift Package Manager to install, it is recommended to choose **Up to Next Major Version**, then click **Add Package**.

1.  Keep the Clickstream product checked as default.

1.  Choose **Add Package** again to finish the package installation.

![Dialog box for choosing package products with Clickstream library selected for SwiftDemoApp target.](https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/add-package-1.png)

### 2 Parameter configuration
<a name="parameter-configuration"></a>

 Download your `amplifyconfiguration.json` file from your Clickstream guidance control plane. Copy and paste it to your project root folder:

![Xcode project navigator showing amplifyconfiguration file highlighted in the project structure.](https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/configure-parameter.png)

 The JSON file will be as follows:

```
{
  "analytics": {
    "plugins": {
      "awsClickstreamPlugin ": {
        "appId": "appId",
        "endpoint": "https://example.com/collect",
        "isCompressEvents": true,
        "autoFlushEventsInterval": 10000,
        "isTrackAppExceptionEvents": false
      }
    }
  }
}
```

 In the file, your `appId` and `endpoint` are already configured. The explanation for each property is as follows:
+  **appId (Required):** the app id of your project in web console.
+  **endpoint (Required):** the endpoint url you will upload the event to AWS server.
+  **isCompressEvents:** whether to compress event content when uploading events, and the default value is `true`.
+  **autoFlushEventsInterval:** event sending interval, and the default value is `10s`.
+  **isTrackAppExceptionEvents:** whether auto track exception event in app, and the default value is `false `.

### 3 Initialize the SDK
<a name="initialize-the-sdk-1"></a>

 Once you have configured the parameters, you need to initialize it in AppDelegate's `didFinishLaunchingWithOptions` lifecycle method to use the SDK.

**Swift**

```
import Clickstream
...
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // Override point for customization after application launch.
    do {
        try ClickstreamAnalytics.initSDK()
    } catch {
        assertionFailure("Fail to initialize ClickstreamAnalytics: \(error)")
    }
    return true
}
```

**Objective-C**

```
@import Clickstream;

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    NSError *error = nil;
    [ClickstreamObjc initSDKAndReturnError:&error];
    if (error) {
        NSLog(@"Fail to initialize ClickstreamAnalytics: %@", error.localizedDescription);
    }
    return YES;
}
```

**SwfitUI configuration**

If your project is developed with SwiftUI, you need to create an application delegate and attach it to your App through `UIApplicationDelegateAdaptor`.

```
@main
struct YourApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) var appDelegate
    var body: some Scene {
        WindowGroup {
            YourView()
        }
    }
}
```

Clickstream Swift SDK depends on method swizzling to automatically record screen views. SwiftUI apps must record screen view events manually, and disable automatic tracking of screen view events by setting `configuration.isTrackScreenViewEvents(false)` when the SDK is initialized.

### 5 Start using
<a name="record-event-1"></a>

**Record event**

 Add the following code where you need to report an event.

**Swift**

```
import Clickstream

// for record an event with custom attributes
let attributes: ClickstreamAttribute = [
    "category": "shoes",
    "currency": "CNY",
    "value": 279.9
]
ClickstreamAnalytics.recordEvent("button_click", attributes)

// for record an event directly
ClickstreamAnalytics.recordEvent("button_click")
```

**Objective-C**

```
@import Clickstream;

// for record an event with custom attributes
NSDictionary *attributes =@{
    @"category": @"shoes",
    @"currency": @"CNY",
    @"value": @12.34
};
[ClickstreamObjc recordEvent:@"button_click" :attributes];
```

**Add global attribute**

1. Add global attributes when initializing the SDK.

   The following example code shows how to add traffic source fields as global attributes when initializing the SDK.

   **Swift**

   ```
   import Clickstream

   let configuration = ClickstreamConfiguration()
       .withAppId("your appId")
       .withEndpoint("https://example.com/collect")
       .withInitialGlobalAttributes([
           ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_SOURCE: "amazon",
           ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_MEDIUM: "cpc",
           ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_CAMPAIGN: "summer_promotion",
           ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_CAMPAIGN_ID: "summer_promotion_01",
           ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_TERM: "running_shoes",
           ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_CONTENT: "banner_ad_1",
           ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_CLID: "amazon_ad_123",
           ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_CLID_PLATFORM: "amazon_ads",
           ClickstreamAnalytics.Attr.APP_INSTALL_CHANNEL: "App Store"
   ])
   try ClickstreamAnalytics.initSDK(configuration)
   ```

   **Objective-C**

   ```
   @import Clickstream;

   NSDictionary *globalAttributes = @{
       Attr.TRAFFIC_SOURCE_SOURCE: @"amazon",
       Attr.TRAFFIC_SOURCE_MEDIUM: @"cpc",
       Attr.TRAFFIC_SOURCE_CAMPAIGN: @"summer_promotion",
       Attr.TRAFFIC_SOURCE_CAMPAIGN_ID: @"summer_promotion_01",
       Attr.TRAFFIC_SOURCE_TERM: @"running_shoes",
       Attr.TRAFFIC_SOURCE_CONTENT: @"banner_ad_1",
       Attr.TRAFFIC_SOURCE_CLID: @"amazon_ad_123",
       Attr.TRAFFIC_SOURCE_CLID_PLATFORM: @"amazon_ads",
       Attr.APP_INSTALL_CHANNEL: @"App Store",
   };
   ClickstreamConfiguration *configuration = [[[[[ClickstreamConfiguration alloc] init]
       withAppId:@"your appId"]
       withEndpoint:@"https://example.com/collect"]
       withInitialGlobalAttributesObjc:globalAttributes];
   [ClickstreamObjc initSDK:configuration error: &error];
   ```

1. Add global attributes after initializing the SDK.

   **Swift**

   ```
   import Clickstream

   let globalAttribute: ClickstreamAttribute = [
       ClickstreamAnalytics.Attr.APP_INSTALL_CHANNEL: "App Store",
       "class": 6,
       "level": 5.1,
       "isOpenNotification": true,
   ]
   ClickstreamAnalytics.addGlobalAttributes(globalAttribute)

   // for delete an global attribute
   ClickstreamAnalytics.deleteGlobalAttributes("level")
   ```

   **Objective-C**

   ```
   @import Clickstream;

   NSDictionary *attributes =@{
       Attr.APP_INSTALL_CHANNEL: @"App Store",
       @"class": @6,
       @"level": @5.1,
       @"isOpenNotification": @YES
   };
   [ClickstreamObjc addGlobalAttributes :attributes];

   // for delete an global attribute
   [ClickstreamObjc deleteGlobalAttributes: @[@"level"]];
   ```

It is recommended to set global attributes when initializing the SDK, global attributes will be included in all events that occur after it is set.

**Login and logout**

**Swift**

```
import Clickstream

// when user login usccess.
ClickstreamAnalytics.setUserId("userId")

// when user logout
ClickstreamAnalytics.setUserId(nil)
```

****Objective-C****

```
@import Clickstream;

// when user login usccess.
[ClickstreamObjc setUserId:@"userId"];

// when user logout
[ClickstreamObjc setUserId:NULL];
```

**Add user attribute**

**Swift**

```
import Clickstream

let userAttributes : ClickstreamAttribute=[
    "_user_age": 21,
    "_user_name": "carl"
]
ClickstreamAnalytics.addUserAttributes(userAttributes)
```

****Objective-C****

```
@import Clickstream;

NSDictionary *userAttributes =@{
    @"_user_age": @21,
    @"user_name": @"carl"
};
[ClickstreamObjc addUserAttributes:userAttributes];
;
```

Current login user's attributes will be cached in disk, so the next time app launch you don't need to set all user's attribute again, of course you can use the same API `ClickstreamAnalytics.addUserAttributes()` to update the current user's attribute when it changes.

**Important**
 If your application is already published and most users have already logged in, please manually set the user attributes once when integrate the Clickstream SDK for the first time to ensure that subsequent events contains user attributes.

**Record event with items**

You can add the following code to log an event with an item.

**Swift**

```
import Clickstream

let attributes: ClickstreamAttribute = [
    ClickstreamAnalytics.Item.ITEM_ID: "123",
    ClickstreamAnalytics.Item.CURRENCY: "USD",
    "event_category": "recommended"
]

let item_book: ClickstreamAttribute = [
    ClickstreamAnalytics.Item.ITEM_ID: 123,
    ClickstreamAnalytics.Item.ITEM_NAME: "Nature",
    ClickstreamAnalytics.Item.ITEM_CATEGORY: "book",
    ClickstreamAnalytics.Item.PRICE: 99.9,
    "book_publisher": "Nature Research"
]
ClickstreamAnalytics.recordEvent("view_item", attributes, [item_book])
```

****Objective-C****

```
@import Clickstream;

NSDictionary *attributes = @{
    Attr.VALUE: @99.9,
    Attr.CURRENCY: @"USD",
    "event_category": @"recommended"
};
NSDictionary *item_book = @{
    ClickstreamItemKey.ITEM_ID: @123,
    ClickstreamItemKey.ITEM_NAME: @"Nature",
    ClickstreamItemKey.ITEM_CATEGORY: @"book",
    ClickstreamItemKey.PRICE: @99.9,
    "book_publisher": @"Nature Research"
};
[ClickstreamObjc recordEvent:@"view_item" :attributes, @[item_book]];
```

For more information about logging more attributes in an item, refer to item attributes.

**Important**
Only pipelines from version 1.1.0 can handle items with custom attribute.
**ITEM\_ID **is required attribute, if not set the item will be discarded.

**Record screen view events manually **

By default, SDK will automatically track the preset \_screen\_view event when ViewController triggers viewDidAppear.

You can manually record screen view events whether automatic screen view tracking is enabled, add the following code to record a screen view event with two attributes.
+ **SCREEN\_NAME:** Required. Your screen's name.
+ **SCREEN\_UNIQUE\_ID:** Optional. Set the unique value of your ViewController or UIView. If you do not set, SDK will set a default value based on the current ViewController's hashValue.

**Swift**

```
import Clickstream

ClickstreamAnalytics.recordEvent(ClickstreamAnalytics.EventName.SCREEN_VIEW, [
    ClickstreamAnalytics.Attr.SCREEN_NAME: "HomeView",
    ClickstreamAnalytics.Attr.SCREEN_UNIQUE_ID: "your screen uniqueId"
])
```

****Objective-C****

```
@import Clickstream;

NSDictionary *attributes = @{
    Attr.SCREEN_NAME: @"HomeView",
    Attr.SCREEN_UNIQUE_ID: @"your screen uniqueId"
};
```

**Send event immediately**

**Swift**

```
import Clickstream
// for send event immediately. ClickstreamAnalytics.flushEvents()
```

****Objective-C****

```
@import Clickstream;
// for send event immediately.
[ClickstreamObjc flushEvents];
```

**Disable SDK**

You can disable the SDK if needed. After disabling the SDK, the SDK will not handle the logging and sending of any events. Of course you can enable the SDK when you need to continue logging events.

**Swift**

```
import Clickstream

// disable SDK ClickstreamAnalytics.disable()

// enable SDK
ClickstreamAnalytics.enable()
```

****Objective-C****

```
@import Clickstream;

// disable SDK
[ClickstreamObjc disable];

// enable SDK
[ClickstreamObjc enable];
```

**Other configurations **

In addition to the required appId and endpoint, you can configure other information to get more customized usage when initializing the SDK:

**Swift**

```
import Clickstream

let configuration = ClickstreamConfiguration()
    .withAppId("your appId")
    .withEndpoint("https://example.com/collect")
    .withLogEvents(true)
    .withCompressEvents(true)
    .withSendEventInterval(10000)
    .withSessionTimeoutDuration(1800000)
    .withTrackScreenViewEvents(true)
    .withTrackUserEngagementEvents(true)
    .withTrackAppExceptionEvents(true)
    .withAuthCookie("your authentication cookie")
    .withInitialGlobalAttributes([ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_SOURCE: "amazon"])
try ClickstreamAnalytics.initSDK(configuration)
```

**Objective-C**

```
@import Clickstream;

ClickstreamConfiguration *configuration = [[[[[[[[[[[[[ClickstreamConfiguration alloc] init]
    withAppId:@"your appId"]
    withEndpoint:@"https://example.com/collect"]
    withLogEvents:TRUE]
    withCompressEvents:TRUE]
    withSendEventInterval: 10000]
    withSessionTimeoutDuration: 1800000]
    withTrackScreenViewEvents:TRUE]
    withTrackUserEngagementEvents:TRUE]
    withTrackAppExceptionEvents:TRUE]
    withAuthCookie: @"your auth cookie"]
    withInitialGlobalAttributesObjc:@{Attr.TRAFFIC_SOURCE_SOURCE: @"amazon"}];
[ClickstreamObjc initSDK:configuration error: &error];
```

Here is an explanation of each option:

|  **Method name**  |  **Parameter type**  |  **Required**  |  **Default value**  |  **Description**  |
| --- | --- | --- | --- | --- |
|  withAppId()  | String |  true  |  --  | The app ID of your application in the web console. |
|  withEndpoint() | String |  true  |  --  |  The endpoint path where you will upload the event to the Clickstream ingestion server. |
| withLogEvents() | Bool | false | false | Whether to automatically print an event JSON for [debugging events](https://awslabs.github.io/clickstream-analytics-on-aws/en/latest/sdk-manual/swift/#debug-events). |
| withCompressEvents() | Bool | false | true | Whether to compress event content by gzip when uploading events. |
| withSendEventsInterval() | Int | false | 10,000 | Event sending interval in milliseconds. |
| withSessionTimeoutDuration() | Int64 | false | 1,800,000 | The duration of the session timeout in milliseconds. |
| withTrackScreenViewEvents()  | Bool | false | true | Whether to auto-record screen view events. |
| withTrackUserEngagementEvents() | Bool | false | true | Whether to auto-record user engagement events. |
|  withTrackAppExceptionEvents() | Bool |  false  | true | Whether to auto-record app exception events. |
| withAuthCookie() | String |  false  |  --  | Your auth cookie for AWS application load balancer auth cookie. |

**Configuration update**

After initializing the SDK, you can use the following code to customize the conﬁguration of the SDK.

**Swift**

```
import Clickstream

// config the sdk after initialize.
do {
    var configuration = try ClickstreamAnalytics.getClickstreamConfiguration()
    configuration.withAppId("your appId")
        .withEndpoint("https://example.com/collect")
        .withLogEvents(true)
        .withCompressEvents(true)
        .withTrackAppExceptionEvents(true)
        .withTrackScreenViewEvents(true)
        .withTrackUserEngagementEvents(true)
        .withAuthCookie("your authentication cookie")
} catch {
    print("Failed to config ClickstreamAnalytics: \(error)")
}
```

**Objective-C**

```
@import Clickstream;

// config the sdk after initialize.
ClickstreamConfiguration *configuration = [ClickstreamObjc getClickstreamConfigurationAndReturnError:&error];
configuration = [[[[[[[configuration withAppId:@"your appId"]
    withEndpoint:@"https://example.com/collect"]
    withLogEvents:TRUE]
    withCompressEvents:TRUE]
    withTrackScreenViewEvents:TRUE]
    withTrackUserEngagementEvents:TRUE]
    withTrackAppExceptionEvents:TRUE];
```

**Debug events**

 You can follow the steps below to view the event raw JSON and debug your events.

1. Set the `isLogEvents` option when with true in debug mode.

1. Integrate the SDK and launch your app by Xcode, then open the log panel.

1. Input **EventRecorder** to the ﬁlter, and you will see the JSON content of all events recorded by Clickstream Swift SDK.

## Data format definition
<a name="data-format-definition-1"></a>

### Data type
<a name="data-type"></a>

Clickstream Swift SDK supports the following data types:

|  **Data type**  |  **Range**  |  **Example**  |
| --- | --- | --- |
|  Int  |  -214748364 \~ 2147483647  |  12  |
|  Int64  |  -9223372036854775808 \~ 9223372036854775807  |  26854775808  |
|  Double  |  -2.22E-308 \~ 1.79E\+308  |  3.14  |
|  Boolean  |  true, false  |  true  |
|  String  |  1024 characters maximum |  "Clickstream"  |

### Naming rules
<a name="naming-rules-1"></a>

1.  The event name and attribute name cannot start with a number, and only contain uppercase and lowercase letters, numbers, and underscores. In case of an invalid event name, it will throw `precondition failure`, In case of an invalid attribute name or user attribute name, it will discard the attribute and record error.

1.  Do not use `_` as prefix in an event name or attribute name, because the `_` prefix is reserved for the guidance.

1.  The event name and attribute name are case sensitive, so `Add_to_cart` and `add_to_cart` will be recognized as two different event names.

### Event and attribute limitation
<a name="event-and-attribute-limitation-1"></a>

 To improve the efficiency of querying and analysis, we apply limitations to event data as follows:

|  **Item**  |  **Recommended**  |  **Maximum (hard limit)**  |  **Strategy**  | Error code |
| --- | --- | --- | --- | --- |
| Event name invalid | N/A | N/A | discard event, print log and record \_clickstream\_error event | 1001 |
|  Length of event name  |  less than 25 characters  |  50 characters  | discard event, print log and record \_clickstream\_error event | 1002 |
|  Length of event attribute name  |  less than 25 characters  |  50 characters  | discard the attribute, print log and record error in event attribute  | 2001 |
| Attribute name invalid | N/A | N/A | discard the attribute, print log and record error in event attribute  | 2002 |
|  Length of event attribute value  |  less than 100 characters  |  1024 characters  | discard the attribute, print log and record error in event attribute  | 2003 |
|  Event attribute per event  |  less than 50 attributes  |  500 event attributes  | discard the attribute, print log and record error in event attribute  | 2004 |
|  User attribute number |  less than 25 attribtues |  100 user attributes  | discard event, print log and record \_clickstream\_error event | 3001 |
|  Length of user attribute name  |  less than 25 characters  |  50 characters  | discard event, print log and record \_clickstream\_error event | 3002 |
| User attribute name invalid | N/A | N/A | discard event, print log and record \_clickstream\_error event | 3003 |
|  Length of user attribute value  |  less than 50 characters  |  256 characters  | discard event, print log and record \_clickstream\_error event | 3004 |
| Item number in one event |  less than 50 items |  100 items | discard the item, print log and record error in event attribute | 4001 |
| Length of item attribute value |  less than 100 characters |  256 characters | discard the item, print log and record error in event attribute | 4002 |
| Custom item attribute number in one item |  less than 10 custom attributes |  10 custom attributes | discard the item, print log and record error in event attribute | 4003 |
| Length of item attribute name |  less than 25 characters |  50 characters | discard the item, print log and record error in event attribute | 4004 |
| Item attribute name invalid |  N/A | N/A | discard the item, print log and record error in event attribute | 4005 |

 **Rules:**
+  The character limits are the same for single-width character languages (for example, English) and double-width character languages (for example, Chinese).
+  The limitation of event attribute per event involves both common attributes and preset attributes.
+  If the attribute or user attribute with the same name is added more than twice, the latest value will apply.
+ All errors that exceed the limit will be recorded `_error_code` and `_error_message` in the event attributes.

## Preset events
<a name="preset-events-and-attributes-1"></a>

### Automatically collected events
<a name="preset-events-1"></a>

|  **Event name**  |  **Triggered**  |  **Event attributes**  |
| --- | --- | --- |
| \_first\_open |  when the user launches an app the first time after installation | N/A |
|  \_session\_start  | when a user first opens the app or a user returns to the app after 30 minutes of inactivity period | \_session\_id<br />\_session\_start\_timestamp |
|  \_screen\_view  |  when a new screen opens | \_screen\_name<br />\_screen\_id<br />\_screen\_unique\_id<br />\_previous\_screen\_name<br />\_previous\_screen\_id<br />\_previous\_screen\_unique\_id<br /> \_entrances<br />\_previous\_timestamp<br />\_engagement\_time\_msec |
| \_user\_engagement  | when user navigates away from current screen and the screen is in focus for at least one second  | \_engagement\_time\_msece |
|  \_app\_start  |  every time the app goes to visible  | \_is\_first\_time (when it is the first \_app\_start event after the application starts, the value is true)  |
|  \_app\_end  |  every time the app goes to invisible  |   |
| \_profile\_set |  when the addUserAttributes() or setUserId() API is called  |  |
| \_app\_exception | when the app crashes | \_exception\_message<br />\_exception\_stack |
| \_app\_update | when the app is updated to a new version and launched again | \_previous\_app\_version |
|  \_os\_update  |  when device operating system is updated to a new version  |  \_previous\_os\_version  |
| \_clickstream\_error  | event\_name is invalid or user attribute is invalid | \_error\_code<br />\_error\_message |

### Session definition
<a name="session-definition-1"></a>

 In Clickstream Swift SDK, we do not limit the total time of a session. As long as the time between the next entry of the app and the last exit time is within the allowable timeout period, the current session is considered to be continuous.

The **\_session\_start** event triggered when the app open for the first time, or the app was open to the foreground and the time between the last exit exceeded **session\_time\_out **period. The following are session-related attributes.
+  **\_session\_id:** It is calculated by concatenating the last 8 characters of uniqueId and the current millisecond, for example: dc7a7a18-20230905-131926703.
+  **\_session\_duration:** We calculate the `_session_duration` by minus the current event create timestamp and the session's `_session_start_timestamp`. This attribute will be added in every event during the session.
+  **\_session\_number:** The auto increment number of session in current device, and the initial value is 1.
+ **Session timeout duration: **By default, it is 30 minutes, which can be customized through the configuration update API.

### Screen view definition
<a name="screen-view-definition-1"></a>

 In Clickstream Swift SDK, we define the `_screen_view` as an event that records a user's browsing path of screen. When a screen transition started, the `_screen_view` event will be recorded if any of the following conditions is met:
+  No screen was previously set.
+  The new screen name differs from the previous screen title.
+  The new screen id differs from the previous screen id.
+  The new screen unique id differs from the previous screen unique id.

 This event listens for UIViewController's `onViewDidAppear` lifecycle method to determine the screen transition.. In order to track screen browsing path, we use `_previous_screen_name `, `_previous_screen_id` and `_previous_screen_unique_id` to link the previous screen. In addition, there are some other attributes in screen view event.
+  \_screen\_unique\_id: We calculate the screen unique id by getting the current screen's hashcode, for example: "5260751568".
+  \_entrances: The first screen view event in a session is 1, others is 0.
+  \_previous\_timestamp: The timestamp of the previous \_screen\_view event.
+  \_engagement\_time\_msec: The previous page last engagement milliseconds.

When the app goes to the background for more than 30 minutes and then opened again, a new session will be generated, the previous screen information will be cleared, and a new screen view event will be sent.

### User engagement definition
<a name="user-engagement-definition-1"></a>

 In Clickstream Swift SDK, we define the `user_engagement` as an event that records the screen browsing time, and we only send this event when user leave the screen and the screen has focus for at least one second.

 We define that users leave the screen in the following situations.
+  When the user navigates to another screen.
+  The user moves the app screen to the background.
+  The user exit the app, or kill the process of app.

 **engagement\_time\_msec**: We calculate the milliseconds from when a screen is visible to when the user leave the screen.

### Event attributes
<a name="common-attributes-and-reserved-attributes-1"></a>

** Sample event structure **

```
{
    "app_id": "Shopping",
    "app_package_name": "com.company.app",
    "app_title": "Shopping",
    "app_version": "1.0",
    "brand": "apple",
    "carrier": "UNKNOWN",
    "country_code": "US",
    "device_id": "A536A563-65BD-49BE-A6EC-6F3CE7AC8FBE",
    "device_unique_id": "",
    "event_id": "91DA4BBE-933F-4DFA-A489-8AEFBC7A06D8",
    "event_type": "add_to_cart",
    "hashCode": "63D7991D",
    "locale": "en_US",
    "make": "apple",
    "model": "iPhone 14 Pro",
    "network_type": "WIFI",
    "os_version": "16.4",
    "platform": "iOS",
    "screen_height": 2556,
    "screen_width": 1179,
    "sdk_name": "aws-solution-clickstream-sdk",
    "sdk_version": "0.4.1",
    "system_language": "en",
    "timestamp": 1685082174195,
    "unique_id": "0E6614B7-2D2C-4774-AB2F-B0A9E6C3BFAC",
    "zone_offset": 28800000,
    "user": {
        "_user_city": {
            "set_timestamp": 1685006678437,
            "value": "Shanghai"
        },
        "_user_first_touch_timestamp": {
            "set_timestamp": 1685006678434,
            "value": 1685006678432
        },
        "_user_name": {
            "set_timestamp": 1685006678437,
            "value": "carl"
        }
    },
    "attributes": {
        "event_category": "recommended",
        "currency": "CNY",
        "_session_duration": 15349,
        "_session_id": "0E6614B7-20230526-062238846",
        "_session_number": 3,
        "_session_start_timestamp": 1685082158847,
        "_screen_name": "ProductDetailViewController",
        "_screen_unique_id": "5260751568"
    }
}
```

 All user attributes will be stored in `user` object, and all custom and global attributes in `attributes` object.

**Common attribute**

|  **Attribute name**  |  **Description**  | It is generated ... | It is used to or for ... |
| --- | --- | --- | --- |
|  hashCode  | the AnalyticsEvent Object's hash code  | generated from String(format: "%08X", hasher.combine(eventjson)) | distinguish different events |
|  app\_id  |  clickstream app id  | generated when clickstream app create from guidance control plane | identify the events for your apps |
|  unique\_id  |  the unique id for user  | generated from UUID().uuidString during the SDK first initialization. It will be changed after user relogin to another user who never login, and when user relogin to the previous user in same device. The unique\_id will reset to the previous user's unique\_id. | identity different users and associate the behavior of logging in and not logging in |
|  device\_id | the unique id for device  | generated from `UIDevice.current.identifierForVendor?.uuidString ?? UUID().uuidString`.<br />It will be changed after app is reinstalled. | distinguish different devices |
| device\_unique\_id | the device advertising id | generated from ASIdentifierManager.shared().advertisingIdentifier.uuidString ?? "" | distinguish different devices |
| event\_type | event name | set by user or SDK | distinguish different event types |
| event\_id | the unique id for event | generated from UUID().uuidString when the event is created | distinguish each event |
| timestamp | event create timestamp | generated from Date().timeIntervalSince1970 \* 1000 when the event is created | data analysis needs |
| platform | the platform name | for iOS device, it is always "iOS" | data analysis needs |
| os\_version | the iOS operating system version | generated from UIDevice.current.systemVersion | data analysis needs |
| make | the manufacturer of the device | for iOS device, it is always "apple" | data analysis needs |
| brand | the brand of the device | for iOS device, it is always "apple" | data analysis needs |
| model | the model of the device | generated from mapping of device identifier | data analysis needs |
| carrier | the device network operator name | generated from CTTelephonyNetworkInfo().serviceSubscriberCellularProviders?.first?.value, and its default value is "UNKNOWN" | data analysis needs |
| network\_type | the current device network type | generated from NWPathMonitor, it can be “Mobile", "WIFI" or "UNKNOWN" | data analysis needs |
| screen\_height | the absolute height of the available display size in pixels | generated from UIScreen.main.bounds.size.height \* UIScreen.main.scale | data analysis needs |
| screen\_width | the absolute width of the available display size in pixels | generated from UIScreen.main.bounds.size.width \* UIScreen.main.scale | data analysis needs |
| zone\_offset | the device raw offset from GMT in milliseconds | generated from TimeZone.current.secondsFromGMT()\*1000 | data analysis needs |
| locale | the default locale (language, country and variant) for this device of the Java Virtual Machine | generated from Locale.current | data analysis needs |
| system\_language | the devie language code | generated from Locale.current.languageCode, and its default is value "UNKNOWN" | data analysis needs |
| country\_code | country/region code for this device | generated from `Locale.current.regionCode`<br />and its default value is "UNKNOWN" | data analysis needs |
| sdk\_version | clickstream SDK version | generated from PackageInfo.version | data analysis needs |
| sdk\_name | clickstream SDK name | it is always "aws-solution-clickstream-sdk" | data analysis needs |
| app\_version | the app version name of user's app | generated from Bundle.main.infoDictionary["CFBundleShortVersionString"] ?? "" | data analysis needs |
| app\_package\_name | the app package name of user's app | generated from Bundle.main.infoDictionary["CFBundleIdentifier"] ?? "" | data analysis needs |
| app\_title | the display name of user's app | generated from Bundle.main.infoDictionary["CFBundleName"] ?? "" | data analysis needs |

** User attributes **

|  **Attribute name**  |  **Description**  |
| --- | --- |
|  \_user\_id  |  Reserved for user id that is assigned by app  |
|  \_user\_ltv\_revenue  |  Reserved for user lifetime value  |
|  \_user\_ltv\_currency  |  Reserved for user lifetime value currency  |
|  \_user\_first\_touch\_timestam  |  The time (in microseconds) when the user first opened the app or visited the site, and it is included in every event in user object  |

 **Event attributes**

|  **Attribute name**  | Data type | Auto track |  **Description**  |
| --- | --- | --- | --- |
| \_traffic\_source\_source | String | false | Reserved for traffic source source. Name of the network source that acquired the user when the event were reported. Example: Google, Facebook, Bing, Baidu. |
|  \_traffic\_source\_medium  | String | false |  Reserved for traffic medium. Use this attribute to store the medium that acquired user when events were logged.  |
| \_traffic\_source\_campaign | String | false | Reserved for traffic source campaign. Use this attribute to store the campaign of your traffic source. Example: summer\_sale, holiday\_specials |
| \_traffic\_source\_campaign\_id | String | false | Reserved for traffic source campaign id. Use this attribute to store the campaign id of your traffic source. Example: campaign\_1, campaign\_2. |
| \_traffic\_source\_term | String | false | Reserved for traffic source term. Use this attribute to store the term of your traffic source. Example: running\_shoes, fitness\_tracker |
| \_traffic\_source\_content | String | false | Reserved for traffic source content. Use this attribute to store the content of your traffic source. Example: banner\_ad\_1, text\_ad\_2 |
| \_traffic\_source\_clid | String | false | Reserved for traffic source clid. Use this attribute to store the clid of your traffic source. Example: amazon\_ad\_123, google\_ad\_456 |
| \_traffic\_source\_clid\_platform | String | false | Reserved for traffic source clid platform. Use this attribute to store the clid platform of your traffic source. Example: amazon\_ads, google\_ads |
| \_app\_install\_channel | String | false | Reserved for install source, it is the channel for app was downloaded. |
|  \_traffic\_source\_name  | String | false |  Reserved for traffic name. Use this attribute to store the marketing campaign that acquired user when events were logged.  |
|  \_traffic\_source\_source  | String | false |  Reserved for traffic source. Name of the network source that acquired the user when the event were reported.  |
|  \_channel  | String | false |  The channel for app was downloaded  |
|  \_session\_id  | String | true |  Added in all events.  |
|  \_session\_start\_timestamp  | long | true |  Added in all events.  |
|  \_session\_duration  | long | true |  Added in all events.  |
|  \_session\_number  | int | true |  Added in all events.  |
| \_screen\_name | String | true |  Added in all events.  |
| \_screen\_unique\_id | String | true |  Added in all events.  |

 **Item attributes**

|  **Attribute name**  |  **Data type**  |  **Required**  |  **Description**  |
| --- | --- | --- | --- |
|  id  |  string  |  False  |  The id of the item  |
|  name  |  string  |  False  |  The name of the item  |
|  brand  |  string  |  False  |  The brand of the item  |
|  currency |  string |  False |  The currency of the item |
|  price  |  number  |  False  |  The price of the item  |
|  quantity  |  string  |  False  |  The quantity of the item  |
|  creative\_name  |  string  |  False  |  The creative name of the item  |
|  creative\_slot  |  string  |  False  |  The creative slot of the item  |
|  location\_id  |  string  |  False  |  The location id of the item  |
|  category  |  string  |  False  |  The category of the item  |
|  category2  |  string  |  False  |  The category2 of the item  |
|  category3  |  string  |  False  |  The category3 of the item  |
|  category4  |  string  |  False  |  The category4 of the item  |
|  category5  |  string  |  False  |  The category5 of the item  |

You can use the listed preset item attributes, or you can add custom attributes to an item. In addition to the preset attributes, an item can add up to 10 custom attributes.

## Change log
<a name="change-log-2"></a>

For more information, see [change logs on GitHub](https://github.com/awslabs/clickstream-android/releases).

**Sample project **

[Sample iOS Project for SDK integration](https://github.com/aws-samples/clickstream-sdk-samples/tree/main/ios)

**Reference link **

[Source code](https://github.com/awslabs/clickstream-swift)

[Project issue](https://github.com/awslabs/clickstream-swift/issues)

[API Documentation](https://awslabs.github.io/clickstream-swift/)

[ClickstreamObjc Api Reference](https://awslabs.github.io/clickstream-swift/Classes/ClickstreamObjc.html)
