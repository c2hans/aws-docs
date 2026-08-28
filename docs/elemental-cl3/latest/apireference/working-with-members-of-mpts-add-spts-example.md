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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
