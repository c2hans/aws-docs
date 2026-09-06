---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-modify-attributes.html
---

# PUT: Modify the Attributes of an MPTS
<a name="working-with-mpts-modify-attributes"></a>

## HTTP Request and Response
<a name="working-with-mpts-modify-attributes-http-request-response"></a>

### Request URL
<a name="working-with-mpts-modify-attributes-http-request-response-url"></a>

Change any of the attributes of the specified MPTS output, except the list of SPTS programs. To work with the SPTS programs in the MPTS, use the [MPTS Member commands](working-with-members-of-mpts-add-spts.md).

```
PUT http://<Conductor IP address>/mpts/<ID of mpts>
```

### Call Header
<a name="working-with-mpts-modify-attributes-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="working-with-mpts-modify-attributes-http-request-response-request-body"></a>

The body contains only the elements to change; see POST above.
