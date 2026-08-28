---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-create.html
---

# POST: Create a Redundancy Group
<a name="set-up-redundancy-groups-create"></a>

Create a new redundancy group for AWS Elemental Live or AWS Elemental Statmux redundancy group with the specified attributes.

## HTTP Request and Response
<a name="set-up-redundancy-groups-create-http-request-response"></a>

### Request URL
<a name="set-up-redundancy-groups-create-http-request-response-url"></a>

```
POST http://<Conductor IP address>/redundancy_groups
```

### Call Header
<a name="set-up-redundancy-groups-create-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="set-up-redundancy-groups-create-http-request-response-request-body"></a>

The request contains XML content consisting of one `redundancy_group` element with the following elements.

| Element | Value | Description |
| --- | --- | --- |
| name | String | A name you assign. This must be unique in the cluster. |
| product\_name | String | A name which must specify “live” if nodes in this group are running AWS Elemental Live; specify “statmux” for nodes running AWS Elemental Statmux.<br />**This value is case-sensitive and requires all letters to be in lower case.**<br />All the nodes that you add to the redundancy group must have the same product\_name.  |

### Response
<a name="set-up-redundancy-groups-create-http-request-response-response"></a>

The response repeats back the data that you posted with the addition of:
+ id: The newly assigned ID for the redundancy group.

The response is identical to the response to a GET Redundancy Group. For an example, see [GET List: Get a List of Redundancy Groups](set-up-redundancy-groups-get-a-list.md).

## Example
<a name="set-up-redundancy-groups-create-example"></a>

### Request
<a name="set-up-redundancy-groups-create-example-request"></a>

This request creates one redundancy group named “backup” with its product set as “live” and its product version set at “2.7.0.12345.”

```
POST http://198.51.100.0/redundancy_groups
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<redundancy_group>
  <name>backup</name>
  <product_name>live</product_name>
</redundancy_group>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
