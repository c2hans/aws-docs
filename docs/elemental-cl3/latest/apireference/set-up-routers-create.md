---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-routers-create.html
---

# POST: Create a Router
<a name="set-up-routers-create"></a>

This request creates a new router to correspond to a router that is connected to HD-SDI inputs on one or more AWS Elemental Live nodes. (The same router can have connections to several nodes.)

## HTTP Request and Response
<a name="set-up-routers-create-http-request-response"></a>

### Request URL
<a name="set-up-routers-create-http-request-response-url"></a>

```
POST http://<Conductor IP address>/routers
```

### Call Header
<a name="set-up-routers-create-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="set-up-routers-create-http-request-response-request-body"></a>

The request body is XML content consisting of one `router` element, consisting of the following elements.

| Element | Value | Description |
| --- | --- | --- |
| name | String | This name appears in the Inputs drop-down list. |
| ip  | String | The IP address without any protocol. |
| max\_inputs | Integer | The number of inputs you want to use on this router. This number must be less than or equal to the number of physical inputs on the router. |
| max\_outputs | Integer | The number of outputs you want to use on this router. This number must be less than or equal to the number of physical outputs on the router.  |
| router\_type | String | One of these:+  blackmagic\_videohub <br />+  miranda\_nvision <br />+  harris\_panacea <br />+  snell\_aurora  |
| level\_id | Integer | This appears only for Harris Panacea and Miranda nVision. |
| user\_id | Integer |  This appears only for Miranda nVision. |
| matrix\_id | Integer | This appears only for Snell Aurora. |

### Response
<a name="set-up-routers-create-http-request-response-response"></a>

The response repeats back the data that you posted with the addition of <id>: the newly assigned ID for the router.

The response is identical to the response to a GET Router. See the following example.

## Example
<a name="set-up-routers-create-example"></a>

### Request
<a name="set-up-routers-create-example-request"></a>

This request creates one router with the name “SDI\_Router.” This router has 12 inputs and 12 outputs, so these numbers are set in the max\_inputs and max\_outputs.

```
POST http://198.51.100.0/routers
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
----------------------------------------
<router>
    <name>SDI_Router</name>
    <ip>192.168.10.10</ip>
    <router_type>blackmagic_videohub</router_type>
    <max_inputs>12</max_inputs>
    <max_outputs>12</max_outputs>
</router>
```

### Response
<a name="set-up-routers-create-example-response"></a>

In this example, the router is given the ID 1.

```
<?xml version="1.0" encoding="UTF-8"?>
<router href="/routers" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
    <id>1</id>
    <name>BlackMagic1</name>
    <ip>192.168.10.10</ip>
    <router_type>blackmagic_videohub</router_type>
    <max_inputs>12</max_inputs>
    <max_outputs>12</max_outputs>
<router>
```
