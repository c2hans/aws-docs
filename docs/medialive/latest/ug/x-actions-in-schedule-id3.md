---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/x-actions-in-schedule-id3.html
---

# How ID3 metadata actions work
<a name="x-actions-in-schedule-id3"></a>

You can set up an action to insert ID3 data in the channel. You can set up an action to insert ID3 data in each segment in the following types of outputs:
+ CMAF Ingest
+ HLS
+ MediaPackage

Before you add ID3 metadata actions to the schedule, read [Inserting ID3 metadata using the schedule](insert-id3-metadata-via-schedule.md).

**Insert ID3 metadata with fixed start**

When you create the action, you include a start time. The start time for the action must be at least 15 seconds in the future but not more than 14 days in the future. After that cutoff, MediaLive rejects the request to create the action.

After you have created the action, the action sits in the schedule. Approximately 15 seconds before the start time, the schedule passes the action to the channel. At the start time, the channel inserts the data into the channel.

**Insert ID3 metadata with immediate start**

When you create the action, you set the start type to *immediate*.

The schedule immediately passes the action to the channel. The channel immediately inserts the data into the channel.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
