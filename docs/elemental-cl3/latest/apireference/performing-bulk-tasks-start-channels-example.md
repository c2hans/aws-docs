---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/performing-bulk-tasks-start-channels-example.html
---

# Example
<a name="performing-bulk-tasks-start-channels-example"></a>

**Request**

This request starts the channels with the IDs 14, 8 and 10.

```
POST http://198.51.100.0/channels/start
----------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
----------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<channel_ids type="array">
  <channel_id>14</channel_id>
  <channel_id>8</channel_id>
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
