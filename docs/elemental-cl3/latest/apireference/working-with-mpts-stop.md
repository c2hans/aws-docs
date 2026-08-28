---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-stop.html
---

# DELETE Stop: Stop an MPTS
<a name="working-with-mpts-stop"></a>

Stop an MPTS output. If the specified MPTS output is currently running, it will stop. If the specified MPTS output is currently idle, it will simply remain idle.

Stopping the MPTS output does not stop the individual SPTS programs associated with the MPTS output.

## HTTP Request and Response
<a name="working-with-mpts-stop-http-request-response"></a>

### Request URL
<a name="working-with-mpts-stop-http-request-response-url"></a>

```
DELETE http://<Conductor IP address>/mpts/<ID of MPTS>/mux
```

### Call Header
<a name="working-with-mpts-stop-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
