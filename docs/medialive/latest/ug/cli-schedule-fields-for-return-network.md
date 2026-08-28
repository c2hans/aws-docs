---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-for-return-network.html
---

# Return-to-network message – payload
<a name="cli-schedule-fields-for-return-network"></a>

For information about the meaning and values for the fields in the following JSON, see [Fields for a return-to-network message](schedule-fields-for-return-to-network.md).

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
    "Scte35ReturnToNetworkSettings": {
     "SpliceEventId": integer
    }
   }
  }
 ]
}
```

## Example
<a name="json-return-network-example"></a>

This example of a request creates a return-to-network with a UTC start time of 20:42:19.

```
{
  "ChannelId": "999999",
  "Creates": {
    "ScheduleActions": [
      {
        "ScheduleActionStartSettings": {
          "FixedModeScheduleActionStartSettings": {
            "Time": "2018-05-21T20:42:19.000Z"
          }
      },
      "ActionName": "end-adavail-3708",
      "ScheduleActionSettings": {
        "Scte35ReturnToNetworkSettings": {
          }
        }
      }
    ]
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
