---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-add-spts.html
---

# POST: Add an SPTS to an MPTS
<a name="working-with-members-of-mpts-add-spts"></a>

Add an SPTS to the specified MPTS output.

## HTTP Request and Response
<a name="working-with-members-of-mpts-add-spts-http-request-response"></a>

### Request URL
<a name="working-with-members-of-mpts-add-spts-http-request-response-url"></a>

```
POST http://<Conductor IP address>/mpts/<ID of mpts>/mpts_members
```

### Call Header
<a name="working-with-members-of-mpts-add-spts-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="working-with-members-of-mpts-add-spts-http-request-response-request-body"></a>

The request body contains XML content consisting of one `mpts_member` element with the following elements.

| Element | Value | Description |
| --- | --- | --- |
| type | String  | The type is always “conductor.” |
| program\_number | Integer  | The program number to use for this SPTS program. 1 – 65535. This must be unique within this MPTS output. |
| pid\_map | See below. | The PID assignments to use for this member in the MPTS output. If no values are provided, PIDs are assigned automatically.<br />All PIDs must be unique among all SPTS programs in the MPTS output (not just unique within the individual SPTS program).<br />Support is provided for both PID keys with single values and those with multiple values. See below for details. |
| channel\_id | Integer  | The ID of the Conductor Live channel that produces the desired SPTS. To obtain the ID of a specific channel, see [GET List: Get List of Channels](get-list-of-channels.md).<br />This channel:+  Can belong to a maximum of two different MPTS outputs. <br />+  Must include at least one UDP output that is set up to produce input into an MPTS: in other words, the MPTS field is set to `Remote` (not to `Local` or `None`). <br />For information on all the special requirements for the channel, see [Create a Profile for MPTS Channels](https://docs.aws.amazon.com/elemental-cl3/latest/ug/setting-up-mpts-outputs.html#step-b-create-a-profile-for-mpts-channels) in the AWS Elemental Conductor Live User Guide. |

#### PID Map
<a name="working-with-members-of-mpts-add-spts-http-request-response-request-body-PID-map"></a>

The PID map is XML content consisting of one <pid\_map> element that contains the following elements.

|  |  |  |  |  |
| --- |--- |--- |--- |--- |
| <pid\_map> |   |   | 0 or 1 instances | Object |
|   | <pmt\_pid> <br /><video\_pid><br /><pcr\_pid><br /><scte35\_pid><br /><klv\_data\_pid><br /><dvb\_teletext\_pid><br /><etv\_platform\_pid><br /><etv\_signal\_pid><br /><timed\_metadata\_pid><br /><private\_metadata\_pid><br /><ecm\_pid><br /><arib\_captions\_pid> |   | 0 or 1 instances | Integer |
|   | <audio\_pids> |   | 0 or 1 instances | Object |
|   |   | <audio\_pid> | 1 or more instances | Integer |
|   | <dvb\_sub\_pids> |   | 0 or 1 instances | Object |
|   |   | <dvb\_sub\_pid> | 1 or more instances | Integer |

For example:

```
<pid_map>
  <pmt_pid>888</pmt_pid>
  <audio_pids type="array">
    <audio_pid>240</audio_pid>
    <audio_pid>241</audio_pid>
  </audio_pids>
</pid_map>
```

### Response
<a name="working-with-members-of-mpts-add-spts-http-request-response-response"></a>

The response repeats back the data that you posted with the addition of:
+ id: The newly assigned ID for the mpts\_member.

The response is identical to the response to a GET MPTS Member. See below for an example.
