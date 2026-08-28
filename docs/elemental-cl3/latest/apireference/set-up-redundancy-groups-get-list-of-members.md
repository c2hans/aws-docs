---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-get-list-of-members.html
---

# GET List: Get a List of Redundancy Group Members
<a name="set-up-redundancy-groups-get-list-of-members"></a>

Get the list of the nodes that are members of the specified redundancy group.

## HTTP Request and Response
<a name="set-up-redundancy-groups-get-list-of-members-http-request-response"></a>

### Request URL
<a name="set-up-redundancy-groups-get-list-of-members-http-request-response-url"></a>

```
GET http://<Conductor IP address>/redundancy_groups/<ID of redundancy group>/members
```

### Call Header
<a name="set-up-redundancy-groups-get-list-of-members-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-redundancy-groups-get-list-of-members-http-request-response-response"></a>

The response is XML content consisting of one `redundancy_group_members` element with the following.
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Zero or more `redundancy_group_member` elements, one for each group found. Each `redundancy_group_member` element contains several elements:

| Element | Value | Description |
| --- | --- | --- |
| id | Integer | The member ID for this node.   Within <redundancy\_group\_members>, <id> is the ID for this node as identified inside the redundancy group, assigned with the node that was added to the redundancy group. Within <node>, <id> is the unique ID for this node as identified in all of Conductor Live, assigned when the node was added to the cluster.  |
| role | String | The current role of the node in the redundancy group: “active” or “backup.” |
| node | Object | The node information for this member of the redundancy group; see [Setting up Nodes](set-up-nodes.md). |

## Example
<a name="set-up-redundancy-groups-get-list-of-members-example"></a>

The response shows that the redundancy group with the ID 1 has two members–one backup and one active.

```
GET http://198.51.100.0/redundancy_groups/1/members
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<redundancy_group_members href="/redundancy_groups/1/members" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
   <redundancy_group_member>
    <id type="integer">5</id>
    <role>active</role>
    <node>
      <id type="integer">2</id>
      <hostname>live_1</hostname>
      <ip_addr>10.4.138.233</ip_addr>
      <product_name>Live</product_name>
      <status>online</status>
      <version>2.9.2.40404</version>
      <channels type="integer">0</channels>
      <inflight_channels type="integer">0</inflight_channels>
      <mptses type="integer">1</mptses>
      <active_alerts type="integer">0</active_alerts>
      <recent_error_messages type="integer">0</recent_error_messages>
    </node>
  </redundancy_group_member>
  <redundancy_group_member>
    <id type="integer">6</id>
    <role>backup</role>
    <node>
      <id type="integer">3</id>
      <hostname>live_2</hostname>
      <ip_addr>10.4.138.234</ip_addr>
      <product_name>Live</product_name>
      <status>online</status>
      <version>2.9.2.40404</version>
      <channels type="integer">0</channels>
      <inflight_channels type="integer">0</inflight_channels>
      <mptses type="integer">0</mptses>
      <active_alerts type="integer">0</active_alerts>
      <recent_error_messages type="integer">0</recent_error_messages>
    </node>
  </redundancy_group_member>
</redundancy_group_members>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
