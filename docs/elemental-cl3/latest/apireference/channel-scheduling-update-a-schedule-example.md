---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-update-a-schedule-example.html
---

# Example
<a name="channel-scheduling-update-a-schedule-example"></a>

To change the name of schedule 17 on channel 1 to “NewName” send the following:

```
PUT http://198.51.100.0/channels/1/schedules/17
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<schedule>
  <name>NewName</name>
</schedule>
```
