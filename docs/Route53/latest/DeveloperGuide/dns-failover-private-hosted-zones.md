---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html
---

# Configuring failover in a private hosted zone
<a name="dns-failover-private-hosted-zones"></a>

If you're creating failover records in a private hosted zone, note the following:
+ Route 53 health checkers are outside the VPC. To check the health of an endpoint within a VPC by IP address, you must assign a public IP address to the instance in the VPC.
+ You can create a CloudWatch metric, associate an alarm with the metric, and then create a health check that is based on the data stream for the alarm. For example, you might create a CloudWatch metric that checks the status of the EC2 `StatusCheckFailed` metric, add an alarm to the metric, and then create a health check that is based on the data stream for the alarm to check instances within a Virtual Private Cloud (VPC) that only have private IP addresses. For information about creating CloudWatch metrics and alarms by using the CloudWatch console, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/).

For more information, see [Working with private hosted zones](hosted-zones-private.md) and [Monitoring health checks using CloudWatch](monitoring-health-checks.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
