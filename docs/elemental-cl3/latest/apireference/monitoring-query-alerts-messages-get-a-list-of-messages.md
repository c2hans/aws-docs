---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-query-alerts-messages-get-a-list-of-messages.html
---

# GET Messages: Get a List of Messages
<a name="monitoring-query-alerts-messages-get-a-list-of-messages"></a>

Get a list of messages on one or more nodes in the cluster.

## HTTP Request and Response
<a name="monitoring-query-alerts-messages-get-a-list-of-messages-http-request-response"></a>

### Request URL
<a name="monitoring-query-alerts-messages-get-a-list-of-messages-http-request-response-url"></a>

The request consists of the operation, the URL of the Conductor Live node, the messages request, and optional filter parameters. If using multiple filters, enter the ampersand (&) between each filter parameter. For example:

```
GET http://<Conductor IP address>/messages?<filter>=<value>&<filter>=<value>
```

The following filter parameters are available for the GET request. See the [examples](monitoring-query-alerts-messages-get-a-list-of-alerts.md#monitoring-query-alerts-messages-get-a-list-of-alerts-example)for a variety of filter parameters.

| Filter | Value | Description |
| --- | --- | --- |
| origin |  Integer | Filter for messages that were originate with a specific node. Enter the ID of the node as assigned by Conductor Live.<br />See [Where Alerts Come From and Where They Apply](monitoring-query-alerts-messages-get-a-list-of-alerts.md#monitoring-query-alerts-messages-get-a-list-of-alerts-http-request-response-url-where-alerts-come-from). |
| node |  Integer | Filter for messages that apply to a specific node. Enter the ID of the node as assigned by AWS Elemental Conductor Live 3.<br />Typically, for a node, do not enter both the origin and node filters. |
| channel |  Integer | Filter for messages that apply to a specific channel. Enter the ID of the channel as assigned by Conductor Live.<br />You can enter both an origin and channel. |
| mpts |  Integer | Filter for messages that apply to a specific Multi-Program Transport Stream (MPTS) output. Enter the ID of the MPTS output as assigned by Conductor Live.<br />You can enter both an origin and an MPTS. |
| type |  String | Case-insensitive match. See the Status > Messages screen on the Conductor Live web interface for a list of applicable types. |
| code |  String | Filter for only those messages with the specified message codes. Enter a comma-separated list of 1 or more numeric codes. For a list of codes, see the Status > Messages screen on the Conductor Live web interface.  |
| page |  Integer | Default is 1. |
| per\_page |  Integer | Default is 20. |

#### Origin, Node, Channel, MPTS
<a name="monitoring-query-alerts-messages-get-a-list-of-messages-http-request-response-url-origin-node-channel-mpts"></a>

A message may originate with an Conductor Live node or it may originate with a worker node and get pushed to Conductor Live. In both cases, the message may relate to a node and/or a channel or Multi-Program Transport Stream (MPTS) output.

For example, if a channel on Live node live-01 fails, then a message may occur. The message originates from Live node live-01 and applies to node live-01 and channel Channel\_A.

Or a node live-01 may fail, resulting in a message. In this case, the message originates from the Conductor node (not from live-01), but it applies to node live-01.

#### page and per\_page
<a name="monitoring-query-alerts-messages-get-a-list-of-messages-http-request-response-url-page-and-per_page"></a>

The per\_page parameter chunks messages into groups or “pages” of a given count. For example, “30” means chunk messages into one page for IDs 1-30, another for 31-60, and so on. The page parameter identifies a given page. For example, if per\_page is “30,” then page 3 contains IDs 61-90.

Enter only the page (per\_page uses the default), only the per\_page (page uses the default), or both.

Messages are not sorted into any order, so you cannot obtain the newest messages, for example. The key use for these filter parameters is to retrieve a large number of messages by specifying a high number in per\_page.

### Call Header
<a name="monitoring-query-alerts-messages-get-a-list-of-messages-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md) .

### Response
<a name="monitoring-query-alerts-messages-get-a-list-of-messages-http-request-response-response"></a>

The response is XML content consisting of one **message** element with the following.
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Several elements from the table below.

| Element | Value | Description |
| --- | --- | --- |
| id | Integer | A unique ID for this alert, assigned by Conductor Live. |
| type | String | The type of the message. |
| code | Integer | The internal code assigned to this type of alert. |
| message | String | A longer description. |
| data | String | A data string that can hold additional information on the message. |
| notes | String | A notes string that is always null. |
| messageable\_id | Integer | The unique ID for the entity in alertable\_type. This is the ID that is included in the response of a GET. For example, GET Node includes the ID that uniquely identifies the node. |
| messageable\_type | String | The type of the output in the channel (event) that this alert specifically applies to. Otherwise null. |
| node\_id | Integer | The ID which identifies the same piece of data as the origin filter in the request; see [GET Alerts: Get a List of Alerts](monitoring-query-alerts-messages-get-a-list-of-alerts.md). |
| remote\_id | Integer | The ID of the entity (channel or MPTS) as assigned by the worker node that is running this entity. The ID assigned by Conductor Live may be different from the ID assigned by the worker node.  |
| updated\_at | Time | The last time this alert was updated. |
