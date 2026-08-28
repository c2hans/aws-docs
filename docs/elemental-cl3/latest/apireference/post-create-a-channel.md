---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/post-create-a-channel.html
---

# POST: Create a Channel
<a name="post-create-a-channel"></a>

Create a new channel.

## HTTP Request and Response
<a name="post-create-a-channel-http-request-response"></a>

### Request URL
<a name="post-create-a-channel-http-request-response-url"></a>

```
POST http://<Conductor IP address>/channels
```

### Call Header
<a name="post-create-a-channel-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="post-create-a-channel-http-request-response-request-body"></a>

The request body contains XML content consisting of one `channel` element and some or all of the following elements.

| Element | Value | Description |
| --- | --- | --- |
| name | String | [Required] A name you assign which must be unique in the cluster. |
| profle\_id | Integer | [Required] The ID of the profile to associate with this channel. <br />To obtain the ID of a specific profile, see [GET List: Get a List of Profiles](get-list-of-profiles.md). |
| node\_id | Integer | [Optional] The ID of the node to associate with this channel.<br />To obtain the ID of a specific node, see [GET List: Get a List of Nodes in the Cluster](set-up-nodes-get-list-of-nodes.md).  |
| permalink\_name | String | [Optional] A name for the permalink. A permalink provides a mechanism for referencing a channel in a PUT, GET, or DELETE. With a permalink, you can reference a channel immediately after creating it because you already know its value; you don’t have to first do a GET in order to get the automatically assigned ID.<br />If you specify a value in this element, the permalink takes that name. <br />If you leave this element empty, the value is set to be identical to the name element (converted to lower case and with spaces converted to underscores). |
| channel\_params | Array | [Optional] Required if the specified profile contains channel parameters, in which case you must provide values for each of these parameters. <br />Each channel parameter is represented by a name-value pair. Note that the default value set at profile creation is only for profile validation purposes and is not present in the channel.<br />See below for an example. |

### Response
<a name="post-create-a-channel-http-request-response-response"></a>

The response repeats back the data that you posted with the addition of:
+ id: element containing the newly assigned ID for the channel.
+ status: the current status of the channel. See [Channel Status Elements](monitoring-manage-channels.md#monitoring-manage-channels-status) for a list of states.

The response is identical to the response to a GET Channel. See below for an example.

## Example
<a name="post-create-a-channel-example"></a>

### Request
<a name="post-create-a-channel-example-request"></a>

This request creates one channel with the name “Channel C”, associated with the profile that has the ID 3 and the node that that has the ID 10. The profile has a channel parameter called {{input network location}}, so the channel must provide a value for that parameter: udp://239.255.1.10:5001.

For information on channel parameters, see [Setting Up Channels](https://docs.aws.amazon.com/elemental-cl3/latest/ug/setting-up-channels.html) in the AWS Elemental Conductor Live User Guide. For a list of channel parameters, see [Supported Channel Parameters for Conductor Live](https://docs.aws.amazon.com/elemental-cl3/latest/ug/channel-parameters.html) in the AWS Elemental Conductor Live User Guide.

```
POST http://198.51.100.0/channels
------------------------------------------
Content-type:application/xml
Accept:application/xml
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<channel>
  <name>Channel C</name>
  <profile_id>3</profile_id>
  <node_id>10</node_id>
  <permalink_name>Mendis_News_Channel</permalink_name>
  <channel_params type="array">
    <channel_param>
      <name>input network location</name>
      <value>udp://239.255.10.23:5001</value>
      </channel_param>
    <channel_param>
      .
      .
      .
    </channel_param>
  /channel_params>
</channel>
```

### Response
<a name="post-create-a-channel-example-response"></a>

In this example, the channel is given the ID 2.

```
<?xml version="1.0" encoding="UTF-8"?>
<channel href="/channels" product="AWS Elemental Conductor Live" version="3.3.0.nnnnn">
  <id>2</id>
  <name>Channel C</name>
  <profile_id>3</profile_id>
  <channel_params type="array">
    <channel_param>
      <name>input network location</name>
      <value>udp://239.255.10.23:5001</value>
    </channel_param>
   </channel_params>
  <node_id>10</node_id>
  <permalink_name>Mendis_News_Channel</permalink_name>
  <status>idle</status>
</channel>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
