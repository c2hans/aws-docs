---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/get-list-of-channels.html
---

# GET List: Get List of Channels
<a name="get-list-of-channels"></a>

Get a list of all channels, including the attributes of each channel. The attributes include a status.

## HTTP Request and Response
<a name="get-list-of-channels-http-request-response"></a>

### Request URL
<a name="get-list-of-channels-http-request-response-url"></a>

```
GET http://<Conductor IP address>/channels?metacounts=true
```

where :
+ ?metacounts=true is optional.

### Call Header
<a name="get-list-of-channels-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="get-list-of-channels-response"></a>

The response is XML content consisting of one `channels` element with the following.
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+  Zero or more `channel` elements, one for each channel found. Each element contains several elements.

| Element | Value | Description |
| --- | --- | --- |
| id | Integer | The ID for this channel, assigned by the system when the channel is created. |
| name | String | The name you assigned to the channel |
| profile\_id | Integer | The ID of the profile associated with this channel.  |
| channel\_params | Array | The channel parameters contained in the specified profile, if any. |
| node\_id | Integer | The ID of the node associated with this channel.  |
| status | String | The current status of the channel. See the table below.  |
| permalink\_name | String | The name of the permalink associated with this channel. |
| service\_name | String | The service name associated with this channel if the associated profile has the Extract SDT field enabled. Empty if the service name is not part of the source or if the Extract SDT field is disabled. |
| service\_provider\_name | String | The service name associated with this channel if the associated profile has the Extract SDT field enabled. Empty if the service provider name is not part of the source or if the Extract SDT field is disabled. |
| active\_alerts | Integer | This setting is included only if the request includes ?metacounts=true.<br />The count of alerts that are currently active for this channel. |
| recent\_error\_messages | Integer | This setting is included only if the request includes ?metacounts=true.<br />The count of recent error messages for this channel. |

## Example
<a name="get-list-of-channels-example"></a>

This response shows two channels:
+ One channel has the ID 1 and that is associated with profile ID 2 and with node ID 3. This channel also has one channel parameter.
+ The other channel has the ID 5 and that is associated with profile ID 4 and with node ID 6. It has no channel parameters.

Also note that the channel with ID 1 has a user-specified permalink while the channel with ID 5 has a permalink that is identical to the channel named: this indicates that the permalink was assigned by the system.

```
GET http://198.51.100.0/channels?metacounts=true
------------------------------------------
Content-type:application/xml
------------------------------------------
<channels href="/channels" product="AWS Elemental Conductor Live" version="3.0.nnnnn">
  <channel>
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
  <channel>
    <id>5</id>
    <name>Channel C</name>
    <profile_id>4</profile_id>
    <channel_params type="array"/>
    <node_id>6</node_id>
    <permalink_name>Channel C</permalink_name>
    <service_name>MendisNatureChannel</service_name>
    <service_provider_name>MendisNetworks</service_provider_name>
    <status>idle</status>
    </active_alerts>
    </recent_error_messages>
  </channel>
  </channel>
</channels>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
