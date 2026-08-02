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
