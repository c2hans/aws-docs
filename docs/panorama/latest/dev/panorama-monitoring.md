---
source_url: https://docs.aws.amazon.com/panorama/latest/dev/panorama-monitoring.html
---

End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

# Monitoring AWS Panorama resources and applications
<a name="panorama-monitoring"></a>

You can monitor AWS Panorama resources in the AWS Panorama console and with Amazon CloudWatch. The AWS Panorama Appliance connects to the AWS Cloud over the internet to report its status and the status of connected cameras. While it is on, the appliance also sends logs to CloudWatch Logs in real time.

The appliance gets permission to use AWS IoT, CloudWatch Logs, and other AWS services from a service role that you create the first time that you use the AWS Panorama console. For more information, see [AWS Panorama service roles and cross-service resources](permissions-services.md).

For help troubleshooting specific errors, see [Troubleshooting](panorama-troubleshooting.md).

**Topics**
+ [Monitoring in the AWS Panorama console](monitoring-console.md)
+ [Viewing AWS Panorama logs](monitoring-logging.md)
+ [Monitoring appliances and applications with Amazon CloudWatch](monitoring-metrics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
