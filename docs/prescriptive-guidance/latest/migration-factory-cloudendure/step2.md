---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-factory-cloudendure/step2.html
---

# Step 2. Build the servers
<a name="step2"></a>

After you import the application and server metadata, you verify the source machines and install the replication agent to start data replication.

## Verify prerequisites for source servers
<a name="2-verify-prereq"></a>

In this step, you make sure that your source servers have the required configuration to start the data replication. For example, if the source server is a Windows server, it must meet these requirements:
+ TCP port 443 outbound must be open for the source machine to connect to the AWS Transform MGN console.
+ TCP port 1500 outbound must be open for the source machine to connect to the MGN replication server in the target virtual private cloud (VPC) on AWS.
+ The server must be running .NET Framework version 3.5 or later.
+ The server must have at least 3 GB of free space on drive C.

Cloud Migration Factory includes an automation script that you run on the migration execution server to verify the prerequisites automatically for all source Windows and Linux servers.

For detailed instructions, see [Check prerequisites](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/list-of-automated-migration-activities-using-factory-web-console.html#prerequisites-2) in the *Cloud Migration Factory Implementation Guide*.

## Install the replication agent
<a name="2-install-agent"></a>

After checking the prerequisites, you install the replication agent on the source machines. This process usually takes 5-10 minutes per server, but Cloud Migration Factory includes an automation script to push the agents to all the source servers in the same wave. This script works for multiple target AWS Regions and accounts.

The agent installation script uses the AWS API to pull the installation token for the target AWS account.

For detailed instructions, see [Install the replication agents](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/list-of-automated-migration-activities-using-factory-web-console.html#install-the-replication-agents) in the *Cloud Migration Factory Implementation Guide*.

## Push the post-launch script
<a name="2-post-launch"></a>

One of the common tasks of rehost migration is uninstalling old software such as VMware tools and backup software from target EC2 instances, and installing new software such as the AWS Systems Manager agent. Completing these activities manually could take 15–30 minutes per server, but Cloud Migration Factory automates this process to accelerate the cutover time.

MGN supports post-launch scripts that help you automatically run operating system configuration tasks, such as installing or uninstalling software.

For detailed instructions, see [Push the post-launch scripts](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/list-of-automated-migration-activities-using-factory-web-console.html#push-the-post-launch-scripts) in the *Cloud Migration Factory Implementation Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
