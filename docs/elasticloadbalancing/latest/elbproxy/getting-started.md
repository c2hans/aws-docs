---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/getting-started.html
---

# Get started: create your first proxy

In this tutorial, you create your first proxy with Elastic Load Balancing for Envoy (ELB for Envoy). You create a proxy that runs a sample Envoy configuration, confirm that the proxy becomes active, send a request to it, and then delete it. The tutorial takes about 20 minutes.

**Topics**
+ [Prerequisites](#getting-started-prerequisites)
+ [Step 1: Save the sample Envoy configuration](#getting-started-step1)
+ [Step 2: Create a proxy](#getting-started-step2)
+ [Step 3: Wait for and view your proxy](#getting-started-step3)
+ [Step 4: Send a test request to your proxy](#getting-started-step4)
+ [Step 5: Clean up](#getting-started-step5)
+ [Next steps](#getting-started-next-steps)

## Prerequisites
<a name="getting-started-prerequisites"></a>

Before you begin, complete the tasks in [Set up ELB for Envoy](setting-up.md). You need the following:
+ A proxy role ARN that ELB for Envoy can assume to publish logs and access AWS services on your behalf.
+ A VPC with at least two subnets in different Availability Zones, and a security group that allows inbound traffic on port `80`.
+ The AWS CLI installed and configured.

## Step 1: Save the sample Envoy configuration
<a name="getting-started-step1"></a>

Create an Envoy configuration file for your proxy. The following configuration file listens on port `80` and responds to every request with a short message. Save it to your computer as `config.yaml`.

```
admin:
  address:
    socket_address:
      address: 127.0.0.1
      port_value: 9901

static_resources:
  listeners:
  - name: listener_0
    address:
      socket_address:
        address: 0.0.0.0
        port_value: 80
    filter_chains:
    - filters:
      - name: envoy.filters.network.http_connection_manager
        typed_config:
          "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
          stat_prefix: ingress_http
          route_config:
            name: local_route
            virtual_hosts:
            - name: local_service
              domains: ["*"]
              routes:
              - match:
                  prefix: "/"
                direct_response:
                  status: 200
                  body:
                    inline_string: "Your proxy is running\n"
          http_filters:
          - name: envoy.filters.http.router
            typed_config:
              "@type": type.googleapis.com/envoy.extensions.filters.http.router.v3.Router
```

## Step 2: Create a proxy
<a name="getting-started-step2"></a>

Create the proxy with the console, the AWS CLI, or AWS CloudFormation. Choose the method that you want to use.

------
#### [ Console ]

**To open the proxy creation wizard**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Proxies**.

1. Choose **Create proxy**.

**To configure and create the proxy**

1. For **Step 1: Create proxy**, configure the basic settings for your proxy:
   + For **Identifiers**, enter a **Name** for your proxy.
   + For **IP addresses**, choose **IPv4 addressing**, **IPv6 addressing**, or both. Enable at least one.
   + For **Network mapping**, choose the VPC for your proxy. Then, under **Availability Zones and subnets**, select at least two Availability Zones and a subnet in each zone.
   + For **Security groups**, select at least one security group in the proxy's VPC.
   + Select the IAM role for your proxy.
   + For **Proxy type and version**, keep **Type** as **Envoy**, then select a **Version**.

   Defaults apply to the settings you don't change, such as **Certificates** and **Attributes**. You can edit attributes after you create the proxy.

1. For **Step 2: Configure proxy**, under **Proxy configuration**, choose a **Source** for your configuration. For this tutorial, upload the `config.yaml` file from Step 1, or paste its YAML. Defaults apply to the encryption type and configuration archive.

1. (Optional) For **Step 3: Add service integrations**, skip AWS WAF for this tutorial.

1. For **Review and create**, review your configuration, then choose **Create proxy**.

1. Verify that the proxy appears with the `create-in-progress` state. The proxy becomes `active` when provisioning completes.

------
#### [ AWS CLI ]

Create the proxy with the **create-proxy** command. You specify the proxy type, version, IP addressing, VPC networking, proxy role, and the configuration file.

```
aws elb-proxy create-proxy \
--cli-input-json \
'{
    "name": "my-proxy",
    "type": "envoy",
    "proxyVersion": "1.40",
    "roleArn": "arn:aws:iam::<account-id>:role/<your-proxy-role>",
    "networkConfiguration": {
        "ipConfiguration": {
            "ipAddressingConfiguration": {
                "ipv4Addressability": "internet-facing",
                "ipv6Addressability": "off"
            }
        },
        "vpcConfiguration": {
            "subnets": [
                { "subnetId": "<subnet-id-1>" },
                { "subnetId": "<subnet-id-2>" }
            ],
            "securityGroups": [
                { "securityGroupId": "<security-group-id>" }
            ]
        }
    }
}' \
--configuration configurationFile={configurationBytes@=file:///tmp/config.yaml}
```

Replace the placeholders as follows:
+ `<account-id>`: your AWS account ID.
+ `<your-proxy-role>`: the name of the proxy role you created in [Set up ELB for Envoy](setting-up.md).
+ `<subnet-id-1>` and `<subnet-id-2>`: the IDs of two subnets in different Availability Zones.
+ `<security-group-id>`: the ID of a security group that allows inbound traffic on port `80`.

Set the `file://` path to the location where you saved `config.yaml`.

**Note**
With AWS CLI version 2, you might need to add the `--cli-binary-format raw-in-base64-out` flag, because this version defaults to base64 input.

The command returns the proxy details, including the proxy ARN and the DNS name. Note the proxy ARN. You use it to refer to the proxy in later commands.

------
#### [ CloudFormation ]

Create a proxy with the [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/) resource `AWS::ElasticLoadBalancingProxy::Proxy`.

```yaml
Resources:
  MyProxy:
    Type: AWS::ElasticLoadBalancingProxy::Proxy
    Properties:
      Name: my-proxy
      Type: envoy
      ProxyVersion: "1.40"
      RoleArn: arn:aws:iam::123456789012:role/my-proxy-role
      ConfigurationFile:
        ConfigurationBytes: |
          # Contents of config.yaml from Step 1
      IpAddressingConfiguration:
        Ipv4Addressability: internet-facing
        Ipv6Addressability: "off"
      Subnets:
        - subnet-0123456789abcdef0
        - subnet-0fedcba9876543210
      SecurityGroups:
        - sg-0123456789abcdef0
```

Replace the following values:
+ `RoleArn`: the ARN of the proxy role you created in [Set up ELB for Envoy](setting-up.md).
+ `Subnets`: the IDs of two subnets in different Availability Zones.
+ `SecurityGroups`: the ID of a security group that allows inbound traffic on port `80`.
+ `ConfigurationBytes`: the contents of the `config.yaml` file from Step 1.

------

## Step 3: Wait for and view your proxy
<a name="getting-started-step3"></a>

A new proxy starts in the `create-in-progress` state. After it is fully provisioned, the proxy is in the `active` state. View your proxy with the console or the AWS CLI. Choose the method that you want to use.

------
#### [ Console ]

**To view your proxy**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Proxies**.

1. On the **Proxies** page, find your proxy. The list shows the columns **Name**, **Status**, **Type**, **VPC ID**, and **Date created**. A new proxy shows a **Status** of **Create in progress** and changes to **Active** when it is fully provisioned.

1. Wait until the **Status** is **Active**, then choose the proxy **Name** to open its details page and view the DNS name. Use the DNS name to send requests to your proxy.

------
#### [ AWS CLI ]

Use the **get-proxy** command to check the current state.

```
aws elb-proxy get-proxy --proxy-identifier <proxy-arn>
```

Replace {{proxy-arn}} with the proxy ARN returned in Step 2.

To list all proxies in your account and Region, use the **list-proxies** command.

```
aws elb-proxy list-proxies
```

Wait until **get-proxy** reports the `active` state before you send traffic to the proxy. Note the DNS name from the output for the next step.

------

## Step 4: Send a test request to your proxy
<a name="getting-started-step4"></a>

After the proxy is `active`, use the DNS name from the proxy details to confirm that the proxy responds. Use **dig** to confirm that the DNS name resolves, and **curl** to send a request.

```
dig A <dns-name>
curl http://<dns-name>/
```

Replace {{dns-name}} with the DNS name of your proxy.

The **curl** command returns the message from your configuration file:

```
Your proxy is running
```

## Step 5: Clean up
<a name="getting-started-step5"></a>

When you finish, delete the proxy that you created in this tutorial. Delete the proxy with the console, the AWS CLI, or AWS CloudFormation. Choose the method that you want to use.

**Warning**
Deleting a proxy is permanent. After deletion completes, the proxy and its DNS name are gone and can't be recovered.

------
#### [ Console ]

**To delete your proxy**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Proxies**.

1. Select the proxy to delete.

1. Choose **Delete proxy**.

1. In the confirmation dialog, enter **confirm**, and then choose **Delete**.

1. The proxy shows **Delete in progress** until deletion completes, and then no longer appears in the list.

------
#### [ AWS CLI ]

Use the **delete-proxy** command.

```
aws elb-proxy delete-proxy --proxy-identifier <proxy-arn>
```

Replace {{proxy-arn}} with the proxy ARN.

A deleted proxy is in the `delete-in-progress` state until deletion completes. After deletion completes, the proxy no longer appears in the output of **list-proxies**.

------
#### [ CloudFormation ]

Delete the stack that you created in Step 2.

------

## Next steps
<a name="getting-started-next-steps"></a>
+ To learn about proxy networking, state, attributes, and DNS names, see [Proxies for ELB for Envoy](proxies.md).
+ To learn how to write Envoy configuration for your proxy, see [Envoy configuration for ELB for Envoy](envoy-configuration.md).
+ To update the configuration of an existing proxy, see [Update a proxy configuration](update-proxy-configuration.md).
