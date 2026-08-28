---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-delete-spts-program.html
---

# DELETE: Delete an SPTS Program
<a name="working-with-members-of-mpts-delete-spts-program"></a>

Delete the specified SPTS program from the specified MPTS output.

## HTTP Request and Response
<a name="working-with-members-of-mpts-delete-spts-program-http-request-response"></a>

### Request URL
<a name="working-with-members-of-mpts-delete-spts-program-http-request-response-url"></a>

```
DELETE http://<Conductor IP address>/mpts/mpts_id/mpts_members/<mpts_member_id>
```

### Call Header
<a name="working-with-members-of-mpts-delete-spts-program-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
