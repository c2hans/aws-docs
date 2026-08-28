---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/including-the-cloud-watch-agent-in-your-am-is.html
---

# Including the CloudWatch agent in your AMIs
<a name="including-the-cloud-watch-agent-in-your-am-is"></a>

The advantage of using this approach is that you don't have to wait for the CloudWatch agent to be installed and configured, and you can immediately begin logging and monitoring. This helps you better monitor your instance provisioning and startup steps in case instances fail to start. This approach is also appropriate if you don't plan to use the Systems Manager agent. If you use this approach, you should evaluate the following considerations:
+ **An update process must exist because AMIs might not include the most recent CloudWatch agent version**. The CloudWatch agent installed in an AMI is only current to the last time the AMI was created. You should include an additional method for updating the agent on a regular basis and when the EC2 instance is provisioned. If you use Systems Manager, you can use the Installing the CloudWatch agent using Systems Manager Distributor and State Manager (p. 20) solution provided in this guide for this. If you don't use Systems Manager, you can use a user data script to update the agent on instance startup and reboot.
+ **Your CloudWatch agent configuration file must be retrieved on instance startup**. If you don't use Systems Manager, you can configure a user data script to retrieve the configuration files on boot and then restart the CloudWatch agent.
+ **The CloudWatch agent must be restarted after your CloudWatch configuration is updated**.
+ **AWS credentials must not be saved in the AMI**. Make sure that no local AWS credentials are stored in the AMI. If you use Amazon EC2, you can apply the necessary IAM role to your instance and avoid local credentials. If you use on-premises instances, you should automate or manually update the instance credentials before starting the CloudWatch agent.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
