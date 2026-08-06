---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-create.html
---

# POST: Create an MPTS
<a name="working-with-mpts-create"></a>

Create an MPTS output. Note that its SPTS programs (members) must be added after the MPTS is created. Use instruction for [POST MPTS member](working-with-members-of-mpts-add-spts.md).

## HTTP Request and Response
<a name="working-with-mpts-create-http-request-response"></a>

### Request URL
<a name="working-with-mpts-create-http-request-response-url"></a>

```
POST http://<Conductor IP address>/mpts
```

### Call Header
<a name="working-with-mpts-create-http-request-response-call-header"></a>
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="working-with-mpts-create-http-request-response-request-body"></a>

The request contains XML content consisting of one **mpts** element, with the following elements.

<a name="working-with-mpts-create-http-request-response-request-body-table"></a>
<table>
<thead>
  <tr><th>Element</th><th>Value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>name</td><td>String</td><td>A name for the MPTS</td></tr>
  <tr><td>node\_id</td><td>String</td><td>The node where the MPTS will be created: where the muxing of the individual programs occurs. <br />Specify a node that is not set up as backup nodes in a redundancy group. To obtain the ID of a specific node, see [GET List: Get a List of Nodes in the Cluster](set-up-nodes-get-list-of-nodes.md).<br />Select the correct node. Be aware of the type and choose:+  Any AWS Elemental Live node, if you are creating an MPTS consisting only of Constant Bitrate (CBR) programs. <br />+  An AWS Elemental Live node with the AWS Elemental Statmux option if you are creating an MPTS that includes at least one AWS Elemental Statmux program. <br />+  An AWS Elemental Statmux stand-alone node if you are creating an MPTS that includes at least one AWS Elemental Statmux program. </td></tr>
  <tr><td>permalink\_name</td><td>String</td><td>A name for the permalink. A permalink provides a mechanism for referencing an MPTS in a PUT, GET, or DELETE. With a permalink, you can reference an MPTS immediately after creating it because you already know its value; you don’t have to first do a GET in order to get the automatically assigned ID.<br />If you specify a value in this element, the permalink takes that name. <br />If you leave this element empty, the value is set to be identical to the name element (converted to lower case and with spaces converted to underscores).</td></tr>
  <tr><td>bitrate</td><td>Integer</td><td>The total bitrate for the MPTS in bits/second.</td></tr>
  <tr><td>video\_allocation</td><td>Integer</td><td>The bitrate to allocate for video traffic in bits/second.</td></tr>
  <tr><td>transport\_stream\_id</td><td>Integer</td><td>The value for the transport stream ID field in the Program Map Table. Range 0 to 65535.</td></tr>
  <tr><td>udp\_buffer\_size</td><td>String</td><td>Size of network output buffer. This buffer is used to limit PCR jitter on the network. +  Auto: Selects optimal size based on the video elementary stream properties.  <br />+  Custom: Establishes a non-negative integer for the number of bits to use for the buffer.  <br />+  Off: Smooths bursts in the network output but does not attempt to limit PCR jitter; this can be used to achieve low-latency streams where output devices do not require buffer-compliant outputs. </td></tr>
  <tr><td>output\_listening</td><td>String</td><td>This field is used to set up for output redundancy with output listening and applies only if your Statmux statmux deployment involves AWS Elemental Live nodes as the encoders and an AWS Elemental Statmux node as the muxer; see [Setting Up MPTS Outputs](https://docs.aws.amazon.com/elemental-cl3/latest/ug/setting-up-mpts-outputs.html) in the AWS Elemental Conductor Live User Guide.<br />If you are not setting up for this type of redundancy or if the AWS Elemental Live node is both the encoder and muxer, omit this field.</td></tr>
  <tr><td>output\_listening\_interval</td><td>Boolean</td><td>The specified detection interval for the output listening feature, in milliseconds. See above for details.</td></tr>
  <tr><td>allocation\_message\_priority</td><td>String</td><td>This field is used to set up for multiplexer redundancy and applies only if your Statmux deployment involves AWS Elemental Live nodes as the encoders and an AWS Elemental Statmux node as the muxer; see [Setting Up MPTS Outputs](https://docs.aws.amazon.com/elemental-cl3/latest/ug/setting-up-mpts-outputs.html) in the AWS Elemental Conductor Live User Guide.<br />If you are not setting up for this type of redundancy or if the AWS Elemental Live node is both the encoder and muxer, omit this field.</td></tr>
  <tr><td>pat\_interval</td><td>Integer</td><td>The PAT interval in ms for the entire MPTS.<br />Range: 10 – 1000 (Default is 100).</td></tr>
  <tr><td>destination/uri</td><td>String</td><td>The primary destination for the MPTS output. This can be a UDP or RTP location. Format:<br /><protocol>://<IP address>:<port></td></tr>
  <tr><td>destination/username</td><td>String</td><td>The username for the destination, if required.</td></tr>
  <tr><td>destination/password</td><td>String</td><td>The password for the destination, if required.</td></tr>
  <tr><td>secondary\_destination/<br />uri</td><td>String</td><td rowspan="3">Optional. The secondary destination, interface, and virtual source address.<br />Completing a secondary destination provides “network failure redundancy” for the MPTS. The muxer sends the output to both destination 1 and destination 2; if one destination fails, downstream systems can obtain it from the other. See [Setting Up MPTS Outputs](https://docs.aws.amazon.com/elemental-cl3/latest/ug/setting-up-mpts-outputs.html) in the AWS Elemental Conductor Live User Guide.<br />If you are not setting up for network failure redundancy, omit these fields.</td></tr>
  <tr><td>secondary\_destination/<br />username</td><td>String</td></tr>
  <tr><td>secondary\_destination/<br />password</td><td>String</td></tr>
  <tr><td>fec\_output\_settings</td><td>String</td><td>See below for details.</td></tr>
  <tr><td>additional\_system\_latency</td><td>String</td><td>Specify additional time (in milliseconds) to add to the “maximum encoding latency” – the time between when the SPTS channels send their complexity data to the muxer and when the muxer expects the related encoded content for all channels. <br />Typically, specify additional time only if the Buffer Size (set in the video stream) for one of the SPTS channels is longer than typical,or if an SPTS channel is set up for 4 Quadrant-4k HEVC encoding via bonded Live 401 or 402 encoders. <br />Note that you will not be able to change this value while the MPTS is running; you will have to stop the MPTS output and then restart it. This is the only field on the MPTS that you cannot change after creation.</td></tr>
  <tr><td>dvb\_sdt\_settings/rep\_interval</td><td>Integer</td><td>The SDT interval in ms, for the entire MPTS.<br />Range: 25 – 2000 (Default is 500)</td></tr>
  <tr><td>dvb\_tdt\_settings/rep\_interval</td><td>Integer</td><td>The TDT interval in ms, for the entire MPTS.<br />Range: 1000 – 30000 (Default is 1000)</td></tr>
  <tr><td>dvb\_nit\_settings/rep\_interval</td><td>Integer</td><td>The NIT interval in ms, for the entire MPTS.<br />Range: 25 – 10000 (Default is 500)</td></tr>
  <tr><td>dvb\_nit\_settings/network\_id</td><td>Integer</td><td>The numeric identifier of the network to which the MPTS belongs.</td></tr>
  <tr><td>dvb\_nit\_settings/network\_name</td><td>String</td><td>The network name.</td></tr>
</tbody>
</table>

fec\_output\_settings

| Element | Value | Description |
| --- | --- | --- |
| include\_column\_fec | Boolean | True means enable column-based FEC; must be true. |
| include\_row\_fec | Boolean | True means enables row-based FEC; enabled by default. |
| column\_depth | Integer | Parameter D from SMPTE 2022-1. Range 4-20. The height of the FEC protection matrix. The number of transport stream packets per column error correction packet.  |
| row\_length | Integer | Parameter L from SMPTE 2022-1. Range 1-20. The width of the FEC protection matrix. This must be between 1 and 20, inclusive. If only Column FEC is used, then larger values increase robustness.<br />If Row FEC is used, then this is the number of transport stream packets per row error correction packet. |

### Response
<a name="working-with-mpts-create-http-request-response-response"></a>

The response repeats back the data that you posted, with the addition of:
+ id: The newly assigned ID for the MPTS .

The response is identical to the response to a GET MPTS. For a complete example, see [GET: Get the Attributes of an MPTS Output](working-with-mpts-get-attributes-of-mpts-output.md).
