---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-nodes-get-attributes-of-node.html
---

# GET: Get the Attributes of a Node
<a name="set-up-nodes-get-attributes-of-node"></a>

Get the attributes on the specified node.

## HTTP Request and Response
<a name="set-up-nodes-get-attributes-of-node-http-request-response"></a>

### Request URL
<a name="set-up-nodes-get-attributes-of-node-http-request-response-url"></a>

```
GET http://<Conductor IP address>/nodes/<ID of node>
```

### Call Header
<a name="set-up-nodes-get-attributes-of-node-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md) .

### Response
<a name="set-up-nodes-get-attributes-of-node-http-request-response-response"></a>

The response is XML content consisting of one `node` element, containing the same elements as the response for GET Node List above.

## Example
<a name="set-up-nodes-get-attributes-of-node-example"></a>

This request gets the attributes for the node that has the ID 3.

```
GET http://198.51.100.0/nodes/3
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<node>
  <id>3</id>
  <hostname>ecle-22334455</hostname>
  <ip_addr>10.4.136.92</ip_addr>
  <status>active</status>
  <product_name>Live</product_name>
  <version>2.7.0.67890</version>
  <channels>3</channels>
  <inflight_channels type="integer">0</inflight_channels>
  <mptses type="integer">0</mptses>
  <active_alerts type="integer">0</active_alerts>
  <recent_error_messages type="integer">0</recent_error_messages>
  <redundancy_group nil="true"/>
  <authentication>
    <user_id type="integer">1</user_id>
  </authentication>
</node>
```
