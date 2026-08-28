---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html
---

# Installing the CloudWatch agent
<a name="install-CloudWatch-Agent-on-EC2-Instance"></a>

You can install the CloudWatch agent on your Amazon EC2 instances, on-premises servers, and in containerized environments to collect metrics, logs, and traces. The agent supports Linux, Windows, and macOS operating systems. There are several ways to install the agent, including using Systems Manager, from the CloudWatch console, installing from the command line, or installing using a configuration file. Before installing, make sure you have the required IAM permissions and network access configured.

**Topics**
+ [Install and Configure Amazon CloudWatch Agent with Workload Detection in the CloudWatch console](install-cloudwatch-agent-workload-detection.md)
+ [Manual installation on Amazon EC2](manual-installation.md)
+ [Install the CloudWatch agent using AWS Systems Manager](installing-cloudwatch-agent-ssm.md)
+ [Install the CloudWatch agent on on-premises servers](install-CloudWatch-Agent-on-premise.md)
+ [Install the CloudWatch agent on Azure](install-CloudWatch-Agent-on-Azure.md)
+ [Install the CloudWatch agent on new instances using CloudFormation](Install-CloudWatch-Agent-New-Instances-CloudFormation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
