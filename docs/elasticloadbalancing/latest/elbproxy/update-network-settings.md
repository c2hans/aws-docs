---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/update-network-settings.html
---

# Update proxy network settings

After you create a proxy, you can change which subnets and security groups it uses. In ELB for Envoy, the subnets set the Availability Zones that the proxy runs in, and the security groups control what traffic can reach the proxy and what traffic the proxy can send. You update both with the `UpdateProxyNetworkConfiguration` operation.

You must provide at least one of `subnets` or `securityGroups`. The subnets and security groups you provide replace the proxy's current values for that field.

**Warning**
You can't change the IP addressing configuration (the IPv4 and IPv6 addressability settings) after you create a proxy. To change the IP addressing configuration, create a new proxy.

Before you update network settings, make sure you have the following:
+ The ARN of an existing proxy.
+ The subnets you want the proxy to use. You must specify at least two subnets in different Availability Zones, and all subnets must belong to the same VPC.
+ The security groups you want the proxy to use. You must specify at least one security group in the same VPC as your subnets.
+ For IPv6 or dualstack proxies, subnets that have an IPv6 CIDR block associated. For IPv6-only proxies (IPv4 set to `off`), `ipv6Native` subnets. For all other configurations, non-`ipv6Native` subnets.

Update the network settings using the console, the AWS CLI, or CloudFormation. Choose the tab for the method that you want to use.

------
#### [ Console ]

**To update the network settings of a proxy**

1. Open the ELB for Envoy console.

1. In the navigation pane, choose **Proxies**.

1. Choose the proxy that you want to update to open its details page. Alternatively, select the proxy in the **Proxies** list.

1. Choose **Edit network settings**.

1. On the **Edit network settings** page, for **Subnets**, select the subnets you want the proxy to use.

1. For **Security groups**, select the security groups you want the proxy to use.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

To update the network settings of a proxy, run the **update-proxy-network-configuration** command. Provide the subnets, the security groups, or both.

```
aws elb-proxy update-proxy-network-configuration \
    --cli-input-json '{
        "proxyIdentifier": "<proxy-arn>",
        "vpcConfiguration": {
            "subnets": [
                { "subnetId": "subnet-ac32c587" },
                { "subnetId": "subnet-bd43d698" }
            ],
            "securityGroups": [
                { "securityGroupId": "sg-00281fc98f42f773e" }
            ]
        }
    }'
```

Replace {{proxy-arn}} with the ARN of your proxy, for example `arn:aws:elasticloadbalancing:us-east-1:123456789012:proxy/my-proxy:01f705a93c276c01`. Replace the subnet IDs and security group ID with the values you want the proxy to use.

------
#### [ CloudFormation ]

Set the subnets and security groups on your `AWS::ElasticLoadBalancingProxy::Proxy` resource and update the stack. For the full resource, see [Create a proxy](create-proxy.md).

```yaml
Properties:
  Subnets:
    - subnet-0123456789abcdef0
    - subnet-0fedcba9876543210
  SecurityGroups:
    - sg-0123456789abcdef0
```

Updating `Subnets` or `SecurityGroups` changes them in place. Changing `IpAddressingConfiguration` replaces the proxy and gives it a new DNS name.

------

## Verify the update
<a name="update-network-settings-verify"></a>

To confirm the new network settings, run the **get-proxy** command and inspect the `networkConfiguration.vpcConfiguration` field in the response.

```
aws elb-proxy get-proxy --proxy-identifier <proxy-arn>
```

Replace {{proxy-arn}} with the ARN of your proxy. The response shows the proxy's current security groups and the Availability Zones that correspond to its subnets.
