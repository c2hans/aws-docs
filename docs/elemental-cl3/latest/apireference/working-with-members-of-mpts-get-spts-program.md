---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-get-spts-program.html
---

# GET: Get an SPTS Program
<a name="working-with-members-of-mpts-get-spts-program"></a>

Get the specified SPTS program from the specified MPTS output.

## HTTP Request and Response
<a name="working-with-members-of-mpts-get-spts-program-http-request-response"></a>

### Request URL
<a name="working-with-members-of-mpts-get-spts-program-http-request-response-url"></a>

```
GET http://<Conductor IP address>/mpts/<ID of mpts>/mpts_members/<ID of mpts member>
```

### Call Header
<a name="working-with-members-of-mpts-get-spts-program-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="working-with-members-of-mpts-get-spts-program-http-request-response-response"></a>

The response contains XML content consisting of one **mpts\_member** element, with the same elements as the response for GET SPTS Program List above.
