---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-activate-mgi.html
---

# Activate motion graphic overlay – payload
<a name="cli-schedule-fields-activate-mgi"></a>

For information about the meaning and values for the fields in the following JSON, see [Fields for activating a motion graphics overlay](schedule-fields-for-mg.md).

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
    "MotionGraphicsImageActivateSettings": {
     "Duration": integer
     "Url": "string"
     "Username": "string",
     "PasswordParam": "string"
    }
   }
  ]
 }
}
```

## Example
<a name="json-activate-mgi-example"></a>

This example of a request creates a motion graphics overlay action called mg\_ticker\_tape. The motion graphic asset is stored at http://example.com/ticker\_tape.html. This server requires user credentials. The request doesn't include a duration. Instead, the intention is to send a separate deactivate request at the appropriate time.

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
   "ActionName": "mg_ticker_tape",
   "ScheduleActionSettings": {
    "MotionGraphicsImageActivateSettings": {
     "Url": "https://example.com/ticker_tape.html"
     "Username": "medialiveoperator",
     "PasswordParam": "/medialive/12345"
    }
   }
  ]
 }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
