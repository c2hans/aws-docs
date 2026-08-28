---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/web-sdk.html
---

# Web SDK
<a name="web-sdk"></a>

## Introduction
<a name="introduction-2"></a>

The Clickstream Web SDK can help you easily collect click stream data from browser to your AWS environments through the data pipeline provisioned by this solution.

 The SDK is based on the amplify-js SDK core library and developed according to the amplify-js SDK plug-in specification. In addition, the SDK is equipped with features that automatically collect common user events and attributes (for example, page view and first open) to simplify data collection for users.

## Integrate the SDK
<a name="integrate-the-sdk-2"></a>

 **Using NPM**

1. Include SDK

   ```
   npm install @aws/clickstream-web
   ```

1. Initialize the SDK

    You need to configure the SDK with default information before using it. To do this, firstly copy your initial code from your guidance web console. The initial code is like:

   ```
   import { ClickstreamAnalytics } from '@aws/clickstream-web';

   ClickstreamAnalytics.init({
      appId: "your appId",
      endpoint: "https://example.com/collect",
   });
   ```

    Then, add the code to your your app's root entry point, for example index.js/app.tsx in React or main.ts in Vue/Angular.

    In the code, appId and endpoint are already set up. Alternatively, you can manually add this code snippet and replace the values of appId and endpoint after you registered app to a data pipeline in the guidance web console.

 **Using JS File**

1. Download the clickstream-web.min.js from the assets in [GitHub Release](https://github.com/awslabs/clickstream-web/releases) page, and then copy it into your project.

1. Add the following initial code into your index.html.

   ```
   <script src="path to your clickstream-web.min.js"></script>
   <script>
       window.ClickstreamAnalytics.init({
           appId: 'your appId',
           endpoint: 'https://example.com/collect',
       })
   </script>
   ```

    You can find the appId and endpoint in the application detail page of the guidance web console.

    To lazy load the SDK, use the async attribute and place the `ClickstreamAnalytics.init()` method after `window.onload` or `DOMContentLoaded`.

## Start using
<a name="get-started"></a>

### Record event
<a name="record-event-2"></a>

 Add the following code where you need to record event.

```
import { ClickstreamAnalytics } from '@aws/clickstream-web';
// record event with attributes
ClickstreamAnalytics.record({
  name: 'button_click',
  attributes: {
    category: 'shoes',
    currency: 'CNY',
    value: 279.9,
  }
});

//record event with name
ClickstreamAnalytics.record({ name: 'buttonClick' });
```

### Add global attribute
<a name="add-global-attribute"></a>
+ Add global attributes when initializing the SDK. The following example code shows how to add traffic source fields as global attributes when initializing the SDK.

  ```
  import { ClickstreamAnalytics, Attr } from '@aws/clickstream-web';

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
     }
  });
  ```
+ Add global attributes after initializing the SDK.

  ```
  ClickstreamAnalytics.setGlobalAttributes({
    _traffic_source_medium: "Search engine",
    level: 10,
  });
  ```

It is recommended to set global attributes when initializing the SDK, and global attributes will be included in all events that occur after it is set. You also can remove a global attribute by setting its value to null.

### Login and logout
<a name="login-and-logout"></a>

```
import { ClickstreamAnalytics } from '@aws/clickstream-web';

// when user login success.
ClickstreamAnalytics.setUserId("1234");

// when user logout
ClickstreamAnalytics.setUserId(null);
```

### Add user attribute
<a name="add-user-attribute"></a>

```
ClickstreamAnalytics.setUserAttributes({
  userName:"carl",
  userAge: 22
});
```

 Current login user's attributes will be cached in localStorage, so the next time the browser opens you don't need to set up all user's attributes again. You can also use the same api ClickstreamAnalytics.setUserAttributes() to update the current user's attributes in case of any changes.

**Important**
 If your application is already published and most users have already logged in, please manually set the user attributes once when integrating the Clickstream SDK for the first time to ensure that subsequent events contain user attributes.

### Record event with items
<a name="record-event-with-items"></a>

You can add the following code to log an event with an item.

```
import { ClickstreamAnalytics, Item, Attr } from '@aws/clickstream-web';

const itemBook: Item = {
  id: '123',
  name: 'Nature',
  category: 'book',
  price: 99,
  book_publisher: 'Nature Research',
};

ClickstreamAnalytics.record({
  name: 'view_item',
  attributes: {
    [Attr.CURRENCY]: 'USD',
    [Attr.VALUE]:99,
    event_category: 'recommended',
  },
  items: [itemBook],
});
```

For more information about logging more attributes in an item, refer to item attributes.

**Important**
Only pipelines from version 1.1.0 can handle items with custom attribute. **ITEM\_ID** is required attribute, if not set the item will be discarded.

### Send event immediate in batch mode
<a name="send-event-immediate-in-batch-mode"></a>

 In batch mode, you can still send an event immediately by setting the **isImmediate** attribute to true, as shown in the following code.

```
import { ClickstreamAnalytics } from '@aws/clickstream-web';

ClickstreamAnalytics.record({
  name: 'button_click',
  isImmediate: true,
});
```

### Other configurations
<a name="customize-configurations"></a>

 In addition to the required appId and endpoint, you can configure other information for customization purposes:

```
import { ClickstreamAnalytics, SendMode, PageType } from '@aws/clickstream-web';

ClickstreamAnalytics.init({
   appId: "your appId",
   endpoint: "https://example.com/collect",
   sendMode: SendMode.Batch,
   sendEventsInterval: 5000,
   isTrackPageViewEvents: true,
   isTrackUserEngagementEvents: true,
   isTrackClickEvents: true,
   isTrackSearchEvents: true,
   isTrackScrollEvents: true,
   isTrackPageLoadEvents: true,
   isTrackAppStartEvents: true,
   isTrackAppEndEvents: true,
   pageType: PageType.SPA,
   isLogEvents: false,
   authCookie: "your auth cookie",
   sessionTimeoutDuration: 1800000,
   idleTimeoutDuration: 120000,
   searchKeyWords: ['product', 'class'],
   domainList: ['example1.com', 'example2.com'],
});
```

 Each option is explained below:

|  **Name**  |  **Required**  |  **Default value**  |  **Description**  |
| --- | --- | --- | --- |
|  appId  |  true  |  N/A  |  the app id of your application in the web console  |
|  endpoint  |  true  |  N/A  |  the endpoint path where you will upload the event to Clickstream ingestion server  |
|  sendMode  |  false  |  Immediate  |  there are two ways to send events: Immediate and Batch  |
|  sendEventsInterval  |  false  |  5,000  |  event sending interval in milliseconds, only works in Batch mode  |
|  isTrackPageViewEvents  |  false  |  true  |  whether to auto record page view events in the browser  |
|  isTrackUserEngagementEvents  |  false  |  true  |  whether to auto record user engagement events in the browser  |
|  isTrackClickEvents  |  false  |  true  |  whether to auto record link click events in the browser  |
|  isTrackSearchEvents  |  false  |  true  |  whether to auto record search result page events in the browser  |
|  isTrackScrollEvents  |  false  |  true  |  whether to auto record page scroll events in the browser  |
|  pageType  |  false  |  SPA  |  the website type: SPA for single page application, and multiPageApp for multiple page application. This attribute works only when the value of attribute isTrackPageViewEvents is true.  |
|  isLogEvents  |  false  |  false  |  whether to print out event json in the web console for debugging  |
|  authCookie  |  false  |  --  |  your auth cookie for AWS application load balancer auth cookie  |
|  sessionTimeoutDuration  |  false  |  1,800,000  |  the duration for session timeout in milliseconds  |
|  searchKeyWords  |  false  |  --  |  the customized keywords to trigger the \_search event. By default, it supports q, s, search, query and keyword in query parameters.  |
|  domainList  |  false  |  --  |  the domain list can be configured if a website crosses multiple domains. The \_outbound attribute of the \_click event will be true when a link leads to a website that's not a part of your configured domain.  |

### Configuration update
<a name="update-configuration"></a>

 You can update the default configuration after initializing the SDK. The following are additional configuration options that you can customize.

```
import { ClickstreamAnalytics } from '@aws/clickstream-web';

ClickstreamAnalytics.updateConfigure({
  isLogEvents: true,
  authCookie: 'your auth cookie',
  isTrackPageViewEvents: false,
  isTrackUserEngagementEvents: false,
  isTrackClickEvents: false,
  isTrackScrollEvents: false,
  isTrackSearchEvents: false,
});
```

### Debug events
<a name="debug-events"></a>

 You can follow the steps below to view the event raw json and debug your events.

1.  Use `ClickstreamAnalytics.init()` API to set the `isLogEvents` attribute to true in debug mode.

1.  Integrate the SDK and launch your web application in a browser, and then open the Inspection page and switch to console tab.

1.  Enter `EventRecorder` to Filter, and you will see the JSON content of all events recorded by Clickstream Web SDK.

## Data format definition
<a name="data-format-definition-2"></a>

### Data type
<a name="data-type-1"></a>

 Clickstream Web SDK supports the following data types:

|  **Data type**  |  **Range**  |  **Example**  |
| --- | --- | --- |
|  number  |  5e-324\~1.79e\+308  |  12, 26854775808, 3.14  |
|  boolean  |  true false  |  true  |
|  string  |  max 1024 characters  |  "Clickstream"  |

### Naming rules
<a name="naming-rules-2"></a>

1.  The event name and attribute name cannot start with a number, and only contains uppercase and lowercase letters, numbers, and underscores. If the event name is invalid, the SDK will record `_clickstream_error` event; if the attribute or user attribute name is invalid, the attribute will be discarded and the SDK also records `_clickstream_error` event.

1.  Do not use `_` as prefix in an event name or attribute name, because the `_` prefix is reserved for the guidance.

1.  The event name and attribute name are case sensitive, so `Add_to_cart` and `add_to_cart` will be recognized as two different event names.

### Event and attribute limitation
<a name="event-and-attribute-limitation-2"></a>

 In order to improve the efficiency of querying and analysis, we apply limits to event data as follows:

|  **Error code**  |  **Name**  |  **Suggestion**  |  **Hard limit**  |  **Strategy**  |
| --- | --- | --- | --- | --- |
|  1001  |  Invalid event name  |  N/A  |  N/A  |  discard event, print log and record \_clickstream\_error event  |
|  1002  |  Length of event name  |  Less than 25 characters  |  50 characters  |  discard event, print log and record \_clickstream\_error event  |
|  2001  |  Length of event attribute name  |  Less than 25 characters  |  50 characters  |  discard the attribute, print log and record error in event attribute  |
|  2002  |  Attribute name invalid  |  N/A  |  N/A  |  discard the attribute, print log and record error in event attribute  |
|  2003  |  Length of event attribute value  |  Less than 100 characters  |  1024 characters  |  discard the attribute, print log and record error in event attribute  |
|  2004  |  Event attribute per event  |  Less than 50 attributes  |  500 event attributes  |  discard the attribute that exceed, print log and record error in event attribute  |
|  3001  |  User attribute number  |  Less than 25 attributes  |  100 user attributes  |  discard the attribute that exceed, print log and record \_clickstream\_error event  |
|  3002  |  Length of user attribute name  |  Less than 25 characters  |  50 characters  |  discard the attribute, print log and record \_clickstream\_error event  |
|  3003  |  User attribute name invalid  |  N/A | N/A  |  discard the attribute, print log and record \_clickstream\_error event  |
|  3004  |  Length of User attribute value  |  Less than 50 characters  |  256 characters  |  discard the attribute, print log and record \_clickstream\_error event  |
|  4001  |  Item number in one event  |  Less than 50 items  |  100 items  |  discard the item, print log and record error in event attribute  |
|  4002  |  Length of item attribute value  |  Less than 100 characters  |  256 characters  |  discard the item, print log and record error in event attribute  |
|  4003 |  Custom item attribute number in one item  |  Less than 10 custom attributes |  10 custom attributes |  discard the item, print log and record error in event attribute  |
|  4004 |  Length of item attribute name |  Less than 25 characters |  50 characters |  discard the item, print log and record error in event attribute  |
|  4005 |  Item attribute name invalid | N/A | N/A |  discard the item, print log and record error in event attribute  |

**Important**
 The character limits are the same for single-width character languages (for example, English) and double-width character languages (for example, Chinese).
 The limit of event attribute per event includes common attributes and preset attributes.
 If the attribute or user attribute with the same name is added more than twice, the latest value will apply.
 All errors that exceed the limit will be recorded \_error\_code and \_error\_message these two attribute in the event attributes.

## Preset events
<a name="preset-events-2"></a>

### Automatically collected events
<a name="automatically-collected-events"></a>

|  **Event name**  |  **Triggered**  |  **Event Attributes**  |
| --- | --- | --- |
|  \_first\_open  |  the first time a user launches the site in a browser  |   |
|  \_session\_start  |  when a user first visits the site or a user returns to the website after 30 minutes of inactivity period, [Learn more](android-sdk.md#session-definition)  |  1.\_session\_id <br /> 2.\_session\_start\_timestamp  |
|  \_page\_view  |  when new page is opens, [Learn more](#page-view-definition)  | 1.\_page\_referrer<br />2.\_page\_referrer\_title<br />3.\_entrances<br />4.\_previous\_timestamp<br />5. \_engagement\_time\_msec |
|  \_user\_engagement  |  when user navigates away from current webpage and the page is in focus for at least one second, [Learn more](android-sdk.md#user-engagement-definition)  |  1.\_engagement\_time\_msec  |
|  \_app\_start  |  every time the browser goes to visible  | 1. \_is\_first\_time(when it is the first \_app\_start event after the application starts, the value is true)  |
|  \_app\_end  |  every time the browser goes to invisible  |   |
|  \_profile\_set  |  when the addUserAttributes() or setUserId() api called  |   |
|  \_scroll  |  the first time a user reaches the bottom of each page (that is, when a 90% vertical depth becomes visible)  |  \_engagement\_time\_msec  |
|  \_search  |  each time a user performs a site search, indicated by the presence of a URL query parameter, by default we detect q, s, search, query and keyword in query parameters  |  \_search\_key (the keyword name)<br /> \_search\_term (the search content) |
|  \_click  |  each time a user clicks a link that leads away from the current domain (or configured domain list)  | 1.\_link\_classes(the content of class in tag <a> )<br />2.\_link\_domain (the domain of herf in tag <a> ) <br />3.\_link\_id (the content of id in tag <a> ) <br />4.\_link\_url (the content of herf in tag <a> )<br />5.\_outbound (if the domain is not in configured domain list, the attribute value is true) |
| \_page\_load | each time a new page loaded, and browser [PerformanceObserver](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceNavigationTiming/toJSON#examples) triggered navigation event. |  1.   duration  <br />2.  deliveryType  <br />3.  nextHopProtocol  <br />4.   renderBlockingStatus  <br />5.  startTime  <br />6.  redirectStart  <br />7.  redirectEnd  <br />8.  workerStart  <br />9.  fetchStart  <br />10.  domainLookupStart  <br />11.  domainLookupEnd  <br />12.  connectStart  <br />13.  secureConnectionStart  <br />14.  connectEnd  <br />15.  requestStart  <br />16.  firstInterimResponseStart  <br />17.  responseStart  <br />18.  responseEnd  <br />19.  ransferSize  <br />20.   encodedBodySize <br />21.  decodedBodySize  <br />22.  responseStatus  <br />23.  unloadEventStart  <br />24.  unloadEventEnd  <br />25.  domInteractive  <br />26.  domContentLoadedEventStart <br />27.  domContentLoadedEventEnd  <br />28.  domComplete  <br />29.  loadEventStart  <br />30.  loadEventEnd  <br />31.  type  <br />32.  edirectCount  <br />33.  activationStart  <br />34.  criticalCHRestart  <br />35.  serverTiming  <br />For more detail you can refer [PerformanceNavigationTiming](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceNavigationTiming) and [toJson](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceNavigationTiming/toJSON) Method   |
|  \_clickstream\_error  |  event\_name is invalid or user attribute is invalid  | 1. \_error\_code<br />2. \_error\_message  |

### Session definition
<a name="session-definition-2"></a>

 In Clickstream Web SDK, there is no limit to the total time of a session. As long as the time between the next entry of the browser and the last exit time is within the allowable timeout period, the current session is considered to be continuous.

 The `_session_start` event is initiated when the website opens for the first time, or the browser opens to the foreground and the time between the last exit exceeded `session_time_out` period, and the following are session-related attributes.
+  \_session\_id: We calculate the session id by concatenating the last 8 characters of uniqueId and the current millisecond, for example,`dc7a7a18-20230905-131926703`.
+  \_session\_duration : We calculate the session duration by minus the current event create timestamp and the session's \_session\_start\_timestamp, this attribute will be added in every event during the session.
+  \_session\_number : It indicates the auto increment number of session in current browser, and has an initial value `1`.
+  Session timeout duration: By default, it is `30` minutes, which can be customized through the [configuration](#customize-configurations) API.

### Page view definition
<a name="page-view-definition"></a>

 In Clickstream Web SDK, the `_page_view` refers to an event that records a user's browsing path of page. When a page transition started, the `_page_view` event will be recorded if any of the following conditions is met:
+  No page was previously set.
+  The new page title differs from the previous page title.
+  The new page URL differs from the previous page URL.

 This event listens for pushState, popState in history, and replaceState of window to determine the page transition. In order to track page browsing path, we use \_page\_referrer (last page URL) and page\_referrer\_title to link the previous page. There are some other attributes in page view event.
+  \_entrances: It is `1` for the first page view event in a session. Otherwise, it is `0`.
+  \_previous\_timestamp: The timestamp of the previous \_page\_view event.
+  \_engagement\_time\_msec: The previous page last engagement in milliseconds.

When the page goes to invisible for more than 30 minutes and then is opened again, a new session will be generated, the previous page URL will be cleared, and a new page view event will be sent.

### User engagement definition
<a name="user-engagement-definition-2"></a>

 In Clickstream Web SDK, the `_user_engagement` refers to an event that records the page browsing time. This event is sent only when a user leaves the page and the page has focus for at least one second.

 We define that users leave the page in the following situations.
+  When the user navigates to another page under the current domain.
+  When the user clicks a link that leads away from the current domain.
+  When the user clicks another browser tab or minimizes the current browser window.
+  When the user closes the website tab or closes the browser application.

 **engagement\_time\_msec**: We calculate the milliseconds from when the current page is visible to when the user leaves the current page excluding the idle time in between.

## Event attributes
<a name="event-attributes"></a>

### Sample event structure
<a name="sample-event-structure"></a>

```
{
    "unique_id": "c84ad28d-16a8-4af4-a331-f34cdc7a7a18",
    "event_type": "add_to_cart",
    "event_id": "460daa08-0717-4385-8f2e-acb5bd019ee7",
    "timestamp": 1667877566697,
    "device_id": "f24bec657ea8eff7",
    "platform": "Web",
    "make": "Google Inc.",
    "locale": "zh_CN",
    "screen_height": 1080,
    "screen_width": 1920,
    "viewport_height": 980,
    "viewport_width": 1520,
    "zone_offset": 28800000,
    "system_language": "zh",
    "country_code": "CN",
    "sdk_version": "0.2.0",
    "sdk_name": "aws-solution-clickstream-sdk",
    "host_name": "https://example.com",
    "app_id": "appId",
    "items": [{
        "id": "123",
        "name": "Nike",
        "category": "shoes",
        "price": 279.9
    }],
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
        "_latest_referrer": "https://amazon.com/s?k=nike",
        "_latest_referrer_host": "amazon.com",
        "_page_title": "index",
        "_page_url": "https://example.com/index.html"
    }
}
```

 All user attributes will be stored in user object, and all custom and global attributes in attributes object.

### Common attributes
<a name="common-attributes"></a>

|  **Attribute name**  |  **Data type**  |  **Description**  |  **How to generate**  |  **Usage and purpose**  |
| --- | --- | --- | --- | --- |
|  hashCode  |  string  |  the event object's hash code  |  calculated by library @aws-crypto/sha256-js  |  distinguish different events  |
|  app\_id  |  string  |  the app\_id for your app  |  generated by clickstream guidance when you register an app to a data pipeline  |  identify the events for your apps  |
|  unique\_id  |  string  |  the unique id for user  |  generated from uuidV4() during the SDK first initialization. It will be changed if user logout and then login to a new user. When user re-login to the previous user in the same browser, the unique\_Id will be reset to the same previous unique\_id.  |  the unique id to identity different users and associating the behavior of logged-in and not logged-in  |
|  device\_id  |  string  |  the unique id for device  |  generated from uuidV4() when the website is first open, then the uuid will stored in localStorage and will never be changed  |  distinguish different devices  |
|  event\_type  |  string  |  event name  |  set by developer or SDK  |  distinguish different events type  |
|  event\_id  |  string  |  the unique id for event  |  generated from uuidV4() when the event create  |  distinguish different events  |
|  timestamp  |  number  |  event create timestamp in millisecond  |  generated from new Date().getTime() when event create  |  data analysis needs  |
|  platform  |  string  |  the platform name  |  for browser is always Web  |  data analysis needs  |
|  make  |  string  |  the browser make  |  generated from window.navigator.product or window.navigator.vendor  |  data analysis needs  |
|  screen\_height  |  number  |  the screen height pixel  |  generated from window.screen.height  |  data analysis needs  |
|  screen\_width  |  number  |  the screen width pixel  |  generated from window.screen.width  |  data analysis needs  |
|  viewport\_height  |  number  |  the website viewport height pixel  |  generated from window.innerHeight  |  data analysis needs  |
|  viewport\_width  |  number  |  the website viewport width pixel  |  generated from window.innerWidth  |  data analysis needs  |
|  zone\_offset  |  number  |  the device raw offset from GMT in milliseconds.  |  generated from currentDate.getTimezoneOffset()\*60000  |  data analysis needs  |
|  locale  |  string  |  the default locale(language, country and variant) for the browser  |  generated from window.navigator.language  |  data analysis needs  |
|  system\_language  |  string  |  the browser language code  |  generated from window.navigator.language  |  data analysis needs  |
|  country\_code  |  string  |  country/region code for the browser  |  generated from window.navigator.language  |  data analysis needs  |
|  sdk\_version  |  string  |  clickstream sdk version  |  generated from package.json  |  data analysis needs  |
|  sdk\_name  |  string  |  clickstream sdk name  |  this will always be aws-solution-clickstream-sdk  |  data analysis needs  |
|  host\_name  |  string  |  the website hostname  |  generated from window.location.hostname  |  data analysis needs  |

### User attributes
<a name="user-attributes"></a>

|  **Attribute name**  |  **Description**  |
| --- | --- |
|  \_user\_id  |  Reserved for user id that is assigned by app  |
|  \_user\_ltv\_revenue  |  Reserved for user lifetime value  |
|  \_user\_ltv\_currency  |  Reserved for user lifetime value currency  |
|  \_user\_first\_touch\_timestamp  |  Added to the user object for all events. The time (in milliseconds) when the user first visited the website.  |

### Event attributes
<a name="event-attributes-1"></a>

|  **Attribute name**  |  **Data type**  |  **Auto track**  |  **Description**  |
| --- | --- | --- | --- |
| \_traffic\_source\_source | String | false | Reserved for traffic source source. Name of the network source that acquired the user when the event were reported. Example: Google, Facebook, Bing, Baidu |
|  \_traffic\_source\_medium  | String  |  false  |  Reserved for traffic medium. Use this attribute to store the medium that acquired user when events were logged. Example: Email, Paid search, Search engine.  |
| \_traffic\_source\_campaign | String | false | Reserved for traffic source campaign. Use this attribute to store the campaign of your traffic source. Example: summer\_sale, holiday\_specials |
|  \_traffic\_source\_name  | String  |  false  |  Reserved for traffic name. Use this attribute to store the marketing campaign that acquired user when events were logged. Example: Summer promotion.  |
| \_traffic\_source\_campaign\_id  | String | false | Reserved for traffic source campaign id. Use this attribute to store the campaign id of your traffic source. Example: campaign\_1, campaign\_2 |
| \_traffic\_source\_term  | String | false  | Reserved for traffic source term. Use this attribute to store the term of your traffic source. Example: running\_shoes, fitness\_tracker. |
| \_traffic\_source\_content  | String | false | Reserved for traffic source content. Use this attribute to store the content of your traffic source. Example: banner\_ad\_1, text\_ad\_2. |
| \_traffic\_source\_clid  | String | false | Reserved for traffic source clid. Use this attribute to store the clid of your traffic source. Example: amazon\_ad\_123, google\_ad\_456. |
| \_traffic\_source\_clid\_platform  | String | false | Reserved for traffic source clid platform. Use this attribute to store the clid platform of your traffic source. Example: amazon\_ads, google\_ads |
|  \_session\_id  | String |  true  |  Added in all events.  |
|  \_session\_start\_timestamp  |  number  |  true  |  Added in all events. The value is millisecond.  |
|  \_session\_duration  |  number  |  true  |  Added in all events. The value is millisecond.  |
|  \_session\_number  |  number  |  true  |  Added in all events.  |
|  \_page\_title  |  String  |  true  |  Added in all events.  |
|  \_page\_url  |  String  |  true  |  Added in all events.  |
|  \_latest\_referrer  |  String  |  true  |  Added in all events. The last off-site url.  |
|  \_latest\_referrer\_host  |  String  |  true  |  Added in all events. The last off-site domain name.  |

### Item attributes
<a name="item-attributes"></a>

|  **Attribute name**  |  **Data type**  |  **Required**  |  **Description**  |
| --- | --- | --- | --- |
|  id  |  string  |  False  |  The id of the item  |
|  name  |  string  |  False  |  The name of the item  |
|  brand  |  string  |  False  |  The brand of the item  |
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

You can use the listed preset item attributes, and you can also add custom attributes to an item. In addition to the preset attributes, an item can add up to 10 custom attributes.

## Google Tag Manager integration
<a name="google-tag-manager-integration"></a>

1. Download the Clickstream SDK template file (.tpl) from the SDK Release Page.

1. Refer to the Google Tag Manager Import Guide for instructions on importing the .tpl file as a custom template in your tag manager console.

1. Refer to the Use your new tag to add ClickstreamAnalytics tag to your container.

1. The ClickstreamAnalytics tag currently supports four tag types:

   • Initialize SDK

   • Record Custom Event

   • Set User ID

   • Set User Attribute

**Important**
Please ensure that you initialize the SDK tag first before use other ClickstreamAnalytics tag types.

## Change logs
<a name="change-logs"></a>

 For more information, see the [change logs on GitHub](https://github.com/awslabs/clickstream-web/releases).

## Sample project
<a name="sample-project-123"></a>

 [Sample Web Project for SDK integration](https://github.com/aws-samples/clickstream-sdk-samples/tree/main/retail-web)

## References
<a name="w2aac19c15c21"></a>

 [Source code](https://github.com/awslabs/clickstream-web)

 [Project issue](https://github.com/awslabs/clickstream-web/issues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
