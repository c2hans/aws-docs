---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/setting-up.html
---

# Set up ELB for Envoy

Before you create your first proxy with Elastic Load Balancing for Envoy (ELB for Envoy), complete the account, permissions, AWS CLI, proxy role, and network prerequisites in this section. You create the proxy role one time per account and Region.

After you finish these steps, see [Get started: create your first proxy](getting-started.md) to create your first proxy, or see [Create a proxy](create-proxy.md) for all proxy creation options.

**Topics**
+ [Prerequisites](#setting-up-prerequisites)
+ [Create a proxy role](#setting-up-proxy-role)
+ [Network prerequisites](#setting-up-network)

## Prerequisites
<a name="setting-up-prerequisites"></a>

Before you begin, make sure that you have the following:
+ An AWS account. If you don't have one, you can [create an AWS account](https://aws.amazon.com/).
+ An IAM principal (user or role) with permissions to create IAM roles (`iam:CreateRole` and `iam:PutRolePolicy`) and to call ELB for Envoy operations in the `elasticloadbalancing` namespace.
+ A virtual private cloud (VPC) with at least two subnets in different Availability Zones, and at least one security group. See [Network prerequisites](#setting-up-network).

## Create a proxy role
<a name="setting-up-proxy-role"></a>

When you create a proxy, you specify a proxy role. The proxy role is an IAM role that ELB for Envoy assumes to publish Envoy logs to Amazon CloudWatch Logs and access AWS services on your behalf. You pass the role ARN as the `roleArn` input when you create a proxy.

ELB for Envoy assumes the role through the `elasticloadbalancing.amazonaws.com` service principal with the `sts:AssumeRole` action. The following trust policy grants this access.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "elasticloadbalancing.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

To let ELB for Envoy publish Envoy logs, grant the role at least the following permissions to CloudWatch Logs.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:*:logs:*:*:log-group:/aws/elb-proxy/*",
                "arn:*:logs:*:*:log-group:/aws/elb-proxy/*:log-stream:*"
            ]
        }
    ]
}
```

Create the role with the AWS CLI.

Install and configure the AWS CLI. For more information, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS CLI User Guide*.

**To create the proxy role**

1. Save the trust policy shown earlier in this section as `trust-policy.json`.

1. Save the CloudWatch Logs permissions shown earlier in this section as `logs-policy.json`.

1. Create the role with the trust policy.

   ```
   aws iam create-role \
       --role-name aws-elb-proxy-role \
       --assume-role-policy-document file://trust-policy.json
   ```

1. Attach the log permissions to the role.

   ```
   aws iam put-role-policy \
       --role-name aws-elb-proxy-role \
       --policy-name aws-elb-proxy-logs \
       --policy-document file://logs-policy.json
   ```

1. Verify that the role exists.

   ```
   aws iam get-role --role-name aws-elb-proxy-role
   ```

   The command returns the role, including its ARN. Note the ARN. You provide it as the `roleArn` input when you create a proxy.

## Network prerequisites
<a name="setting-up-network"></a>

A proxy runs in a VPC that you specify. Before you create a proxy, prepare the following network resources. To change these resources after you create a proxy, see [Update proxy network settings](update-network-settings.md).

**Subnets and Availability Zones**
+ Provide at least two subnets in different Availability Zones for high availability. All subnets must belong to the same VPC.
+ For IPv6 or dualstack addressing, each subnet must have an IPv6 CIDR block associated. To verify, check the `ipv6CidrBlockAssociationSet` field with **aws ec2 describe-subnets**.
+ For IPv6-only addressing (IPv4 set to `off`), you must use `ipv6Native` subnets. All other configurations require non-`ipv6Native` subnets.

**Security groups**
+ Provide at least one security group in the same VPC as your subnets. Security group rules control what traffic can reach your proxy and what traffic your proxy can send.
+ For IPv4 configurations, add inbound rules that allow IPv4 traffic on the ports that your proxy listens on.
+ For IPv6 or dualstack configurations, also add inbound rules that allow IPv6 traffic. For example, use `::/0` as the source for an internet-facing proxy, or your VPC's IPv6 CIDR for an internal proxy.

For more information about IP addressing, DNS names, and how a proxy uses your network, see [Proxies for ELB for Envoy](proxies.md).
