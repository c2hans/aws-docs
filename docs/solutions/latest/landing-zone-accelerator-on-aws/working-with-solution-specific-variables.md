---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/working-with-solution-specific-variables.html
---

# Working with solution-specific variables
<a name="working-with-solution-specific-variables"></a>

This section provides information about working with variables.

## Policy replacement variables
<a name="policy-replacement-variables"></a>

This solution supports the concept of environment variables in policy documents. These variables are processed at CDK application runtime and are replaced with contextual values based on the runtime environment and, if applicable, user-defined configurations.

The following policy types support variable replacements:
+ AWS Organization policies (SCPs, tag policies, backup policies)
+ IAM policies
+ AWS KMS key policies
+ VPC endpoint policies (available as of v1.5.0)

  Policy replacement variables support the following variable keys:
+  `${ACCELERATOR_DEFAULT_PREFIX_SHORTHAND}` - Short version of the prefix applied to solution-provisioned resources (first four letters, capitalized)
+  `${ACCELERATOR_PREFIX_ND}` - Prefix applied to solution-provisioned resources without dashes
+  `${ACCELERATOR_PREFIX_LND}` - Prefix applied to solution-provisioned resources in lowercase and without dashes
+  `${ACCELERATOR_PREFIX}` - Prefix applied to solution-provisioned resources
+  `${ACCELERATOR_SSM_PREFIX}` - Prefix applied to solution-provisioned Parameter Store parameters (includes leading forward slash (/))
+  `${ACCOUNT_ID}` - Account ID the policy is deployed to
+  `${AUDIT_ACCOUNT_ID}` - Account ID of the Audit account
+  `${ACCELERATOR_CENTRAL_LOGS_BUCKET_NAME}` - Central Log bucket name
+  `${HOME_REGION}` - AWS Region the solution is deployed to
+  `${LOGARCHIVE_ACCOUNT_ID}` - Account ID of the Log Archive account
+  `${MANAGEMENT_ACCOUNT_ACCESS_ROLE}` - Role name that the solution uses for cross-account access, for example, `AWSControlTowerExecution`
+  `${MANAGEMENT_ACCOUNT_ID}` - Account ID of the Management account
+  `${PARTITION}` - Partition that the policy is deployed to
+  `${ORG_ID}` - The ID of the AWS Organization
+  `${REGION}` - AWS Region that the policy is deployed to
**Note**
As of version 1.4.0 of this solution, the `ACCELERATOR_PREFIX` and associated variables listed are derived from the **Accelerator Resource name Prefix** value input in the [installer stack parameter](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/working-with-solution-specific-variables.html) . For previous versions, the prefix value was `AWSAccelerator`.

The following policy sample shows how you can implement the variables:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyAllAWSServicesExceptBreakglassRoles",
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "ArnNotLike": {
          "aws:PrincipalArn": [
            "arn:${PARTITION}:iam::*:role/${MANAGEMENT_ACCOUNT_ACCESS_ROLE}",
            "arn:${PARTITION}:iam::*:role/aws*",
            "arn:${PARTITION}:iam::*:role/${ACCELERATOR_PREFIX}*",
            "arn:${PARTITION}:iam::*:role/cdk-accel-*"
          ]
        }
      }
    }
  ]
}
```

## Parameter Store reference variables
<a name="parameter-store-reference-variable"></a>

This solution provides dynamic lookups from the Parameter Store within configuration files. This feature primarily meets two customer needs:
+ Customers wishing to reuse a single generic Landing Zone Accelerator on AWS configuration across multiple Landing Zone Accelerator on AWS deployments
+ Customers wishing to simplify their configuration files and decrease the number of manual configuration edits

**Note**
Parameter Store lookup functionality was made available starting with the v1.5.0 release.

You can leverage this pattern by creating an additional, optional configuration file in the configuration repository named `replacements-config.yaml`.

```
 globalReplacements:
  - key: SnsEmail
    path: /accelerator/replacements/SnsEmailAddress
```

In the above example, we have a single *replacement* defined:
+ The configuration files use the `key` in `SnsEmail` to indicate which value to replace.
+ The path of `/accelerator/replacements/SnsEmailHigh` describes the Parameter Store path where the corresponding replacement value exists.

**Note**
Parameter Store parameters used for replacements must exist in the `homeRegion` of the management account.

You must explicitly create the Systems Manager parameter `/accelerator/replacements/SnsEmailHigh`. Create this Systems Manager parameter with an appropriate replacement value through Landing Zone Accelerator on AWS or by following this guide.

```
 aws ssm put-parameter \
     --name "/accelerator/replacements/SnsEmailAddress" \
     --value "example_email@example.com" \
     --type String \
```

After you create the Systems Manager parameter, you can reference the value from within the configuration files. For example, we might create a new Amazon SNS topic in the `global-config.yaml` file where the email address value uses the replacement previously defined:

```
  snsTopics:
    topics:
     - name: SampleTopic
        emailAddresses:
          - {{SnsEmail}}
```

**Note**
All YAML configuration files use replacements except `accounts-config.yaml`.

This feature also includes functionality to look up account IDs based on the account name without the use of Systems Manager parameters:

```
  parameters:
   - name: TrustedAccounts
     value: {{account Management}}
```

The double-curly brace notation is reserved for usage in the LZA configuration files by LZA replacements and [SSM dynamic references](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html#dynamic-references-ssm). Any instances of this syntax that do not follow the SSM dynamic reference syntax or exist in the `replacements-config.yaml` file will throw an error during configuration validation.

If you must use this syntax in your configuration files, you can skip static configuration validation by setting `cdkOptions.skipStaticValidation` to `true` in the `global-config.yaml` file.

## $ACCEL\_LOOKUP reference variable
<a name="accel-lookup-reference-variable"></a>

This solution supports the concept of referencing variables within configuration files. This lookup is processed at CDK application runtime and are replaced with contextual values based on the runtime environment and, if applicable, user-defined configurations. These variables are used in specific cases within the configuration files for dynamically looking up specific values and are scoped to only the following use cases:

### Systems Manager automation document variables
<a name="ssm-automation-document-variables"></a>

The following variables allow for defining Systems Manager Automation documents in the solution `security-config.yaml`:
+  `${ACCEL_LOOKUP::KMS}` - Resolves to the main Amazon S3 AWS KMS key ID for the solution deployment
+  `${ACCEL_LOOKUP::Bucket:elbLogs}` - Resolves to the centralized logging Amazon S3 bucket for Elastic Load Balancing
+  `${ACCEL_LOOKUP::InstanceProfile:EC2-Default-SSM-AD-Role}` - Used for custom remediation AWS Config rules to allow automatic remediation to be performed using that role on certain rules

### Launch template variables
<a name="launch-template-variables"></a>

The following variable allow for referencing local or public image IDs for Amazon EC2 launch templates in the solution `customization-config.yaml`:
+  `${ACCEL_LOOKUP::ImageId:/path/to/ssm/parameter}` - Local or public SSM parameter store lookup for Image ID

### Amazon EC2 firewall configuration variables
<a name="ec2-firewall-configuration-variables"></a>

As of v1.5.0 of this solution, the following variables are available when deploying a custom third-party Amazon EC2 firewall in the solution `customization-config.yaml`. These variables require your firewall vendor to support bootstrapping the instance using a configuration file from an S3 bucket. For more information on the specific implementation, see the [Ec2FirewallInstanceConfig](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/typedocs/latest/classes/_aws_accelerator_config.Ec2FirewallInstanceConfig.html) or [Ec2FirewallAutoScalingGroupConfig](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/typedocs/latest/classes/_aws_accelerator_config.Ec2FirewallAutoScalingGroupConfig.html) references.

#### Hostname replacement
<a name="hostname-replacement"></a>

Use this variable to lookup up the name of the firewall instance as defined in `customization-config.yaml`.

**Note**
This replacement is only available for standalone firewall instances defined under [Ec2FirewallInstanceConfig](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/typedocs/latest/classes/_aws_accelerator_config.Ec2FirewallInstanceConfig.html). Firewall autoscaling groups are not supported.

 `${ACCEL_LOOKUP::EC2:INSTANCE:HOSTNAME}`

#### VPC replacements
<a name="vpc-replacements"></a>

Use these variables to look up metadata about the VPC that the firewall is deployed to.

**Note**
 `${ACCEL_LOOKUP::EC2:VPC:<METADATA_TYPE>_<INDEX>} - <METADATA_TYPE>` is a type listed below, and `<INDEX>` is the index number of the VPC CIDR range based on the order in which the CIDR was associated with the VPC. Index numbering is zero-based, so the index of the primary range associated with the VPC is `0`.

| Metadata Type | Description |
| --- | --- |
| CIDR | The VPC CIDR range in CIDR notation (specifically, 10.0.0.0/16) |
| NETMASK | The network mask of the VPC CIDR (specifically, 255.255.0.0) |
| NETWORKIP | The network address of the VPC CIDR (specifically, 10.0.0.0) |
| ROUTERIP | The VPC router address of the VPC CIDR (specifically, 10.0.0.1) |

Example usage: `${ACCEL_LOOKUP::EC2:VPC:CIDR_0}` - translates to the primary CIDR range of the VPC.

#### Subnet replacements
<a name="subnet-replacements"></a>

Use these variables to look up metadata about subnets in the VPC the firewall is deployed to.

**Note**
 `${ACCEL_LOOKUP::EC2:SUBNET:<METADATA_TYPE>:<SUBNET_NAME>} - <METADATA_TYPE>` is a type listed below, and `<SUBNET_NAME>` is the logical name of the subnet as defined in your solution `network-config.yaml`.

| Metadata Type | Description |
| --- | --- |
| CIDR | The subnet CIDR range in CIDR notation (specifically, 10.0.0.0/16) |
| NETMASK | The network mask of the subnet (specifically, 255.255.0.0) |
| NETWORKIP | The network address of the subnet (specifically, 10.0.0.0) |
| ROUTERIP | The VPC router address of the subnet (specifically, 10.0.0.1) |

Example usage: `${ACCEL_LOOKUP::EC2:SUBNET:CIDR:firewall-subnet-a}` - translates to the CIDR range of a subnet named `firewall-subnet-a` in the VPC.

#### Network interface IP replacements
<a name="network-interface-ip-replacements"></a>

Use these variables to look up public and private IP addresses assigned to the firewall network interfaces.

**Note**
These replacements are only available for standalone firewall instances defined under [Ec2FirewallInstanceConfig](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/typedocs/latest/classes/_aws_accelerator_config.Ec2FirewallInstanceConfig.html). Firewall autoscaling groups are not supported.

**Note**
 `${ACCEL_LOOKUP::EC2:ENI_<ENI_INDEX>:<IP_TYPE>_<IP_INDEX>} - <ENI_INDEX>` is the device index of the network interface as defined in the firewall launch template, `<IP_TYPE>` is either a public or private IP of the interface, and `<IP_INDEX>` is the index of the interface IP address. Index numbering is zero-based, so the primary interface of the instance is `0` and its primary IP address is also `0`.

| IP Type | Description |
| --- | --- |
| PRIVATEIP | A private IP address associated with the interface |
| PUBLICIP | A public IP address associated with the interface |

Example usage: `${ACCEL_LOOKUP::EC2:ENI_0:PRIVATEIP_0}` - translates to the primary private IP address of the primary network interface.

#### Network interface subnet replacements
<a name="network-interface-subnet-replacements"></a>

Use these variables to look up metadata about the subnet that a network interface is deployed to.

**Note**
These replacements are only available for standalone firewall instances defined under ` [Ec2FirewallInstanceConfig](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/typedocs/latest/classes/_aws_accelerator_config.Ec2FirewallInstanceConfig.html) `. Firewall autoscaling groups are not supported.

 `${ACCEL_LOOKUP::EC2:ENI_<ENI_INDEX>:SUBNET_<METADATA_TYPE>} - <ENI_INDEX>` is the device index of the network interface as defined in the firewall launch template and `<METADATA_TYPE>` is a type listed below. Index numbering is zero-based, so the primary interface of the instance is `0`.

| Metadata Type | Description |
| --- | --- |
| CIDR | The subnet CIDR range in CIDR notation (specifically, 10.0.0.0/16) |
| NETMASK | The network mask of the subnet (specifically, 255.255.0.0) |
| NETWORKIP | The network address of the subnet (specifically, 10.0.0.0) |
| ROUTERIP | The VPC router address of the subnet (specifically, 10.0.0.1) |

Example usage: `${ACCEL_LOOKUP::EC2:ENI_0:SUBNET_CIDR}` - translates to the subnet CIDR range of the primary network interface.

#### Site-to-Site VPN replacements
<a name="site-to-site-vpn-replacements"></a>

Use these variables to look up metadata about site-to-site VPNs that are created between a firewall network interface and AWS gateway.

**Note**
These replacements are only available for standalone firewall instances defined under [Ec2FirewallInstanceConfig](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/typedocs/latest/classes/_aws_accelerator_config.Ec2FirewallInstanceConfig.html). To utilize the replacements, there must be a [CustomerGatewayConfig](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/typedocs/latest/classes/_aws_accelerator_config.CustomerGatewayConfig.html) that references a firewall instance network interface as its `ipAddress` property. You can reference any VPN connection `name` configured under this customer gateway item for dynamic configuration of the VPN connection(s) on your firewall. Firewall autoscaling groups are not supported for this replacement type.

**Note**
 `${ACCEL_LOOKUP::EC2:VPN:<METADATA_TYPE>:<VPN_NAME>} - <METADATA_TYPE>` is a type listed below, and `<VPN_NAME>` is the logical name of the VPN connection as defined in your solution `network-config.yaml`. For metadata types with index values, index numbering is zero-based, so the primary tunnel of the VPN connection is `0`.

| Metadata Type | Description |
| --- | --- |
|  **AWS\_BGPASN**  | The BGP autonomous system number (ASN) of the AWS gateway device (specifically, 65000) |
|  **CGW\_BGPASN**  | The BGP autonomous system number (ASN) of the customer gateway device (specifically, 65000) |
|  **CGW\_OUTSIDEIP**  | The outside (public) IP address of the customer gateway device |
|  ** `AWS_INSIDEIP_<TUNNEL_INDEX>` **  | The inside (link-local) IP address of the AWS gateway device, where `<TUNNEL_INDEX>` is the index number of the VPN tunnel (specifically, 169.254.100.1) |
|  **CGW\_INSIDEIP\_`<TUNNEL\_INDEX>`**  | The inside (link-local) IP address of the customer gateway device, where `<TUNNEL_INDEX>` is the index number of the VPN tunnel (specifically, 169.254.100.2) |
|  **AWS\_OUTSIDEIP\_`<TUNNEL\_INDEX>`**  | The outside (public) IP address of the AWS gateway device, where `<TUNNEL_INDEX>` is the index number of the VPN tunnel |
|  **INSIDE\_CIDR\_`<TUNNEL\_INDEX>`**  | The inside (link-local) CIDR range of the tunnel, where `<TUNNEL_INDEX>` is the index number of the VPN tunnel |
|  **INSIDE\_NETMASK\_`<TUNNEL\_INDEX>`**  | The inside (link-local) subnet mask of the tunnel, where `<TUNNEL_INDEX>` is the index number of the VPN tunnel (specifically, 255.255.255.252) |
|  **PSK\_`<TUNNEL\_INDEX>`**  | The pre-shared key of the tunnel, where `<TUNNEL_INDEX>` is the index number of the VPN tunnel |

Example usage: `${ACCEL_LOOKUP::EC2:VPN:AWS_OUTSIDEIP_0:accelerator-vpn}` - translates to the AWS-side public IP of the primary VPN tunnel for a VPN named `accelerator-vpn`.

#### Firewall configuration S3 bucket replacement
<a name="firewall-configuration-s3-bucket-replacement"></a>

To support the above dynamic configuration replacements, the solution creates an S3 bucket in the target account from which the Amazon EC2 firewall can read the resulting configuration file. To dynamically target this bucket in your Amazon EC2 firewall user data script, you may use the following variable:

 `${ACCEL_LOOKUP::S3:BUCKET:firewall-config}`

#### Customer gateway IP replacement
<a name="customer-gateway-ip-replacement"></a>

To support the previous dynamic Amazon EC2 firewall customer gateway and site-to-site VPN connection creation, use the following variable as the [CustomerGatewayConfig](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/typedocs/latest/classes/_aws_accelerator_config.CustomerGatewayConfig.html) `ipAddress` property:

 `${ACCEL_LOOKUP::EC2:ENI_<ENI_INDEX>:<FIREWALL_INSTANCE_NAME>},` where `<ENI_INDEX>` is the device index of the network interface as defined in the firewall launch template and `<FIREWALL_INSTANCE_NAME>` is the name of the firewall instance as defined in [EC2FirewallInstanceConfig](https://awslabs.github.io/landing-zone-accelerator-on-aws/latest/typedocs/latest/classes/_aws_accelerator_config.Ec2FirewallInstanceConfig.html). Index numbering is zero-based, so the primary interface of the instance is `0`.

**Note**
This reference variable is only available for Amazon EC2 firewall network interfaces that have the `associateElasticIp` property set to `true`. It is not supported for Amazon EC2 firewall autoscaling groups.

Example usage: `${ACCEL_LOOKUP::EC2:ENI_0:accelerator-firewall}` - translates to the primary public IP address of the primary network interface of a firewall named `accelerator-firewall`.
