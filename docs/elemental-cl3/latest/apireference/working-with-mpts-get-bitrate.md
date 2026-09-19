---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-bitrate.html
---

# GET Bitrate: Get the Bitrate of an MPTS Output
<a name="working-with-mpts-get-bitrate"></a>

## HTTP Request and Response
<a name="working-with-mpts-get-bitrate-http-request-response"></a>

### Request URL
<a name="working-with-mpts-get-bitrate-http-request-response-url"></a>

Get the status of the specified MPTS output.

```
GET http://<Conductor IP address>/mpts/<ID of mpts>/status
```

### Call Header
<a name="working-with-mpts-get-bitrate-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="working-with-mpts-get-bitrate-http-request-response-response"></a>

If the MPTS output has *not* been running in the last hour (meaning no bitrate information exists), then the response is XML content consisting of one `mpts_stats` that contains:
+ id\_type
+ an empty mpts\_members array

If there is bitrate information within the last hour for the MPTS output, then the response is XML content consisting of one `mpts_stats` elements (of type “array”) that contains:
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ One `mpts_stats` element that contains the following.

<a name="working-with-mpts-get-bitrate-http-request-response-response-table"></a>
<table>
<thead>
  <tr><th>Element</th><th>Value</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td>mpts_stats</td><td></td><td>One instance</td></tr>
  <tr><td>id</td><td>Integer</td><td>A temporary ID for the specified MPTS. This ID is ephemeral and should not be stored.</td></tr>
  <tr><td>mpts_members</td><td>Array</td><td>1 or more instances</td></tr>
  <tr><td>mpts_member</td><td>Array</td><td>1 or more instances</td></tr>
  <tr><td>id<br /> </td><td>Integer</td><td>A temporary ID for the MPTS member in the specified MPTS. This ID is ephemeral and should not be stored.</td></tr>
  <tr><td>name</td><td>String</td><td>The name of the MPTS member, which is identical to the name attribute of the channel that is associated with this MPTS member. So, if the MPTS member is associated with Channel_C, the name of the MPTS member is Channel_C.</td></tr>
  <tr><td>series_data</td><td></td><td>1 instance for each mpts_member.</td></tr>
  <tr><td>series_datum</td><td></td><td>1 or more instances.<br />Each mpts_member contains one series_data that itself contains several series_datum elements. All the MPTS members contain the same number of series_datum. In other words, every member has a snapshot at timestamp “1418939884” (the timestamp may vary by 1 second in different mpts_members). </td></tr>
  <tr><td>timestamp</td><td>Integer</td><td>The timestamp for this piece of data in Unix time.</td></tr>
  <tr><td>mpts_id</td><td>Integer</td><td>Same as the first id: A temporary ID for the specified MPTS. </td></tr>
  <tr><td>channel_id</td><td>Integer</td><td>The ID of the channel that is associated with this MPTS member. So the name (above) and this channel_id refer to the same channel entity.</td></tr>
  <tr><td>bitrate</td><td>Float</td><td>The bitrate (in bits/second) for this MPTS member at the point identified by the timestamp.</td></tr>
</tbody>
</table>
