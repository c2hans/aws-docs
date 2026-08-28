---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-get-attributes-of-members.html
---

# GET: Get the Attributes of a Redundancy Group Member
<a name="set-up-redundancy-groups-get-attributes-of-members"></a>

Get the attributes of the specified member in the specified redundancy group.

## HTTP Request and Response
<a name="set-up-redundancy-groups-get-attributes-of-members-http-request-response"></a>

### Request URL
<a name="set-up-redundancy-groups-get-attributes-of-members-http-request-response-url"></a>

```
GET http://<Conductor IP address>/redundancy_groups/<ID of redundancy group>/members/<ID of member node>
```

### Call Header
<a name="set-up-redundancy-groups-get-attributes-of-members-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-redundancy-groups-get-attributes-of-members-http-request-response-response"></a>

The response is XML content consisting of one `redundancy_group` element containing the same elements as the response for [GET List: Get a List of Redundancy Groups](set-up-redundancy-groups-get-a-list.md).

## Example
<a name="set-up-redundancy-groups-get-attributes-of-members-example"></a>

This request gets the attributes for the redundancy group member that has the ID 3 within the redundancy group and that belongs to the redundancy group with the ID 1. The node’s ID independent of redundancy group is 2.

```
GET http://198.51.100.0/redundancy_groups/1/members/3
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<redundancy_group_member href="/redundancy_groups/1/members/3" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
  <id type="integer">3</id>
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
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
