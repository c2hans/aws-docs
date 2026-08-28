---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-get-attributes.html
---

# GET: Get Attributes of a Redundancy Group
<a name="set-up-redundancy-groups-get-attributes"></a>

Get the attributes of the specified redundancy group.

## HTTP Request and Response
<a name="set-up-redundancy-groups-get-attributes-http-request-response"></a>

### Request URL
<a name="set-up-redundancy-groups-get-attributes-http-request-response-url"></a>

```
GET http://<Conductor IP address>/redundancy_groups/<ID of redundancy group>
```

### Call Header
<a name="set-up-redundancy-groups-get-attributes-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-redundancy-groups-get-attributes-http-request-response-response"></a>

The response is XML content consisting of one `redundancy_group` element, with the same elements as the response for [GET List: Get a List of Redundancy Groups](set-up-redundancy-groups-get-a-list.md).

## Example
<a name="set-up-redundancy-groups-get-attributes-example"></a>

This response shows the attributes for the group that has the ID 1.

```
GET http://198.51.100.0/redundancy_groups/1
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<redundancy_group>
  <id>1</id>
  <name>2.5 nodes</name>
  <product_name>live</product_name>
</redundancy_group>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
