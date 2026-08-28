---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/operational-metrics-and-alarms.html
---

# Operational metrics and alarms
<a name="operational-metrics-and-alarms"></a>

 This solution has a dash to list all the metrics for monitoring the core Lambdas and DynamoDB tables.

1.  Navigate to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home).

1.  Select dashboard with prefix `RuleExtensionServiceDashboard`.

 The metrics includes lambda invoke latency, API Gateway call response status and Error, DynamoDB capacity and latency.

 This solution tolerates underlying system failure to prevent catastrophic cascade effect to your configured rules and firewall configurations. The primary design principle is to preserve the rule status in the database and AWS Network Firewall if underlying system failure happens. Once the impaired systems back up, the rules can sync up to the network firewall.

 The following table lists potential service failures and the handling mechanism in place:

|  **Service Name**  |  **Failure Type**  |  **Handling Mechanism**  |  **Behaviours once service back online**  |
| --- | --- | --- | --- |
|  AWS Config  |  Unreachable  |  Send notification to registered email, trigger alarm in CloudWatch  |  All the rules will be re-evaluated and applied to AWS Network Firewall, no rules will be marked as failed (because of the AWS Config failure) during the process  |
|   |  Internal Error  |  Send notification to registered email, trigger alarm in CloudWatch  |  \*  |
|  AWS Network Firewall  |  Unreachable  |  Error rate alarm in CloudWatch  |  \*  |
|   |  Internal Error  |  Error rate alarm in CloudWatch  |  \*  |
|  AWS EventBridge  |  Fail to send trigger event  |  Invocation alarm triggers in CloudWatch  |  \*  |
|  AWS DynamoDB  |  Unreachable  |  Trigger alarm in CloudWatch  |  \*  |

 Find the alarms configured for this solution by navigating to the CloudWatch console and selecting Alarms. By default, the alarms’ action is to send an email to the registered email address. Refer to [Update solution configuration](deployment.md#step-1.-update-solution-configuration) for information about how to configure alarms.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Object and Rule Extensions for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
