---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-list-of-mpts-outputs.html
---

# GET List: Get a List of MPTS Outputs
<a name="working-with-mpts-get-list-of-mpts-outputs"></a>

Get the attributes and SPTS programs of all MPTS outputs.

## HTTP Request and Response
<a name="working-with-mpts-get-list-of-mpts-outputs-http-request-response"></a>

### Request URL
<a name="working-with-mpts-get-list-of-mpts-outputs-http-request-response-url"></a>

```
GET http://<Conductor IP address>/mpts
```

### Call Header
<a name="working-with-mpts-get-list-of-mpts-outputs-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="working-with-mpts-get-list-of-mpts-outputs-http-request-response-response"></a>

The response contains XML content consisting of one `mpts_list` element with the following.
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Zero or more `mpts `elements, one for each MPTS found. Each element contains several elements.

| Element | Value | Description |
| --- | --- | --- |
| id | Integer | The ID for this MPTS output assigned by the system when the MPTS is created. |
| Other elements | See [POST: Create an MPTS](working-with-mpts-create.md). |  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
