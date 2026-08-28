---
source_url: https://docs.aws.amazon.com/res/latest/ug/log-groups.html
---

# Amazon CloudWatch Logs
<a name="log-groups"></a>

Research and Engineering Studio creates the following log groups in CloudWatch during installation. See the following table for default retentions:

| CloudWatch Log groups | Retention |
| --- | --- |
| /aws/lambda/{{<installation-stack-name>}}-cluster-endpoints | Never expire |
| /aws/lambda/{{<installation-stack-name>}}-cluster-manager-scheduled-ad-sync | Never expire |
| /aws/lambda/{{<installation-stack-name>}}-cluster-settings | Never expire |
| /aws/lambda/{{<installation-stack-name>}}-oauth-credentials | Never expire |
| /aws/lambda/{{<installation-stack-name>}}-self-signed-certificate | Never expire |
| /aws/lambda/{{<installation-stack-name>}}-update-cluster-prefix-list | Never expire |
| /aws/lambda/{{<installation-stack-name>}}-vdc-scheduled-event-transformer | Never expire |
| /aws/lambda/{{<installation-stack-name>}}-vdc-update-cluster-manager-client-scope | Never expire |
| /aws/lambda/{{<installation-stack-name>}}-backend-lambda | Never expire |
| /aws/lambda/{{<environment-name>}}-dcv-session-management-lambda | Never expire |
| /{{<installation-stack-name>}}/cluster-manager | 3 months |
| /{{<installation-stack-name>}}/vdc/controller | 3 months |
| /{{<installation-stack-name>}}/vdc/dcv-connection-gateway | 3 months |

If you would like to change the default retention for a log group, you can go to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch) and follow the directions to [ Change log data retention in CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Research and Engineering Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query res` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
