---
source_url: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns-updating.html
---

# View and update DNS attributes for your VPC
<a name="vpc-dns-updating"></a>

You can view and update the DNS support attributes for your VPC using the Amazon VPC console. These settings control whether your instances get public DNS hostnames and whether the Amazon DNS server can resolve your private DNS names. Configuring these attributes correctly is vital for ensuring seamless communication within your VPC.

**To describe and update DNS support for a VPC using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Your VPCs**.

1. Select the checkbox for the VPC.

1. Review the information in **Details**. In this example, both **DNS hostnames** and **DNS resolution** are enabled.
![The DNS Settings tab.](http://docs.aws.amazon.com/vpc/latest/userguide/images/dns-settings.png)

1. To update these settings, choose **Actions** and then choose **Edit VPC settings**. Select or clear **Enable** on the appropriate DNS attribute and choose **Save changes**.

**To describe DNS support for a VPC using the command line**
+ [describe-vpc-attribute](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-attribute.html) (AWS CLI)
+ [Get-EC2VpcAttribute](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2VpcAttribute.html) (AWS Tools for Windows PowerShell)

**To update DNS support for a VPC using the command line**
+ [modify-vpc-attribute](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpc-attribute.html) (AWS CLI)
+ [Edit-EC2VpcAttribute](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2VpcAttribute.html) (AWS Tools for Windows PowerShell)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
