---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-get-attributes-of-a-schedule-example.html
---

# Example
<a name="channel-scheduling-get-attributes-of-a-schedule-example"></a>

This response shows the information for the schedule with the ID 13.

```
<schedule>
    <id type="integer">13</id>
    <name>MthruF</name>
    <active type="boolean">false</active>
    <cron>0 3 * * 1,2,3,4,5</cron>
    <duration type="integer">3600</duration>
    <repeat type="boolean">true</repeat>
</schedule>
```
