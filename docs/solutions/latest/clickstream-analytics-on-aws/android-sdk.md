---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/android-sdk.html
---

# Android SDK
<a name="android-sdk"></a>

## Introduction
<a name="introduction"></a>

Clickstream Android SDK can help you easily collect in-app click stream data from Android devices to your AWS environments through the data pipeline provisioned by this guidance.

The SDK is based on the Amplify for Android SDK Core Library and developed according to the Amplify Android SDK plug-in specification. In addition, the SDK provides features that automatically collect common user events and attributes (for example, screen view and first open) to accelerate data collection for users.

### Platform support
<a name="platform-support"></a>

 Clickstream Android SDK supports Android 4.1 (API level 16) and later.

## Integrate the SDK
<a name="integrate-the-sdk"></a>

### 1 Include the SDK
<a name="include-the-sdk"></a>

 Add the Clickstream SDK dependency to your `app` module's `build.gradle` file. For example,

```
dependencies {
    implementation 'software.aws.solution:clickstream:0.13.0'
}
```

If needed, you can synchronize your project with [the latest version](https://central.sonatype.com/artifact/software.aws.solution/clickstream/versions).

### 2 Configure parameters
<a name="configure-parameters"></a>

 Find the `res` directory under your `project/app/src/main`, and manually create a raw folder in the `res` directory.

![Project tree showing amplifyconfiguration.json file selected in the raw folder under res.](http://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/images/amplifyconfiguration.png)

 Download your `amplifyconfiguration.json` file from your clickstream control plane, and paste it to the raw folder. The JSON file is like:

```
{
  "analytics": {
    "plugins": {
      "awsClickstreamPlugin": {
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

 In the file, your `appId` and `endpoint` are already set up. The explanation for each property is as follows:
+  **appId (Required):** the app id of your project in web console.
+  **endpoint (Required):** the endpoint url you will upload the event to AWS server.
+  **isCompressEvents:** whether to compress event content when uploading events, and the default value is `true`
+  **autoFlushEventsInterval:** event sending interval, and the default value is `10s`
+  **isTrackAppExceptionEvents:** whether auto track exception event in app, and the default value is `false `

### 3 Initialize the SDK
<a name="initialize-the-sdk"></a>

It is recommended that you initialize the SDK in your application's `onCreate()` method.

**Note**
The initialization code needs to run in the main thread.

```
import software.aws.solution.clickstream.ClickstreamAnalytics;

public void onCreate() {
    super.onCreate();

    try{
        ClickstreamAnalytics.init(getApplicationContext());
        Log.i("MyApp", "Initialized ClickstreamAnalytics");
    } catch (AmplifyException error){
        Log.e("MyApp", "Could not initialize ClickstreamAnalytics", error);
    }
}
```

### 4 Start using
<a name="configure-the-sdk"></a>

**Record event**

 Add the following code where you need to report an event.

```
import software.aws.solution.clickstream.ClickstreamAnalytics;
import software.aws.solution.clickstream.ClickstreamEvent;

// for record an event with custom attributes
ClickstreamEvent event = ClickstreamEvent.builder()
    .name("button_click")
    .add("category", "shoes")
    .add("currency", "CNY")
    .add("value", 279.9)
    .build();
ClickstreamAnalytics.recordEvent(event);

// for record an event directly
ClickstreamAnalytics.recordEvent("button_click");
```

**Add global attribute**

1. Add global attributes when initializing the SDK. The following example code shows how to add traffic source fields as global attributes when initializing the SDK.

   ```
   import software.aws.solution.clickstream.ClickstreamAnalytics;

   ClickstreamAttribute globalAttributes = ClickstreamAttribute.builder()
         .add(ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_SOURCE, "amazon")
         .add(ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_MEDIUM, "cpc")
         .add(ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_CAMPAIGN, "summer_promotion")
         .add(ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_CAMPAIGN_ID, "summer_promotion_01")
         .add(ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_TERM, "running_shoes")
         .add(ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_CONTENT, "banner_ad_1")
         .add(ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_CLID, "amazon_ad_123")
         .add(ClickstreamAnalytics.Attr.TRAFFIC_SOURCE_CLID_PLATFORM, "amazon_ads")
         .add(ClickstreamAnalytics.Attr.APP_INSTALL_CHANNEL, "Amazon Store")
         .build();
   ClickstreamConfiguration configuration = new ClickstreamConfiguration()
         .withAppId("your appId")
         .withEndpoint("http://example.com/collect")
         .withInitialGlobalAttributes(globalAttributes);
   ClickstreamAnalytics.init(getApplicationContext(), configuration);
   ```

1. Add global attributes after initializing the SDK.

   ```
   import software.aws.solution.clickstream.ClickstreamAnalytics;
   import software.aws.solution.clickstream.ClickstreamAttribute;

   ClickstreamAttribute globalAttribute = ClickstreamAttribute.builder()
       .add(ClickstreamAnalytics.Attr.APP_INSTALL_CHANNEL, "Amazon Store")
       .add("level", 5.1)
       .add("class", 6)
       .add("isOpenNotification", true)
       .build();
   ClickstreamAnalytics.addGlobalAttributes(globalAttribute);
   ```

   It is recommended to set global attributes when initializing the SDK. Global attributes will be included in all events that occur after it is set.

**Delete global attribute**

```
import software.aws.solution.clickstream.ClickstreamAnalytics;
ClickstreamAnalytics.deleteGlobalAttributes("level");
```

**Login and logout**

```
import software.aws.solution.clickstream.ClickstreamAnalytics;
```

```
// when user login success
ClickstreamAnalytics.setUserId("UserId");

// when user logout
ClickstreamAnalytics.setUserId(null);
```

**Add user attribute**

```
import software.aws.solution.clickstream.ClickstreamAnalytcs;
import software.aws.solution.clickstream.ClickstreamUserAttribute;

ClickstreamUserAttribute clickstreamUserAttribute = ClickstreamUserAttribute.builder()
    .add("_user_age", 21)
    .add("_user_name", "carl")
    .build();
ClickstreamAnalytics.addUserAttributes(clickstreamUserAttribute);
```

The currently logged-in user's attributes will be cached in disk. The next time the app launches, you don't need to set all of the user's attributes again. You can use the same API `ClickstreamAnalytics.addUserAttributes()` to update the the current user's attributes when they change.

**Important**
If your application is already published and most users have already logged in, please manually set the user attributes once when integrating the Clickstream SDK for the first time. This ensures that subsequent events contain user attributes.

**Record event with items**

You can add the following code to log an event with an item.

```
import software.aws.solution.clickstream.ClickstreamAnalytcs;
import software.aws.solution.clickstream.ClickstreamItem;

ClickstreamItem item_book = ClickstreamItem.builder()
    .add(ClickstreamAnalytics.Item.ITEM_ID, "123")
    .add(ClickstreamAnalytics.Item.ITEM_NAME, "Nature")
    .add(ClickstreamAnalytics.Item.ITEM_CATEGORY, "book")
    .add(ClickstreamAnalytics.Item.PRICE, 99)
    .add("book_publisher", "Nature Research")
    .build();

ClickstreamEvent event = ClickstreamEvent.builder()
    .name("view_item")
    .add(ClickstreamAnalytics.Attr.VALUE, 99)
    .add(ClickstreamAnalytics.Attr.CURRENCY, "USD")
    .add("event_category", "recommended")
    .setItems(new ClickstreamItem[] {item_book})
    .build();

ClickstreamAnalytics.recordEvent(event);
```

For more information about logging more attribute in an item, please refer to Item attributes.

**Important**
Only pipelines from version 1.1.0 can handle items with custom attribute.
`ITEM_ID` is a required attribute. If this attribute is not set, the item will be discarded.

**Record screen view events manually**

By default, the SDK will automatically track the **preset \_screen\_view event** when Activity triggers **onResume**.

You can manually record screen view events whether automatic screen view tracking is enabled, add the following code to record a screen view event with two attributes.
+ **SCREEN\_NAME:** Required. Your screen's name.
+ **SCREEN\_UNIQUE\_ID:** Optional. Set the hashcode of your Fragment or View. If you do not set this attribute, the SDK will set a default value based on the current Activity's **hashCode**.

```
import software.aws.solution.clickstream.ClickstreamAnalytcs;

ClickstreamEvent event = ClickstreamEvent.builder()
     .name(ClickstreamAnalytics.Event.SCREEN_VIEW)
     .add(ClickstreamAnalytics.Attr.SCREEN_NAME, "HomeFragment")
     .add(ClickstreamAnalytics.Attr.SCREEN_UNIQUE_ID, String.valueOf(HomeFragment.hashCode()))
     .build();
ClickstreamAnalytics.recordEvent(event);
```

**Send event immediately**

```
// for send event immediately.
ClickstreamAnalytics.flushEvent();
```

**Disable SDK**

You can disable the SDK if needed. After disabling the SDK, the SDK will not handle the logging and sending of any events. Of course you can enable the SDK when you need to continue logging events.

Please note that the disable and enable code needs to be run in the main thread.

```
import software.aws.solution.clickstream.ClickstreamAnalytics;

// disable SDK
ClickstreamAnalytics.disable();

// enable SDK
ClickstreamAnalytics.enable();
```

**Other configuration**

In addition to the required appId and endpoint, you can configure other information to get more****customized usage when initializing the SDK:

```
import software.aws.solution.clickstream.ClickstreamAnalytics;

// config the SDK after initialize.
ClickstreamAnalytics.getClickStreamConfiguration()
        .withAppId("your appId")
        .withEndpoint("https://example.com/collect")
        .withAuthCookie("your authentication cookie")
        .withSendEventsInterval(10000)
        .withSessionTimeoutDuration(1800000)
        .withTrackScreenViewEvents(false)
        .withTrackUserEngagementEvents(false)
        .withTrackAppExceptionEvents(false)
        .withLogEvents(true)
        .withCustomDns(CustomOkhttpDns.getInstance())
        .withCompressEvents(true);

ClickstreamAnalytics.init(getApplicationContext(), configuration);
```

Here is an explanation of each method.

|  **Method name**  |  **Parameter type**  |  **Required**  |  **Default value**  |  **Description**  |
| --- | --- | --- | --- | --- |
|  withAppId()  |  String  |  true  |  N/A  |  The app ID of your application in the web console.  |
|  withEndpoint()  |  String  |  true  |  N/A  |  The endpoint path you will upload the event to Clickstream ingestion server. |
|  withAuthCookie()  |  String  |  false  |  N/A  |  Your auth cookie for AWS application load balancer auth cookie. |
|  withSendEventsInterval()  |  long  |  false  |  1800000  |  Event sending interval in milliseconds. |
|  withSessionTimeoutDuration()  |  long  |  false  |  5000  |  The duration of the session timeout in milliseconds. |
|  withTrackScreenViewEvents()  |  boolean  |  false  |  true  |  Whether to auto-record screen view events. |
|  withTrackUserEngagementEvents()  |  boolean  |  false  |  true  |  Whether to auto-record user engagement events. |
|  withTrackAppExceptionEvents()  |  boolean  |  false  |  true  |  Whether to auto-record app exception events. |
|  withLogEvents()  |  boolean  |  false  |  false  |  Whether to automatically print event JSON for debugging events. |
|  withCustomDns()  |  String  |  false  |  N/A  |  The method for setting your custom DNS. |
|  withCompressEvents()  |  boolean  |  false  |  true  |  Whether to compress event content by gzip when uploading events.  |

By default, we will use the configurations in **amplifyconfiguration.json** file. If you add a custom configuration, the added configuration items will override the default values.

You can also add all the configuration parameters you need in the init method without using the **amplifyconfiguration.json** file.

**Conﬁguration update**

You can update the default configuration after initializing the SDK, below are the additional configuration options you can customize.

```
import software.aws.solution.clickstream.ClickstreamAnalytics;

// config the SDK after initialize.
ClickstreamAnalytics.getClickStreamConfiguration()
        .withAppId("your appId")
        .withEndpoint("https://example.com/collect")
        .withAuthCookie("your authentication cookie")
        .withTrackScreenViewEvents(false)
        .withTrackUserEngagementEvents(false)
        .withTrackAppExceptionEvents(false)
        .withLogEvents(true)
        .withCustomDns(CustomOkhttpDns.getInstance())
        .withCompressEvents(true);
```

**Debug events**

You can follow the steps below to view the event raw JSON and debug your events.

1. Enable the** withLogEvents **configuration when initializing the SDK.

   ```
   import software.aws.solution.clickstream.ClickstreamAnalytics;

   // log the event in debug mode.
   ClickstreamConfiguration configuration = new ClickstreamConfiguration()
       ...
       .withLogEvents(true);
   ClickstreamAnalytics.init(getApplicationContext(), configuration);
   ```

1. Integrate the SDK and launch your app by Android Studio, then open the **Logcat **window.

1. Input `EventRecorder` to the filter, and you will see the JSON content of all events recorded by Clickstream Android SDK.

**Configure custom DNS**

```
import software.aws.solution.clickstream.ClickstreamAnalytics;

// config custom DNS.
ClickstreamAnalytics.getClickStreamConfiguration()
        .withCustomDns(CustomOkhttpDns.getInstance());
```

If you want to use custom DNS for network request, you can create your `CustomOkhttpDns` which implementation `okhttp3.Dns`, then configure `.withCustomDns(CustomOkhttpDns.getInstance())` to make it work. Here is an [example code](https://github.com/awslabs/clickstream-android/blob/main/clickstream/src/test/java/software/aws/solution/clickstream/IntegrationTest.java#L503-L516).

### Data format definition
<a name="data-format-definition"></a>

#### Data types
<a name="data-types"></a>

 Clickstream Android SDK supports the following data types:

|  **Data type**  |  **Range**  |  **Example**  |
| --- | --- | --- |
|  int  |  -214748364 \~ 2147483647  |  12  |
|  long  |  -9223372036854775808 \~ 9223372036854775807  |  26854775808  |
|  double  |  4.9E-324 \~ 1.7976931348623157E308  |  3.14  |
|  boolean  | true, false |  true  |
|  String  |  1024 characters maximum |  "Clickstream"  |

#### Naming rules
<a name="naming-rules"></a>

1.  The event name and attribute name cannot start with a number, and only contain uppercase and lowercase letters, numbers, and underscores. In case of an invalid event name, it will throw `IllegalArgumentException`. In case of an invalid attribute name or user attribute name, it will discard the attribute and record error.

1.  Do not use `_` as prefix in an event name or attribute name, because the `_` prefix is reserved for the guidance.

1.  The event name and attribute name are case sensitive, so `Add_to_cart` and `add_to_cart` will be recognized as two different event names.

#### Event and attribute limitation
<a name="event-and-attribute-limitation"></a>

 To improve the efficiency of querying and analysis, we apply limitations to event data as follows:

|  **Item**  |  **Recommended**  |  **Maximum**  |  **Strategy**  | Error code |
| --- | --- | --- | --- | --- |
|  Event name invalid | N/A | N/A | discard event, print log and record \_clickstream\_error event | 1001 |
| Length of event name  |  less than 25 characters  |  50 characters  | discard event, print log and record \_clickstream\_error event | 1002 |
|  Length of event attribute name  |  less than 25 characters  |  50 characters  |  discard the attribute, print log and record error in event attribute  | 2001 |
| Attribute name invalid | N/A | N/A |  discard the attribute, print log and record error in event attribute  | 2002 |
|  Length of event attribute value  |  less than 100 characters  |  1024 characters  |  discard the attribute, print log and record error in event attribute  | 2003 |
|  Event attribute per event  |  less than 50 attributes |  500 event attributes  |  discard the attribute, print log and record error in event attribute  | 2004 |
|  User attribute number |  less than 25 attributes |  100 user attributes  |  discard the attribute, print log and record \_clickstream\_error event  | 3001 |
|  Length of user attribute name  |  less than 25 characters  |  50 characters  |  discard the attribute, print log and record \_clickstream\_error event  | 3002 |
| User attribute name invalid | N/A | N/A |  discard the attribute, print log and record \_clickstream\_error event  | 3003 |
|  Length of user attribute value  |  less than 50 characters  |  256 characters  |  discard the attribute, print log and record \_clickstream\_error event  | 3004 |
| Item number in one event  | under 50 items  | 100 items  | discard the item, print log and record error in event attribute  | 4001  |
| Length of item attribute value  | under 100 characters  | 256 characters  | discard the item, print log and record error in event attribute  | 4002  |
| Custom item attribute number in one item  | under 10 custom attributes  | 10 custom attributes  | discard the item, print log and record error in event attribute  | 4003  |
| Length of item attribute name  | under 25 characters  | 50 characters | discard the item, print log and record error in event attribute  | 4004  |
| Item attribute name invalid  | --  |  --  | discard the item, print log and record error in event attribute  | 4005  |

**Important**
 The character limits are the same for single-width character languages (for example, English) and double-width character languages (for example, Chinese).
 The limitation for event attribute per event involves both common attributes and preset attributes.
 If the attribute or user attribute with the same name is added more than twice, the latest value will apply.

### Preset events
<a name="preset-events-and-attributes"></a>

#### Automatically collected events
<a name="preset-events"></a>

|  **Event name**  |  **Triggered**  |  **Event attributes**  |
| --- | --- | --- |
| \_first\_open | when the user launches an app the first time after installation | N/A |
|  \_session\_start  |  when a user first open the app or a user returns to the app after 30 minutes of inactivity period  | \_session\_id<br />\_session\_start\_timestamp |
|  \_screen\_view  |  when a new screen opens | \_screen\_name<br />\_screen\_id<br />\_screen\_unique\_id<br />\_previous\_screen\_name<br />\_previous\_screen\_id<br />\_previous\_screen\_unique\_id<br />\_entrances<br /> \_previous\_timestamp<br />\_engagement\_time\_msec |
| \_user\_engagement | when a user navigates away from current screen and the screen is in focus for at least one second | \_engagement\_time\_msec |
| \_app\_start | every time the app goes to visible |  \_is\_first\_time (when it is the first \_app\_start event after the application starts, the value is true) |
| \_app\_end | every time the app goes to invisible | N/A |
|  \_profile\_set  |  when the addUserAttributes() or setUserId() API is called  | N/A |
|  \_app\_exception  |  when the app crashes  | \_exception\_message<br />\_exception\_stack |
|  \_app\_update  |  when the app is updated to a new version and launched again  |  \_previous\_app\_version  |
|  \_os\_update  |  when device operating system is updated to a new version  |  \_previous\_os\_version  |
|  \_clickstream\_error  |  event\_name is invalid or user attribute is invalid  | \_error\_code<br /> \_error\_message |

#### Session definition
<a name="session-definition"></a>

 In Clickstream Android SDK, we do not limit the total time of a session. As long as the time between the next entry of the app and the last exit time is within the allowable timeout period, the current session is considered to be continuous.

The **\_session\_start** event triggered when the app open for the first time, or the app was open to the foreground and the time between the last exit exceeded **session\_time\_out **period. The following are session-related attributes.
+  **\_session\_id:** It is calculated by concatenating the last 8 characters of uniqueId and the current millisecond, for example: dc7a7a18-20230905-131926703.
+  **\_session\_duration:** We calculate the `_session_duration` by minus the current event create timestamp and the session's `_session_start_timestamp`. This attribute will be added in every event during the session.
+  **\_session\_number:** The auto increment number of session in current device, and the initial value is 1.
+ **Session timeout duration: **By default, it is 30 minutes, which can be customized through the configuraton update API.

#### Screen view definition
<a name="screen-view-definition"></a>

 In Clickstream Android SDK, we define the `_screen_view` as an event that records a user's browsing path of screen. When a screen transition started, the `_screen_view` event will be recorded if any of the following conditions is met:
+  No screen was previously set.
+  The new screen name differs from the previous screen title.
+  The new screen id differs from the previous screen id.
+  The new screen unique id differs from the previous screen unique id.

 This event listens for Activity's `onResume` lifecycle method to judgment the screen transition. In order to track screen browsing path, we use `_previous_screen_name `, `_previous_screen_id` and `_previous_screen_unique_id` to link the previous screen. In addition, there are some other attributes in screen view event.
+  **\_screen\_unique\_id:** We calculate the screen unique id by getting the current screen's hashcode, for example: "126861252".
+ ** \_entrances: **The first screen view event in a session is 1, others is 0.
+ ** \_previous\_timestamp:** The timestamp of the previous \_screen\_view event.
+ ** \_engagement\_time\_msec: **The previous page last engagement milliseconds.

When the app goes to the background for more than 30 minutes and then is opened again, a new session will be generated, the previous screen information will be cleared, and a new screen view event will be sent.

#### User engagement definition
<a name="user-engagement-definition"></a>

 In Clickstream Android SDK, we define the `user_engagement` as an event that records the screen browsing time, and we only send this event when user leave the screen and the screen has focus for at least one second.

 We define that users leave the screen in the following situations.
+  When the user navigates to another screen.
+  The user moves the app screen to the background.
+  The user exit the app, or kill the process of app.

 **engagement\_time\_msec**: We calculate the milliseconds from when a screen is visible to when the user leave the screen.

#### Event attributes
<a name="common-attributes-and-reserved-attributes"></a>

** Sample event structure **

```
{
    "event_type": "add_to_cart",
    "event_id": "460daa08-0717-4385-8f2e-acb5bd019ee7",
    "timestamp": 1667877566697,
    "device_id": "f24bec657ea8eff7",
    "platform": "Android",
    "os_version": "10",
    "make": "Samsung",
    "brand": "Samsung",
    "model": "TAS-AN00",
    "locale": "zh_CN_#Hans",
    "carrier": "CDMA",
    "network_type": "Mobile",
    "screen_height": 2259,
    "screen_width": 1080,
    "zone_offset": 28800000,
    "system_language": "zh",
    "country_code": "CN",
    "sdk_version": "0.7.1",
    "sdk_name": "aws-solution-clickstream-sdk",
    "app_version": "1.0",
    "app_package_name": "com.notepad.app",
    "app_title": "Notepad",
    "app_id": "notepad-4a929eb9",
    "user": {
        "_user_id": {
            "value": "312121",
            "set_timestamp": 1667877566697
        },
        "_user_name": {
            "value": "carl",
            "set_timestamp": 1667877566697
        },
        "_user_first_touch_timestamp": {
            "value": 1667877267895,
            "set_timestamp": 1667877566697
        }
    },
    "attributes": {
        "event_category": "recommended",
        "currency": "CNY",
        "_session_id": "dc7a7a18-20221108-031926703",
        "_session_start_timestamp": 1667877566703,
        "_session_duration": 391809,
        "_session_number": 1,
        "_screen_name": "ProductDetailActivity",
        "_screen_unique_id": "126861252"
    }
}
```

 All user attributes will be stored in `user` object, and all custom and global attributes in `attributes` object.

**Common attribute**

|  **Attribute name**  |  **Description**  | It is generated... | It is used to or for... |
| --- | --- | --- | --- |
|  app\_id  |  clickstream app id  | generated when clickstream app create from guidance control plane | identify the events for your apps |
|  unique\_id  |  the unique id for user  | generated from UUID.randomUUID().toString() during the SDK first initialization. It will be changed after user relogin to another user who never login, and when user relogin to the previous user in same device. The unique\_id will reset to the previous user's unique\_id. | identity different users and associate the behavior of logging in and not logging in |
|  device\_id | the unique id for device  | generated from `Settings.System.getString(context.getContentResolver()`, `Settings.Secure.ANDROID_ID)`.<br />If Android ID is null or "", we will use UUID instead. | distinguish different devices |
| event\_type | event name | set by developer or SDK | distinguish different event types |
| event\_id | the unique id for event | generated from UUID.randomUUID().toString() when the event is created | distinguish each event |
| timestamp | event create timestamp | generated from System.currentTimeMillis() when the event is created | data analysis needs |
| platform | the platform name | for Android device, it is always "Android" | data analysis needs |
| os\_version | the platform version code | generated from Build.VERSION.RELEASE | data analysis needs |
| make | the manufacturer of the device | generated from Build.MANUFACTURER | data analysis needs |
| brand | the brand of the device | generated from Build.BRAND | data analysis needs |
| model | the model of the device | generated from Build.MODEL | data analysis needs |
| carrier | the device network operator name | generated from TelephonyManager.getNetworkOperatorName(), the default is "UNKNOWN" | data analysis needs |
| network\_type | the current device network type | generated from android.netConnectivityManager, it can be “Mobile", "WIFI" or "UNKNOWN" | data analysis needs |
| screen\_height | the absolute height of the available display size in pixels | generated from applicationContext.resources.displayMetrics.heightPixels | data analysis needs |
| screen\_width | the absolute width of the available display size in pixels | generated from applicationContext.resources.displayMetrics.widthPixels | data analysis needs |
| zone\_offset | the device raw offset from GMT in milliseconds | generated from java.util.Calendar.get(Calendar.ZONE\_OFFSET) | data analysis needs |
| locale | the default locale (language, country and variant) for this device of the Java Virtual Machine | generated from java.util.Local.getDefault() | data analysis needs |
| system\_language | the devie language code | generated from java.util.Local.getLanguage(), and its default is value "UNKNOWN" | data analysis needs |
| country\_code | country/region code for this device | generated from `java.util.Local.getCountry()`<br />and its default value is "UNKNOWN" | data analysis needs |
| sdk\_version | clickstream SDK version | generated from BuildConfig.VERSION\_NAME | data analysis needs |
| sdk\_name | clickstream SDK name | it is always "aws-solution-clickstream-sdk" | data analysis needs |
| app\_version | the app version name of user's app | generated from android.content.pm.PackageInfo.versionName, and its default value is "UNKNOWN" | data analysis needs |
| app\_package\_name | the app package name of user's app | generated from android.content.pm.PackageInfo.packageName, and its default value is "UNKNOWN" | data analysis needs |
| app\_title | the display name of user's app | generated from android.content.pm.getApplicationLabel(appInfo) | data analysis needs |

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
|  \_session\_id  | String | true |  Added in all events.  |
|  \_session\_start\_timestamp  | long | true |  Added in all events.  |
|  \_session\_duration  | long | true |  Added in all events.  |
|  \_session\_number  | int | true |  Added in all events.  |
| \_screen\_name | String | true |  Added in all events.  |
| \_screen\_unique\_id | String | true |  Added in all events.  |

 **Item attributes**

|  **Attribute name**  | Data type | Auto track |  **Description**  |
| --- | --- | --- | --- |
| id  | String | False | The ID of the item  |
| name  | String | False | The name of the item  |
| brand | String | False | The brand of the item  |
| currency  | String | False | The currency of the item  |
| price  | String | False | The price of the item  |
| quantity  | String | False | The quantity of the item  |
| creative\_name  | String | False | The creative name of the item |
| creative\_slot  | String | False | The creative slot of the item  |
| location\_id  | String | False | The location id of the item  |
| category  | String | False | The category of the item  |
| category2  | String | False | The category2 of the item  |
| category3  | String | False | The category3 of the item  |
| category4  | String | False | The category4 of the item  |
| category5 | String | False | The category5 of the item  |

You can use the above preset item attributes, of course, you can also add custom attributes to an item. In addition to the preset attributes, an item can add up to 10 custom attributes.

**Change log**

[GitHub change log](https://github.com/awslabs/clickstream-android/releases).

**Sample project**

[Sample Android Project for SDK integration](https://github.com/aws-samples/clickstream-sdk-samples/tree/main/android).

**Reference link **

[Source code](https://github.com/awslabs/clickstream-android)

[Project issues](https://github.com/awslabs/clickstream-android/issues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
