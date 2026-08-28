---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-cli-update-channel.html
---

# Update a channel with the AWS CLI
<a name="lake-cli-update-channel"></a>

This section describes how you can use the AWS CLI to update a channel for a CloudTrail Lake integration. You can run the `update-channel` command to update the name of the channel or to specify a different destination event data store. You cannot update the source of a channel.

When you run the command, the `--channel` parameter is required.

The following is an example that demonstrates how to update the channel name and destination.

```
aws cloudtrail update-channel \
--channel aws:cloudtrail:us-east-1:123456789012:channel/EXAMPLE8-0558-4f7e-a06a-43969EXAMPLE \
--name "new-channel-name" \
--destinations '[{"Type": "EVENT_DATA_STORE", "Location": "EXAMPLEf852-4e8f-8bd1-bcf6cEXAMPLE"}, {"Type": "EVENT_DATA_STORE", "Location": "EXAMPLEg922-5n2l-3vz1- apqw8EXAMPLE"}]'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
