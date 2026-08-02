---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-start.html
---

# POST Start: Start an MPTS
<a name="working-with-mpts-start"></a>

Start an MPTS output. If the specified MPTS output is currently idle, then it will start. If the MPTS output is currently running, it will simply continue running.

When an MPTS output is started, the system looks for the video output from each SPTS program associated with the MPTS output. It looks for this output at the destination specified in that SPTS program. All the SPTS programs are then muxed into one video output.

If there is no output for a given SPTS program, the muxing continues without that SPTS program’s content.

If all the SPTS program outputs are missing, the muxing continues without any content. In other words, no content is produced for this MPTS output. Note that a lack of content from all SPTS programs does not cause the MPTS muxing to fail.

## HTTP Request and Response
<a name="working-with-mpts-start-http-request-response"></a>

### Request URL
<a name="working-with-mpts-start-http-request-response-url"></a>

```
POST http://<Conductor IP address>/mpts/<ID of MPTS>/mux
```

### Call Header
<a name="working-with-mpts-start-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).
