---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-list-of-mpts-outputs-example.html
---

# Example
<a name="working-with-mpts-get-list-of-mpts-outputs-example"></a>

**Request**

```
GET http://198.51.100.0/mpts
```

**Response**

```
<?xml version="1.0" encoding="UTF-8"?>
<mpts_list href="/mpts_list" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
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
  <additional_system_latency>0</additional_system_latency>
  <allocation_message_priority>primary</allocation_message_priority>
  <alerts type ="array">
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
<mpts>
  <mpts_id>
  <name>mpts_B</name>
  <node_id>3</node_id>
.
.
.
  </mpts_members>
</mpts>
<mpts_list>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
