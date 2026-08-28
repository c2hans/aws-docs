---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/StopTheCWLAgent.html
---

# Stop the CloudWatch Logs agent
<a name="StopTheCWLAgent"></a>

Use the following procedure to stop the CloudWatch Logs agent on your EC2 instance.

**To stop the agent**

1. Connect to your EC2 instance. For more information, see [Connect to Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-connect-to-instance-linux.html) in the *Amazon EC2 User Guide*.

   For more information about connection issues, see [Troubleshooting Connecting to Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html) in the *Amazon EC2 User Guide*.

1. At a command prompt, type the following command:

   ```
   sudo service awslogs stop
   ```

   If you are running Amazon Linux 2, type the following command:

   ```
   sudo service awslogsd stop
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
