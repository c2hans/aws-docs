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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
