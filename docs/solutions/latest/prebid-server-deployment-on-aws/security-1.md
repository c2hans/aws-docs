---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/security-1.html
---

# Security
<a name="security-1"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

AWS Identity and Access Management (IAM) roles allow customers to assign granular access policies and permissions to services and users on the AWS Cloud. This solution creates IAM roles and policies with minimal permission that grant access to the solution’s resources.

## Amazon CloudFront
<a name="amazon-cloudfront"></a>

This solution deploys an Amazon CloudFront distribution and uses the default CloudFront domain name and SSL certificate. The default CloudFront SSL certificate only supports TLSv1. To use a later TLS version (TLS1.2 and above), use your own domain name and custom SSL certificate. For more information, refer to [Using alternate domain names and HTTPS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-alternate-domain-names.html) in the *Amazon CloudFront Developer Guide*.

The Amazon CloudFront distribution is the unified network entry point. It helps to reduce latency by delivering data through globally dispersed points of presence (PoPs) with automated network mapping and intelligent routing. The inbound traffic to the CloudFront can be either HTTP or HTTPS for compatibility with various clients. As the Prebid Server hosted by ECS only supports HTTP, HTTPS proxy design is used in this solution to improve security. The CloudFront distribution acts as a TLS proxy, where APIs can be delivered over HTTPS using the latest version Transport Layer Security (TLSv1.3) to encrypt and secure communication between viewer clients and the CloudFront.

## Application Load Balancer (ALB)
<a name="application-load-balancer-alb-1"></a>

ALB distributes incoming request traffic for Prebid Server through the cluster of containers. ALB provides a single entry point into the cluster, and it is the primary origin for the CloudFront distribution. CloudFront and the ALB use a shared secret header to prevent external traffic from bypassing the CloudFront distribution and accessing ALB directly. For more information, see [Restricting access to Application Load Balancers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.html) in the *Amazon CloudFront Developer Guide*.

## Amazon VPC
<a name="amazon-vpc-1"></a>

Amazon VPC is configured with multiple subnets, routes, security groups, and NAT gateways. Security groups permit traffic to and from the subnets. The VPC contains the network interfaces for the Prebid Server cluster nodes. ALB has an interface in each private subnet of the VPC. Each container instance (or node) has an interface in its private subnet of the VPC. The actual number of interfaces varies based on the number of containers running. The VPC is configured for private IP addresses only, and container networks configured within the VPC use the NAT gateway as a default route to the internet for communication.

## AWS Fargate
<a name="aws-fargate"></a>

This solution uses Amazon ECS to containerize the Prebid Server. The container runs the open source Prebid Server and is hosted by the Elastic Container Repository for AWS Solutions. A custom build is applied to the open source project’s default container in configuration settings for areas including file output and bidder adapter. To see how the ECS containers are constructed, refer to the [Dockerfile](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws/blob/main/deployment/ecr/prebid-server/Dockerfile). If you need to access these containers while they are running in Fargate, see [Using Amazon ECS Exec to access your containers on AWS Fargate and Amazon EC2](https://aws.amazon.com/blogs/containers/new-using-amazon-ecs-exec-access-your-containers-fargate-ec2/) on the *AWS Blog*.

## Security groups
<a name="security-groups"></a>

This solution creates an Amazon EC2 security group within an Amazon VPC and associates it with ALB to act as a virtual firewall for the EC2 instances to control incoming and outgoing traffic. A rule with prefix list is added to the security group that allows ingress only from the CloudFront distribution.

## AWS WAF
<a name="aws-waf-1"></a>

This solution deploys AWS WAF and Shield Standard as a protection mechanism from DDoS attacks against the Prebid Server cluster. One or more managed rule groups can be activated in AWS WAF by default after extended testing including rules in the Baseline Rule Group and the IP Reputation Rule Group. AWS WAF allows the securement of web applications’ API from attacks before reaching to the servers. The customer has the option to activate, purchase, or use existing rule subscriptions, or add regular expression or CIDR matching rules as needed.

## Customer managed AWS KMS keys
<a name="customer-managed-aws-kms-keys"></a>

AWS Key Management Service (KMS) lets customers create and manage cryptographic keys to activate server-side encryption. This solution creates six KMS keys and uses them in the S3 buckets storing artifacts, CloudFront access log data, CloudTrail events, DataSync log and metric files, and metadata of AWS AWS Glue Data Catalog to secure data at rest.

## Audit trails
<a name="audit-trails"></a>

CloudTrail is configured in this solution for auditing API calls against resources and used for problem analysis and remediation. CloudWatch alarms are used by compute resources for software failures. All compute resources send logging output to CloudWatch logs. CloudFront standard logs are configured to create log files that contain information about the user requests initiated to the solution’s CloudFront distribution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
