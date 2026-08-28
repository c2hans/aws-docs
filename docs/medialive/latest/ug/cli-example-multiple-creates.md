---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/cli-example-multiple-creates.html
---

# Combination of create actions
<a name="cli-example-multiple-creates"></a>

Here is an example of a JSON body to pass into the `--creates` parameter of the `batch-update-schedule` AWS CLI command. It contains two actions to create. In this example, both actions are splice\_inserts, but in fact you can combine any number and any type of create actions.

```
{
    "ScheduleActions": [
      {
        "ScheduleActionSettings": {
          "Scte35SpliceInsertSettings": {
            "Duration": 1350000,
            "SpliceEventId": 3
          }
        },
        "ActionName": "SpliceInsert-01",
        "ScheduleActionStartSettings": {
          "FixedModeScheduleActionStartSettings": {
            "Time": "2018-11-05T16:10:30.000Z"
          }
        }
      },
      {
        "ScheduleActionSettings": {
          "Scte35SpliceInsertSettings": {
            "Duration": 2700000,
            "SpliceEventId": 3
          }
        },
        "ActionName": "SpliceInsert-02",
        "ScheduleActionStartSettings": {
          "FixedModeScheduleActionStartSettings": {
            "Time": "2018-11-05T16:30:45.000Z"
          }
        }
      }
    ]
  }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
