---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/get-attributes-of-a-channel.html
---

# GET: Get the Attributes of a Channel
<a name="get-attributes-of-a-channel"></a>

Get the attributes of the specified channel.

## HTTP Request and Response
<a name="get-attributes-of-a-channel-http-request-response"></a>

### Request URL
<a name="get-attributes-of-a-channel-http-request-response-url"></a>

```
GET http://<Conductor IP address>/channels/<ID of channel>?metacounts=true
```

where:
+ ?metacounts=true is optional but adds additional information to the response.

### Response
<a name="get-attributes-of-a-channel-http-request-response-response"></a>

The response contains XML content consisting of one `channel` element with the same elements as the response for GET Channel List, above.

### Call Header
<a name="get-attributes-of-a-channel-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

## Example
<a name="get-attributes-of-a-channel-example"></a>

This response shows the information for the channel with the ID 1.

```
GET http://198.51.100.0/channels/1
----------------------------------------
Content-type:application/xml
----------------------------------------
<channel href="/channels/1" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
  <id>1</id>
  <name>Channel A</name>
  <profile_id>2</profile_id>
  <channel_params type="array">
    <channel_param>
      <name>input network location</name>
      <value>udp://239.255.1.10:5001</value>
    </channel_param>
  </channel_params>
  <node_id>3</node_id>
    <permalink_name>Mendis_News_Channel/permalink_name>
    <service_name>MendisNewsChannel</service_name>
    <service_provider_name>MendisNetworks</service_provider_name>
    <status>running</status>
    <active_alerts>2</active_alerts>
    <recent_error_messages>0</recent_error_messages>
</channel>
```
