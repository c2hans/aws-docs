---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/http-api.html
---

# HTTP API
<a name="http-api"></a>

 This section introduces how to send your clickstream data directly to the Clickstream ingestion server via HTTP requests. The Clickstream data processing module will correctly process your data simultaneously by following the guidelines below. Then, you can visually analyze them in the subsequent report module.

## Request endpoint
<a name="request-endpoint"></a>

 After creating the application in the solution web console, you will get the **Server Endpoint** and **App ID** on the details page. For example:
+  **Server Endpoint**: `https://example.com/collect`
+  **App ID**: `my_app`

## API Specification
<a name="api-specification"></a>
+  The app ID in the query parameters must be one of the applications you create for the project in the solution web console. Otherwise, the server will respond to HTTP status code 403.
+  The request body contains four parts: common attributes, items, user, and attributes. The public attributes require the event\_type, event\_id, timestamp, and app\_id; the rest are optional parameters.
+  The total size of the body of a single request cannot exceed 1MB. Otherwise, the HTTP status code 413 will return.

**Reqeust method**

 POST

**Request headers**

|  **Parameter name**  |  **Required**  |  **Example**  |  **Description**  |
| --- | --- | --- | --- |
|  Content-Type  |  YES  |  application/json; charset=utf-8  |  Content type  |
|  X-Forwarded-For  |  NO  |  [101.188.67.134](https://whatismyipaddress.com/page/36)  |  Source IP address, it's required if you forward the client requests to clickstream servers from your servers  |
|  User-Agent  |  NO  |  Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36  |  User-Agent  |
|  cookie  |  NO  |  your auth cookie  |  The authentication token for your request. Please refer to [server side configuration](ingestion-endpoint.md).  |

**Request query parameters**

|  **Parameter name**  |  **Required**  |  **Example**  |  **Description**  |
| --- | --- | --- | --- |
|  appId  |  YES  |  test\_app  |  The app ID for your application is created in the guidance web console  |
|  platform  |  NO  |  Android/iOS/Web/...  |  Distinguish between platforms  |
|  event\_bundle\_sequence\_id  |  NO  |  1  |  Request sequence number, an incrementing integer starting from 1  |
|  hashCode  |  NO  |  478acd09  |  The first eight digits of the sha256 calculation result of the request body string  |
|  compression  |  NO  |  gzip  |  Request body compression method. Currently, only gzip is supported. Keeping it absent means no compression  |

**Request body**

 The request body is an array structure that contains the JSON string of one or more events. For example:

```
[
  {
    "event_type": "button_click",
    "event_id": "460daa08-0717-4385-8f2e-acb5bd019ee7",
    "timestamp": 1667877566697,
    "app_id": "your appId",
    "attributes": {
      "productName": "shoes",
      "Price": 99.9
    }
  },
  {
    "event_type": "item_view",
    "event_id": "c6067c1c-fd8d-4fdb-bfaf-cc1212ca0195",
    "timestamp": 1667877565698,
    "app_id": "your appId",
    "attributes": {
      "productName": "book",
      "Price": 39.9
    }
  }
]
```

**Event attributes**

|  **Attributes name**  |  **Required**  |  **Data Type**  |  **Example**  |  **Description**  |
| --- | --- | --- | --- | --- |
|  event\_type  |  YES  |  String  |  button\_click  |  Event type  |
|  event\_id  |  YES  |  String  |  460daa08-0717-4385-8f2e-acb5bd019ee7  |  Event's unique ID, we recommend using UUID to generate  |
|  timestamp  |  YES  |  Long  |  1667877566697  |  The timestamp when the event was generated, in milliseconds  |
|  app\_id  |  YES  |  String  |  shopping\_dev  |  The corresponding id when creating the application in the Clickstream web console  |
|  platform  |  NO  |  String  |  Android/iOS/Web/...  |  Device platform  |
|  os\_version  |  NO  |  String  |  10  |  System version  |
|  unique\_id  |  NO  |  String  |  c84ad28d-16a8-4af4-a331-f34cdc7a7a18  |  Unique ID to identify different users and associate the behavior of logged-in and not logged-in  |
|  device\_id  |  NO  |  String  |  f24bec657ea8eff7  |  Distinguish between different devices  |
|  make  |  NO  |  String  |  Samsung  |  Device manufactory  |
|  brand  |  NO  |  String  |  Samsung  |  Device brand  |
|  model  |  NO  |  String  |  S23 Ultra  |  Device model  |
|  carrier  |  NO  |  String  |  CDMA  |  Device network operator name  |
|  network\_type  |  NO  |  String  |  Mobile  |  Current device network type  |
|  locale  |  NO  |  String  |  zh\_CN  |  Local information  |
|  system\_language  |  NO  |  String  |  zh  |  Device language code  |
|  country\_code  |  NO  |  String  |  CN  |  Device country code  |
|  zone\_offset  |  NO  |  int  |  2880000  |  Device's raw offset from GMT in milliseconds  |
|  screen\_height  |  NO  |  int  |  1920  |  Screen height in pixels  |
|  screen\_width  |  NO  |  int  |  1080  |  Screen width in pixels  |
|  viewport\_height  |  NO  |  int  |  540  |  App viewport height  |
|  viewport\_width  |  NO  |  int  |  360  |  App viewport width  |
|  sdk\_version  |  NO  |  String  |  1.2.3  |  SDK version  |
|  sdk\_name  |  NO  |  String  |  aws-solution-clickstream-sdk  |  SDK name  |
|  app\_package\_name  |  NO  |  String  |  com.example.app  |  User's Application package name  |
|  app\_version  |  NO  |  String  |  1.1.0  |  Application version number  |
|  app\_title  |  NO  |  String  |  shopping  |  Application name  |
|  items  |  NO  |  Object  |  [{   "id": "b011ddc3-632f-47cb-a68a-ad83678ecfed",   "name": "Classic coat-rack",   "category": "housewares",   "price": 167 }]  |  Item list, Supports uploading multiple items at one time. A maximum of 100 items can be uploaded at one time For the item quantity limit, please refer to [Event and Attribute Limitation](web-sdk.md#event-attributes) For the supported attributes of the item, please refer to [item attribute](web-sdk.md#event-attributes)  |
|  user  |  NO  |  Object  |  {   "\_user\_id": {     "value": "0202d0e1",     "set\_timestamp": 1695006816345   },    "username": {      "value": "carl",      "set\_timestamp": 1695006816345   } }  |  User attributes. Each attribute key is the user attribute name. Each attribute contains an object. The object contains two attributes: value: The value of the user attribute. set\_timestamp: The timestamp millisecond value when setting the attribute. Up to 100 user attributes can be added to an event. For specific restrictions, please refer to: [Event and Attribute Limitations](web-sdk.md#event-attributes)  |
|  attributes  |  NO  |  Object  |  {   "productName": "book",   "Price": 39.9 }  |  Custom attributes. Up to 500 custom attributes can be added to an event, and the attribute name must meet the [naming rules](android-sdk.md#data-format-definition).  |

**Request response**

 If the HttpCode status code returned by the request is 200, the request is considered successful, other status codes are failures, and the request does not return any other content.

**HttpCode**

|  **Code**  |  **Description**  |
| --- | --- |
|  200  |  Request successful  |
|  403  |  Request failed. Please check if appId and endpoint match, if configured with authentication, please check whether the authentication cookie is correct  |
|  413  |  Request failed. The request body exceeds 1MB  |

## Request code example
<a name="request-code-example"></a>

** cURL: **

```
curl --location 'https://example.com/collect?appId=test_release&platform=Android&event_bundle_sequence_id=1' \
--header 'Content-Type: application/json; charset=utf-8' \
--header 'X-Forwarded-For: 101.188.67.134' \
--data '[{"event_type":"button_click","event_id":"460daa08-0717-4385-8f2e-acb5bd019ee7","timestamp":1667877566697,"app_id":"your appId","attributes":{"productName":"shoes","Price":99.9}},{"event_type":"item_view","event_id":"c6067c1c-fd8d-4fdb-bfaf-cc1212ca0195","timestamp":1667877565698,"app_id":"your appId","attributes":{"productName":"book","Price":39.9}}]'
```

** C\# HttpClient: **

```
var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Post, "https://example.com/collect?appId=test_release&platform=Android&event_bundle_sequence_id=1");
request.Headers.Add("X-Forwarded-For", "101.188.67.134");
var content = new StringContent("[{\"event_type\":\"button_click\",\"event_id\":\"460daa08-0717-4385-8f2e-acb5bd019ee7\",\"timestamp\":1667877566697,\"app_id\":\"your appId\",\"attributes\":{\"productName\":\"shoes\",\"Price\":99.9}},{\"event_type\":\"item_view\",\"event_id\":\"c6067c1c-fd8d-4fdb-bfaf-cc1212ca0195\",\"timestamp\":1667877565698,\"app_id\":\"your appId\",\"attributes\":{\"productName\":\"book\",\"Price\":39.9}}]", null, "application/json; charset=utf-8");
request.Content = content;
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
```

** Java Okhttp: **

```
OkHttpClient client=new OkHttpClient().newBuilder()
        .build();
        MediaType mediaType=MediaType.parse("application/json; charset=utf-8");
        RequestBody body=RequestBody.create(mediaType,"[{\"event_type\":\"button_click\",\"event_id\":\"460daa08-0717-4385-8f2e-acb5bd019ee7\",\"timestamp\":1667877566697,\"app_id\":\"your appId\",\"attributes\":{\"productName\":\"shoes\",\"Price\":99.9}},{\"event_type\":\"item_view\",\"event_id\":\"c6067c1c-fd8d-4fdb-bfaf-cc1212ca0195\",\"timestamp\":1667877565698,\"app_id\":\"your appId\",\"attributes\":{\"productName\":\"book\",\"Price\":39.9}}]");
        Request request=new Request.Builder()
        .url("https://example.com/collect?appId=test_release&platform=Android&event_bundle_sequence_id=1")
        .method("POST",body)
        .addHeader("Content-Type","application/json; charset=utf-8")
        .addHeader("X-Forwarded-For","101.188.67.134")
        .build();
        Response response=client.newCall(request).execute();
```

** JavaScript Fetch: **

```
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json; charset=utf-8");
myHeaders.append("X-Forwarded-For", "101.188.67.134");

var raw = "[{\"event_type\":\"button_click\",\"event_id\":\"460daa08-0717-4385-8f2e-acb5bd019ee7\",\"timestamp\":1667877566697,\"app_id\":\"your appId\",\"attributes\":{\"productName\":\"shoes\",\"Price\":99.9}},{\"event_type\":\"item_view\",\"event_id\":\"c6067c1c-fd8d-4fdb-bfaf-cc1212ca0195\",\"timestamp\":1667877565698,\"app_id\":\"your appId\",\"attributes\":{\"productName\":\"book\",\"Price\":39.9}}]";

var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
};

fetch("https://example.com/collect?appId=test_release&platform=Android&event_bundle_sequence_id=1", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
```

** Python Request: **

```
import requests

        url = "https://example.com/collect?appId=test_release&platform=Android&event_bundle_sequence_id=1"

        payload = "[{\"event_type\":\"button_click\",\"event_id\":\"460daa08-0717-4385-8f2e-acb5bd019ee7\",\"timestamp\":1667877566697,\"app_id\":\"your appId\",\"attributes\":{\"productName\":\"shoes\",\"Price\":99.9}},{\"event_type\":\"item_view\",\"event_id\":\"c6067c1c-fd8d-4fdb-bfaf-cc1212ca0195\",\"timestamp\":1667877565698,\"app_id\":\"your appId\",\"attributes\":{\"productName\":\"book\",\"Price\":39.9}}]"
        headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'X-Forwarded-For': '101.188.67.134'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
```

## Verification data reported successfully
<a name="verification-data-reported-successfully"></a>

If you enabled data processing, you can query the **event**, **event\_parameter**, **user**, **item** or **ingestion\_events** table in Athena directly through SQL.

Moreover, if you enalbed Redshift in data modeling, you can query the **event**, **event\_parameter**, **user**, or **item** table in Redshift directly through SQL.
