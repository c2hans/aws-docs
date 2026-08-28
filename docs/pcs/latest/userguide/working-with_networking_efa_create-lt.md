---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_efa_create-lt.html
---

# Create or update an EC2 launch template
<a name="working-with_networking_efa_create-lt"></a>

EFA network interfaces are set up in the EC2 launch template for an AWS PCS compute node group. If there are multiple network cards, multiple EFAs can be configured. The EFA security group and the optional placement group are included in the launch template as well.

Here is an example launch template for instances with two network cards, such as **hpc7a.96xlarge**. The instances will be launched in `subnet-{{SubnetID1}}` in cluster placement group `pg-{{PlacementGroupId1}}`.

 Security groups must be added specifically to each EFA interface. Every EFA needs the security group that enables EFA traffic (`sg-{{EfaSecGroupId}}`). Other security groups, especially ones that handle regular traffic like SSH or HTTPS, only need to be attached to the primary network interface (designated by a `DeviceIndex` of `0`). Launch templates where network interfaces are defined do not support setting security groups using the `SecurityGroupIds` parameter—you must set a value for `Groups` in each network interface that you configure.

```
{
    "Placement": {
        "GroupId": "pg-{{PlacementGroupId1}}"
    },
    "NetworkInterfaces": [
        {
            "DeviceIndex": 0,
            "InterfaceType": "efa",
            "NetworkCardIndex": 0,
            "SubnetId": "subnet-{{SubnetId1}}",
            "Groups": [
                "sg-{{SecurityGroupId1}}",
                "sg-{{EfaSecGroupId}}"
            ]
        },
        {
            "DeviceIndex": 1,
            "InterfaceType": "efa",
            "NetworkCardIndex": 1,
            "SubnetId": "subnet-{{SubnetId1}}"
            "Groups": ["sg-{{EfaSecGroupId}}"]
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
