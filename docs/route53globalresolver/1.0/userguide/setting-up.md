---
source_url: https://docs.aws.amazon.com/route53globalresolver/1.0/userguide/setting-up.html
---

# Setting up account access for Amazon Route 53 Global Resolver

Before you start using Amazon Route 53 Global Resolver, you need an AWS account and the appropriate permissions to access Amazon Route 53 Global Resolver resources. This includes creating IAM users and roles with the necessary permissions.

This section guides you through the steps required to configure users and roles to access Amazon Route 53 Global Resolver. For background and additional information about identity and access management for Amazon Route 53 Global Resolver, see [Identity and access management for Amazon Route 53 Global Resolver](security-iam.md).

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Creating policies and roles](#setting-up-permissions)
+ [Network considerations](#setting-up-network)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).

## Creating policies and roles
<a name="setting-up-permissions"></a>

Configure AWS Identity and Access Management (IAM) permissions so your team can deploy and manage Amazon Route 53 Global Resolver resources. You can use administrative permissions for full access or read-only permissions for monitoring and viewing configurations.

All Amazon Route 53 Global Resolver API operations require appropriate IAM permissions. If you don't have the required permissions, API calls will return `AccessDeniedException` (401) or `UnauthorizedException` (401) errors.

### Administrative permissions
<a name="setting-up-permissions-admin"></a>

If you're setting up Amazon Route 53 Global Resolver for the first time or managing all aspects of the service, you need administrative permissions. You can use these AWS managed policies:
+ `AmazonRoute53GlobalResolverFullAccess` - Provides full access to Amazon Route 53 Global Resolver resources, including creating, updating, and deleting global resolvers, DNS views, firewall rules, and domain lists
+ `AmazonRoute53FullAccess` - Required if you plan to use private hosted zone forwarding
+ `CloudWatchLogsFullAccess` - Required if you plan to send logs to Amazon CloudWatch
+ `AmazonS3FullAccess` - Required if you plan to import firewall domain lists from Amazon S3 or send logs to Amazon S3

### Read-only permissions
<a name="setting-up-permissions-readonly"></a>

If you only need to view Amazon Route 53 Global Resolver configurations and logs, you can use these AWS managed policies:
+ `AmazonRoute53GlobalResolverReadOnlyAccess` - Provides read-only access to Amazon Route 53 Global Resolver resources, including viewing global resolvers, DNS views, firewall rules, domain lists, and access sources
+ `AmazonRoute53ReadOnlyAccess` - Required to view private hosted zone associations
+ `CloudWatchReadOnlyAccess` - Required to view logs in Amazon CloudWatch
+ `AmazonS3ReadOnlyAccess` - Required to view firewall domain list files stored in Amazon S3

## Network considerations
<a name="setting-up-network"></a>

Before implementing Amazon Route 53 Global Resolver, consider the following network requirements:

Client IP ranges
This is only required when using access source-based authentication. Identify the IP address ranges (CIDR blocks) for all clients that will use Amazon Route 53 Global Resolver. You'll need these for configuring rules for your access source.

DNS protocols
Determine which DNS protocols your clients will use:
+ **Do53** - Standard DNS over port 53 (UDP/TCP)
+ **DoH** - DNS-over-HTTPS for encrypted queries
+ **DoT** - DNS-over-TLS for encrypted queries

Firewall and security groups
Ensure your network firewalls and security groups allow outbound traffic to Amazon Route 53 Global Resolver anycast IP addresses on the appropriate ports (53 for Do53, 443 for DoH, 853 for DoT).

AWS Cloud WAN core network connectivity
This is only required when you use AWS Cloud WAN (Cloud WAN) core network segments as access sources. Connect your global resolver to a Cloud WAN core network with a core network endpoint so that the core network's segments can be used as access sources. When you connect a core network, clients that reach the global resolver from its segments can resolve DNS queries without you managing individual IP ranges. For more information about core network endpoints, see [Connecting a global resolver to a Cloud WAN core network](core-network-endpoints.md).
