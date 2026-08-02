---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-outputs-create.html
---

# POST: Create a Router Output
<a name="set-up-router-outputs-create"></a>

Create a new output for the specified router. Use this command repeatedly to set up all the router outputs. The total number of Router Output entities for a specified router must not exceed the actual physical outputs on the router.

## HTTP Request and Response
<a name="set-up-router-outputs-create-http-request-response"></a>

### Request URL
<a name="set-up-router-outputs-create-http-request-response-url"></a>

```
POST http://<Conductor IP address>/routers/<ID of router>/outputs
```

### Call Header
<a name="set-up-router-outputs-create-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="set-up-router-outputs-create-http-request-response-request-body"></a>

The request body contains XML content consisting of one `output` element, consisting of the following elements.

| Element | Value | Description |
| --- | --- | --- |
| output\_number | Integer | An ID on the router.<br />The ID of the router output that is connected to an SDI card on the AWS Elemental Live node. You specify the router by its output ID as assigned by the router (not assigned by AWS Elemental software). Check the manufacturer’s documentation for the numbering scheme for the router. <br />For example, the manufacturer may number ports starting from 1 and starting from the upper left. In this case, the second output from the left might be numbered “2.”<br />When adding 4 Quadrant-4k outputs for HEVC, enter the first output number in the sequence. |
| output\_number\_end | Integer | When adding 4 Quadrant-4k outputs for HEVC, enter the last (fourth) output number in the sequence.<br />For example, if you entered “1” for output\_number, you would use “4” for output\_number\_end.<br />This element is not used if you are not adding the 4 Quadrant-4k outputs. |
| device\_id | String | An ID on the SDI card.<br />The ID of the SDI input that is connected to the router output identified by output\_number. <br />This ID is assigned by AWS Elemental Live and provided to Conductor Live when the SDI card is auto-detected. Each port on the entire node is assigned a unique ID (for example, IDs 1-5 on the first card, 6-10 on the second).<br />To obtain the device ID, see the Settings > Input Devices page of the Conductor web interface. The Conductor API does not expose this information.  |

### Response
<a name="set-up-router-outputs-create-http-request-response-response"></a>

The response repeats back the data that you posted with the addition of:
+ id: The newly assigned ID for the router.
+ router\_id: The router to which this router output belongs.

The response is identical to the response to a GET Router Output. See below for an example.

## Example
<a name="set-up-router-outputs-create-example"></a>

### Request
<a name="set-up-router-outputs-create-example-request"></a>

This request creates one output for the router with the ID 2. It specifies that router output ID 3 is connected to SDI card input ID 4.

```
POST http://198.51.100.0/routers/2/outputs
-----------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
-----------------------------------------
<output>
  <output_number>3</output_number>
  <device_id>4</device_id>
</output>
```

### Response
<a name="set-up-router-outputs-create-example-response"></a>

In this example, the router output is given the ID 4.

```
<?xml version="1.0" encoding="UTF-8"?>
<output href="/routers/2/output" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
  <id>4</id>
  <router_id>1</router_id>
  <output_number>2</output_number>
  <output_number_end nil="true"/>
  <device_id>5</device_id>
  <device_type>Device</device_type>
</output>
```
