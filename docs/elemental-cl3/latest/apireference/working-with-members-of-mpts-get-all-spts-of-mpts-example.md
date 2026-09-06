---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-get-all-spts-of-mpts-example.html
---

# Example
<a name="working-with-members-of-mpts-get-all-spts-of-mpts-example"></a>

**Request**

```
GET http://198.51.100.0/mpts/3/mpts_members
```

**Response**

```
<?xml version="1.0" encoding="UTF-8"?>
<mpts_members>
  <mpts_member>
    <id type="integer">3</id>
    <mpts_id type="integer">3</mpts_id>
    <created_at type="datetime">2015-08-18T13:46:23-07:00</created_at>
    <updated_at type="datetime">2015-08-18T13:46:23-07:00</updated_at>
    <channel_id type="integer">6</channel_id>
    <name>Channel_A</name>
    <pid_map>
      <pmt_pid type="integer">100</pmt_pid>
      <video_pid type="integer">101</video_pid>
    </pid_map>
    <program_number type="integer">1</program_number>
    <type>conductor</type>
    <input>
      <uri>udp://127.0.0.1:5004</uri>
    </input>
    <secondary_input nil="true"/>
    <allocation_transmit_destination>
      <uri>udp://127.0.0.1:5005</uri>
    </allocation_transmit_destination>
    <secondary_allocation_transmit_destination nil="true"/>
    <complexity_receipt_destination>
      <uri>udp://127.0.0.1:5002</uri>
    </complexity_receipt_destination>
    <secondary_complexity_receipt_destination nil="true"/>
  </mpts_member>
</mpts_members>
```
