---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/cloud-watch-installation-for-amazon-ec2-and-on-premises.html
---

# CloudWatch installation for Amazon EC2 and on premises
<a name="cloud-watch-installation-for-amazon-ec2-and-on-premises"></a>

Automating the CloudWatch agent's installation process helps you quickly and consistently deploy it and capture the required logs and metrics. There are several approaches for automating the CloudWatch agent installation, including multi-account and multi-Region support. The following automated installation approaches are discussed:
+ **Installing the CloudWatch agent using Systems Manager Distributor and Systems Manager State Manager **– We recommend using this approach if your EC2 instances and on-premises servers are running the Systems Manager agent. This ensures that the CloudWatch agent is kept updated and you can report on and remediate servers that don't have the CloudWatch agent. This approach also scales to support multiple accounts and Regions.
+ **Deploying the CloudWatch agent as a part of the user data script during EC2 instance provisioning **– Amazon EC2 allows you to define a startup script that is run when you first boot or reboot. You can define a script to automate the agent's download and installation process. This can also be included in AWS CloudFormation scripts and AWS Service Catalog products. This approach might be appropriate on an as-needed basis if there is a customized agent installation and configuration approach for a specific workload that deviates from your standards.
+ **Including the CloudWatch agent in Amazon Machine Images (AMIs) **– You can install the CloudWatch agent in your custom AMIs for Amazon EC2. The EC2 instances that use the AMI will automatically have the agent installed and started. However, you must ensure the agent and its configuration are regularly updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
