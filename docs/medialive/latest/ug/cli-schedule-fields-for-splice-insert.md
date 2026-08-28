---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-for-splice-insert.html
---

# Splice\_insert message – payload
<a name="cli-schedule-fields-for-splice-insert"></a>

For information about the meaning and values for the fields in the following JSON, see [Fields for a splice\_insert message](schedule-fields-for-splice_insert.md).

```
{
 "ScheduleActions": [
  {
   "ScheduleActionStartSettings": {
    "FixedModeScheduleActionStartSettings": {
     "Time": "string"
    },
    "FollowModeScheduleActionStartSettings": {
     "FollowPoint": "enum",
     "ReferenceActionName": "string"
    },
    "ImmediateModeScheduleActionStartSettings": {
    }
   },
   "ActionName": "string",
   "ScheduleActionSettings": {
    "Scte35SpliceInsertSettings": {
     "Duration": integer,
     "SpliceEventId": integer
    }
   }
  }
 ]
}
```

## Example of a splice insert with a fixed start time
<a name="json-splice-insert-example"></a>

This example of a request creates an action for a splice\_insert with a UTC start time of 20:42:04.000. It also has an `ActionName` that perhaps references an ad avail from your database, a unique integer for the splice event ID, and a duration of 1,350,000 kHz ticks (15 seconds).

```
{
  "ChannelId": "999999",
  "Creates": {
    "ScheduleActions": [
      {
        "ScheduleActionStartSettings": {
          "FixedModeScheduleActionStartSettings": {
            "Time": "2018-05-21T20:42:04.000Z"
          }
        },
      "ActionName": "adavail-3708",
      "ScheduleActionSettings": {
        "Scte35SpliceInsertSettings": {
          "SpliceEventId": 3708,
          "Duration": 1350000
          }
        }
      }
    ]
  }
}
```

## Example of a splice insert as a follow
<a name="json-splice-insert-example2"></a>

This example of a request creates an action for a splice\_insert to be inserted after the input switch called nature-doco-003 ends. The action has an `ActionName` that perhaps references an ad avail from your database, a unique integer for the splice event ID, and a duration of 1,350,000 kHz ticks (15 seconds).

Follow mode for a SCTE 35 message is useful when you want an ad avail to occur as soon as an input finishes, but you don't know when that will happen.

```
{
  "ChannelId": "999999",
  "Creates": {
    "ScheduleActions": [
      {
        "ScheduleActionStartSettings": {
         "FollowModeScheduleActionStartSettings": {
                "FollowPoint": "END",
                "ReferenceActionName": "nature-doco-003"
        }
      },
      "ActionName": "adavail-3708",
      "ScheduleActionSettings": {
        "Scte35SpliceInsertSettings": {
          "SpliceEventId": 3708,
          "Duration": 1350000
          }
        }
      }
    ]
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
