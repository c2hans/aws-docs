---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/data-channel.html
---

# Understanding messages in the data-channel folder for Amazon Chime SDK media capture pipelines
<a name="data-channel"></a>

The data-channel folder contains data messages in the .txt format, and each message is a JSON object. Messages are visible with all configurations options. File names contain the *yyyy-mm-dd-hour-min-seconds-milleseconds* timestamp. This example shows the data fields in a message.

```
{
    "Timestamp": "{{string}}",
    "Topic": "{{string}}",
    "Data": "{{string}}",
    "SenderAttendeeId": "{{string}}"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
