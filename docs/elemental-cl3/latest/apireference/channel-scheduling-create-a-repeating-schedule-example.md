---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-create-a-repeating-schedule-example.html
---

# Examples
<a name="channel-scheduling-create-a-repeating-schedule-example"></a>

Create a schedule repeating every Monday 8:00 PM Pacific Daylight Time (UTC-07:00) for an hour:

```
POST http://192.0.2.16/channels/1/schedules
------------------------------------------
Content-type:application/xml
Accept: application/xml
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<schedule>
   <name>MondaysAtEight</name>
   <active type="boolean">false</active>
   <cron>0 3 * * 1</cron>
   <duration type="integer">3600</duration>
   <repeat type="boolean">true</repeat>
</schedule>
```

Create a schedule repeating every Monday—Friday 8:00 PM Eastern Standard Time (UTC-05:00) for an hour:

```
POST http://192.0.2.16/channels/1/schedules
------------------------------------------
Content-type:application/xml
Accept: application/xml
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<schedule>
   <name>WeekdaysAtEight</name>
   <active type="boolean">false</active>
   <cron>0 1 * * 1,2,3,4,5</cron>
   <duration type="integer">3600</duration>
   <repeat type="boolean">true</repeat>
</schedule>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
