---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-query-alerts-messages-get-a-list-of-alerts.html
---

# GET Alerts: Get a List of Alerts
<a name="monitoring-query-alerts-messages-get-a-list-of-alerts"></a>

Get a list of alerts on one or more nodes in the cluster.

## HTTP Request and Response
<a name="monitoring-query-alerts-messages-get-a-list-of-alerts-http-request-response"></a>

### Request URL
<a name="monitoring-query-alerts-messages-get-a-list-of-alerts-http-request-response-url"></a>

The request URL consists of the operation, the URL of the Conductor Live node, the alerts request, and optional filter parameters. Use this format:

```
GET http://<Conductor IP address>/alerts?<filter>=<value>&<filter>=<value>
```

The following filter parameters are available for the GET request. See the [examples](#monitoring-query-alerts-messages-get-a-list-of-alerts-example), which show a variety of filter parameters.

**Note**
Requests for alert data can return very large amounts of information. To receive that information in manageable chunks, use pagination as described in [Specifying Pagination of the Response](request-url.md#specify-pagination-of-response).

| Filter | Value | Description and Notes |
| --- | --- | --- |
| status |  String | Filter for only those alerts that are “active” or “inactive”. To show all active alerts, use:<pre>GET http://198.51.100.0/alerts?status=active</pre><br />To show all inactive alerts, use:<pre>GET http://198.51.100.0/alerts?status=inactive</pre><br />In both examples above, the Conductor IP address is 198.51.100.0. |
| origin |  Integer | Filter for alerts that originate from a specific node. See [Where Alerts Come From and Where They Apply](#monitoring-query-alerts-messages-get-a-list-of-alerts-http-request-response-url-where-alerts-come-from) for details.<pre>GET http://198.51.100.0/alerts?origin=2</pre><br />Use the IP address of the Conductor node and the ID of the node as assigned by Conductor Live. In the example above, the Conductor IP address is 198.51.100.0 and the originating node ID is 2. To determine the node ID, send a [GET request](set-up-nodes-get-list-of-nodes.md). |
| node |  Integer | Filter for alerts that apply to a specific node. See [Where Alerts Come From and Where They Apply](#monitoring-query-alerts-messages-get-a-list-of-alerts-http-request-response-url-where-alerts-come-from) for details. Typically, you do not filter for both origin and node.<pre>GET http://198.51.100.0/alerts?node=2</pre><br />In the example above, the Conductor Live IP address is 198.51.100.0 and the originating node ID is 2. To determine the node ID, send a [GET request](set-up-nodes-get-list-of-nodes.md). |
| channel |  Integer | Filter for alerts that apply to a specific channel.<pre>GET http://198.51.100.0/alerts?channel=4</pre><br />In the example above, the Conductor Live IP address is 198.51.100.0 and the ID of the channel the alert is coming from is 4. To determine the channel ID, send a GET request as shown in [this example](get-list-of-channels.md#get-list-of-channels-example).<br />To get all alerts originating from a specific node that apply to a specific channel, you can filter for origin and channel together:<pre>GET http://198.51.100.0/alerts?channel=4&origin=2</pre> |
| mpts |  Integer | Filter for alerts that apply to a specific Multi-Program Transport Stream (MPTS) output. <pre>GET http://198.51.100.0/alerts?mpts=3</pre><br />Enter the ID of the MPTS output as assigned by Conductor Live.<br />You can filter for both an origin and an MPTS. |
| type |  String | Filter for alerts by alert type: CpuAlert, NodeStatusAlert, DiskAlert, InputAlert, and so on. All alerts types that appear in the user interface under Status>Alerts are valid type values.<pre>GET http://198.51.100.0/alerts?type=DiskAlert</pre><br />In the example above, the Conductor Live IP address is 198.51.100.0. |
| code |  String | Filter for only those alerts with the specified alert codes. Enter a list of 1 or more numeric codes. All alerts codes that appear in the user interface under Status>Alerts are valid code values.<pre>GET http://198.51.100.0/alerts?code=4002</pre><br />In the example above, the Conductor Live IP address is 198.51.100.0 and 4002 is the code for DiskAlert. |

#### Where Alerts Come From and Where They Apply
<a name="monitoring-query-alerts-messages-get-a-list-of-alerts-http-request-response-url-where-alerts-come-from"></a>

An alert may originate with an Conductor Live node or it may originate with a worker node and get pushed to Conductor Live. In both cases, the alert may relate to a node and/or a channel or MPTS output.

For example, if a channel on Live node live-01 fails, then an alert occurs. The alert originates from Live node live-01 and applies to node live-01 and channel Channel\_A.

Or a node live-01 may fail, resulting in an alert. In this case, the alert originates from the Conductor node (not from live-01), but it applies to node live-01.

### Call Header
<a name="monitoring-query-alerts-messages-get-a-list-of-alerts-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md) .

### Response
<a name="monitoring-query-alerts-messages-get-a-list-of-alerts-http-request-response-response"></a>

The response is XML content consisting of one **alerts** element that holds the following:
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Zero or more `alert` elements each containing several elements from this table.

| Element | Value | Description |
| --- | --- | --- |
| alertable\_id | Integer | The unique ID for the entity in alertable\_type. This is the ID that is included in the response of a GET. For example, GET Node includes the ID that uniquely identifies the node. |
| alertable\_type | String | The entity that the alert is associated with: Node, Channel, MPTS. |
| eme\_id | Integer | An internal ID. |
| id | Integer | A unique ID for this alert, assigned by Conductor Live. |
| last\_set | Time | The time that the alert was last set (either when it appeared for the first time or when it changed back to set after previously being cleared).<br />Some alerts are set and cleared repeatedly, so the time for these alerts may change. <br />Some are not set and cleared repeatedly, so the time will never change. |
| message | String | A longer description. |
| name | String | A short description. |
| node\_id | Integer | The ID that identifies the same piece of data as the origin filter in the request; see [GET Alerts: Get a List of Alerts](#monitoring-query-alerts-messages-get-a-list-of-alerts). |
| notes | String | A section that shows whether the web interface user has added a note to the alert (Status > Notifications): it appears here. |
| output\_id | Integer | The unique ID for the entity in output\_type.  |
| output\_type | String | The type of the output in the channel (event) that this alert specifically applies to. Otherwise, null. |
| quiet | Boolean | The status of suppression of the alert on the worker node. True means the alert has been suppressed on the worker node. False means it has not been suppressed. |
| remote\_id | Integer | The ID of the entity (channel or MPTS) as assigned by the worker node that is running this entity. The ID assigned by Conductor Live may be different from the ID assigned by the worker node.  |
| set | Boolean | The status of whether the alert has been set. True means it is set. False means it has been cleared or has never been set. |
| threshold |  | The indicator which applies only to alerts that have a threshold assigned to the alerting context. For example, this can be the CPU Alert, which specifies when CPU usage is above a given percentage.<br />If the alert is the type of alert that gets set repeatedly, each time the threshold changes, then this number shows the minimum threshold. The alert does not get set for this first time until this threshold is met.  |
| type | String  | The type of the alert. |
| updated\_at | Time | The last time this alert was updated. |

## Examples
<a name="monitoring-query-alerts-messages-get-a-list-of-alerts-example"></a>

**Example 1**

This example requests all active alerts from node 2.

```
GET http://10.4.138.230/alerts?channel=5&status=active
---------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<alerts href="/alerts" product="AWS Elemental Conductor Live" version="3.2.0.40946" type="array">
  <alert>
    <id type="integer">18</id>
    <type>InputAlert</type>
    <name>Live Event 125  Alert 5302</name>
    <message>Stopped receiving network data on [udp://239.255.10.7:5001]</message>
    <last_set type="datetime">2016-06-01T15:52:17-07:00</last_set>
    <quiet type="boolean">false</quiet>
    <set type="boolean">true</set>
    <threshold nil="true"/>
    <code type="integer">5302</code>
    <notes nil="true"/>
    <alertable_type>Elemental::Live247::Channel</alertable_type>
    <alertable_id type="integer">3</alertable_id>
    <node_id type="integer">2</node_id>
    <updated_at type="datetime">2016-06-01T15:52:18-07:00</updated_at>
    <readable_type>Channel</readable_type>
    <product_type nil="true"/>
  </alert>
  <alert>
    <id type="integer">16</id>
    <type>InputAlert</type>
    <name>Live Event 125  Alert 5201</name>
    <message>[188] Video not detected: Check input signal</message>
    <last_set type="datetime">2016-06-01T15:52:21-07:00</last_set>
    <quiet type="boolean">false</quiet>
    <set type="boolean">true</set>
    <threshold nil="true"/>
    <code type="integer">5201</code>
    <notes nil="true"/>
    <alertable_type>Elemental::Live247::Channel</alertable_type>
    <alertable_id type="integer">3</alertable_id>
    <node_id type="integer">2</node_id>
    <updated_at type="datetime">2016-06-01T15:52:21-07:00</updated_at>
    <readable_type>Channel</readable_type>
    <product_type nil="true"/>
  </alert>
</alerts>
```

**Example 2**

The following example requests all *active input *alerts on *channel 5* but limits the number to *10 alerts per page*.

```
GET http://10.4.138.230/alerts?channel=5&type=InputAlert&status=active&per_page=10
```
