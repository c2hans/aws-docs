---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-groups-remove.html
---

# Remove Capacity Reservations from a group
<a name="cr-groups-remove"></a>

You can remove a Capacity Reservation from a group at any time. Instances that target the group continue running in their current Capacity Reservation and are not affected by the removal. The Capacity Reservation restores the capacity only when you terminate the instances.

**Note**
If a Capacity Reservation that is shared with you is later unshared, Amazon EC2 automatically removes it from the group.

------
#### [ Console ]

**To remove Capacity Reservations from a group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Capacity Reservations**.

1. Choose **Capacity Reservation Resource Group**.

1. Select the group name to open its details page.

1. In the **Capacity Reservations** section, select the Capacity Reservations to remove, then choose **Remove**.

------
#### [ AWS CLI ]

**To remove Capacity Reservations from a group**
Use the [ungroup-resources](https://docs.aws.amazon.com/cli/latest/reference/resource-groups/ungroup-resources.html) command.

The following example removes two Capacity Reservations from the specified group.

```
aws resource-groups ungroup-resources \
    --group {{MyCRGroup}} \
    --resource-arns \
        arn:aws:ec2:{{sa-east-1}}:{{123456789012}}:capacity-reservation/{{cr-0e154d26a16094dd}} \
        arn:aws:ec2:{{sa-east-1}}:{{123456789012}}:capacity-reservation/{{cr-54321abcdef567890}}
```

------
#### [ PowerShell ]

**To remove Capacity Reservations from a group**
Use the [Remove-RGResource](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-RGResource.html) cmdlet.

The following example removes two Capacity Reservations from the specified group.

```
Remove-RGResource `
    -Group {{MyCRGroup}} `
    -ResourceArn `
        "arn:aws:ec2:{{sa-east-1}}:{{123456789012}}:capacity-reservation/{{cr-0e154d26a16094dd}}", `
        "arn:aws:ec2:{{sa-east-1}}:{{123456789012}}:capacity-reservation/{{cr-54321abcdef567890}}"
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
