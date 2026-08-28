---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/view-multicast-group.html
---

# View multicast groups in AWS Transit Gateway
<a name="view-multicast-group"></a>

You can view information about your multicast groups to verify that members were discovered using the IGMPv2 protocol. **Member type** (in the console), or `MemberType` (in the AWS CLI) displays IGMP when AWS discovered members with the protocol.

**To view multicast groups using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Multicast**.

1. Select the multicast domain.

1. Choose the **Groups** tab.

**To view multicast groups using the AWS CLI**
Use the [search-transit-gateway-multicast-groups](https://docs.aws.amazon.com/cli/latest/reference/ec2/search-transit-gateway-multicast-groups.html) command.

The following example shows that the IGMP protocol discovered multicast group members.

```
aws ec2 search-transit-gateway-multicast-groups --transit-gateway-multicast-domain {{tgw-mcast-domain-000fb24d04EXAMPLE}}
{
    "MulticastGroups": [
        {
            "GroupIpAddress": "224.0.1.0",
            "TransitGatewayAttachmentId": "tgw-attach-0372e72386EXAMPLE",
            "SubnetId": "subnet-0187aff814EXAMPLE",
            "ResourceId": "vpc-0065acced4EXAMPLE",
            "ResourceType": "vpc",
            "NetworkInterfaceId": "eni-03847706f6EXAMPLE",
            "MemberType": "igmp"
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
