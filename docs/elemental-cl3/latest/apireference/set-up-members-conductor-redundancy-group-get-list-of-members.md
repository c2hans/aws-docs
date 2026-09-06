---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-members-conductor-redundancy-group-get-list-of-members.html
---

# GET List: Get a List of Conductor Redundancy Group Members
<a name="set-up-members-conductor-redundancy-group-get-list-of-members"></a>

Get the list of the nodes that are members of the specified Conductor redundancy group.

## HTTP Request and Response
<a name="set-up-members-conductor-redundancy-group-get-list-of-members-http-request-response"></a>

### Request URL
<a name="set-up-members-conductor-redundancy-group-get-list-of-members-http-request-response-url"></a>

```
GET http://<Conductor IP address>/conductor_redundancy_groups/<ID of Conductor redundancy group>/members
```

### Call Header
<a name="set-up-members-conductor-redundancy-group-get-list-of-members-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-members-conductor-redundancy-group-get-list-of-members-http-request-response-response"></a>

The response is XML content consisting of one `conductor_redundancy_group_members` element with the following.
+ An HREF attribute that specifies the product and version installed on the Conductor node.
+ Zero, one or two `conductor_redundancy_group_member` elements, one for each Conductor node found. Each element contains several elements.

| Element | Value | Description |
| --- | --- | --- |
| id | Integer | The member ID for this node, an ID for this node that is unique within the Conductor redundancy group. |
| rank | Integer | Each node in the Conductor redundancy group is assigned a random number. This number is used to display nodes on the Conductor web interface. |
| node | Object | The node information for this member of the Conductor redundancy group; see [POST: Add a Node to the Cluster](set-up-nodes-add-note-to-cluster.md). |

## Example
<a name="set-up-members-conductor-redundancy-group-get-list-of-members-example"></a>

The response to this request shows that the Conductor redundancy group with the ID 1 has two members – one node that is the backup and one that is active.

```
GET http://198.51.100.0/conductor_redundancy_groups/1/members
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<conductor_redundancy_group_members href="/conductor_redundancy_groups/1/members" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
  <conductor_redundancy_group_member>
    <id>2</id>
    <rank>153</rank>
    <node>
      <id>5</id>
      <hostname>elae-12345678</hostname>
      <ip_addr>10.4.136.90</ip_addr>
      <status>online</status>
      <product_name>AWS Elemental Conductor Live</product_name>
      <version>3.3.nnnnn</version>
      <channels>0</channels>
      <inflight_channels>0</inflight_channels>
      <mptses>0</mptses>
      <active_alerts>0</active_alerts>
      <recent_error_messages>0</recent_error_messages>
      <redundancy_group nil=’true’>
      <authentication>
        <user_id>1</user_id>
      </authentication>
    </node>
  </conductor_redundancy_group_member>
  <conductor_redundancy_group_member>
    <id>8</id>
    <node>
      <id>2</id>
      <hostname>elae_33445566</hostname>
      <ip_addr>10.4.136.91</ip_addr>
      <status>online</status>
      <product_name>Live</product_name>
      <version>2.7.0.123456</version>
      .
      .
      .
    </node>
  </conductor_redundancy_group_member>
</conductor_redundancy_group_members>
```
