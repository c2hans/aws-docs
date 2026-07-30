---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cb-group.html
---

# Create a resource group for UltraServer Capacity Blocks
<a name="cb-group"></a>

You can use AWS Resource Groups to create logical collections of UltraServer Capacity Blocks. After you create the resource group, you can add UltraServer Capacity Blocks that you own in your account. After you add the UltraServer Capacity Blocks, you can target instances launches to the resource group instead of the individual Capacity Blocks. Instances that target a resource group match with any UltraServer Capacity Blocks in the group that has matching attributes and available capacity. If the resource group does not have an UltraServer Capacity Block with matching attributes and available capacity, the instance launch fails.

If an UltraServer Capacity Block is removed from a resource group while it has running instances, those instances continue to run in the Capacity Block. If an UltraServer Capacity Block in a group ends while it has running instances, the instances are terminated.

You can't add instance Capacity Blocks to a resource group.

To create a resource group for UltraServer Capacity Blocks, use one of the following methods.

------
#### [ AWS CLI ]

**To create a resource group for UltraServer Capacity Blocks**
Use the [create-group](https://docs.aws.amazon.com/cli/latest/reference/resource-groups/create-group.html) AWS CLI command, and for `--configuration`, specify the following:

```
{
  "Configuration": [
    {
      "Type": "AWS::EC2::CapacityReservationPool",
      "Parameters": [
        {
          "Name": "instance-type",
          "Values": [
            "{{instance_type}}"
          ]
        },
        {
          "Name": "reservation-type",
          "Values": [
            "capacity-block"
          ]
        }
      ]
    },
    {
      "Type": "AWS::ResourceGroups::Generic",
      "Parameters": [
        {
          "Name": "allowed-resource-types",
          "Values": [
            "AWS::EC2::CapacityReservation"
          ]
        }
      ]
    }
  ]
}
```

------
#### [ PowerShell ]

**To create a resource group for UltraServer Capacity Blocks**
Use the [New-RGGroup](https://docs.aws.amazon.com/powershell/latest/reference/items/New-RGGroup.html) cmdlet. For `-Configuration`, specify the following:

```
{
  "Configuration": [
    {
      "Type": "AWS::EC2::CapacityReservationPool",
      "Parameters": [
        {
          "Name": "instance-type",
          "Values": [
            "{{instance_type}}"
          ]
        },
        {
          "Name": "reservation-type",
          "Values": [
            "capacity-block"
          ]
        }
      ]
    },
    {
      "Type": "AWS::ResourceGroups::Generic",
      "Parameters": [
        {
          "Name": "allowed-resource-types",
          "Values": [
            "AWS::EC2::CapacityReservation"
          ]
        }
      ]
    }
  ]
}
```

------

After you create a resource group for UltraServer Capacity Block, use one of the following methods to add existing UltraServer Capacity Blocks to it.

------
#### [ AWS CLI ]

**To add an UltraServer Capacity Block to a resource group**
Use the [ group-resources](https://docs.aws.amazon.com/cli/latest/reference/resource-groups/group-resources.html) command. For `--group` specify the name of the resource group you created. For `--resource-arns`, specify the ARNs of the UltraServer Capacity Blocks to add.

```
aws resource-groups group-resources \
--group {{MyCRGroup}} \
--resource-arns {{CapacityReservationArn}}
```

------
#### [ PowerShell ]

**To add an UltraServer Capacity Block to a resource group**
Use the [Add-RGResource](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-RGResource.html) cmdlet. For `-Group` specify the name of the resource group you created. For `-ResourceArn `, specify the ARNs of the UltraServer Capacity Blocks to add.

The following example adds two Capacity Reservations to the specified group.

```
Add-RGResource `
-Group {{MyCRGroup}} `
-ResourceArn {{CapacityReservationArn}}
```

------
