---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-deactivate-mgi.html
---

# Deactivate motion graphic overlay – payload
<a name="cli-schedule-fields-deactivate-mgi"></a>

For information about the meaning and values for the fields in the following JSON, see [Fields for deactivating a motion graphics overlay](schedule-fields-for-mg-deactivate.md).

```
{
"ChannelId": "string",
"Creates": {
 "ScheduleActions": [
  {
   "ScheduleActionStartSettings": {
    "FixedModeScheduleActionStartSettings": {
     "Time": "string"
    },
    "ImmediateModeScheduleActionStartSettings": {
    }
   },
   "ActionName": "string",
   "ScheduleActionSettings": {
    "MotionGraphicsImageDeactivateSettings": {
     }
    }
   }
  ]
 }
}
```

## Example
<a name="json-deactivate-mgi-example"></a>

This example of a request creates an action to end a motion graphic overlay at 23:59:00.000 (UTC). :

```
{
"ChannelId": "999999",
"Creates": {
 "ScheduleActions": [
  {
  "ScheduleActionStartSettings": {
   "FixedModeScheduleActionStartSettings": {
   "Time": "2018-05-21T23:59:00.000Z"
   },
   "ActionName": "deactivate-ticker-tape",
   "ScheduleActionSettings": {
    "MotionGraphicsImageDeactivateSettings": {
     }
    }
   }
  ]
 }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
