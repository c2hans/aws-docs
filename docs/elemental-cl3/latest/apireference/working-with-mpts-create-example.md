---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-create-example.html
---

# Example
<a name="working-with-mpts-create-example"></a>

**Request**

This request creates one MPTS with the name “mpts\_A”, associated with the node that has the ID 3. The MPTS will contain three channels with channel IDs 3, 6, 7.

```
POST http://198.51.100.0/mpts
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<mpts>
  <name>mpts_A</name>
  <node_id>3</node_id>
  <permalink_name>MendisChannelsMPTS</permalink_name>
  <bitrate>38800000</bitrate>
  <video_allocation>35000000</video_allocation>
  <transport_stream_id>1</transport_stream_id>
  <udp_buffer_size>Auto</udp_buffer_size>
  <output_listening>false</output_listening>
  <pat_interval>40</pat_interval>
  <destination
    <uri>udp://10.10.10.1:5000</uri>
  </destination>
  <secondary_destination>
    <uri>udp://10.10.10.40:5000</uri>
  </secondary_destination>
  <fec_output_settings>
    <include_column_fec>true</include_column_fec>
    <include_row_fec>true</include_row_fec>
    <column_depth>4</column_depth>
    <row_length>6</row_length>
  </fec_output_settings>
  <allocation_message_priority>primary</allocation_message_priority>
  <mpts_members type="array">
    <mpts_member>
      <channel_id>3</channel_id>
      <pid_map>
        <pmt_pid>200</pmt_pid>
        <audio_pids type="array">
          <audio_pid>240</audio_pid>
          <audio_pid>241</audio_pid>
        </audio_pids>
      </pid_map>
      <program_number>1</program_number>
      <type>conductor</type>
    </mpts_member>
    <mpts_member>
      <channel_id>6</channel_id>
      <pid_map>
        <pmt_pid>300</pmt_pid>
        <audio_pids type="array">
          <audio_pid>340</audio_pid>
          <audio_pid>341</audio_pid>
        </audio_pids>
      </pid_map>
      <program_number>2</program_number>
      <type>conductor</type>
    </mpts_member>
    <mpts_member>
      <channel_id>7</channel_id>
      <pid_map>
        <pmt_pid>400</pmt_pid>
        <audio_pids type="array">
          <audio_pid>440</audio_pid>
          <audio_pid>441</audio_pid>
        </audio_pids>
      </pid_map>
      <program_number>3</program_number>
      <type>conductor</type>
    </mpts_member>
  </mpts_members>
</mpts>
```

**Response**

The response returns the data you specified, along with:
+ A unique mpts\_id for the MPTS. In this example, the MPTS has been given the ID 12.
+ A `created_at` element and `updated_at` element that shows the date and time in ISO 8601 format, with the timezone designator indicated as an offset from UTC. For example, 2015-08-17T11:59:35-07:00 is the time in the time zone that is 7 hours behind UTC.
+ An `alerts` element. Typically, this element is empty after initial creation (because the MPTS has not been started).

```
<?xml version="1.0" encoding="UTF-8"?>
<mpts href="/mpts" product="AWS Elemental Conductor Live version="3.3.nnnnn">
  <id>12</id>
  <name>mpts_A</name>
  <node_id>3</node_id>
.
.
.
</mpts>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
