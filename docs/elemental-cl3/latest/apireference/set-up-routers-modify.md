---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-routers-modify.html
---

# PUT: Modify a Router
<a name="set-up-routers-modify"></a>

Modify the attributes of the specified router. You cannot use this command to modify the inputs or outputs of the router; to do that, use PUT Router Input and PUT Router Output.

## HTTP Request and Response
<a name="set-up-routers-modify-http-request-response"></a>

### Request URL
<a name="set-up-routers-modify-http-request-response-url"></a>

```
PUT http://<Conductor IP address>/routers/<ID of router>
```

### Call Header
<a name="set-up-routers-modify-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="set-up-routers-modify-http-request-response-request-body"></a>

The request body contains only the elements to change. For a list of available elements, see [POST: Create a Router](set-up-routers-create.md).

## Example
<a name="set-up-routers-modify-example"></a>

This request changes the router with the ID 3. It changes its max\_inputs to 8.

```
PUT http://198.51.100.0/routers/3
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
----------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<router>
  <router_type>blackmagic_videohub</router_type>
  <max_inputs>8</max_inputs>
</router>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
