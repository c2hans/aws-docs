---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-outputs-delete.html
---

# DELETE: Delete a Router Output
<a name="set-up-router-outputs-delete"></a>

Delete the specified output on the specified router.

## HTTP Request and Response
<a name="set-up-router-outputs-delete-http-request-response"></a>

### Request URL
<a name="set-up-router-outputs-delete-http-request-response-url"></a>

```
DELETE http://<Conductor IP address>/routers/<ID of router>/outputs/<ID of output>
```

### Call Header
<a name="set-up-router-outputs-delete-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

## Example
<a name="set-up-router-outputs-delete-example"></a>

This request deletes the output with the ID 1 from the router with the ID 2.

```
DELETE http://198.51.100.0/routers/2/outputs/1
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
