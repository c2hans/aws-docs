---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-redundancy-groups-modify.html
---

# PUT: Modify a Redundancy Group
<a name="set-up-redundancy-groups-modify"></a>

Change the name of the specified redundancy group.

## HTTP Request and Response
<a name="set-up-redundancy-groups-modify-http-request-response"></a>

### Request URL
<a name="set-up-redundancy-groups-modify-http-request-response-url"></a>

```
PUT http://<Conductor IP address>/redundancy_groups/<ID of redundancy group>
```

### Call Header
<a name="set-up-redundancy-groups-modify-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="set-up-redundancy-groups-modify-http-request-response-request-body"></a>

The body contains only the elements to change. For the format, see [POST: Create a Redundancy Group](set-up-redundancy-groups-create.md).

## Example
<a name="set-up-redundancy-groups-modify-example"></a>

This request changes the name of the redundancy group with the ID 1. It changes the name to “backup\_nodes.”

```
PUT http://198.51.100.0/redundancy_groups/1
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<redundancy_group>
<name>backup_nodes</name>
</redundancy_group>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
