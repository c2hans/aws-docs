---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-create-a-one-time-schedule-example.html
---

# Example
<a name="channel-scheduling-create-a-one-time-schedule-example"></a>

```
POST http://192.0.2.16/channels/1/schedules
------------------------------------------
Content-type:application/xml
Accept: application/xml
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<schedule>
    <name>RunOneHour</name>
    <active>true</active>
    <duration>3600</duration>
    <repeat>false</repeat>
    <run_at>2017-09-06T13:24:00-07:00</run_at>
</schedule>
```
