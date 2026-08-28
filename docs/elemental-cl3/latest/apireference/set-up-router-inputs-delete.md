---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-inputs-delete.html
---

# DELETE: Delete a Router Input
<a name="set-up-router-inputs-delete"></a>

Delete the specified input on the specified router. To get the ID of the input, use GET Router List and look for the <id> element (not the <input\_number> element\!).

## HTTP Request and Response
<a name="set-up-router-inputs-delete-http-request-response"></a>

### Request URL
<a name="set-up-router-inputs-delete-http-request-response-url"></a>

```
DELETE http://<Conductor IP address>/routers/<ID of router>/inputs/<ID of input>
```

### Call Header
<a name="set-up-router-inputs-delete-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`.

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

## Example
<a name="set-up-router-inputs-delete-example"></a>

This request deletes the input with the ID 1 from the router with the ID 2.

```
DELETE http://198.51.100.0/routers/2/inputs/1
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
