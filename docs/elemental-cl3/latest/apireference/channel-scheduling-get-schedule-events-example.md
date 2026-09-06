---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-get-schedule-events-example.html
---

# Example
<a name="channel-scheduling-get-schedule-events-example"></a>

This response shows the information for the schedule with the ID 15.

```
<?xml version="1.0" encoding="UTF-8"?>
<schedule_events href="/events" product="AWS Elemental Conductor Live + Cable Package + Audio Package + Audio Normalization Package + Audio Decode Package + HEVC Package + AWS Elemental Statmux Package + Motion Image Inserter Package" version="3.2.0.41691" type="array">
    <schedule_event>
        <id type="integer">801</id>
        <start_at type="datetime">2016-07-08T10:00:00-07:00</start_at>
        <stop_at type="datetime">2016-07-08T10:01:00-07:00</stop_at>
        <state type="integer">1</state>
        <message></message>
        <schedule_id type="integer">15</schedule_id>
    </schedule_event>
</schedule_events>
```
