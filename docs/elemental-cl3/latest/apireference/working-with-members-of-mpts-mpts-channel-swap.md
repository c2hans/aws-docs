---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-mpts-channel-swap.html
---

# PUT: MPTS Channel Swap
<a name="working-with-members-of-mpts-mpts-channel-swap"></a>

Swap the channel assigned to the MPTS.

## HTTP Request and Response
<a name="working-with-members-of-mpts-mpts-channel-swap-http-request-response"></a>

### Request URL
<a name="working-with-members-of-mpts-mpts-channel-swap-http-request-response-url"></a>

```
PUT http://<Conductor IP address>/mpts/<ID of mpts>
```

### Call Header
<a name="working-with-members-of-mpts-mpts-channel-swap-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="working-with-members-of-mpts-mpts-channel-swap-http-request-response-request-body"></a>

The request body contains XML content consisting of one `mpts_members `element, consisting of the following.
+ Two `mpts_member` elements:
  + One to remove the existing channel assignment, containing the following elements.

<a name="working-with-members-of-mpts-mpts-channel-swap-http-request-response-request-body-table"></a>
<table>
<thead>
  <tr><th>Element</th><th>Value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>program_number</td><td>Integer </td><td>The program number used for this SPTS program. To obtain the program number for a specific channel, see <a href="working-with-members-of-mpts-get-all-spts-of-mpts.md">GET List: Get All SPTS of an MPTS</a>.</td></tr>
  <tr><td>pid_map</td><td>See the <a href="working-with-members-of-mpts-add-spts.md#working-with-members-of-mpts-add-spts-http-request-response-request-body-PID-map">PID map</a>.</td><td>PID assignments to use for this member in the MPTS output. If no values are provided, PIDs will be assigned automatically. <br />All PIDs must be unique among all SPTS programs in the MPTS output (not just unique within the individual SPTS program).<br />Support is provided for both PID keys with single values and those with multiple values. See below for details.</td></tr>
  <tr><td>channel_id</td><td>integer</td><td>The ID of the new Conductor Live channel that will produce the desired SPTS. To obtain the ID of a specific channel, see <a href="get-list-of-channels.md">GET List: Get List of Channels</a>.<br />This channel:<ul><li> Can belong to a maximum of two different MPTS outputs. </li><li> Must include at least one UDP output that is set up to produce input into an MPTS: in other words, the MPTS field is set to <code>Remote</code> (not to <code>Local</code> or <code>None</code>).  </li></ul><br />For information on all the special requirements for the channel, see <a href="https://docs.aws.amazon.com/elemental-cl3/latest/ug/setting-up-mpts-outputs.html#step-b-create-a-profile-for-mpts-channels">Create a Profile for MPTS Channels</a> in the AWS Elemental Conductor Live User Guide.</td></tr>
</tbody>
</table>

  + Another to add a new channel assignment, using the following elements.

<a name="working-with-members-of-mpts-mpts-channel-swap-http-request-response-request-body-table2"></a>
<table>
<thead>
  <tr><th>Element</th><th>Value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>type</td><td>String </td><td>Always “conductor”</td></tr>
  <tr><td>program_number</td><td>Integer </td><td>The program number used for this SPTS program. To obtain the program number for a specific channel, see <a href="working-with-members-of-mpts-get-all-spts-of-mpts.md">GET List: Get All SPTS of an MPTS</a>.</td></tr>
  <tr><td>pid_map</td><td>See the <a href="working-with-members-of-mpts-add-spts.md#working-with-members-of-mpts-add-spts-http-request-response-request-body-PID-map">PID map</a>.</td><td>The PID assignments to use for this member in the MPTS output. If no values are provided, PIDs are assigned automatically. <br />All PIDs must be unique among all SPTS programs in the MPTS output (not just unique within the individual SPTS program).<br />Support is provided for both PID keys with single values and with multiple values. See below for details.</td></tr>
  <tr><td>channel_id</td><td>Integer </td><td>The ID of the new Conductor Live channel that produces the desired SPTS. To obtain the ID of a specific channel, see <a href="get-list-of-channels.md">GET List: Get List of Channels</a>.<br />This channel:<ul><li> Can belong to a maximum of two different MPTS outputs. </li><li> Must include at least one UDP output that is set up to produce input into an MPTS: in other words, the MPTS field is set to <code>Remote</code> (not to <code>Local</code> or <code>None</code>).  </li></ul><br />For information on all the special requirements for the channel, see the section on creating a profile for MPTS in the AWS Elemental Conductor Live User Guide.</td></tr>
</tbody>
</table>
