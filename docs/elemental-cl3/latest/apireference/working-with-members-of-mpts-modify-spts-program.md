---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-modify-spts-program.html
---

# PUT: Modify an SPTS Program
<a name="working-with-members-of-mpts-modify-spts-program"></a>

Change the PID map and program number of the specified MPTS member.

Do not use PUT to modify the channel ID; instead, delete the MPTS member (DELETE) and recreate it (POST) with the new channel ID.

## HTTP Request and Response
<a name="working-with-members-of-mpts-modify-spts-program-http-request-response"></a>

### Request URL
<a name="working-with-members-of-mpts-modify-spts-program-http-request-response-url"></a>

```
PUT http://<Conductor IP address>/mpts/<ID of mpts>/mpts_members/<ID of mpts member>
```

### Call Header
<a name="working-with-members-of-mpts-modify-spts-program-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="working-with-members-of-mpts-modify-spts-program-http-request-response-request-body"></a>

The body contains only the elements to change; see POST above.
