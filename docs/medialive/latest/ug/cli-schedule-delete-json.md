---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/cli-schedule-delete-json.html
---

# JSON payload for delete actions
<a name="cli-schedule-delete-json"></a>

 In the `Deletes` section, include the list of actions to delete by entering an array of `ActionNames`. The array contains one or more action names. You can obtain these action names using the `DescribeChannel` command (see [Viewing the schedule (AWS CLI)](viewing-schedule-using-cli.md).

```
{
  "ChannelId": "string",
  "Deletes": {
      "ActionNames": [
          ""
    ]
  }
}
```

## Example
<a name="cli-schedule-delete-json-example"></a>

This example of a request deletes the three actions identified by `ActionNames` that were assigned when you created the actions.

```
{
  "ChannelId": "999999",
  "Deletes": {
      "ActionNames": [
          "stop-overlay-33",
          "adavail-3711",
          "end-adavail-3711"
      ]
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
