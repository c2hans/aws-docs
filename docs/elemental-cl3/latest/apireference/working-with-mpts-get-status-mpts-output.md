---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-status-mpts-output.html
---

# GET Status: Get the Status of an MPTS Output
<a name="working-with-mpts-get-status-mpts-output"></a>

## HTTP Request and Response
<a name="working-with-mpts-get-status-mpts-output-http-request-response"></a>

### Request URL
<a name="working-with-mpts-get-status-mpts-output-http-request-response-url"></a>

Get the status of the specified MPTS output.

```
GET http://<Conductor IP address>/mpts/<ID of mpts>/status
```

### Call Header
<a name="working-with-mpts-get-status-mpts-output-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="working-with-mpts-get-status-mpts-output-http-request-response-response"></a>

The response contains XML content consisting of one `mpts_status` element,with the same elements as the response for GET MPTS Status above.
