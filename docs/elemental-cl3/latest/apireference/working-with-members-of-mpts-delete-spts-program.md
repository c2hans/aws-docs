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
