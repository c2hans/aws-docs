---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-routers-get-router-attributes.html
---

# GET: Get Router Attributes
<a name="set-up-routers-get-router-attributes"></a>

Get the attributes of the specified video SDI router, including the data that is contained in the Router Input and Router Output.

## HTTP Request and Response
<a name="set-up-routers-get-router-attributes-http-request-response"></a>

### Request URL
<a name="set-up-routers-get-router-attributes-http-request-response-url"></a>

```
GET http://<Conductor IP address>/routers/<ID of router>
```

### Call Header
<a name="set-up-routers-get-router-attributes-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-routers-get-router-attributes-http-request-response-response"></a>

The response contains XML content consisting of one `router` element, containing the same elements as the response for [GET List: Get a List of Routers](set-up-routers-get-a-list-of-routers.md).

## Example
<a name="set-up-routers-get-router-attributes-example"></a>

This response shows the information for the router with the ID 1. For this router, two inputs have been set up, but, so far, no outputs have been set up. The outputs would have to be set up in order for the router to be useable as an input source.

```
GET http://198.51.100.0/routers/1
---------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<router href="/routers/2" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
 <id>2</id>
 <name>SDI_Router</name>
 <ip>192.168.10.12</ip>
 <router_type>harris_panacea</router_type>
 <max_inputs>12</max_inputs>
 <max_outputs>12</max_outputs>
 <level_id>0</level_id>
 <inputs>
    <input>
      <id>3</id>
      <name>Input 1</name>
      <router_id>2</router_id>
      <input_number>1</input_number>
    </input>
      <input>
      <id>4</id>
      <name>Input 2</name>
      <router_id>2</router_id>
      <input_number>2</input_number>
    </input>
  </inputs>
 <outputs/>
</router>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
