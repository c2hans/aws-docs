---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-members-conductor-redundancy-group-get-attributes.html
---

# GET: Get the Attributes of a Conductor Redundancy Group Member
<a name="set-up-members-conductor-redundancy-group-get-attributes"></a>

Get the attributes of the specified member in the specified Conductor redundancy group.

## HTTP Request and Response
<a name="set-up-members-conductor-redundancy-group-get-attributes-http-request-response"></a>

### Request URL
<a name="set-up-members-conductor-redundancy-group-get-attributes-http-request-response-url"></a>

```
GET http://<Conductor IP address>/conductor_redundancy_groups/<ID of Conductor redundancy group>/members/<ID of member node>
```

### Call Header
<a name="set-up-members-conductor-redundancy-group-get-attributes-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-members-conductor-redundancy-group-get-attributes-http-request-response-response"></a>

The response is XML content consisting of one `conductor_redundancy_group` element with the same elements as the response for GET Member List above.

## Example
<a name="set-up-members-conductor-redundancy-group-get-attributes-example"></a>

This request gets the attributes for the Conductor redundancy group that has the ID 1.

```
GET http://198.51.100.0/conductor_redundancy_groups/1/members/1
--------------------------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<conductor_redundancy_group_member href="/conductor_redundancy_groups/1/members" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
  <id>1</id>
  <rank>13</rank>
  <node>
    .
    .
    .
  </node>
  </conductor_redundancy_group_member>
```
