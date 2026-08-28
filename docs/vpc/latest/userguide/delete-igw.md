---
source_url: https://docs.aws.amazon.com/vpc/latest/userguide/delete-igw.html
---

# Delete an internet gateway
<a name="delete-igw"></a>

If you no longer need internet access for a VPC, you can detach the internet gateway from the VPC and then delete it. You can't delete an internet gateway if it's still attached to a VPC. You can't detach an internet gateway if the VPC has resources with associated public IP addresses or Elastic IP addresses.

**To detach an internet gateway from a VPC using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Internet gateways**.

1. Select the check box for the internet gateway.

1. To attach it, choose **Actions**, Attach to VPC, select an available VPC, and choose **Attach internet gateway**.

1. To detach it, choose **Actions**, **Detach from VPC** and choose **Detach internet gateway**. When prompted for confirmation, choose **Detach internet gateway**.

**To describe your internet gateways, including attachments, using the command line**
+ [describe-internet-gateways](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-internet-gateways.html) (AWS CLI)
+ [Get-EC2InternetGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InternetGateway.html) (AWS Tools for Windows PowerShell)

**To detach an internet gateway from a VPC using the command line**
+ [detach-internet-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/detach-internet-gateway.html) (AWS CLI)
+ [Dismount-EC2InternetGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/Dismount-EC2InternetGateway.html) (AWS Tools for Windows PowerShell)

**To delete an internet gateway using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Internet gateways**.

1. Select the check box for the internet gateway.

1. Choose **Actions**, **Delete internet gateway**.

1. When prompted for confirmation, enter **delete**, and then choose **Delete internet gateway**.

**To delete an internet gateway using the command line**
+ [delete-internet-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-internet-gateway.html) (AWS CLI)
+ [Remove-EC2InternetGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2InternetGateway.html) (AWS Tools for Windows PowerShell)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
