---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/create-proxy.html
---

# Create a proxy

A proxy is an ELB for Envoy resource that runs your Envoy configuration on ELB for Envoy nodes that AWS manages. When you create a proxy, ELB for Envoy provisions a dedicated DNS endpoint in the VPC that you specify and runs the configuration that you provide.

This topic covers all options for creating a proxy. For a guided first-time walkthrough, see [Get started: create your first proxy](getting-started.md). To learn how proxies run your configuration, see [How proxies work](how-proxies-work.md).

## Prerequisites
<a name="create-proxy-prerequisites"></a>

Before you create a proxy, make sure that you have the following:
+ A VPC with at least two subnets in different Availability Zones. Each subnet must have at least 8 available IPv4 addresses for the proxy to scale.
+ One or more security groups in that VPC that allow the client traffic you expect.
+ A proxy role. This is an AWS Identity and Access Management (IAM) role that you pass as `roleArn`. Its trust policy must allow the `elasticloadbalancing.amazonaws.com` service principal to call `sts:AssumeRole`, and it must grant the proxy permission to publish logs. For the full role setup, see [Set up ELB for Envoy](setting-up.md).
+ An Envoy configuration file (the bootstrap YAML). For how to author it, see [Envoy configuration for ELB for Envoy](envoy-configuration.md).

The following options require extra resources:
+ To protect the proxy with AWS WAF, create a web ACL first. See [Protect a proxy with AWS WAF](waf.md).
+ To encrypt the proxy's configuration with your own key, create a customer managed AWS KMS key first. See [Encrypt a proxy configuration with a customer managed key](proxy-encryption.md).
+ To terminate TLS with an AWS Certificate Manager (ACM) certificate, request or import the certificate first. See [Terminate TLS with an ACM certificate](tls-acm-certificate.md).

### Proxy role permissions
<a name="create-proxy-role-permissions"></a>

The proxy role trust policy must allow ELB for Envoy to assume the role:

```json
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

At a minimum, grant the role permission to publish Envoy process logs to Amazon CloudWatch Logs:

```json
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
```

Add any further permissions that your Envoy configuration needs when its filters and extensions call AWS services.

## CreateProxy inputs
<a name="create-proxy-inputs"></a>

The following table describes the inputs to the `CreateProxy` operation. The console and AWS CLI set the same inputs.

| Input | Type | Required | Description |
| --- | --- | --- | --- |
| name | String | Yes | The name of the proxy. The name must be unique within your account for the Region. Valid characters are a-z, A-Z, 0-9, and hyphens (-), with 1–32 characters. You can't use a hyphen as the first or last character. |
| type | String | Yes | The type of proxy. The only value is envoy. |
| proxyVersion | String | Yes | The version of the proxy software, in major.minor format (for example, 1.40). |
| roleArn | String | Yes | The ARN of the proxy role (an IAM role). The role provides permissions to the code that your Envoy configuration runs on the proxy, such as filters and extensions, when that code calls AWS services. |
| configuration | Object | Yes | The configuration for the proxy. Contains configurationFile and an optional configurationArchive. |
| configuration.configurationFile | Blob (YAML) | Yes | The Envoy configuration file (bootstrap YAML). |
| configuration.configurationArchive | Blob (ZIP) | No | A ZIP archive of files that the configuration file references. Omit it if your configuration references no external files. |
| networkConfiguration.ipConfiguration.ipAddressingConfiguration.ipv4Addressability | String | Yes | The IPv4 addressing for the proxy: off, internet-facing, or internal. |
| networkConfiguration.ipConfiguration.ipAddressingConfiguration.ipv6Addressability | String | Yes | The IPv6 addressing for the proxy: off, internet-facing, or internal. |
| networkConfiguration.vpcConfiguration.subnets | List | Yes | The subnets for the proxy. Each entry is a subnetId. At least one is required. |
| networkConfiguration.vpcConfiguration.securityGroups | List | Yes | The security groups for the proxy. Each entry is a securityGroupId. At least one is required. |
| attributes | List | No | Key-value proxy attributes that control secondary behavior. Attributes that you don't set take their default values, and you can change them after creation. See [Proxy attributes](proxy-attributes.md). |
| customerKmsKeyArn | String | No | The ARN of a customer managed AWS KMS key used to encrypt the proxy's configuration content. If you don't set it, ELB for Envoy uses the default AWS owned key. See [Encrypt a proxy configuration with a customer managed key](proxy-encryption.md). |
| tags | Map | No | The tags for the proxy, as key-value pairs. A tag key has 1–128 characters; a tag value has 0–256 characters. See [Tag a proxy](tag-proxy.md). |
| clientToken | String | No | A unique, case-sensitive identifier that you provide to make the create request idempotent. |

**Note**
You can't set `off` for both `ipv4Addressability` and `ipv6Addressability`, and you can't mix `internal` with `internet-facing` across the two. At least one address type must be on, and both must use the same scheme. For IP addressing details, see [How proxies work](how-proxies-work.md).

The configuration file and archive have maximum size limits. For the current limits, see [Envoy configuration limits and unsupported features](envoy-limits.md).

## Create a proxy
<a name="create-proxy-create"></a>

Create a proxy using the console, the AWS CLI, or CloudFormation. Choose the tab for the method that you want to use.

------
#### [ Console ]

You create a proxy with a wizard that has three steps and a review page. The following procedures cover each step.

**To open the create proxy wizard**

1. Open the ELB for Envoy console.

1. In the navigation pane, choose **Proxies**.

1. Choose **Create proxy**.

**To configure basic settings (Step 1: Create proxy)**

1. For **Name**, enter a name for the proxy. You can't change the name after you create the proxy.

1. (Optional) Under **Tags**, choose **Add new tag**, then enter a **Key** and **Value** for each tag.

1. Under **IP addresses**, choose an **IPv4 addressing** option and an **IPv6 addressing** option. Choose **Internet-facing**, **Internal**, or **Off** for each.

1. Under **Network mapping**, choose a **VPC**, select at least two Availability zones, and choose a **Subnet** for each selected zone.

1. Under **Security groups**, select one or more security groups.

1. Under **Identity and Access Management (IAM) role**, choose the proxy role for **IAM role**. Only roles that trust the `elasticloadbalancing.amazonaws.com` service principal can be selected.

1. Choose **Next**.

**Note**
Under **Proxy type and version control**, **Type** is **Envoy** and **Version** shows the supported proxy version. Both are read-only.

**Note**
To set secondary behavior at create time, expand **Attributes** and change any of **WAF fail open**, **SYN cookie mode**, **Deletion protection**, or **Envoy log level**. Unchanged attributes take their default values. For details, see [Proxy attributes](proxy-attributes.md).

**Note**
To associate ACM certificates after the proxy is created, select them under **Certificates** in this step. For details, see [Terminate TLS with an ACM certificate](tls-acm-certificate.md).

**To provide the configuration (Step 2: Configure proxy)**

1. Under **Proxy configuration**, for **Source**, choose how to import your configuration: **Select S3 bucket**, **Enter manually**, **Upload local file**, or **Reuse from existing proxy**.

1. Provide the Envoy configuration YAML using the selected source.

1. (Optional) Under **Advanced configurations**, for **Proxy configuration archive**, upload a `.zip` archive of files that your configuration references.

1. Choose **Next**.

**Note**
You can choose an **Encryption type** under **Advanced configurations**. To use your own key, choose the customer managed key option and select an **AWS KMS key**. The key policy must trust the `elasticloadbalancing.amazonaws.com` service principal. For details, see [Encrypt a proxy configuration with a customer managed key](proxy-encryption.md).

**To add service integrations (Step 3: Add service integrations)**

1. Under **AWS Web Application Firewall (WAF)**, select **Apply application layer security protections** to associate a web ACL.

1. For **Web ACL**, choose an existing web ACL to associate with the proxy.

1. Choose **Next**.

**Note**
Service integrations are optional. You can add or change the WAF association after you create the proxy. For details, see [Protect a proxy with AWS WAF](waf.md).

**To review and create (Review and create)**

1. Review the settings for **Step 1: Create proxy**, **Step 2: Configure proxy**, and **Step 3: Service integrations**.

1. To change a setting, choose **Edit** for that step.

1. Choose **Create proxy**.

After you choose **Create proxy**, the proxy starts in the `create-in-progress` state. When provisioning finishes, the proxy enters the `active` state.

------
#### [ AWS CLI ]

**To create a proxy (AWS CLI)**

1. Create a proxy with the **create-proxy** command. Pass the proxy settings with `--cli-input-json` and the configuration content with `--configuration`.

   ```
   aws elb-proxy create-proxy \
     --cli-input-json '{
       "name": "my-proxy",
       "type": "envoy",
       "proxyVersion": "1.40",
       "roleArn": "arn:aws:iam::<account-id>:role/<proxy-role-name>",
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
     --configuration configurationFile={configurationBytes@=file:///tmp/config.yaml},configurationArchive={configurationBytes@=fileb:///tmp/archive.zip}
   ```

   Replace {{account-id}} with your AWS account ID. Replace {{proxy-role-name}} with the name of your proxy role. Replace {{subnet-id-1}} and {{subnet-id-2}} with your subnet IDs. Replace {{security-group-id}} with your security group ID. Replace `/tmp/config.yaml` with the path to your Envoy configuration file, and `/tmp/archive.zip` with the path to your configuration archive.
**Note**
The `configurationArchive` is optional. If your Envoy configuration references no external files, omit the `configurationArchive={...}` portion of `--configuration`.
**Note**
When you use AWS CLI version 2, add `--cli-binary-format raw-in-base64-out`. This version defaults to base64 input, and the flag lets you pass the configuration content as raw bytes.

1. (Optional) To associate a web ACL at create time, add the `waf.web_acl_arn` attribute.

   Fragment:

   ```
     --attributes key=waf.web_acl_arn,value=<web-acl-arn>
   ```

   Replace {{web-acl-arn}} with the ARN of your web ACL. For details, see [Protect a proxy with AWS WAF](waf.md).

1. (Optional) To encrypt the configuration with your own key, add `"customerKmsKeyArn": "<kms-key-arn>"` to the `--cli-input-json` object. Replace {{kms-key-arn}} with the ARN of your customer managed AWS KMS key. For details, see [Encrypt a proxy configuration with a customer managed key](proxy-encryption.md).

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
          # Your Envoy configuration
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
+ `Name`: a name for the proxy.
+ `RoleArn`: the ARN of the proxy role from [Set up ELB for Envoy](setting-up.md).
+ `Subnets`: at least two subnets in different Availability Zones.
+ `SecurityGroups`: one or more security groups in the proxy's VPC.
+ `ConfigurationBytes`: your Envoy configuration.

**Note**
Changing `IpAddressingConfiguration` after creation replaces the proxy.

------

## Verify that the proxy is active
<a name="create-proxy-verify"></a>

Confirm that the proxy finished provisioning before you send traffic to it.

**To check proxy status (AWS CLI)**

1. Run the **get-proxy** command.

   ```
   aws elb-proxy get-proxy --proxy-identifier <proxy-arn>
   ```

   Replace {{proxy-arn}} with the ARN of your proxy. A proxy ARN has the form `arn:aws:elasticloadbalancing:<region>:<account-id>:proxy/...`.

1. Repeat the command until `status` reports `active`. The proxy response also includes the `dnsName` that clients use to reach the proxy.

In the console, the proxy appears on the **Proxies** page, where its status changes from `create-in-progress` to `active`.

## Clean up
<a name="create-proxy-cleanup"></a>

To delete a proxy that you no longer need, see [Delete a proxy](delete-proxy.md).
