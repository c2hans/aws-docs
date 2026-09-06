---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-controls-by-caf-capability/infrastructure-controls.html
---

# Security control recommendations for protecting infrastructure
<a name="infrastructure-controls"></a>

Infrastructure protection is a key part of any security program. It includes control methodologies that help you protect your networks and compute resources. Examples of infrastructure protection include trust boundaries, a defense-in-depth approach, security hardening, patch management, and operating system authentication and authorization. For more information, see [Infrastructure protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in the AWS Well-Architected Framework. The security controls in this section can help you implement best practices for infrastructure protection.

Controls in this section:
+ [Specify default root objects for CloudFront distributions](#default-root-objects)
+ [Scan application code to identify common security issues](#scan-app-code)
+ [Create network layers by using dedicated VPCs and subnets](#network-layers)
+ [Restrict incoming traffic to only authorized ports](#authorized-ports)
+ [Block public access to Systems Manager documents](#block-ssm-doc-access)
+ [Block public access to Lambda functions](#block-lambda-access)
+ [Restrict inbound and outbound traffic in the default security group](#default-security-group)
+ [Scan for software vulnerabilities and unintended network exposure](#scan-software-vulnerabilities)
+ [Set up AWS WAF](#setup-aws-waf)
+ [Configure advanced protections against DDoS attacks](#ddos-attacks)
+ [Use a defense-in-depth approach to control network traffic](#defense-in-depth)

## Specify default root objects for CloudFront distributions
<a name="default-root-objects"></a>

[Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) speeds up distribution of your web content by delivering it through a worldwide network of data centers, which lowers latency and improves performance. If you don't define a default root object, requests for the root of your distribution pass to your origin server. If you are using an Amazon Simple Storage Service (Amazon S3) origin, the request might return a list of the contents in your S3 bucket or a list of the private contents of your origin. Specifying a default root object helps you avoid exposing the contents of your distribution.

For more information, see the following resources:
+ [Specifying a default root object](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html) in the CloudFront documentation

## Scan application code to identify common security issues
<a name="scan-app-code"></a>

The AWS Well-Architected Framework recommends that you scan libraries and dependencies for issues and defects. There are many source code analysis tools that you can use to scan source code. For example, Amazon CodeGuru can scan for common security issues in Java or Python applications and provide recommendations for remediation.

For more information, see the following resources:
+ [CodeGuru documentation](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html)
+ [Source code analysis tools](https://owasp.org/www-community/Source_Code_Analysis_Tools) on the OWASP Foundation website
+ [Perform vulnerability management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_compute_vulnerability_management.html) in the AWS Well-Architected Framework

## Create network layers by using dedicated VPCs and subnets
<a name="network-layers"></a>

The AWS Well-Architected Framework recommends that you group components that share sensitivity requirements into layers. This minimizes the potential scope of impact of unauthorized access. For example, a database cluster that doesn't require internet access should be placed in a private subnet of its VPC to make sure that there is no route to or from the internet.

AWS offers many services that can help you test and identify public reachability. For example, Reachability Analyzer is a configuration analysis tool that helps you test connectivity between a source and destination resources in your VPCs. Also, Network Access Analyzer can help you identify unintended network access to resources.

For more information, see the following resources:
+ [Create network layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_create_layers.html) in the AWS Well-Architected Framework
+ [Reachability Analyzer documentation](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html)
+ [Network Access Analyzer documentation](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html)
+ [Create a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/create-subnets.html) in the Amazon Virtual Private Cloud (Amazon VPC) documentation

## Restrict incoming traffic to only authorized ports
<a name="authorized-ports"></a>

Unrestricted access, such as traffic from the `0.0.0.0/0` source IP address, increases the risk for malicious activity, such as hacking, denial-of-service (DoS) attacks, and loss of data. Security groups provide stateful filtering of ingress and egress network traffic to AWS resources. No security group should allow unrestricted ingress access to well-known ports, such as SSH and Windows remote desktop protocol (RDP). For inbound traffic, in your security groups, allow only TCP or UDP connections on authorized ports. For connecting to Amazon Elastic Compute Cloud (Amazon EC2) instances, use [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) or [Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html) instead of direct SSH or RDP access.

For more information, see the following resources:
+ [Work with security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html) in the Amazon EC2 documentation
+ [Control traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html#DefaultSecurityGroup) in the Amazon VPC documentation

## Block public access to Systems Manager documents
<a name="block-ssm-doc-access"></a>

Unless your use case requires public sharing to be turned on, the AWS Systems Manager best practices recommend that you block public sharing for Systems Manager documents. Public sharing might provide unintended access to documents. A public Systems Manager document can expose valuable and sensitive information about your account, resources, and internal processes.

 For more information, see the following resources:
+ [Best practices for shared Systems Manager documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-ssm-sharing.html#best-practices-shared) in the Systems Manager documentation
+ [Modify permissions for a shared Systems Manager document](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-ssm-sharing.html#modify-permissions-shared) in the Systems Manager documentation

## Block public access to Lambda functions
<a name="block-lambda-access"></a>

[AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. Lambda functions should not be publicly accessible because this might allow unintended access to the function code.

We recommend that you configure [resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_resource-based) for Lambda functions to deny access from outside of your account. You can achieve this by removing permissions or by adding the `AWS:SourceAccount` condition to the statement that allows access. You can update resource-based policies for Lambda functions through the Lambda API or AWS Command Line Interface (AWS CLI).

We also recommend that you enable the **[Lambda.1] Lambda function policies should prohibit public access** control in AWS Security Hub CSPM. This control validates that resource-based policies for Lambda functions prohibit public access.

For more information, see the following resources:
+ [AWS Lambda controls](https://docs.aws.amazon.com/securityhub/latest/userguide/lambda-controls.html) in the Security Hub CSPM documentation
+ [Using resource-based policies for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) in the Lambda documentation
+ [Resources and conditions for Lambda actions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-api-permissions-ref.html) in the Lambda documentation

## Restrict inbound and outbound traffic in the default security group
<a name="default-security-group"></a>

If you don't associate a custom security group when you provision an AWS resource, then the resource is associated with the VPC's default security group. The default rules for this security group allow all inbound traffic from all resources that are assigned to this security group, and they allow all outbound IPv4 and IPv6 traffic. This might permit unintended traffic to the resource.

AWS recommends that you don't use the default security group. Instead, create custom security groups for specific resources or groups of resources.

Because the default security group can't be deleted, we recommend that you change the default security group rules to restrict inbound and outbound traffic. When configuring security group rules, follow the principle of least privilege.

We also recommend that you enable the **[EC2.2] VPC default security groups should not allow inbound or outbound traffic** control in Security Hub CSPM. This control validates that the default security group of a VPC denies inbound and outbound traffic.

For more information, see the following resources:
+ [Control traffic to your AWS resources using security groups in the Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html#DefaultSecurityGroup) documentation
+ [Default security groups for your VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/default-security-group.html) in the Amazon VPC documentation
+ [Amazon EC2 controls](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-2) in the Security Hub CSPM documentation

## Scan for software vulnerabilities and unintended network exposure
<a name="scan-software-vulnerabilities"></a>

We recommend that you enable Amazon Inspector in all of your accounts. [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) is a vulnerability management service that continually scans your Amazon EC2 instances, Amazon Elastic Container Registry (Amazon ECR) container images, and Lambda functions for software vulnerabilities and unintended network exposure. It also supports deep inspection of Amazon EC2 instances. When Amazon Inspector identifies a vulnerability or an open network path, it produces a finding that you can investigate. If Amazon Inspector and Security Hub CSPM are both set up in your account, then Amazon Inspector automatically sends security findings to Security Hub CSPM for centralized management.

For more information, see the following resources:
+ [Scanning resources with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-resources.html) in the Amazon Inspector documentation
+ [Amazon Inspector Deep inspection for Amazon EC2](https://docs.aws.amazon.com/inspector/latest/user/scanning-ec2.html#deep-inspection) in the Amazon Inspector documentation
+ [Scan EC2 AMIs using Amazon Inspector](https://aws.amazon.com/blogs/security/how-to-scan-ec2-amis-using-amazon-inspector/) in the AWS Security Blog
+ [Building a scalable vulnerability management program on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/vulnerability-management/introduction.html) in AWS Prescriptive Guidance
+ [Automate network protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_auto_protect.html) in the AWS Well-Architected Framework
+ [Automate compute protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_compute_auto_protection.html) in the AWS Well-Architected Framework

## Set up AWS WAF
<a name="setup-aws-waf"></a>

[AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) is a web application firewall that helps you monitor and block HTTP or HTTPS requests that are forwarded to your protected web application resources, such as Amazon API Gateway APIs, Amazon CloudFront distributions, or Application Load Balancers. Based on criteria that you specify, the service responds to requests either with the requested content, with an HTTP 403 status code (Forbidden), or with a custom response. AWS WAF can help protect web applications or APIs against common web exploits that can affect availability, compromise security, or consume excessive resources. Consider setting up AWS WAF in your AWS accounts and using a combination of AWS managed rules, custom rules, and partner integrations to help protect your applications from application layer (layer 7) attacks.

For more information, see the following resources:
+ [Getting started with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html) in the AWS WAF documentation
+ [AWS WAF delivery partners](https://aws.amazon.com/waf/partners/) on the AWS website
+ [Security automations for AWS WAF](https://aws.amazon.com/solutions/implementations/security-automations-for-aws-waf/) in the AWS Solutions Library
+ [Implement inspection and protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_inspection.html) in the AWS Well-Architected Framework

## Configure advanced protections against DDoS attacks
<a name="ddos-attacks"></a>

[AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html) provides protections against distributed denial of service (DDoS) attacks for AWS resources at the network and transport layers (layer 3 and 4) and the application layer (layer 7). This service is available in two options: AWS Shield Standard and AWS Shield Advanced. Shield Standard automatically protects supported AWS resources, at no additional charge.

We recommend that you subscribe to Shield Advanced, which provides expanded DDoS attack protection for protected resources. The protections that you receive from Shield Advanced vary depending on your architecture and configuration choices. Consider implementing Shield Advanced protections for applications where you need any of the following:
+ Guaranteed availability for the users of the application.
+ Rapid access to DDoS mitigation experts if the application is affected by a DDoS attack.
+ Awareness by AWS that the application might be affected by a DDoS attack and notification of attacks from AWS and escalation to your security or operations teams.
+ Predictability in your cloud costs, including when a DDoS attack affects your use of AWS services.

For more information, see the following resources:
+ [AWS Shield Advanced overview](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html) in the Shield documentation
+ [AWS Shield Advanced protected resources](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary-protected-resources.html) in the Shield documentation
+ [AWS Shield Advanced capabilities and options](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary-capabilities.html) in the Shield documentation
+ [Responding to DDoS events](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-responding.html) in the Shield documentation
+ [Implement inspection and protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_inspection.html) in the AWS Well-Architected Framework

## Use a defense-in-depth approach to control network traffic
<a name="defense-in-depth"></a>

AWS Network Firewall is a stateful, managed, network firewall and intrusion detection and prevention service for virtual private clouds (VPCs) in the AWS Cloud. It helps you deploy essential network protections at the perimeter of the VPC. This includes filtering traffic going to and coming from an internet gateway, NAT gateway, or over VPN or AWS Direct Connect. Network Firewall includes features that help protect against common network threats. The stateful firewall in Network Firewall can incorporate context from traffic flows, such as connections and protocols, to enforce policies.

For more information, see the following resources:
+ [AWS Network Firewall documentation](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)
+ [Control traffic at all layers](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_layered.html) in the AWS Well-Architected Framework
