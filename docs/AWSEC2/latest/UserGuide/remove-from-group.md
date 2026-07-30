---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/remove-from-group.html
---

# Remove a Capacity Reservation from a group
<a name="remove-from-group"></a>

You can use the following examples to remove a Capacity Reservation from a group.

------
#### [ AWS CLI ]

**To remove a Capacity Reservation from a group**
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

**To remove a Capacity Reservation from a group**
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
