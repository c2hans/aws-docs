---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-outputs-modify.html
---

# PUT: Modify a Router Output
<a name="set-up-router-outputs-modify"></a>

Modify the attributes of the specified output on the specified router. Modify the attributes if a cable from the router output moves to a different SDI card input.

## HTTP Request and Response
<a name="set-up-router-outputs-modify-http-request-response"></a>

### Request URL
<a name="set-up-router-outputs-modify-http-request-response-url"></a>

```
PUT http://<Conductor IP address>/routers/<ID of router>/outputs/<ID of output>
```

### Call Header
<a name="set-up-router-outputs-modify-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="set-up-router-outputs-modify-http-request-response-request-body"></a>

The body contains only the elements to change. For available elements, see [POST: Create a Router](set-up-routers-create.md).

## Example
<a name="set-up-router-outputs-modify-example"></a>

This request changes the router output with the ID 4. This input belongs to the router with the ID 2. It changes its device\_id to 3 to indicate that the connection represented by this router output is actually to the SDI input that has the ID 3.

```
PUT http://198.51.100.0/routers/2/outputs/4
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<output>
  <device_ID>3</device_id>
</output>
```
