---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-delete-mpts-output.html
---

# DELETE: Delete an MPTS Output
<a name="working-with-mpts-delete-mpts-output"></a>

## HTTP Request and Response
<a name="working-with-mpts-delete-mpts-output-http-request-response"></a>

### Request URL
<a name="working-with-mpts-delete-mpts-output-http-request-response-url"></a>

Delete the MPTS output that has the specified ID. To get the ID of a specific MPTS output, see [GET List: Get a List of MPTS Outputs](working-with-mpts-get-list-of-mpts-outputs.md).

```
DELETE http://<Conductor IP address>/mpts/<id of mpts>
```

### Call Header
<a name="working-with-mpts-delete-mpts-output-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
