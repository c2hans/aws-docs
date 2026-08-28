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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
