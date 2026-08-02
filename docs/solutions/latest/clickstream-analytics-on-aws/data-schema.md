---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/data-schema.html
---

# Data schema
<a name="data-schema"></a>

This article explains the data schema and format in Clickstream Analytics on AWS. This guidance uses an **event-based** data model to store and analyze clickstream data. Every activity (such as click and view) on the clients is modeled as an event with dimensions, and each dimension represents a parameter of the event. Dimensions are common for all events.

You can use JSON objects to store custom event parameters as key-value pairs into special dimensions, which helps you to collect information that is specific for your business. Those JSON objects are stored in special data types, which allow you to extract the values in the analytics engines.

## Database and table
<a name="database-and-table"></a>

 For each project, the guidance creates a database with name of `<project-id>` in Amazon Redshift and Athena. Each app will have a schema with name of `app_id`. In Athena, all tables are added partitions of `app_id`, year, month, and day. Based on the event data, the guidance's data-processing module creates the following four base tables:
+ **event-v2:** This table stores event data. Each record represents an individual event.
+ **user-v2:** This table stores the latest user attributes. Each record represents a visitor (pseudonymous user).
+ **item-v2:** This table stores event-item data. Each record represents an event that is associated with an item.
+ **session:** This table stores session data. Each record represents a session for each pseudonymous user.

## Columns
<a name="columns"></a>

Each column in the tables represents a specific parameter for an event, user, or item. Some parameters are nested within a `Super` field in Amazon Redshift or a `Map` field in Athena. Those fields (such as `custom_parameters`, `user_properties`) contain parameters that are repeatable. The following table describes the fields.

### Event table fields
<a name="event-table-fields"></a>

|  **Field Name**  |  **Data Type - Redshift**  |  **Data Type - Athena**  |  **Description**  |
| --- | --- | --- | --- |
|  event\_timestamp  |  TIMESTAMP  |  TIMESTAMP  | The timestamp (in microseconds, UTC) when the event was logged on the client. |
|  event\_id  |  VARCHAR  |  STRING  |  Unique ID for the event.  |
| event\_time\_msec | BIGINT | BIGINT | The time in UNIX timestamp format (microseconds) when the event was logged on the client. |
|  event\_name  |  VARCHAR  |  STRING  |  The name of the event.  |
|  event\_value  | DOUBLE PRECISION | FLOAT | The value of the event's "value" parameter. |
|  event\_value\_currency |  VARCHAR  |  STRING  |  The currency of the value associated with the event. |
|  event\_bundle\_sequence\_id  |  BIGINT  |  BIGINT  |  The sequential ID of the bundle in which these events were uploaded.  |
|  ingest\_timestamp  |  BIGINT  |  BIGINT  |  Timestamp offset between collection time and upload time in micros.  |
|  device.mobile\_brand\_name  |  VARCHAR  |  STRING  |  The device brand name.  |
|  device.mobile\_model\_name  |  VARCHAR  |  STRING  |  The device model name.  |
|  device.manufacturer  |  VARCHAR  |  STRING  |  The device manufacturer name.  |
|  device.carrier  |  VARCHAR  |  STRING  |  The device network provider name.  |
|  device.network\_type  |  VARCHAR  |  STRING  |  The network\_type of the device, e.g., WIFI, 5G  |
|  device.operating\_system  |  VARCHAR  |  STRING  |  The operating system of the device.  |
|  device.operating\_system\_version  |  VARCHAR  |  STRING  |  The OS version.  |
|  device.vendor\_id  |  VARCHAR  |  STRING  |  IDFV (present only if IDFA is not collected).  |
|  device.advertising\_id  |  VARCHAR  |  STRING  |  Advertising ID/IDFA.  |
|  device.system\_language  |  VARCHAR  |  STRING  |  The OS language.  |
|  device.time\_zone\_offset\_seconds  |  BIGINT  |  BIGINT  |  The offset from GMT in seconds.  |
|  device.ua\_browser  |  VARCHAR  |  STRING  |  The browser in which the user viewed content, derived from User Agent string  |
|  device.ua\_browser\_version  |  VARCHAR  |  STRING  |  The version of the browser in which the user viewed content, derive from User Agent  |
|  device.ua\_device  |  VARCHAR  |  STRING  |  The device in which user viewed content, derive from User Agent.  |
|  device.ua\_device\_category  |  VARCHAR  |  STRING  |  The device category in which user viewed content, derive from User Agent.  |
| device.ua\_os |  VARCHAR  |  STRING  | The operating system of the device in which user viewed content, derive from User Agent. |
| device.ua\_os\_version |  VARCHAR  |  STRING  | The operating system version of the device category in which user viewed content, derive from User Agent. |
| device.ua | SUPER | MAP | The parsed User Agent in key-value pairs |
|  device.screen\_width  |  VARCHAR  |  STRING  |  The screen width of the device.  |
|  device.screen\_height  |  VARCHAR  |  STRING  |  The screen height of the device.  |
| device.viewport\_width | VARCHAR | STRING | The screen width of the browser viewport. |
| device.viewport\_height | VARCHAR | STRING | The screen height of the browser viewport. |
|  geo.continent  |  VARCHAR  |  STRING  |  The continent from which events were reported, based on IP address.  |
|  geo.sub\_continent  |  VARCHAR  |  STRING  |  The subcontinent from which events were reported, based on IP address.  |
|  geo.country  |  VARCHAR  |  STRING  |  The country from which events were reported, based on IP address.  |
|  geo.region  |  VARCHAR  |  STRING  |  The region from which events were reported, based on IP address.  |
|  geo.metro  |  VARCHAR  |  STRING  |  The metro from which events were reported, based on IP address.  |
|  geo.city  |  VARCHAR  |  STRING  |  The city from which events were reported, based on IP address.  |
|  geo.locale  |  VARCHAR  |  STRING  |  The locale information obtained from device.  |
|  traffic\_source\_name  |  VARCHAR  |  STRING  |  Name of the marketing campaign that acquired the user when the events were reported.  |
|  traffic\_source\_medium  |  VARCHAR  |  STRING  |  Name of the medium (paid search, organic search, email, etc.) that acquired the user when the events were reported.  |
|  traffic\_source\_campaign  |  VARCHAR  |  STRING  |  The marketing campaign (derive from utm\_campaign) associated with the event.  |
| traffic\_source\_content | VARCHAR | STRING | The marketing campaign content (derive from utm\_content) associated with the event. |
| traffic\_source\_term | VARCHAR | STRING | The marketing campaign term (derive from utm\_term) associated with the event. |
| traffic\_source\_campaign\_id | VARCHAR | STRING | The marketing campaign id (derive from utm\_id) associated with the event. |
| traffic\_source\_clid | VARCHAR | STRING | The click id associated with the event. |
| traffic\_source\_clid\_platform | VARCHAR | STRING | The platform of the click id associated with the event. |
| traffic\_source\_channel\_group | VARCHAR | STRING | The channel group (assigned by traffic classification rules) associated with the event. |
| traffic\_source\_category | VARCHAR | STRING | The source category (i.e., Search, Social, Video, Shopping) based on the traffic source associated with the event. |
| user\_first\_touch\_time\_msec | BIGINT | BIGINT | The time in UNIX timestamp format (microseconds) when the user first touch the app or website. |
| app\_package\_id | VARCHAR | STRING | The package name or bundle ID of the app. |
| app\_version | VARCHAR | STRING | The app's versionName (Android) or short bundle version. |
| app\_title | VARCHAR | STRING | The app's name. |
| app\_id | VARCHAR | STRING | The App ID (created by this guidance) associated with the app. |
| app\_install\_source | VARCHAR | STRING | The store from which user installed the app. |
|  platform  |  VARCHAR  |  STRING  |  The data stream platform (Web, IOS or Android) from which the event originated.  |
|  project\_id  |  VARCHAR  |  STRING  |  The project id associated with the app.  |
| screen\_view\_screen\_name |  VARCHAR  | STRING | The screen name associated with the event. |
| screen\_view\_screen\_id |  VARCHAR  | STRING | The screen class id associated with the event. |
| screen\_view\_screen\_unique\_id  |  VARCHAR  | STRING | The unique screen id associated with the event |
| screen\_view\_previous\_screen\_name |  VARCHAR  | STRING | The previous unique screen id associated with the event. |
| screen\_view\_previous\_screen\_id | VARCHAR | STRING | The previous unique screen id associated with the event. |
| screen\_view\_previous\_screen\_unique\_id  | VARCHAR | STRING | The previous unique screen id associated with the event. |
| screen\_view\_entrances  | BOOLEAN | BOOLEAN | Whether the screen is the entrance view of the session. |
| page\_view\_page\_referrer  | VARCHAR | STRING | The referrer page url.  |
| page\_view\_page\_referrer\_title | VARCHAR | STRING | The referrer page title. |
|  page\_view\_previous\_time\_msec | BIGINT | BIGINT | The timestamp of the previous page\_view event.  |
|  page\_view\_engagement\_time\_msec  | BIGINT | BIGINT | The previous page\_view duration in milliseconds. |
| page\_view\_page\_title | VARCHAR | STRING | The title of the webpage associated with the event. |
|  page\_view\_page\_url  | VARCHAR | STRING | The url of the webpage associated with the event.  |
| page\_view\_page\_url\_path | VARCHAR  | STRING | The url path of the webpage associated with the event.  |
|  page\_view\_page\_url\_query\_parameters  | SUPER  |  MAP  | The query parameters in key-value pairs of the page url associated with the event.  |
| page\_view\_hostname  | VARCHAR  | STRING  | The host name of the web page associated with the event.  |
| page\_view\_latest\_referrer  | VARCHAR  | STRING  | The url of the latest external referrer.  |
| page\_view\_latest\_referrer\_host  | VARCHAR  | STRING  | The hostname of the latest external referrer.  |
| page\_view\_entrances  | BOOLEAN  | BOOLEAN  | Whether the page is the entrance view of the session.  |
| app\_start\_is\_first\_time | BOOLEAN  | BOOLEAN | Whether the app start is a new app launch.  |
| upgrade\_previous\_app\_version  | VARCHAR | STRING | Previous app version before app upgrade event.  |
| upgrade\_previous\_os\_version  | VARCHAR | STRING | Previous os version before OS upgrade event.  |
| search\_key  | VARCHAR | STRING | The name of the keyword in the URL when user perform search on web site.  |
| search\_term  | VARCHAR  | STRING  | The search content in the URL when user perform search on web site.  |
| outbound\_link\_classes  | VARCHAR | STRING  | The content of class in tag that associated with the outbound link.  |
| outbound\_link\_domain  |  VARCHAR  | STRING  | The domain of href in tag that associated with the outbound link.  |
| outbound\_link\_id  | VARCHAR  | STRING  | The content of id in tag that associated with the outbound link.  |
| outbound\_link\_url  | VARCHAR  | STRING  | The content of href in tag that associated with the outbound link.  |
| outbound\_link  | BOOLEAN  | BOOLEAN  | Whether the link is outbound link or not.  |
| user\_engagement\_time\_msec  | BIGINT  | BIGINT  | The user engagement duration in milliseconds.  |
| user\_id  | VARCHAR  | STRING  | The unique ID assigned to a user through setUserId() API.  |
| user\_pseudo\_id  | VARCHAR  | STRING  | The pseudonymous id generated by SDK for the user.  |
| session\_id  | VARCHAR  | STRING  | The session id associated with the event.  |
| session\_start\_time\_msec  | BIGINT  | BIGINT  | The start time in UNIX timestamp of the session.  |
| session\_duration  | BIGINT  | BIGINT  | The duration the session lasts, in milliseconds.  |
| session\_number  | BIGINT  | BIGINT  | Number of the sessions generated from the client.  |
| scroll\_engagement\_time\_msec  | BIGINT  | BIGINT  | The engagement time on the web page until user scroll.  |
| sdk\_error\_code  | VARCHAR  | STRING  | The error code generated by SDK when an event is invalid in some way.  |
| sdk\_error\_message  | VARCHAR  | STRING  | The error message generated by SDK an event is invalid in some way.  |
| sdk\_version  | VARCHAR  | STRING  | The version of the SDK.  |
| sdk\_name  | VARCHAR  | STRING  | The name of the SDK.  |
| app\_exception\_message  | VARCHAR  | STRING  | The exception message when the app crashes or throws an exception.  |
| app\_exception\_stack  | VARCHAR  | STRING  | The exception stack trace when the app crashes or throws an exception.  |
| custom\_parameters\_json\_str  | VARCHAR  | STRING  | All the custom event parameters stored in key-value pairs.  |
| custom\_parameters | SUPER  | MAP  | All the custom event parameters stored in key-value pairs.  |
|  process\_info  | SUPER  | MAP  | Store information about the data processing. |
| created\_time | TIMESTAMP | TIMESTAMP | Store information about the data processing.  |

### User table fields
<a name="user-table-fields"></a>

|  **Field Name**  |  **Data Type - Redshift**  |  **Data Type - Athena**  |  **Description**  |
| --- | --- | --- | --- |
|  event\_timestamp  |  BIGINT  |  STRING  |  The timestamp of when the user attributes was collected.  |
|  user\_id  |  VARCHAR  |  STRING  |  The unique ID assigned to a user through setUserId() API.  |
|  user\_pseudo\_id  |  VARCHAR  |  STRING  |  The pseudonymous id generated by SDK for the user.  |
|  user\_properties  |  SUPER  |  ARRAY  |  Properties of the user.  |
| user\_properties\_json\_str | VARCHAR | STRING | Properties of the user. |
| first\_touch\_timestamp | BIGINT | BIGINT | The time (in microseconds) at which the user first opened the app or visited the site. |
| first\_visit\_date  |  Date  |  Date  |  Date of the user's first visit. |
| first\_referer  |  VARCHAR  |  STRING  |  The first referer detected for the user. |
| first\_traffic\_source |  VARCHAR  |  STRING  | The the network source that acquired the user that was first detected for the user, e.g., Google, Baidu  |
| first\_traffic\_source\_medium  |  VARCHAR  |  STRING  | The medium of the network source that acquired the user that was first detected for the user, e.g., paid search, organic search, email, etc |
| first\_traffic\_source\_campaign  | VARCHAR | STRING | The name of the marketing campaign that acquired the user that was first detected for the user. |
| first\_traffic\_source\_content  | VARCHAR | STRING | The marketing campaign content that acquired the user that was first detected for the user. |
| first\_traffic\_source\_term  | VARCHAR | STRING | The keyword of the marketing ads that acquired the user that was first detected for the user. |
| first\_traffic\_source\_campaign\_id  | VARCHAR | STRING | The id of the marketing campaign that acquired the user that was first detected for the user. |
| first\_traffic\_source\_clid\_platform  | VARCHAR | STRING | The click id platform of the marketing campaign that acquired the user that was first detected for the user.  |
| first\_traffic\_source\_clid  | VARCHAR | STRING | The click id of the marketing campaign that acquired the user that was first detected for the user.  |
| first\_traffic\_source\_channel\_group first\_traffic\_source\_category | VARCHAR | STRING | The channel group of the traffic source that acquired the user that was first detected for the user.  |
|  first\_app\_install\_source  | VARCHAR | STRING | The source category (i.e., Search, Social, Video, Shopping) based on the traffic source that acquired the user for the first time.  |
| process\_info  | SUPER  | MAP  | The install channel for the user, e.g., Google Play Store information about the data processing. |
| created\_time  | TIMESTAMP | TIMESTAMP |  Store information about the data processing. |

### Session table fields
<a name="session-table-fields"></a>

|  **Field Name**  |  **Data Type - Redshift**  |  **Data Type - Athena**  |  **Description**  |
| --- | --- | --- | --- |
| event\_timestamp  | TIMESTAMP  | STRING | The timestamp of when the event occurred.  |
| user\_pseudo\_id  | VARCHAR | STRING | The pseudonymous ID generated by the SDK for the user. |
| session\_id  | VARCHAR | STRING | The ID assigned to a session. |
| user\_id  | VARCHAR | STRING | The unique ID assigned to a user through the setUserId() API.  |
| session\_number  | BIGINT | INT | The sequence number of the session in the client. |
| session\_start\_time\_msec  | BIGINT | BIGINT | The start time of the session in milliseconds.  |
| session\_source  | VARCHAR | STRING  | The traffic source of the session. |
| session\_medium  | VARCHAR | STRING  | The traffic source medium of the session. |
| session\_campaign  | VARCHAR | STRING  | The traffic source campaign of the session. |
| session\_content  | VARCHAR | STRING  | The traffic source content of the session. |
| session\_term  | VARCHAR | STRING | The traffic source term of the session.  |
| session\_campaign\_id  | VARCHAR | STRING | The traffic source campaign ID of the session. |
| session\_clid\_platform  | VARCHAR | STRING | The platform of the CLID (Click ID) of the session. |
| session\_clid  | VARCHAR | STRING | The CLID (Click ID) of the session. |
| session\_channel\_group  | VARCHAR | STRING | The traffic source channel group of the session.  |
| session\_source\_category  | VARCHAR | STRING | The traffic source category of the session source.  |
| process\_info  | SUPER | MAP | Additional data processing information. |
| created\_time  | TIMESTAMP | STRING  | The timestamp of when the session data was created. |

### Item table fields
<a name="item-table-fields"></a>

|  **Field Name**  |  **Data Type - Redshift**  |  **Data Type - Athena**  |  **Description**  |
| --- | --- | --- | --- |
|  event\_timestamp  | TIMESTAMP | STRING | The timestamp of when the event occurred. |
| event\_id  | VARCHAR  | STRING  |  The ID of the event.  |
| event\_name  | VARCHAR | STRING | The name of the event. |
| platform | VARCHAR | STRING | The platform associated with the event. |
| user\_pseudo\_id | VARCHAR | STRING | The pseudonymous ID generated by the SDK for the user. |
| user\_id | VARCHAR | STRING | The unique ID assigned to a user through the setUserId() API. |
| item\_id | VARCHAR | STRING | The ID of the item. |
| name | VARCHAR | STRING | The name of the item. |
| brand | VARCHAR | STRING | The brand of the item.  |
| currency | VARCHAR | STRING | The currency associated with the item price. |
| price | DOUBLE PRECISION  | DOUBLE | The price of the item.  |
| quantity | DOUBLE PRECISION  | DOUBLE | The quantity of the item in the event. |
| creative\_name | VARCHAR | STRING | The name of the creative associated with the item. |
| creative\_slot | VARCHAR | STRING | The slot of the creative associated with the item. |
| location\_id  | VARCHAR | STRING | The ID of the location associated with the item.  |
| category | VARCHAR | STRING | The category of the item. |
| category2 | VARCHAR | STRING | The second category of the item.  |
| category3 | VARCHAR | STRING | The third category of the item.  |
| category4 | VARCHAR | STRING | The fourth category of the item.  |
| category5 | VARCHAR | STRING | The fifth category of the item. |
| custom\_parameters\_json\_str | VARCHAR | STRING | The JSON string representation of custom parameters.  |
| custom\_parameters  | SUPER  | MAP  | Additional custom parameters.  |
| process\_info | SUPER  | MAP  | Additional process information. |
| created\_time | TIMESTAMP | STRING | The timestamp of when the item data was created. |
