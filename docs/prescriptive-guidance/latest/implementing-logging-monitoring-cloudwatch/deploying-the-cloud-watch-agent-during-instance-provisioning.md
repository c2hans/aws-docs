---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/deploying-the-cloud-watch-agent-during-instance-provisioning.html
---

# Deploying the CloudWatch agent during instance provisioning
<a name="deploying-the-cloud-watch-agent-during-instance-provisioning"></a>

You can use this approach if you don't plan to use Systems Manager and want to selectively use CloudWatch for your EC2 instances. Typically, this approach is used on a one-time basis or when a specialized configuration is required. AWS provides [direct links](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/download-cloudwatch-agent-commandline.html) for the CloudWatch agent that can be downloaded in your start-up or user data scripts. The agent installation packages can be silently run without user interaction, which means that you can use them in automated deployments. If you use this approach, you should evaluate the following considerations:
+ **Increased risk that users won't install the agent or configure standard metrics**. Users might provision instances without including the necessary steps to install the CloudWatch agent. They could also misconfigure the agent, which might cause logging and monitoring inconsistencies.
+ **The installation scripts must be OS specific and suitable for different OS versions**. You require separate scripts if you intended to use both Windows and Linux. The Linux script should also have different installation steps based on the distribution.
+ **You must regularly update the CloudWatch agent with new versions when available**. This can be automated if you use Systems Manager with State Manager, but you can also configure the user data script to rerun on instance startup. The CloudWatch agent is then updated and reinstalled on every reboot.
+ **You must automate the retrieval and application of standard CloudWatch configurations**. This can be automated if you use Systems Manager with State Manager, but you can also configure a user data script to retrieve the configuration files on boot and restart the CloudWatch agent.
