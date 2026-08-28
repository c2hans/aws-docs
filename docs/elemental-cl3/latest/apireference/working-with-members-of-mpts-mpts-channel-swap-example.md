---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-mpts-channel-swap-example.html
---

# Example
<a name="working-with-members-of-mpts-mpts-channel-swap-example"></a>

This request swaps channel 3 for channel 4 and uses default PID value (so does not specify any PIDs).

**Request**

```
PUT http://198.51.100.0/mpts/1
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<mpts>
  <mpts_members type="array">
    <mpts_member>
      <channel_id>3</channel_id>
      <_destroy>1</_destroy>
    </mpts_member>
    <mpts_member>
      <type>conductor</type>
      <program_number>1</program_number>
      <channel_id>4</channel_id>
    </mpts_member>
  </mpts_members>
</mpts>
```

**Response**

```
PUT http://198.51.100.0/mpts/1
----------------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<mpts>
  <id type="integer">1</id>
  <node_id type="integer">2</node_id>
  <created_at type="datetime">2016-05-18T07:54:06-07:00</created_at>
  <updated_at type="datetime">2016-05-18T07:54:06-07:00</updated_at>
  <additional_system_latency type="integer">0</additional_system_latency>
  <allocation_message_priority>primary</allocation_message_priority>
  <bitrate type="integer">38800000</bitrate>
  <name>mpts</name>
  <output_listening type="boolean">false</output_listening>
  <controller_only type="boolean">false</controller_only>
  <output_listening_interval type="integer">500</output_listening_interval>
  <pat_interval type="integer">100</pat_interval>
  <transport_stream_id type="integer">1</transport_stream_id>
  <udp_buffer_size>Auto</udp_buffer_size>
  <video_allocation type="integer">35000000</video_allocation>
  <permalink_name>mpts</permalink_name>
  <mpts_members type="array">
    <mpts_member>
      <id type="integer">2</id>
      <mpts_id type="integer">1</mpts_id>
      <created_at type="datetime">2016-05-18T08:06:26-07:00</created_at>
      <updated_at type="datetime">2016-05-18T08:06:27-07:00</updated_at>
      <channel_id type="integer">4</channel_id>
      <name>mpts channel - duplicate</name>
      <pid_map>
        <pmt_pid type="integer">100</pmt_pid>
        <video_pid type="integer">101</video_pid>
        <dvb_teletext_pid type="integer">105</dvb_teletext_pid>
        <audio_pids type="array">
          <audio_pid type="integer">140</audio_pid>
          <audio_pid type="integer">141</audio_pid>
          <audio_pid type="integer">142</audio_pid>
          <audio_pid type="integer">143</audio_pid>
          <audio_pid type="integer">144</audio_pid>
          <audio_pid type="integer">145</audio_pid>
          <audio_pid type="integer">146</audio_pid>
          <audio_pid type="integer">147</audio_pid>
          <audio_pid type="integer">148</audio_pid>
          <audio_pid type="integer">149</audio_pid>
          <audio_pid type="integer">150</audio_pid>
          <audio_pid type="integer">151</audio_pid>
          <audio_pid type="integer">152</audio_pid>
          <audio_pid type="integer">153</audio_pid>
          <audio_pid type="integer">154</audio_pid>
          <audio_pid type="integer">155</audio_pid>
          <audio_pid type="integer">156</audio_pid>
        </audio_pids>
        <ecm_pid type="integer">110</ecm_pid>
        <arib_captions_pid type="integer">111</arib_captions_pid>
      </pid_map>
      <program_number type="integer">1</program_number>
      <type>conductor</type>
      <input>
        <uri>rtp://239.20.20.20:5001</uri>
      </input>
      <secondary_input>
        <uri>rtp://239.20.20.20:5010</uri>
      </secondary_input>
      <allocation_transmit_destination>
        <uri>udp://239.20.30.20:5001</uri>
      </allocation_transmit_destination>
      <secondary_allocation_transmit_destination>
        <uri>udp://239.20.20.80:5001</uri>
      </secondary_allocation_transmit_destination>
      <complexity_receipt_destination>
        <uri>udp://239.10.20.20:5001</uri>
      </complexity_receipt_destination>
      <secondary_complexity_receipt_destination>
        <uri>udp://239.20.40.20:5001</uri>
      </secondary_complexity_receipt_destination>
    </mpts_member>
  </mpts_members>
  <destination>
    <uri>udp://10.10.10.1:5000</uri>
  </destination>
  <secondary_destination nil="true"/>
  <fec_output_settings nil="true"/>
  <dvb_sdt_settings nil="true"/>
  <dvb_tdt_settings nil="true"/>
  <dvb_nit_settings nil="true"/>
</mpts>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
