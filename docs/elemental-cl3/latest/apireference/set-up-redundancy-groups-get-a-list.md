---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-get-a-list.html
---

# GET List: Get a List of Redundancy Groups
<a name="set-up-redundancy-groups-get-a-list"></a>

Get a list of all redundancy groups, including the attributes of each group.

## HTTP Request and Response
<a name="set-up-redundancy-groups-get-a-list-http-request-response"></a>

### Request URL
<a name="set-up-redundancy-groups-get-a-list-http-request-response-url"></a>

```
GET http://<Conductor IP address>/redundancy_groups
```

### Call Header
<a name="set-up-redundancy-groups-get-a-list-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-redundancy-groups-get-a-list-http-request-response-response"></a>

The response is XML content consisting of one `redundancy_groups` element with the following .
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Zero or more `redundancy_group ` elements, one for each group found. Each `redundancy_group ` element contains several elements.

| Element | Value | Description |
| --- | --- | --- |
| id | Integer | The ID of this redundancy group. <br />  |
| name | String | The name you assigned to the group. |
| product\_name | String | The software type running on the nodes of the redundancy group. Values are “live” or “statmux.” |

## Example
<a name="set-up-redundancy-groups-get-a-list-example"></a>

The response to this request shows two redundancy groups named “2.5 nodes” (intended for AWS Elemental Live nodes running version 2.5.x) and “2.4 nodes” (intended for AWS Elemental Live nodes running version 2.4.x).

```
GET http://198.51.100.0/redundancy_groups
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<redundancy_groups href="/redundancy_groups" product="AWS Elemental Conductor Live" version="3.3.43776">
  <redundancy_group>
    <id>1</id>
    <name>2.5 nodes</name>
    <product_name>live</product_name>
  </redundancy_group>
    <id>3</id>
    <name>2.4 nodes</name>
    <product_name>live</product_name>
  </redundancy_group>
</redundancy_groups>
```
