---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-nodes-get-list-of-nodes.html
---

# GET List: Get a List of Nodes in the Cluster
<a name="set-up-nodes-get-list-of-nodes"></a>

Get the list of the nodes in the cluster, including the Conductor Live node and the individual AWS Elemental Live and AWS Elemental Statmux nodes.

## HTTP Request and Response
<a name="set-up-nodes-get-list-of-nodes-http-request-response"></a>

### Request URL
<a name="set-up-nodes-get-list-of-nodes-http-request-response-url"></a>

```
GET http://<Conductor IP address>/nodes
```

### Call Header
<a name="set-up-nodes-get-list-of-nodes-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-nodes-get-list-of-nodes-http-request-response-response"></a>

The response is XML content consisting of one `nodes` element that contains:
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Zero or more `node` elements, one for each node found (Conductor Live, AWS Elemental Live, and AWS Elemental Statmux). Each `node ` element contains several elements.

| Element | Value | Description |
| --- | --- | --- |
| id | Integer | The unique ID of the node, assigned by the system when the node is created. |
| hostname | String | The host name of the node, assigned via a network command during setup of this appliance. Note that you do *not* assign this name when adding the node to the cluster.<br />For example, “ecle-12345678” is a typical name for an Conductor Live node. “elae-12345678” is a typical name for an AWS Elemental Live node. |
| ip\_addr | String | The IP address of the node on the network. |
| status | String | The current status of the node: online, offline, failed, unknown. |
| product\_name | String | The product name installed on this node. Always specifies:+  “Conductor Live” for the Conductor Live node. <br />+ “Live” for an AWS Elemental Live node. <br />+ “Statmux” for an AWS Elemental Statmux node.  |
| version | String | The version of the product name installed on this node. |
| channels | Integer | The number of channels that are associated with this node.<br />Always “0” for the Conductor Live node.  |
| inflight\_channels | Integer | Number of channels currently in use for encoding. Always 0 for a Conductor node, 0 or a number for a worker node. |
| mptses | Integer | Number of MPTS outputs associated with this node. Always 0 for a Conductor node, 0 or a number for a worker node. |
| active\_alerts | Integer | Number of alerts that are associated with that node and that are active (they have not been automatically cleared by the system). |
| recent\_error\_messages | Integer | Number of error messages that are associated with that node and that have occurred in the last 168 hours (one week). Does not include content messages, audit messages or warning messages. |
| redundancy\_group |   | The ID assigned to the redundancy group, the name of the redundancy group, and the name of the product running on the worker nodes (values are “live” and “statmux”).<br />If this node is a worker node and belongs to a redundancy group, contains the elements for that group. See [GET List: Get a List of Conductor Redundancy Group Members](set-up-members-conductor-redundancy-group-get-list-of-members.md).<br />If this node is a Conductor node, nil. |
| authentication | Integer | If user authentication is set up on this node, specifies the ID of the “API user” that you created when you set up for authentication, as described in the AWS Elemental Conductor Live Configuration Guide. <br />In effect, a value here tells you that user authentication is enabled on this node.  |

## Example
<a name="set-up-nodes-get-list-of-nodes-example"></a>

The response to this request specifies that there are three nodes set up in the cluster: one Conductor Live node (as indicated by the product\_name) and two AWS Elemental Live nodes. All the nodes have user authentication enabled. In this example, the Conductor Live has the ID 1, but you cannot rely on this node always being assigned that ID.

```
GET http://198.51.100.0/nodes
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<nodes href="/nodes" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
  <node>
    <id>1</id>
    <hostname>ecle-12345678</hostname>
    <ip_addr>198.51.100.0</ip_addr>
    <status>active</status>
    <product_name>AWS Elemental Conductor Live</product_name>
    <version>3.3.nnnnn</version>
    <channels>0</channels>
    <inflight_channels type="integer">0</inflight_channels>
    <mptses type="integer">0</mptses>
    <active_alerts type="integer">0</active_alerts>
    <recent_error_messages type="integer">0</recent_error_messages>
    <redundancy_group nil="true"/>
    <authentication>
      <user_id type="integer">1</user_id>
    </authentication>
  </node>
  <node>
    <id>2</id>
    <hostname>ecle-12345678</hostname>
    <ip_addr>10.4.136.91</ip_addr>
    <status>active</status>
    <product_name>Live</product_name>
    <version>2.7.0.67890</version>
    <channels>4</channels>
    <inflight_channels type="integer">1</inflight_channels>
    <mptses type="integer">3</mptses>
    <active_alerts type="integer">2</active_alerts>
    <recent_error_messages type="integer">0</recent_error_messages>
    <redundancy_group nil="true"/>
    <authentication>
      <user_id type="integer">1</user_id>
    </authentication>
  </node>
  <node>
    <id>3</id>
    <hostname>ecle-22334455</hostname>
    <ip_addr>10.4.136.92</ip_addr>
    <status>active</status>
    <product_name>Live</product_name>
    <version>2.7.0.67890</version>
    <channels>3</channels>
    <inflight_channels type="integer">0</inflight_channels>
    <mptses type="integer">0</mptses>
    <active_alerts type="integer">0</active_alerts>
    <recent_error_messages type="integer">0</recent_error_messages>
    <redundancy_group nil="true"/>
    <authentication>
      <user_id type="integer">1</user_id>
    </authentication>
  </node>
</nodes>
```
