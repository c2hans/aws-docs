---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/delete_eni.html
---

# Delete a network interface
<a name="delete_eni"></a>

Deleting a network interface releases all attributes associated with the interface and releases any private IP addresses or Elastic IP addresses to be used by another instance.

You can't delete a network interface that is in use. First, you must [detach the network interface](network-interface-attachments.md#detach_eni).

------
#### [ Console ]

**To delete a network interface**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Network Interfaces**.

1. Select the checkbox for the network interface, and then choose **Actions**, **Delete**.

1. When prompted for confirmation, choose **Delete**.

------
#### [ AWS CLI ]

**To delete a network interface**
Use the following [delete-network-interface](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-network-interface.html) command.

```
aws ec2 delete-network-interface --network-interface-id {{eni-1234567890abcdef0}}
```

------
#### [ PowerShell ]

**To delete a network interface**
Use the [Remove-EC2NetworkInterface](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2NetworkInterface.html) cmdlet.

```
Remove-EC2NetworkInterface -NetworkInterfaceId {{eni-1234567890abcdef0}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
