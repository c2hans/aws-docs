---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-outputs-get-attributes.html
---

# GET: Get Attributes of a Router Output
<a name="set-up-router-outputs-get-attributes"></a>

Get the attributes of the specified output on the specified router.

## HTTP Request and Response
<a name="set-up-router-outputs-get-attributes-http-request-response"></a>

### Request URL
<a name="set-up-router-outputs-get-attributes-http-request-response-url"></a>

```
GET http://<Conductor IP address>/routers/<ID of router>/outputs/<ID of output>
```

### Call Header
<a name="set-up-router-outputs-get-attributes-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-router-outputs-get-attributes-http-request-response-response"></a>

The response is XML content consisting of one `output` element, containing the same elements as the response for [GET: Get Router Attributes](set-up-routers-get-router-attributes.md).

## Example
<a name="set-up-router-outputs-get-attributes-example"></a>

This request gets the attributes for the output that has the ID 3. The input belongs to the router with this ID 4.

```
GET http://198.51.100.0/routers/4/outputs/3
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<output href="/routers/4/outputs/3" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
  <id>3</id>
  <router_id>4</router_id>
  <output_number>1</output_number>
  <device_id>1</device_id>
  <device_type>Device</device_type>
</output>
```
