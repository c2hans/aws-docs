---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-create-cw-alarms.html
---

# Creating additional CloudWatch alarms for Accelerate
<a name="acc-mem-create-cw-alarms"></a>

You can create additional CloudWatch alarms for AMS Accelerate using custom CloudWatch metrics and alarms for Amazon EC2 instances.

Produce your application monitoring script and custom metric. For more information and access to example scripts, see [Monitoring Memory and Disk Metrics for Amazon EC2 Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mon-scripts.html).

The CloudWatch monitoring scripts for Linux Amazon EC2 instances demonstrate how to produce and consume custom CloudWatch metrics. These sample Perl scripts comprise a fully functional example that reports memory, swap, and disk space utilization metrics for a Linux instance.

**Important**
AMS Accelerate does not monitor CloudWatch alarms created by you.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
