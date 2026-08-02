---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-attributes-of-mpts-output.html
---

# GET: Get the Attributes of an MPTS Output
<a name="working-with-mpts-get-attributes-of-mpts-output"></a>

Get the attributes and SPTS programs of one MPTS output.

## HTTP Request and Response
<a name="working-with-mpts-get-attributes-of-mpts-output-http-request-response"></a>

### Request URL
<a name="working-with-mpts-get-attributes-of-mpts-output-http-request-response-url"></a>

```
GET http://<Conductor IP address>/mpts/<ID of mpts>
```

### Call Header
<a name="working-with-mpts-get-attributes-of-mpts-output-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md) .

### Response
<a name="working-with-mpts-get-attributes-of-mpts-output-http-request-response-response"></a>

The response contains XML content consisting of one `mpts` element, with the same elements as the response for GET MPTS List above.
