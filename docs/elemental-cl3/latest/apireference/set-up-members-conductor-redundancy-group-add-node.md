---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-members-conductor-redundancy-group-add-node.html
---

# POST: Add a Node to a Conductor Redundancy Groups
<a name="set-up-members-conductor-redundancy-group-add-node"></a>

Add a Conductor node to the specified Conductor redundancy group. When setting up a Conductor redundancy group, you must add exactly two nodes.

## HTTP Request and Response
<a name="set-up-members-conductor-redundancy-group-add-node-http-request-response"></a>

### Request URL
<a name="set-up-members-conductor-redundancy-group-add-node-http-request-response-url"></a>

```
POST http://<Conductor IP address>/conductor_redundancy_groups/<ID of Conductor redundancy group>/members
```

### Call Header
<a name="set-up-members-conductor-redundancy-group-add-node-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="set-up-members-conductor-redundancy-group-add-node-http-request-response-request-body"></a>

The response contains XML content consisting of the following.
+ One `conductor_redundancy_groups` element that contains:
  + One or two `conductor_redundancy_group_member` elements with the following elements.

| Element | Value | Description |
| --- | --- | --- |
| node\_id |   | ID of the Conductor node |

### Response
<a name="set-up-members-conductor-redundancy-group-add-node-http-request-response-response"></a>

The response repeats back the data that you posted with the addition of the following.
+ id: The newly assigned ID for the member.

## Example
<a name="set-up-members-conductor-redundancy-group-add-node-example"></a>

### Request
<a name="set-up-members-conductor-redundancy-group-add-node-example-request"></a>

Add the node with the ID 2 to the Conductor redundancy group. In this example, the Conductor redundancy group has the ID 1.

```
POST http://198.51.100.0/conductor_redundancy_groups/1/members
-------------------------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
-------------------------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<conductor_redundancy_group_member>
<node_id>2</node_id>
</conductor_redundancy_group_member>
```

### Response
<a name="set-up-members-conductor-redundancy-group-add-node-example-response"></a>

The response shows the “Conductor redundancy group member” data and the standard node data that was applied to this node. Note that the node has the member ID of 3 (its ID in the Conductor redundancy group) but has the node ID of 2 (its ID in the cluster). For details, see [GET List: Get a List of Redundancy Group Members](set-up-redundancy-groups-get-list-of-members.md).

```
<?xml version="1.0" encoding="UTF-8"?>
<conductor_redundancy_group_member href="/conductor_redundancy_groups/3/members" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
  <id>3</id>
  <node>
    <id>2</id>
    <hostname>elae-12345678</hostname>
    <ip_addr>10.4.136.92</ip_addr>
    <status>online</status>
    <product_name>Live</product_name>
    <version>2.7.0.67890</version>
    <channels>0</channels>
  </node>
</conductor_redundancy_group_member>
```
