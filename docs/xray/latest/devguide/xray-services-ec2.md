---
source_url: https://docs.aws.amazon.com/xray/latest/devguide/xray-services-ec2.html
---

# Amazon Elastic Compute Cloud and AWS X-Ray
<a name="xray-services-ec2"></a>

You can install and run the X-Ray daemon on an Amazon EC2 instance with a user data script. See [Running the X-Ray daemon on Amazon EC2](xray-daemon-ec2.md) for instructions.

Use an instance profile to grant the daemon permission to upload trace data to X-Ray. For more information, see [Giving the daemon permission to send data to X-Ray](xray-daemon.md#xray-daemon-permissions).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
