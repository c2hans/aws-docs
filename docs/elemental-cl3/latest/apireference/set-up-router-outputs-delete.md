---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-outputs-delete.html
---

# DELETE: Delete a Router Output
<a name="set-up-router-outputs-delete"></a>

Delete the specified output on the specified router.

## HTTP Request and Response
<a name="set-up-router-outputs-delete-http-request-response"></a>

### Request URL
<a name="set-up-router-outputs-delete-http-request-response-url"></a>

```
DELETE http://<Conductor IP address>/routers/<ID of router>/outputs/<ID of output>
```

### Call Header
<a name="set-up-router-outputs-delete-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

## Example
<a name="set-up-router-outputs-delete-example"></a>

This request deletes the output with the ID 1 from the router with the ID 2.

```
DELETE http://198.51.100.0/routers/2/outputs/1
```
