---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/developer-guide.html
---

# Developer guide
<a name="developer-guide"></a>

This section addresses the source code, configuration files, and administrator tasks for this solution.

## Source code
<a name="source-code"></a>

Visit our [GitHub repository](https://github.com/awslabs/landing-zone-accelerator-on-aws) to download the source files for this solution and to share your customizations with others. The Landing Zone Accelerator on AWS templates are generated using the AWS CDK. Refer to the [README.md](https://github.com/awslabs/landing-zone-accelerator-on-aws/blob/main/README.md) file for additional information.

## Accessing solution outputs through Parameter Store
<a name="accessing-solution-outputs-through-parameter-store"></a>

This solution provides configuration management for resources provisioned through Parameter Store. The solution records the following resources types and their respective Parameter Store paths.

### Application resources
<a name="application-resources"></a>

| Metadata Type | Description | Path |
| --- | --- | --- |
| Target Group ARN | The Amazon Resource Name (ARN) of the Target Group where ` ${0}${1}#` is replaced with the VPC name, and ` ${2} ` is replaced with the target group name |  `/application/targetGroup/${0}/${1}/${2}/arn`  |

### AWS CloudFormation stacks
<a name="aws-cloudformation-stacks"></a>

| Metadata Type | Description | Path |
| --- | --- | --- |
| AWS CloudFormation Stack ID | The solution CloudFormation stack ID where ` ${0} ` is replaced with the stack name |  `/${0}/stack-id`  |
| Accelerator Version ID | The Accelerator Version where ` ${0} ` is replaced with the stack name |  `/${0}/version`  |

### AWS Organization resources
<a name="aws-organization-resources"></a>

| Metadata Type | Description | Path |
| --- | --- | --- |
| Accelerator Service Control Policy ID | The ID of the Service Control Policy where ` ${0} ` is replaced with the SCP name |  `/organizations/scp/${0}/id`  |

### Central Network resources
<a name="central-network-resources"></a>

| Metadata Type | Description | Path |
| --- | --- | --- |
| VPC IP Address Manager ID | The ID of the VPC IP Address Manager (IPAM) where ` ${0} ` is replaced with the IPAM name |  `/network/ipam/${0}/id`  |
| VPC IP Address Manager Pool ID | The ID of the VPC IP Address Manager (IPAM) Pool where ` ${0} ` is replaced with the IPAM Pool name |  `/network/ipam/pools/${0}/id`  |
| VPC IP Address Manager Scope ID | The ID of the VPC IP Address Manager (IPAM) scope where ` ${0} ` is replaced with the IPAM scope name |  `/network/ipam/scopes/${0}/id`  |
| Amazon Network Firewall ARN | The Amazon Resource Name (ARN) of the Amazon Network Firewall where ` ${0}$${1}#` is replaced with the network firewall name |  `/network/vpc/${0}/networkFirewall/${1}/arn`  |
| Amazon Network Firewall Policy ARN | The Amazon Resource Name (ARN) of the Amazon Network Firewall policy where ` ${0} ` is replaced with the network firewall policy name |  `/network/networkFirewall/policies/${0}/arn`  |
| Amazon Network Firewall Rule Group ARN | The Amazon Resource Name (ARN) of the Amazon Network Firewall Rule Group where ` ${0} ` is replaced with the rule group name |  `/network/networkFirewall/ruleGroups/${0}/arn`  |

### Direct Connect resources
<a name="direct-connect-resources"></a>

| Metadata Type | Description | Path |
| --- | --- | --- |
| Direct Connect Virtual Interface (VIF) ID | The ID of the Direct Connect VIF where ` ${0} ` is replaced with the Direct Connect gateway name; ` ${1} ` is replaced with the VIF name |  `/network/directConnectGateways/${0}/virtualInterfaces/${1}/id`  |
| Direct Connect Gateway ID | The ID of the Direct Connect gateway where ` ${0} ` is replaced with the Direct Connect gateway name |  `/network/directConnectGateways/${0}/id`  |

### Global Network resources
<a name="global-network-resources"></a>

| Metadata Type | Description | Path |
| --- | --- | --- |
| ACM Certificate ARN | The Amazon Resource Name (ARN) of an ACM certificate where ` ${0} ` is replaced with the certificate name |  `/acm/${0}/arn`  |
| Prefix List ID | The ID of the prefix list where ` ${0} ` is replaced with the prefix list name |  `/network/prefixList/${0}/id`  |

### IAM resources
<a name="identity-access-management-iam-resources"></a>

| Metadata Type | Description | Path |
| --- | --- | --- |
| IAM Role ARN | The ARN of the IAM role where ` ${0} ` is replaced with the IAM role name |  `/iam/role/${0}/arn`  |
| IAM Management Policy ARN | The ARN of the IAM managed policy where ` {0} ` is replaced with the IAM managed policy name |  `/iam/policy/${0}/arn`  |
| IAM Group ARN | The ARN of the IAM group where ` ${0} ` is replaced with the IAM group name |  `/iam/group/${0}/arn`  |
| IAM User ARN | The ARN of the IAM user where ` ${0} ` is replaced with the IAM user name |  `/iam/user/${0}/arn`  |

### Load Balancer resources
<a name="load-balancer-resources"></a>

| Metadata Type | Description | Path |
| --- | --- | --- |
| Application Load Balancer ID | The ID of the Application Load Balancer (ALB) where ` ${0} ` is replaced with the VPC name; ` ${1} ` is replaced with the ALB name |  `/network/vpc/${0}/alb/${1}/id`  |
| Network Load Balancer ID | The ID of the Network Load Balancer (NLB) where ` ${0} ` is replaced with the VPC name; ` ${1} ` is replaced with the NLB name |  `/network/vpc/${0}/nlb/${1}/id`  |
| Gateway Load Balancer ARN | The ARN of the Gateway Load Balancer (GWLB) where ` ${0} ` is replaced with the GWLB name |  `/network/gwlb/${0}/arn`  |
| Gateway Load Balancer Endpoint Service ID | The ID of the GWLB service endpoint where ` ${0}$ ` is replaced with the GWLB name |  `/network/gwlb/${0}/endpointService/id`  |

### Route 53 resources
<a name="route-53-resources"></a>

| Metadata Type | Description | Path |
| --- | --- | --- |
| Route 53 DNS Firewall Rule Group ID | The ID of the Route 53 DNS firewall rule group ID where ` ${0} ` is replaced with the DNS firewall rule group name. |  `/network/route53Resolver/firewall/ruleGroups/${0}/id`  |
| Interface Endpoint DNS name | The DNS name of the interface endpoint where ` ${0} ` is replaced with the VPC name; ` ${1} ` is replaced with the interface endpoint service name. |  `/network/vpc/${0}/endpoints/${1}/dns`  |
| Interface Endpoint Hosted Zone ID | The hosted zone ID of the interface endpoint ` ${0} ` is replaced with the VPC name; ` ${1} ` is replaced with the interface endpoint service name. |  `/network/vpc/${0}/endpoints/${1}/hostedZoneId`  |
| Route 53 Private Hosted Zone ID | The ID of the private hosted zone where ` ${0} ` is replaced with the VPC name; ` ${1} ` is replaced with the interface endpoint service name. |  `/network/vpc/${0}/route53/hostedZone/[.red]#${1}/id`  |
| Route 53 Query Logs | The configuration ID of Route 53 query logs where ` ${0} ` is replaced with the query logs configuration name. |  `/network/route53Resolver/queryLogConfigs/${0}/id`  |
| Route 53 Resolver Endpoint ID | The ID of the Route 53 resolver endpoint where ` ${0} ` is replaced with the resolver endpoint name. |  `/network/route53Resolver/endpoints/${0}/id`  |

### Transit Gateway resources
<a name="transit-gateway-tgw-resources"></a>

| Metadata Type | Description | Path |
| --- | --- | --- |
| Transit Gateway ID | The ID of the transit gateway where ` ${0} ` is replaced with the transit gateway name |  `/network/transitGateways/${0}/id`  |
| Transit Gateway Peering ID | The ID of the transit gateway peering ID where ` ${0} ` is replaced with the transit gateway name for either the requester or accepter transit gateway\*; ` ${1} ` is replaced with the transit gateway peering name. |  `/network/transitGateways/${0}/peering/${1}/id`  |
| Transit Gateway Route Table ID | The ID of the transit gateway route table where ` ${0} ` is replaced with the transit gateway name; ` ${1} ` is replaced with the route table name. |  `/network/transitGateways/${0}/routeTables/${1}/id`  |
| Transit Gateway VPN attachment ID | The ID of the transit gateway VPN attachment where ` ${0} ` is replaced with the VPN Connection name. |  `/network/vpnConnection/${0}/id`  |
+ This depends on the account that the parameter is being put in.

### VPC resources
<a name="virtual-private-cloud-vpc-resources"></a>

| Metadata Type | Description | Path |
| --- | --- | --- |
| Virtual Private Cloud (VPC) ID | The ID of the VPC where ` ${0} ` is replaced with the VPC name. |  `/network/vpc/${0}/id`  |
| VPC Peering ID | The ID of the VPC peering connection where ` ${0} ` is replaced with the VPC peering name. |  `/network/vpcPeering/${0}/id`  |
| Internet Gateway ID | The ID of the internet gateway where ` ${0} ` is replaced with the VPC name. |  `/network/vpc/${0}/internetGateway/id`  |
| Virtual Private Gateway ID | The ID of the virtual private gateway where ` ${0} ` is replaced with the VPC name. |  `/network/vpc/${0}/virtualPrivateGateway/id`  |
| Subnet ID | The ID of the subnet where ` ${0} ` is replaced with the VPC name; `${1} is replaced with the subnet name |  `/network/vpc/${0}/subnet/${1}/id`  |
| Route Table ID | The ID of the route table where ` ${0} ` is replaced with the VPC name; ` ${1} ` is replaced with the route table name |  `/network/vpc/${0}/routeTable/${1}/id`  |
| Security Group ID | The ID of the security group where ` ${0} ` is replaced with the VPC name; ` ${1} ` is replaced with the security group name |  `/network/vpc/${0}/securityGroup/${1}/id`  |
| Network ACL ID | The ID of the network ACL (NACL) where ` ${0} ` is replaced with the VPC name; ` ${1} ` is replaced with the NACL name |  `/network/vpc/${0}/networkAcl/${1}/id`  |
| NAT Gateway ID | The ID of the NAT Gateway where ` ${0} ` is replaced with the VPC name; ` ${1} ` is replaced with the NAT Gateway name |  `/network/vpc/${0}/natGateway/${1}/id`  |
| Transit Gateway VPC Attachment ID | The ID of the transit gateway VPC attachment where ` ${0} ` is replaced with the VPC name; ` ${1} ` is replaced with the transit gateway attachment name |  `/network/vpc/${0}/transitGatewayAttachment/${1}/id`  |

### VPN resources
<a name="virtual-private-network-vpn-resources"></a>

| Metadata Type | Description | Path |
| --- | --- | --- |
| Customer Gateway ID | The ID of the customer gateway where ` ${0} ` is replaced with the customer gateway name |  `/network/customerGateways/${0}/id`  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
