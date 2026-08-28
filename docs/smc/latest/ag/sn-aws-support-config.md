---
source_url: https://docs.aws.amazon.com/smc/latest/ag/sn-aws-support-config.html
---

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html).

# Configuring ServiceNow for integration with Support
<a name="sn-aws-support-config"></a>

This section shows you how to integrate Support in ServiceNow.

****To conﬁgure the Support integration System Properties****

1. In the navigator, enter **AWS Service Management**.

1. Choose **System Properties**, then **Support**.

1. Set the system property, as required.

| Available settings | Description |
| --- | --- |
| **Interval**, in minutes, between the execution of full synchronization | Default: **1440 min**  |
| SQS Name created by the CloudFormation stack. The same name must be used for all accounts | Default: AwsServiceManagementConnectorForSupportQueue |
| (Advanced mode) Enable an intermediate table (SMC Support Case table) to synchronize data to and from Support. Use caution; enabling an intermediate table replaces the default Incident table. | Default: False |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Management Connector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query smc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
