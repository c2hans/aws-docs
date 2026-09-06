---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-bitrate.html
---

# GET Bitrate: Get the Bitrate of an MPTS Output
<a name="working-with-mpts-get-bitrate"></a>

## HTTP Request and Response
<a name="working-with-mpts-get-bitrate-http-request-response"></a>

### Request URL
<a name="working-with-mpts-get-bitrate-http-request-response-url"></a>

Get the status of the specified MPTS output.

```
GET http://<Conductor IP address>/mpts/<ID of mpts>/status
```

### Call Header
<a name="working-with-mpts-get-bitrate-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="working-with-mpts-get-bitrate-http-request-response-response"></a>

If the MPTS output has *not* been running in the last hour (meaning no bitrate information exists), then the response is XML content consisting of one `mpts_stats` that contains:
+ id\_type
+ an empty mpts\_members array

If there is bitrate information within the last hour for the MPTS output, then the response is XML content consisting of one `mpts_stats` elements (of type “array”) that contains:
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ One `mpts_stats` element that contains the following.
<a name="working-with-mpts-get-bitrate-http-request-response-response-table"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-bitrate.html)
