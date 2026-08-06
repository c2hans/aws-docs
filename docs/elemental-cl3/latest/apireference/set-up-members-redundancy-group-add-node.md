---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-members-redundancy-group-add-node.html
---

# POST: Add a Node to a Redundancy Group
<a name="set-up-members-redundancy-group-add-node"></a>

Add a node to the specified redundancy group and assign the node’s role as active or backup. The redundancy group must already exist.

## HTTP Request and Response
<a name="set-up-members-redundancy-group-add-node-http-request-response"></a>

### Request URL
<a name="set-up-members-redundancy-group-add-node-http-request-response-url"></a>

```
POST http://<Conductor IP address>/redundancy_groups/<ID of redundancy group>/members
```

### Call Header
<a name="set-up-members-redundancy-group-add-node-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="set-up-members-redundancy-group-add-node-http-request-response-request-body"></a>

The request contains XML content consisting of one `redundancy_groups` element with the following.
+ One or more `redundancy_group_member` elements, each containing the following elements.

| Element | Value | Description |
| --- | --- | --- |
| node\_id | Integer | The ID of the node to add. Use GET Node List to get a list that shows the ID of each node.<br />A node can belong to only one redundancy group.<br />If the node’s role will be “backup,” the node must have no channels associated with it. (You get a “Node is not reservable” error.)<br />To verify its channels, do a GET Channel List and verify if this node is listed as associated with a channel; if it is, do a PUT Channel on that channel so that the channel uses a different node. |
| role | String | The initial role of the node in the redundancy group: “active” or “backup.”+  A backup node automatically switches to "active" if it is selected as a failover node. It then remains active until you change its role (perhaps by doing PUT Member). <br />+  An active node never automatically changes its role.   |

### Response
<a name="set-up-members-redundancy-group-add-node-http-request-response-response"></a>

The response repeats back the data that you posted with the addition of:
+ id: The newly assigned ID for the member.

The response is identical to the response to a GET Redundancy Member. See below for an example.

## Example
<a name="set-up-members-redundancy-group-add-node-example"></a>

### Request
<a name="set-up-members-redundancy-group-add-node-example-request"></a>

Add the node with the ID 2 to the redundancy group that has the ID 3.

```
POST http://198.51.100.0/redundancy_groups/3/members
--------------------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
--------------------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<redundancy_group_member>
<node_id>2</node_id>
<role>active</role>
<redundancy_group_position>1</redundancy_group_position>
</redundancy_group_member>
```

### Response
<a name="set-up-members-redundancy-group-add-node-example-response"></a>

The response shows the “redundancy group member” data and the standard node data that was applied to this node. Note that the node has the member ID of “3” (its ID in the redundancy group) but has the node ID of “2” (its ID in the cluster). For details, see [GET List: Get a List of Redundancy Group Members](set-up-redundancy-groups-get-list-of-members.md).

```
<?xml version="1.0" encoding="UTF-8"?>
<redundancy_group_member href="/redundancy_groups/3/members" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
  <id type="integer">3</id>
  <role>active</role>
  <node>
    <id type="integer">2</id>
    <hostname>live_3</hostname>
    <ip_addr>10.4.138.233</ip_addr>
    <product_name>Live</product_name>
    <status>online</status>
    <version>2.9.2.40404</version>
    <channels type="integer">3</channels>
    <inflight_channels type="integer">0</inflight_channels>
    <mptses type="integer">1</mptses>
    <active_alerts type="integer">0</active_alerts>
    <recent_error_messages type="integer">0</recent_error_messages>
  </node>
</redundancy_group_member>
```
