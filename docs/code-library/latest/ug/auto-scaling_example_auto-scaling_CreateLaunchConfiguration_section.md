---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_CreateLaunchConfiguration_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateLaunchConfiguration` with a CLI
<a name="auto-scaling_example_auto-scaling_CreateLaunchConfiguration_section"></a>

The following code examples show how to use `CreateLaunchConfiguration`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To create a launch configuration**
This example creates a simple launch configuration.

```
aws autoscaling create-launch-configuration \
    --launch-configuration-name {{my-lc}} \
    --image-id {{ami-04d5cc9b88example}} \
    --instance-type {{m5.large}}
```
This command produces no output.
For more information, see [Creating a launch configuration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-config.html) in the *Amazon EC2 Auto Scaling User Guide*.
**Example 2: To create a launch configuration with a security group, key pair, and bootstrapping script**
This example creates a launch configuration with a security group, a key pair, and a bootstrapping script contained in the user data.

```
aws autoscaling create-launch-configuration \
    --launch-configuration-name {{my-lc}} \
    --image-id {{ami-04d5cc9b88example}} \
    --instance-type {{m5.large}} \
    --security-groups {{sg-eb2af88example}} \
    --key-name {{my-key-pair}} \
    --user-data {{file://myuserdata.txt}}
```
This command produces no output.
For more information, see [Creating a launch configuration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-config.html) in the *Amazon EC2 Auto Scaling User Guide*.
**Example 3: To create a launch configuration with an IAM role**
This example creates a launch configuration with the instance profile name of an IAM role.

```
aws autoscaling create-launch-configuration \
    --launch-configuration-name {{my-lc}} \
    --image-id {{ami-04d5cc9b88example}} \
    --instance-type {{m5.large}} \
    --iam-instance-profile {{my-autoscaling-role}}
```
This command produces no output.
For more information, see [IAM role for applications that run on Amazon EC2 instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html) in the *Amazon EC2 Auto Scaling User Guide*.
**Example 4: To create a launch configuration with detailed monitoring enabled**
This example creates a launch configuration with EC2 detailed monitoring enabled, which sends EC2 metrics to CloudWatch in 1-minute periods.

```
aws autoscaling create-launch-configuration \
    --launch-configuration-name {{my-lc}} \
    --image-id {{ami-04d5cc9b88example}} \
    --instance-type {{m5.large}} \
    --instance-monitoring {{Enabled=true}}
```
This command produces no output.
For more information, see [Configuring monitoring for Auto Scaling instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/enable-as-instance-metrics.html) in the *Amazon EC2 Auto Scaling User Guide*.
**Example 5: To create a launch configuration that launches Spot Instances**
This example creates a launch configuration that uses Spot Instances as the only purchase option.

```
aws autoscaling create-launch-configuration \
    --launch-configuration-name {{my-lc}} \
    --image-id {{ami-04d5cc9b88example}} \
    --instance-type {{m5.large}} \
    --spot-price {{"0.50"}}
```
This command produces no output.
For more information, see [Requesting Spot Instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-launch-spot-instances.html) in the *Amazon EC2 Auto Scaling User Guide*.
**Example 6: To create a launch configuration using an EC2 instance**
This example creates a launch configuration based on the attributes of an existing instance. It overrides the placement tenancy and whether a public IP address is set by including the `--placement-tenancy` and `--no-associate-public-ip-address` options.

```
aws autoscaling create-launch-configuration \
    --launch-configuration-name {{my-lc-from-instance}} \
    --instance-id {{i-0123a456700123456}} \
    --instance-type {{m5.large}} \
    --no-associate-public-ip-address \
    --placement-tenancy {{dedicated}}
```
This command produces no output.
For more information, see [Creating a launch configuration using an EC2 instance](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-lc-with-instanceID.html) in the *Amazon EC2 Auto Scaling User Guide*.
**Example 7: To create a launch configuration with a block device mapping for an Amazon EBS volume**
This example creates a launch configuration with a block device mapping for an Amazon EBS `gp3` volume with the device name `/dev/sdh` and a volume size of 20.

```
aws autoscaling create-launch-configuration \
    --launch-configuration-name {{my-lc}} \
    --image-id {{ami-04d5cc9b88example}} \
    --instance-type {{m5.large}} \
    --block-device-mappings '{{[{"DeviceName":"/dev/sdh","Ebs":{"VolumeSize":20,"VolumeType":"gp3"}}]}}'
```
This command produces no output.
For more information, see [EBS](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_Ebs.html) in the *Amazon EC2 Auto Scaling API Reference*.
For information about the syntax for quoting JSON-formatted parameter values, see [Using quotation marks with strings in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS Command Line Interface User Guide*.
**Example 8: To create a launch configuration with a block device mapping for an instance store volume**
This example creates a launch configuration with `ephemeral1` as an instance store volume with the device name `/dev/sdc`.

```
aws autoscaling create-launch-configuration \
    --launch-configuration-name {{my-lc}} \
    --image-id {{ami-04d5cc9b88example}} \
    --instance-type {{m5.large}} \
    --block-device-mappings '{{[{"DeviceName":"/dev/sdc","VirtualName":"ephemeral1"}]}}'
```
This command produces no output.
For more information, see [BlockDeviceMapping](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_BlockDeviceMapping.html) in the *Amazon EC2 Auto Scaling API Reference*.
For information about the syntax for quoting JSON-formatted parameter values, see [Using quotation marks with strings in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS Command Line Interface User Guide*.
**Example 9: To create a launch configuration and suppress a block device from attaching at launch time**
This example creates a launch configuration that suppresses a block device specified by the block device mapping of the AMI (for example, `/dev/sdf`).

```
aws autoscaling create-launch-configuration \
    --launch-configuration-name {{my-lc}} \
    --image-id {{ami-04d5cc9b88example}} \
    --instance-type {{m5.large}} \
    --block-device-mappings '{{[{"DeviceName":"/dev/sdf","NoDevice":""}]}}'
```
This command produces no output.
For more information, see [BlockDeviceMapping](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_BlockDeviceMapping.html) in the *Amazon EC2 Auto Scaling API Reference*.
For information about the syntax for quoting JSON-formatted parameter values, see [Using quotation marks with strings in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS Command Line Interface User Guide*.
+  For API details, see [CreateLaunchConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-launch-configuration.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates a launch configuration named 'my-lc'. The EC2 instances launched by Auto Scaling groups that use this launch configuration use specified instance type, AMI, security group, and IAM role.**

```
New-ASLaunchConfiguration -LaunchConfigurationName my-lc -InstanceType "m3.medium" -ImageId "ami-12345678" -SecurityGroup "sg-12345678" -IamInstanceProfile "myIamRole"
```
+  For API details, see [CreateLaunchConfiguration](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates a launch configuration named 'my-lc'. The EC2 instances launched by Auto Scaling groups that use this launch configuration use specified instance type, AMI, security group, and IAM role.**

```
New-ASLaunchConfiguration -LaunchConfigurationName my-lc -InstanceType "m3.medium" -ImageId "ami-12345678" -SecurityGroup "sg-12345678" -IamInstanceProfile "myIamRole"
```
+  For API details, see [CreateLaunchConfiguration](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
