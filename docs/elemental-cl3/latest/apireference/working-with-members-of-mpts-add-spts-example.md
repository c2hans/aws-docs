---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-add-spts-example.html
---

# Example
<a name="working-with-members-of-mpts-add-spts-example"></a>

This example shows the result of adding the channel with the ID 2 as an SPTS program with the program ID 5 in the MPTS output that has the ID 3.

**Request**

```
POST http://198.51.100.0/mpts/3/mpts_members
--------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
--------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<mpts_member>
  <type>conductor</type>
  <program_number>5</program_number>
  <channel_id>2</channel_id
  <pid_map>
  <pmt_pid>400</pmt_pid>
  <audio_pids type="array">
    <audio_pid>440</audio_pid>
    <audio_pid>441</audio_pid>
  </audio_pids>
  </pid_map>
<mpts_member>
```

**Response**

```
<?xml version="1.0" encoding="UTF-8"?>
<mpts_member href="/mpts/3/mpts_member/4" product="AWS Elemental Conductor Live" version="1.0.3b.12345>
  <id>4</id>
  <channel_id>2</channel_id>
  <pid_map>
  <pmt_pid>400</pmt_pid>
  <audio_pids type="array">
    <audio_pid>440</audio_pid>
    <audio_pid>441</audio_pid>
  </audio_pids>
  </pid_map>
  <program_number>5</program_number>
  <type>conductor</type>
</mpts_member>
```
