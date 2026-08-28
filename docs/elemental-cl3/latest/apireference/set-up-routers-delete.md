---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-routers-delete.html
---

# DELETE: Delete a Router
<a name="set-up-routers-delete"></a>

Deletes the specified router (identified by its internal router ID) and the associated inputs and outputs. To get the internal router ID of a specific router, see [GET: Get Router Attributes](set-up-routers-get-router-attributes.md).

## HTTP Request and Response
<a name="set-up-routers-delete-http-request-response"></a>

### Request URL
<a name="set-up-routers-delete-http-request-response-url"></a>

```
DELETE http://<Conductor IP address>/routers/<ID of router>
```

### Call Header
<a name="set-up-routers-delete-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

## Example
<a name="set-up-routers-delete-example"></a>

This request deletes the router with the ID 2.

```
DELETE http://198.51.100.0/routers/2
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
