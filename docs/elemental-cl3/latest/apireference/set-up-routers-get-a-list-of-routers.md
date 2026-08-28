---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-routers-get-a-list-of-routers.html
---

# GET List: Get a List of Routers
<a name="set-up-routers-get-a-list-of-routers"></a>

Get a list of all video SDI routers, including the data that is contained in the Router Input and Router Output entities.

## HTTP Request and Response
<a name="set-up-routers-get-a-list-of-routers-http-request-response"></a>

### Request URL
<a name="set-up-routers-get-a-list-of-routers-http-request-response-url"></a>

```
GET http://<Conductor IP address>/routers
```

### Call Header
<a name="set-up-routers-get-a-list-of-routers-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-routers-get-a-list-of-routers-http-request-response-response"></a>

The response is XML content consisting of one `routers` element that contains:
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Zero or more `router` elements, one for each router found. Each `router` element consists of several elements.

<a name="set-up-routers-get-a-list-of-routers-http-request-response-response-table"></a>
<table>
<thead>
  <tr><th>Element</th><th>Value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>id</td><td>Integer</td><td rowspan="6">The ID for this router, assigned by the system when the router is created.</td></tr>
  <tr><td>name</td><td>See <a href="set-up-routers-create.md">POST: Create a Router</a>.</td></tr>
  <tr><td>ip </td><td> </td></tr>
  <tr><td>router_type</td><td> </td></tr>
  <tr><td>level_id</td><td> </td></tr>
  <tr><td>user_id</td><td> </td></tr>
  <tr><td>id</td><td> </td><td rowspan="4">See <a href="set-up-router-inputs-create.md">POST: Create a Router Input</a>.</td></tr>
  <tr><td>name</td><td> </td></tr>
  <tr><td>router_id</td><td> </td></tr>
  <tr><td>input_number</td><td> </td></tr>
  <tr><td>id</td><td> </td><td rowspan="4">See <a href="set-up-router-outputs-create.md">POST: Create a Router Output</a>.</td></tr>
  <tr><td>output_number</td><td> </td></tr>
  <tr><td>router_id</td><td> </td></tr>
  <tr><td>device_id</td><td> </td></tr>
</tbody>
</table>

## Example
<a name="set-up-routers-get-a-list-of-routers-example"></a>

### Request
<a name="set-up-routers-get-a-list-of-routers-example-request"></a>

```
GET http://198.51.100.0/routers
```

### Response
<a name="set-up-routers-get-a-list-of-routers-example-response"></a>

```
<?xml version="1.0" encoding="UTF-8"?>
<routers href="/routers" product="AWS Elemental Conductor Live" version="3.3.nnnnn">>
 <router>
    <id>1</id>
    <name>BlackMagic1</name>
    <ip>192.168.10.10</ip>
    <router_type>blackmagic_videohub</router_type>
    <max_inputs>12</max_inputs>
    <max_outputs>12</max_outputs>
    <inputs>
      <input>
        <id>1</id>
        <name>Input 1</name>
        <router_id>1</router_id>
        <input_number>1</input_number>
      </input>
      <input>
        <id>2</id>
        <name>Input 2</name>
        <router_id>1</router_id>
        <input_number>2</input_number>
      </input>
    </inputs>
    <outputs>
     <output>
       <id>9</id>
       <router_id>1</router_id>
       <output_number>1</output_number>
       <device_id>1</device_id>
       <device_type>Device</device_type>
     </output>
    </outputs>
  </router>
.
.
.
  <router>
.
.
.
 </router>
</routers>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
