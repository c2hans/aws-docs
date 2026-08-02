---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/connecting-to-instances.html
---

# Connecting to AL2023 instances
<a name="connecting-to-instances"></a>

Use SSH or AWS Systems Manager to connect to your AL2023 instance.

**Connect to your instance using SSH**
For instructions on how to use SSH to connect to an instance, see [Connect to your Linux instance using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html) in the *Amazon EC2 User Guide*.

**Connect to your instance using AWS Systems Manager**
For instructions on how to use AWS Systems Manager to connect to an AL2023 instance, see [Connect to your Linux instance using Session Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/session-manager.html) in the *Amazon EC2 User Guide*.

**Using Amazon EC2 Instance Connect**
The AL2023 AMI, excluding the minimal AMI, comes with the EC2 Instance Connect agent installed by default. To use EC2 Instance Connect with an AL2023 instance launched from the minimal AMI, you must install the `ec2-instance-connect` package. For instructions on using EC2 Instance Connect, see [Connect to your Linux instance with EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-eic.html) in the *Amazon EC2 User Guide*.
