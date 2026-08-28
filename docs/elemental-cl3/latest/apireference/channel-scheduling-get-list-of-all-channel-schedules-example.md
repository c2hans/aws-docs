---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/channel-scheduling-get-list-of-all-channel-schedules-example.html
---

# Example
<a name="channel-scheduling-get-list-of-all-channel-schedules-example"></a>

This response shows two schedules:
+ One schedule has the ID 13 and is a repeating schedule that runs the channel on weekdays for an hour.
+ The other schedule has the ID 20 and will run the channel one time for half an hour.

```
GET http://198.51.100.0/channels/1/schedules
------------------------------------------
Content-type:application/xml
<?xml version="1.0" encoding="UTF-8"?>
<schedules href="/channels/1/schedules" product="AWS Elemental Conductor Live + Cable Package + Audio Package + Audio Normalization Package + Audio Decode Package + HEVC Package + AWS Elemental Statmux Package + Motion Image Inserter Package" version="3.2.0.41691" type="array">
    <schedule>
        <id type="integer">13</id>
        <name>MthruF</name>
        <active type="boolean">false</active>
        <cron>0 3 * * 1,2,3,4,5</cron>
        <duration type="integer">3600</duration>
        <repeat type="boolean">true</repeat>
    </schedule>
    <schedule>
        <id type="integer">20</id>
        <name>OneTime</name>
        <active type="boolean">false</active>
        <duration type="integer">1800</duration>
        <repeat type="boolean">false</repeat>
        <run_at type="datetime">2016-07-07T15:22:00-07:00</run_at>
    </schedule>
</schedules>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
