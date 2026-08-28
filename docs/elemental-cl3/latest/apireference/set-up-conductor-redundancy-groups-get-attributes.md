---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-conductor-redundancy-groups-get-attributes.html
---

# GET: Get the Attributes of the Conductor Redundancy Group
<a name="set-up-conductor-redundancy-groups-get-attributes"></a>

Get a list of all Conductor redundancy groups, including the attributes of each group. There is only ever one Conductor redundancy group, so the list contains only one item. However, you cannot assume its ID is always going to be 1: if you create a Conductor redundancy group and then delete it and then create another one, the ID of the new group will be 2.

There is only one Conductor redundancy group, so there is no difference between GET and GET List; only GET is described in this guide.

## HTTP Request and Response
<a name="set-up-conductor-redundancy-groups-get-attributes-http-request-response"></a>

### Request URL
<a name="set-up-conductor-redundancy-groups-get-attributes-http-request-response-url"></a>

```
GET http://<Conductor IP address>/conductor_redundancy_groups
```

### Call Header
<a name="set-up-conductor-redundancy-groups-get-attributes-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-conductor-redundancy-groups-get-attributes-http-request-response-response"></a>

The response is XML content consisting of one `conductor_redundancy_groups` element with the following.
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Zero or one `conductor_redundancy_group ` elements. Each element contains several elements.

| Element | Value | Description |
| --- | --- | --- |
| id | Integer | The ID for this Conductor redundancy group. |
| vip | String | A valid IPv4 address. This address is the “cluster ID” for the two Conductor nodes. |
| vrid | Integer | The Virtual Router ID, a number from 1-254. |
| enabled | Boolean | True if Conductor redundancy is enabled on the cluster.<br />False if it is not enabled.<br />Read only. |
| name | String | The name of the group. |
| product\_name | String | This setting is always “conductor\_live.”<br />Read -only. |

## Example
<a name="set-up-conductor-redundancy-groups-get-attributes-example"></a>

The response to this request shows one Conductor redundancy group with the ID 1.

```
GET http://198.51.100.0/conductor_redundancy_groups
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<conductor_redundancy_groups href="/conductor_redundancy_groups" product="AWS Elemental Conductor Live" version="3.3.43776">
  <conductor_redundancy_group>
    <id type="integer">2</id>
    <vip>10.10.10.111</vip>
    <vrid type="integer">13</vrid>
    <enabled type="boolean">false</enabled>
    <name>ConductorRedundancy</name>
    <product_name>conductor_live</product_name>
  </conductor_redundancy_group>
</conductor_redundancy_groups>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
