---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-fields-for-deactivate-image.html
---

# Deactivate global overlay action – payload
<a name="cli-schedule-fields-for-deactivate-image"></a>

For information about the meaning and values for the fields in the following JSON, see [Fields for deactivating a global image overlay](schedule-fields-for-deactivate-image.md).

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
    "StaticImageDeactivateSettings": {
     "FadeOut": integer,
     "Layer": integer
    }
   }
  }
 ]
}
```

## Example
<a name="json-deactivate-image-example"></a>

This example of a request creates an action to remove an image overlay at 20:42:04.000 (UTC) with a 500-millisecond fadeout that is added onto the end time, which means that the overlay will be invisible at 20:42:04.500.

The action removes the images overlay that is in the global layer 4. This means it removes the image *only if* it was inserted using the global action (StaticImageActivateSettings). It doesn't remove the overlay from the per-outputs layer 4.

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
      "ActionName": "stop-overlay-029",
      "ScheduleActionSettings": {
        "StaticImageDeactivateSettings": {
          "FadeOut": 500,
          "Layer": 4
          }
        }
      }
    ]
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
