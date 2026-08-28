---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/neptune-BG-monitoring.html
---

# Monitoring the progress of a Neptune Blue/Green deployment
<a name="neptune-BG-monitoring"></a>

You can monitor the progress of the Neptune Blue/Green solution by going to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/) and looking at logs in the `/aws/neptune/{{(Neptune Blue/Green deployment ID)}}` CloudWatch log group. You can find a link to the CloudWatch logs in the outputs of the solution's CloudFormation stack:

![Screenshot of the Blue/Green CloudFormation stack output](http://docs.aws.amazon.com/neptune/latest/userguide/images/BG-stack-output.png)

If you provided a public subnet as a stack parameter, you can also SSH to your Amazon EC2 instance created as part of the stack and refer to the log in `/var/log/cloud-init-output.log`.

The log shows the actions taken by the Neptune Blue/Green solution, as shown in this screenshot:

![Screenshot of the Neptune Blue/Green log screen](http://docs.aws.amazon.com/neptune/latest/userguide/images/BG-log-screenshot.png)

Log messages show the sync status between the blue and green clusters:

![Screenshot of Neptune Blue/Green solution log messages](http://docs.aws.amazon.com/neptune/latest/userguide/images/BG-log-messages.png)

The sync process checks the replication lag by computing the difference between the latest stream `eventID` on the blue cluster and the replication checkpoint present in the DynamoDB checkpoint table created by the Neptune-to-Neptune replication stack. Using these messages, you can monitor the current replication difference.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
