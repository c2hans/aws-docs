---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-stop-channels-example.html
---

# Example
<a name="performing-bulk-tasks-stop-channels-example"></a>

**Request**

This request starts the channels with the IDs 14 and 10.

```
POST http://198.51.100.0/stop/
----------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
----------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<channel_ids type="array">
  <channel_id>14</channel_id>
  <channel_id>10</channel_id>
</channel_ids>
```

**Response**

```
<task_report>
  <id>43</id>
  <created_at>2015-05-28T11:29:56-07:00</created_at>
  <description>Channel Start</description>
  <failed_count>0</failed_count>
  <successful_count>0</successful_count>
  <task_count>1</task_count>
  <updated_at>2015-05-28T11:29:56-07:00</updated_at>
</task_report>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
