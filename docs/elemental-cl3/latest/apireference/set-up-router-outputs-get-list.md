---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-outputs-get-list.html
---

# GET List: Get Router Output List
<a name="set-up-router-outputs-get-list"></a>

Get the list of outputs for the specified router.

## HTTP Request and Response
<a name="set-up-router-outputs-get-list-http-request-response"></a>

### Request URL
<a name="set-up-router-outputs-get-list-http-request-response-url"></a>

```
GET http://<Conductor IP address>/routers/<ID of router>/outputs
```

### Call Header
<a name="set-up-router-outputs-get-list-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-router-outputs-get-list-http-request-response-response"></a>

The response contains XML content consisting of one `outputs` element with the following.
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Zero or more `output` elements, one for each input found. Each `output` element contains several elements.

| Element | Value | Description |
| --- | --- | --- |
| id | Integer | The ID for this output, unique for this router and assigned by the system when the output is created. |
| output\_number | Integer | The ID of the router output that is connected to the SDI card identified by device\_id (below). This ID is the ID assigned by the router (not as assigned by AWS Elemental Live). |
| router\_id | Integer | The router that this output belongs to-- a unique ID assigned by AWS Elemental Live. |
| device\_id | String | The ID the SDI input that is connected to the router output identified by output\_number. This ID is assigned by AWS Elemental Live when the SDI card is auto-detected. Each port on the entire node is assigned a unique ID (for example, IDs 1-4 on the first card, 5-8 on the second). |
| device\_type | String | A string which always specifies “Device.” |

## Example
<a name="set-up-router-outputs-get-list-example"></a>

This request is for the outputs associated with the router with the ID 2. The response specifies that there are two outputs in this router with IDs 3 and 4.

```
GET http://198.51.100.0/routers/2/outputs
----------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<outputs href="/routers/2/outputs" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
  <output>
    <id>3</id>
    <output_number>5</output_number>
    <router_id>2</router_id>
    <device_id>1</device_id>
  </output>
  <output>
    <id>4</id>
    <output_number>2</output_number>
    <router_id>2</router_id>
    <device_id>7</device_id>
  </output>
</outputs>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
