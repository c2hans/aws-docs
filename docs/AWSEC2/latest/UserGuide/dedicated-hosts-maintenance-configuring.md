---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-maintenance-configuring.html
---

# Configure the host maintenance setting for an Amazon EC2 Dedicated Host
<a name="dedicated-hosts-maintenance-configuring"></a>

Enable host maintenance to ensure that your instances running on a Dedicated Host are automatically recovered onto a new Dedicated Host during a scheduled maintenance event.

If you disable host maintenance, you receive an email notification to evict the degraded host and manually migrate your instances to another host within 28 days. A replacement host is allocated if you have Dedicated Host reservation. After 28 days, the instances running on the degraded host are terminated, and the host is released automatically.

------
#### [ Console ]

**To enable host maintenance for your Dedicated Host**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Dedicated Hosts**.

1. Select the Dedicated Host > **Actions** > **Modify host**.

1. Select *on* in the **Host maintenance** field.

**To disable host maintenance for your Dedicated Host**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Dedicated Hosts**.

1. Select the Dedicated Host > **Actions** > **Modify host**.

1. Select *off* in the **Host maintenance** field.

------
#### [ AWS CLI ]

**To enable host maintenance for your Dedicated Host**
Use the [modify-hosts](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-hosts.html) command.

```
aws ec2 modify-hosts \
    --host-maintenance on \
    --host-ids {{h-0d123456bbf78910d}}
```

**To disable host maintenance for your Dedicated Host**
Use the [modify-hosts](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-hosts.html) command.

```
aws ec2 modify-hosts \
    --host-maintenance off \
    --host-ids {{h-0d123456bbf78910d}}
```

------
#### [ PowerShell ]

**To enable host maintenance for your Dedicated Host**
Use the [Edit-EC2Host](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2Host.html) cmdlet.

```
Edit-EC2Host `
    -HostMaintenance on `
    -HostId {{h-0d123456bbf78910d}}
```

**To disable host maintenance for your Dedicated Host**
Use the [Edit-EC2Host](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2Host.html) cmdlet.

```
Edit-EC2Host `
    -HostMaintenance off `
    -HostId {{h-0d123456bbf78910d}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
