---
source_url: https://docs.aws.amazon.com/vm-import/latest/userguide/import-vm-next-steps.html
---

# Create an EC2 instance from an imported image
<a name="import-vm-next-steps"></a>

After the import image task is complete, you can launch an instance using the resulting AMI or copy the AMI to another Region. For more information, see the following documentation in the *Amazon EC2 User Guide*:
+ [Launch an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html)
+ [Copy an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html)

For some operating systems, the device drivers for enhanced networking and NVMe block devices that are required by [instances built on the Nitro system](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html) are not installed automatically during import. To install these drivers manually, use the directions in the following documentation in the *Amazon EC2 User Guide*.
+ (Windows instances) Install the latest version of one of the following: [EC2LaunchV2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launch-v2-install.html), [EC2Launch](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launch-download.html), or [EC2Config](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UsingConfig_Install.html).
+ (Windows instances) [Install or upgrade AWS NVMe drivers using PowerShell](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/aws-nvme-drivers.html#install-nvme-drivers)
+ (Linux instances) [Install or upgrade the NVMe driver](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nvme-ebs-volumes.html#install-nvme-driver)
+ [Enable enhanced networking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html)

After you finish customizing your instance, create you can create a new image from the customized instance. For more information, see [Create an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-ami.html) in the *Amazon EC2 User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vm-import` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
