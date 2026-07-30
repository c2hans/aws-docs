---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/delete-group.html
---

# Delete a Capacity Reservation group
<a name="delete-group"></a>

You can use the following examples to delete a Capacity Reservation group.

------
#### [ AWS CLI ]

**To delete a group**
Use the [delete-group](https://docs.aws.amazon.com/cli/latest/reference/resource-groups/delete-group.html) command.

```
aws resource-groups delete-group --group {{MyCRGroup}}
```

------
#### [ PowerShell ]

**To delete a group**
Use the [Remove-RGGroup](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-RGGroup.html) cmdlet.

```
Remove-RGGroup -GroupName {{MyCRGroup}}
```

------
