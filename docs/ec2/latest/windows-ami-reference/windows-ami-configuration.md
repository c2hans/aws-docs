---
source_url: https://docs.aws.amazon.com/ec2/latest/windows-ami-reference/windows-ami-configuration.html
---

# Updates applied for AWS Windows AMIs
<a name="windows-ami-configuration"></a>

To help ensure a smooth and consistent launch experience, AWS Windows AMIs include the following updates for initialization, installation, and configuration.

**Note**
When you launch an instance from an Amazon managed AWS Windows AMI, the root device for the Windows instance is an Amazon Elastic Block Store (Amazon EBS) volume. AWS Windows AMIs don't support instance store for the root device.

**Clean and prepare**

| Description | Applies to |
| --- | --- |
| Check for pending file renames or reboots, and reboot as needed | All AMIs |
| Delete `.dmp` files | All AMIs |
| Delete logs (event logs, Systems Manager, EC2Config) | All AMIs |
| Delete temporary folders and files for Sysprep | All AMIs |
| Perform virus scan | All AMIs |
| Pre-compile queued .NET assemblies (before Sysprep) | All AMIs |
| Restore default values for Microsoft browsers | All AMIs |
| Reset the Windows wallpaper | All AMIs |
| Run Sysprep | All AMIs |
| Set EC2Launch v1 to run at the next launch | Windows Server 2016 and 2019 |
| Run Windows maintenance tools | Windows Server 2012 R2 and later |
| Clear recent history (Start menu, Windows Explorer, and more) | Windows Server 2012 R2 and earlier |
| Restore default values for EC2Config | Windows Server 2012 R2 and earlier |

**Install and configure**

| Description | Applies to |
| --- | --- |
| Disable Secure Time Seeding | All AMIs |
| Add links to the Amazon EC2 Windows Guide | All AMIs |
| Attach instance storage volumes to extended mount points | All AMIs |
| Install the current AWS Tools for Windows PowerShell | All AMIs |
| Install the current CloudFormation bootstrap scripts | All AMIs |
| Disable RunOnce for Internet Explorer | All AMIs |
| Enable remote PowerShell | All AMIs |
| Disable hibernation and delete the hibernation file | All AMIs |
| Disable the Connected User Experiences and Telemetry service | All AMIs |
| Set the performance options for best performance | All AMIs |
| Set the power setting to high performance | All AMIs |
| Disable the screen saver password | All AMIs |
| Set the RealTimeIsUniversal registry key | All AMIs |
| Set the timezone to UTC | All AMIs |
| Disable Windows updates and notifications | All AMIs |
| Run Windows Update and reboot until there are no pending updates | All AMIs |
| Set the display in all power schemes to never turn off | All AMIs |
| Set the PowerShell execution policy to "Unrestricted" | All AMIs |
| If Microsoft SQL Server is installed:[See the AWS documentation website for more details](http://docs.aws.amazon.com/ec2/latest/windows-ami-reference/windows-ami-configuration.html) | All AMIs |
| Configure a paging file on the system volume as follows:[See the AWS documentation website for more details](http://docs.aws.amazon.com/ec2/latest/windows-ami-reference/windows-ami-configuration.html) | All AMIs |
| Install the current EC2Launch v2 and SSM Agent | Windows Server 2022 and later |
| Install the current EC2Launch v1 and SSM Agent | Windows Server 2016 and 2019 |
| Install the current SRIOV drivers | Windows Server 2012 R2 and later |
| Install the current EC2WinUtil driver | Windows Server 2008 R2 and later |
| Install the current EC2Config and SSM Agent | Windows Server 2012 R2 and earlier |
| Install the current AWS PV, ENA, and NVMe drivers | Windows Server 2008 R2 and later |
| Allow ICMP traffic through the firewall | Windows Server 2012 R2 and earlier |
| Configure an additional system managed paging file on `Z:`, if available | Windows Server 2012 R2 and earlier |
| Enable file and printer sharing | Windows Server 2012 R2 and earlier |
| Install the current Citrix PV driver | Windows Server 2008 SP2 and earlier |
| Install PowerShell 2.0 and 3.0 | Windows Server 2008 SP2 and R2 |
| Apply the following hotfixes:[See the AWS documentation website for more details](http://docs.aws.amazon.com/ec2/latest/windows-ami-reference/windows-ami-configuration.html) | Windows Server 2008 SP2 and R2 |
