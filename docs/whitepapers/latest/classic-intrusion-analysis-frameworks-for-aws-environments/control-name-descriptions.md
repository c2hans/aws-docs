---
source_url: https://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/control-name-descriptions.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Control Name Descriptions
<a name="control-name-descriptions"></a>

 This section provides detailed descriptions of the controls used in the intrusion method, in the order they are presented in the phases. Intrusion method implementations are likely to follow a category-based implementation.

 For a list of these controls, ordered by category, and for recommendations on how to prioritize implementations, see the [Prioritizing Control Implementations](#aws-network-firewall) section.

## Amazon GuardDuty
<a name="amazon-guardduty"></a>

 [Amazon GuardDuty](https://aws.amazon.com/guardduty) provides intelligent threat detection by collecting, analyzing, and correlating billions of events from AWS CloudTrail, Amazon VPC Flow Logs, and DNS Logs across all of your associated AWS accounts. Amazon GuardDuty cross-references those events with threat intelligence feeds from the AWS Threat Intelligence team and third parties.

 Amazon GuardDuty detects reconnaissance activity, such as unusual API activity, intra-VPC port scanning, unusual patterns of failed login requests, or unblocked port probing from a known, bad IP address.

## Amazon GuardDuty Partners
<a name="amazon-guardduty-partners"></a>

 [Amazon GuardDuty APN Partner](https://aws.amazon.com/guardduty/resources/partners/) products are a complement to Amazon GuardDuty.

## Amazon Detective
<a name="amazon-detective"></a>

 [Amazon Detective](https://aws.amazon.com/detective) makes it easy to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities. Amazon Detective automatically collects log data from your AWS resources and uses machine learning, statistical analysis, and graph theory to build a linked set of data that enables you to easily conduct faster and more efficient security investigations.

 AWS security services like Amazon GuardDuty, Amazon Macie, and AWS Security Hub CSPM as well as partner security products can be used to identify potential security issues, or findings. These services are really helpful in alerting you when something is wrong and pointing out where to go to fix it. But sometimes there might be a security finding where you need to dig a lot deeper and analyze more information to isolate the root cause and take action. Determining the root cause of security findings can be a complex process that often involves collecting and combining logs from many separate data sources, using extract, transform, and load (ETL) tools or custom scripting to organize the data, and then security analysts having to analyze the data and conduct lengthy investigations.

 Amazon Detective simplifies this process by enabling your security teams to easily investigate and quickly get to the root cause of a finding.

## Bottlerocket
<a name="bottlerocket"></a>

 [Bottlerocket](https://aws.amazon.com/bottlerocket) is a Linux-based open-source operating system that is purpose-built by Amazon Web Services for running containers on virtual machines or bare metal hosts. Most customers today run containerized applications on general-purpose operating systems that are updated package-by-package, which makes OS updates difficult to automate. Updates to Bottlerocket are applied in a single step rather than package-by-package. This single-step update process helps reduce management overhead by making OS updates easy to automate using container orchestration services such as Amazon EKS and Amazon ECS. The single-step updates also improve uptime for container applications by minimizing update failures and enabling easy update rollbacks. Additionally, Bottlerocket includes only the essential software to run containers, which improves resource usage and reduces the attack surface.

## AWS WAF, WAF Managed Rules \+ Automation
<a name="aws-waf-waf-managed-rules-automation"></a>

 [AWS WAF](https://aws.amazon.com/waf/) is a web application firewall that helps protect your web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources. AWS WAF gives you control over which traffic to allow or block to your web applications by defining customizable web security rules. You can use AWS WAF to create custom rules that block common attack patterns, such as SQL injection or cross-site scripting, and rules that are designed for your specific application.

### Scanners and Probes
<a name="scanners-and-probes"></a>

 Malicious sources scan and probe Internet-facing web applications for vulnerabilities. They send a series of requests that generate HTTP 4xx error codes, and you can use this history to help identify and block malicious source IP addresses. This solution creates an AWS Lambda function that automatically parses Amazon CloudFront or Application Load Balancer access logs, counts the number of bad requests from unique source IP addresses, and updates AWS WAF to block further scans from those addresses.

### Known Attacker Origins (IP Reputation Lists)
<a name="known-attacker-origins-ip-reputation-lists"></a>

 A number of organizations maintain *IP address reputation lists*, which are lists of IP addresses operated by known attackers, such as spammers, malware distributors, and botnets. These services leverage the information in these reputation lists to help you block requests from malicious IP addresses.

### Bots and Scrapers
<a name="bots-and-scrapers"></a>

 Operators of publicly accessible web applications have to trust that the clients accessing their content identify themselves accurately, and that they will use services as intended. However, some automated clients, such as content scrapers or bad bots, misrepresent themselves to bypass restrictions. These services help you identify and block bad bots and scrapers.

### AWS WAF Security Automations
<a name="aws-waf-security-automations"></a>

Once deployed, AWS WAF protects your Amazon CloudFront distributions or Application Load Balancers by inspecting web requests. You can use AWS WAF to create custom, application-specific rules that block attack patterns to ensure application availability, secure resources, and prevent excessive resource consumption.

 For more information, see [AWS WAF Security Automations](https://aws.amazon.com/solutions/implementations/aws-waf-security-automations/).

## Amazon CloudWatch, CloudWatch Logs, CloudTrail \+ Insights, Reporting & Third Parties
<a name="amazon-cloudwatch-cloudwatch-logs-cloudtrail-insights-reporting-third-parties"></a>

 In addition to Amazon CloudWatch, CloudWatch Logs, AWS CloudTrail, and reporting tools such as Amazon OpenSearch Service, and Amazon Quick, you can integrate with third-party tools such as Splunk, Trend Micro, and Alertlogic.

 You can use [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) to monitor, store, and access your log files from Amazon Elastic Compute Cloud (Amazon EC2) instances, AWS CloudTrail, Amazon Route 53, and other sources. You can then retrieve the associated log data from CloudWatch Logs.

 [Amazon CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) enable you to interactively search and analyze your log data in Amazon CloudWatch Logs. You can run queries to help you quickly and effectively respond to operational issues. If an issue occurs, you can use Amazon CloudWatch Logs Insights to identify potential causes and validate deployed fixes.

 When you create your AWS account, [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html) is automatically enabled. When activity occurs in your AWS account, that activity is recorded in a CloudTrail event. You can easily view events in the CloudTrail console in the event history. From the event history, you can view, search, and download the past 90 days of activity in your AWS account. You can also create a CloudTrail trail to archive, analyze, and respond to changes in your AWS resources.

## Amazon CloudWatch Logs \+ Amazon Lookout for Metrics
<a name="amazon-cloudwatch-logs-amazon-lookout-for-metrics"></a>

 [Amazon Lookout for Metrics](https://aws.amazon.com/lookout-for-metrics/) uses machine learning (ML) to automatically detect and diagnose anomalies (i.e. outliers from the norm) in business and operational time series data, such as a sudden dip in sales revenue or customer acquisition rates. In a couple of clicks, you can connect Amazon Lookout for Metrics to popular data stores like Amazon S3, Amazon Redshift, and Amazon Relational Database Service (RDS), as well as third-party SaaS applications, such as Salesforce, Servicenow, Zendesk, and Marketo, and start monitoring metrics that are important to your business.

 You can use Amazon CloudWatch metrics as a data source for an Amazon Lookout for Metrics detector. For details, see the [Amazon Lookout for Metrics Developer Guide](https://docs.aws.amazon.com/lookoutmetrics/latest/dev/lookoutmetrics-dev.pdf).

## Amazon CloudWatch Logs \+ Amazon Lookout for Metrics \+ Lambda
<a name="amazon-cloudwatch-logs-amazon-lookout-for-metrics-lambda"></a>

 After Amazon Lookout for Metrics creates an anomaly detection model, or detector, you can attach alerts to it using supported output connectors such as Amazon Simple Notiﬁcation Service (Amazon SNS), AWS Lambda functions, Datadog, PagerDuty, Webhooks, and Slack. You can create custom alerts to notify you when Amazon Lookout for Metrics detects an anomaly of a specified severity level. For more details, see [Preview: Amazon Lookout for Metrics, an Anomaly Detection Service for Monitoring the Health of Your Business](https://aws.amazon.com/blogs/aws/preview-amazon-lookout-for-metrics-anomaly-detection-service-monitoring-health-business/).

## AWS Security Hub CSPM
<a name="aws-security-hub"></a>

 [AWS Security Hub CSPM](https://aws.amazon.com/security-hub) gives you a comprehensive view of your high-priority security alerts and compliance status across AWS accounts. With Security Hub CSPM, you now have a single place that aggregates, organizes, and prioritizes your security alerts, or findings, from multiple AWS services, such as Amazon GuardDuty, Amazon Inspector, and Amazon Macie, as well as from AWS Partner offerings.

 A [Security Hub CSPM *insight*](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-insights.html) is a collection of related findings defined by an aggregation statement and optional filters. An insight identifies a security area that requires attention and intervention. Security Hub CSPM offers several managed (default) insights that you cannot modify or delete. You can also create custom insights to track security issues that are unique to your AWS environment and usage.

## AWS Security Hub CSPM Automated Response and Remediation
<a name="aws-security-hub-automated-response-and-remediation"></a>

 The AWS Solutions Implementation [AWS Security Hub CSPM Automated Response and Remediation](https://aws.amazon.com/solutions/implementations/aws-security-hub-automated-response-and-remediation/) addresses this challenge by providing predefined response and remediation actions based on industry compliance standards and best practices.

 AWS Security Hub CSPM Automated Response and Remediation is an add-on solution that works with [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) to provide a ready-to-deploy architecture and a library of automated playbooks. The solution makes it easier for AWS Security Hub CSPM customers to resolve common security findings and to improve their security posture in AWS.

## AWS Security Hub CSPM Partners
<a name="aws-security-hub-partners"></a>

 [AWS Security Hub CSPM APN Partner](https://aws.amazon.com/security-hub/partners/) products are a complement to Amazon GuardDuty.

## Amazon Virtual Private Cloud (Amazon VPC)
<a name="amazon-virtual-private-cloud-amazon-vpc"></a>

 [Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc/) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. You have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways.

 Amazon VPC provides advanced security features, such as security groups and network access control lists, to enable inbound and outbound filtering at the instance level and subnet level. In addition, you can store data in Amazon S3 and restrict access so that it’s only accessible from instances in your Amazon VPC. Optionally, you can choose to launch Dedicated Instances, which run on hardware dedicated to a single customer for additional isolation.

 In this context, Amazon VPC can help prevent attackers from scanning network resources during reconnaissance.

### NAT Gateways
<a name="nat-gateways"></a>

 You can use a [network address translation (NAT) gateway](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html) to enable instances in a private subnet to connect to the internet or other AWS services, but prevent the internet from initiating a connection with those instances.

### Amazon VPC Black Hole Routes
<a name="amazon-vpc-black-hole-routes"></a>

 You can use Amazon VPC black hole routes as an allow list or deny list of network reachable assets before Security Groups or NACLs.

 The state of a route appears in the route table (active \| black hole). When the state is *black hole*, the route’s target isn’t available. For example, the specified gateway isn’t attached to the VPC, or the specified NAT instance has been terminated.

 For more information, see [describe-route-tables](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-route-tables.html) in the *AWS CLI Command Reference*.

### VPC Endpoints
<a name="vpc-endpoints"></a>

 A [VPC endpoint](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-endpoints.html) enables you to privately connect your VPC to supported AWS services and VPC endpoint services powered by PrivateLink, without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC do not require public IP addresses to communicate with resources in the service. Traffic between your VPC and other services does not leave the Amazon network.

## AWS PrivateLink
<a name="aws-privatelink"></a>

 [AWS PrivateLink](https://aws.amazon.com/privatelink) is a purpose-built technology designed for customers to access AWS services in a highly available and scalable manner, while keeping all the network traffic within the AWS network. When you create endpoints for AWS services powered by PrivateLink, these service endpoints appear as Elastic Network Interface (ENI) with private IP addresses in your VPCs. PrivateLink makes it unnecessary to allow list public IP addresses, or manage Internet connectivity using an Internet Gateway, Network Address Translation (NAT) devices, or firewall proxies to connect to AWS services. AWS services available on PrivateLink also support private connectivity over AWS Direct Connect, so applications in your own data centers can connect to AWS services through the Amazon private network using the service endpoints.

## Amazon EC2 Security Groups
<a name="amazon-ec2-security-groups"></a>

 A [security group](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html) is a virtual firewall that controls inbound and outbound traffic to your network resources and Amazon EC2 instance.

## Network Access Control Lists
<a name="network-access-control-lists"></a>

 Similar to a firewall, [Network Access Control Lists (NACLs)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) control traffic in and out of one or more subnets. To add an additional layer of security to your Amazon VPC, you can set up NACLs with rules similar to your security groups.

## AWS Identity and Access Management \+ AWS Organizations
<a name="aws-identity-and-access-management-aws-organizations"></a>

 [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) enables you to securely manage access to AWS services and resources. Using IAM, you can create and manage AWS users and groups, and specify permissions to allow and deny their access to AWS resources.

## AWS Certificate Manager \+ Transport Layer Security
<a name="aws-certificate-manager-transport-layer-security"></a>

 Protecting data in transit denies attackers the ability to capture data in transit during Reconnaissance, unless they are able to impersonate a legitimate endpoint.

 [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) is a service that enables you to easily provision, manage, and deploy public and private Transport Layer Security (TLS) certificates for use with AWS services and your internal connected resources. TLS certificates are used to secure network communications and establish the identity of websites over the internet and resources on private networks.

 For more information, see:
+  [Introducing s2n, a New Open Source TLS Implementation](https://aws.amazon.com/blogs/security/introducing-s2n-a-new-open-source-tls-implementation/)
+  [Easier Certificate Validation Using DNS with AWS Certificate Manager](https://aws.amazon.com/blogs/security/easier-certificate-validation-using-dns-with-aws-certificate-manager/)
+  [Maintaining Transport Layer Security All the Way to Your Container: Using the Network Load Balancer with Amazon ECS](https://aws.amazon.com/blogs/compute/maintaining-transport-layer-security-all-the-way-to-your-container-using-the-network-load-balancer-with-amazon-ecs/)
+  [Encrypting Data in Transit](https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html)

## Network Infrastructure Solutions in the AWS Marketplace
<a name="network-infrastructure-solutions-in-the-aws-marketplace"></a>

 The infrastructure solutions in the AWS Marketplace can help deny attackers access to your data and infrastructure as they conduct reconnaissance.

 For more information, see [Network Infrastructure Software on the AWS Marketplace](https://aws.amazon.com/marketplace/b/2649366011?ref_=hmpg_categories_2649366011).

## Amazon Virtual Private Cloud VPN Gateway \+ AWS Direct Connect
<a name="amazon-virtual-private-cloud-vpn-gateway-aws-direct-connect"></a>

 An Amazon Virtual Private Cloud (Amazon VPC) VPN gateway connection creates a link between your data center (or network) and your Amazon VPC . A customer gateway is the anchor on your side of that connection, and can be a physical or software appliance. The anchor on the AWS side of the VPN connection is known as a virtual private gateway.

 For more information, see https://docs.aws.amazon.com/vpn/index.html.

 You can use [AWS Direct Connect](https://aws.amazon.com/directconnect/) to establish a private virtual interface from your on-premises network directly to your Amazon VPC. This interface provides you with a private, high-bandwidth network connection between your network and your Amazon VPC. With multiple virtual interfaces, you can establish private connectivity to multiple VPCs, while maintaining network isolation.

## Amazon GuardDuty \+ AWS Lambda
<a name="amazon-guardduty-aws-lambda"></a>

 [Amazon GuardDuty](https://aws.amazon.com/guardduty) gives you intelligent threat detection by collecting, analyzing, and correlating billions of events from AWS CloudTrail, Amazon VPC Flow Logs, and DNS Logs across all of your associated AWS accounts, and then cross-references them with threat intelligence feeds from the AWS Threat Intelligence team and third-party information.

 Amazon GuardDuty detects reconnaissance activity, such as unusual API activity, intra-VPC port scanning, unusual patterns of failed login requests, or unblocked port probing from a known bad IP address.

 To learn more about the types of findings that Amazon GuardDuty can identify, see [Finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-active.html).

 [AWS Lambda](https://aws.amazon.com/lambda) is a compute service that lets you run code without provisioning or managing servers. You can use AWS Lambda to run your code in response to events, such as when Amazon GuardDuty finds that a CloudWatch Event was triggered.

 For example, the following blog post describes how to use AWS GuardDuty and AWS Web Application Firewall to automatically block suspicious hosts by triggering AWS Lambda responders: [How to use Amazon GuardDuty and AWS Web Application Firewall to automatically block suspicious hosts](https://aws.amazon.com/blogs/security/how-to-use-amazon-guardduty-and-aws-web-application-firewall-to-automatically-block-suspicious-hosts/).

 When an attack is detected by Amazon GuardDuty, AWS Lambda responders can be used to modify security configurations to block traffic associated with an attack in progress as well as isolate the potentially compromised environment.

 This same approach, AWS GuardDuty > Amazon CloudWatch Events > AWS Lambda responders, can be used to disrupt other flows.

## Honeypot and Honeynet Environments
<a name="honeypot-and-honeynet-environments"></a>

 Deception technology products present themselves as part of a legitimate infrastructure. When an attacker attempts to compromise the infrastructure, the deception technology helps to degrade, detect, and contain the attack, so your system recovers from attacks faster.

 Deception technology products for honeypot or honeynet environments include third-party deception technology solutions, both commercial and open-source. Solutions include Guardicore, Attivo, Illusive, TopSpin, or TrapX. There are also numerous open-source solution honeypot and honeynet projects on GitHub and elsewhere.

## Honeywords and Honeykeys
<a name="honeywords-and-honeykeys"></a>

 Planting false credentials makes attackers think they have something of value when they do not. When an attacker attempts to use stolen, false credentials, it helps your system to detect and contain the attacker, so your system recovers faster. The detected use of honeykeys and honeywords is always a true positive for intrusion attempts.

## AWS WAF \+ AWS Lambda
<a name="aws-waf-aws-lambda"></a>

 [AWS WAF](https://aws.amazon.com/waf/) is a web application firewall that helps protect your web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources. AWS WAF gives you control over which traffic to allow or block to your web applications by defining customizable web security rules. You can use AWS WAF to create custom rules that block common attack patterns, such as SQL injection or cross-site scripting, and rules that are designed for your specific application.

### Honeypot (A) for Bad Bots and Scrapers
<a name="honeypot-a-for-bad-bots-and-scrapers"></a>

 This component automatically sets up a honeypot, which is a security mechanism intended to lure and deflect an attempted attack. The honeypot is a trap endpoint that you can insert in your website to detect inbound requests from content scrapers and bad bots. If a source gets access to the honeypot, the Access Handler AWS Lambda function intercepts and inspects the request to extract its IP address, and then add it to an AWS WAF block list.

## Amazon CloudWatch Events & Alarms \+ Amazon SNS \+ SIEM Solutions
<a name="amazon-cloudwatch-events-alarms-amazon-sns-siem-solutions"></a>

 You can combine Amazon CloudWatch Events & Alarms with Amazon Simple Notification Service (SNS) and integrate them with security information and event management (SIEM) solutions like Splunk or AlertLogic.

 Amazon CloudWatch Events delivers a near real-time stream of system events that describe changes in Amazon Web Services (AWS) resources. Using simple rules that you can quickly set up, you can match events and route them to one or more target functions or streams.

 You can create a CloudWatch alarm that watches a single CloudWatch metric or the result of a math expression based on CloudWatch metrics. The alarm performs one or more actions based on the value of the metric or expression relative to a threshold over a number of time periods. The action can be a notification sent to an Amazon SNS topic.

 You can also add alarms to CloudWatch dashboards and monitor them visually or integrate with other SIEM solutions.

 For more information, see:
+  [Creating custom responses to GuardDuty findings with Amazon CloudWatch Events](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings_cloudwatch.html)
+  [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

## Network Infrastructure Solutions in AWS Marketplace
<a name="network-infrastructure-solutions-in-aws-marketplace"></a>

 The network infrastructure solutions that are available in the AWS Marketplace can help you deny access to the attackers attempting get your data and infiltrate your infrastructure as they conduct reconnaissance.

 For more information, see [Network Infrastructure Software on the AWS Marketplace](https://aws.amazon.com/marketplace/b/2649366011?ref_=hmpg_categories_2649366011).

## Amazon Cognito
<a name="amazon-cognito"></a>

 Amazon Cognito provides solutions to control access to backend resources from your application. You can define roles and assign users to different roles so your application can access only the resources that are authorized for each user.

### Amazon Cognito Identity Pools (Federated Identities)
<a name="amazon-cognito-identity-pools-federated-identities"></a>

 [Amazon Cognito identity pools (federated identities)](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html) enable you to create unique identities for your users and federate them with identity providers. With an identity pool, you can obtain temporary, limited-privilege AWS credentials to access other AWS services.

## Reverse Proxy Architecture
<a name="reverse-proxy-architecture"></a>

 Reverse proxies are a powerful software architecture primitive for fetching resources from a server on behalf of a client. They serve a number of purposes, from protecting servers from unwanted traffic to offloading some of the heavy lifting of HTTP traffic processing.

 For more information, see [NGINX reverse proxy sidecar for a web container hosted with Amazon ECS and AWS Fargate](https://containersonaws.com/pattern/nginx-reverse-proxy-sidecar-ecs-fargate-task).

## Amazon Virtual Private Cloud \+ Automation
<a name="amazon-virtual-private-cloud-automation"></a>

 With Amazon Virtual Private Cloud (Amazon VPC) Subnet Isolation, you can contain compromised systems by using AWS Command Line Interface (AWS CLI), or software development kits using predefined, restrictive security groups. You can save the current security group of the host or instance, and then isolate the host using restrictive ingress and egress security group rules.

 For more information, see [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html).

## AWS Shield
<a name="aws-shield"></a>

 [AWS Shield](https://aws.amazon.com/shield/) is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS. AWS Shield provides always-on detection and automatic, inline mitigations that minimize application downtime and latency, so you don’t have to engage AWS Support to benefit from DDoS protection. There are two tiers of AWS Shield: Standard and Advanced.

 All AWS customers benefit from the automatic protections of AWS Shield Standard, at no additional charge. AWS Shield Standard defends against most common, frequently occurring network and transport layer DDoS attacks that target your website or applications. When you use AWS Shield Standard with Amazon CloudFront and Amazon Route 53, you receive comprehensive availability protection against all known infrastructure (Layer 3 and 4) attacks.

## Amazon VPC Flow Logs \+ Amazon CloudWatch Alarms
<a name="amazon-vpc-flow-logs-amazon-cloudwatch-alarms"></a>

 [Amazon VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) enables you to capture information about the IP traffic going to and from network interfaces in your Amazon VPC. Flow log data is stored using Amazon CloudWatch Logs. After you’ve created a flow log, you can view and retrieve its data in Amazon CloudWatch Logs and Amazon S3, or another analytics tool. You can also use flow logs as a security tool to monitor the traffic that is reaching your instance.

 For more information, see [Publishing flow logs to CloudWatch Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-cwl.html).

## AWS Identity and Access Management (IAM) \+ IAM Policies and Policies Boundaries
<a name="aws-identity-and-access-management-iam-iam-policies-and-policies-boundaries"></a>

 [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) enables you to manage access to AWS services and resources securely. Using IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources.

 You manage access in AWS by creating [policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) and attaching them to IAM identities (users, groups of users, or roles) or AWS resources. A policy is an object in AWS that, when associated with an identity or resource, defines their permissions.

 A [permissions boundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) is a managed policy in which you set the maximum permissions that an identity-based policy can grant to an IAM entity. When you set a permissions boundary for an entity, the entity can perform only the actions that are allowed by both its identity-based policies and its permissions boundaries.

## AWS Identity and Access Management (IAM) Roles
<a name="aws-identity-and-access-management-iam-roles"></a>

 AWS Identity and Access Management (IAM) Roles help deny or contain the blast radius of attacks. For example, you can use an IAM role to grant permissions to applications running on Amazon EC2 instances.

 For more information, see [Using an IAM role to grant permissions to applications running on Amazon EC2 instances](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html).

 Role-based access control (RBAC) and [attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) are authorization strategies that provide flexibility in granting permissions to resources.

## AWS Organizations \+ Service Control Policies (SCPs) \+ AWS Accounts
<a name="aws-organizations-service-control-policies-scps-aws-accounts"></a>

 With [AWS Organizations](https://aws.amazon.com/organizations/), you can create Service Control Policies (SCPs) that centrally control AWS service use across multiple AWS accounts. SCPs put bounds around the permissions that AWS Identity and Access Management (IAM) policies can grant to entities in an account, such as IAM users and roles. For example, IAM policies for an account in your organization cannot grant access to AWS Direct Connect if access is not also allowed by the SCP for the account. Entities can only use the services allowed by both the SCP and the IAM policy for the account.

 [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html) are one type of policy that you can use to manage your organization. SCPs enable you to restrict, at the account level of granularity, what services and actions are available to the users, groups, and roles in those accounts.

## Amazon Simple Storage Service (Amazon S3) Bucket Policies, Object Policies
<a name="amazon-simple-storage-service-amazon-s3-bucket-policies-object-policies"></a>

 A bucket policy is a resource-based AWS Identity and Access Management (IAM) policy. You add a bucket policy to a bucket to grant other AWS accounts or IAM users access permissions for the bucket and the objects in it.

 With an Amazon S3 bucket policy, malicious objects that contain attacker payload can be prevented from directly being uploaded into the bucket. All objects must be uploaded through the application and subject to malware checks before they can be stored in an Amazon S3 bucket.

 For more information, see [Managing access to resources](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-overview.html#access-control-resources-manage-permissions-basics).

## Amazon EC2 – Linux, SELinux – Mandatory Access Control
<a name="amazon-ec2-linux-selinux-mandatory-access-control"></a>

 Mandatory Access Control can be configured as a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls for users (including root) and processes.

## Amazon EC2 – FreeBSD, Trusted BSD – Mandatory Access Control
<a name="amazon-ec2-freebsd-trusted-bsd-mandatory-access-control"></a>

 Mandatory Access Control for FreeBSD and Trusted BSD can be configured as a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls for users (including root) and processes.

## Amazon EC2 – Linux, FreeBSD – Hardening and Minimization
<a name="amazon-ec2-linux-freebsd-hardening-and-minimization"></a>

 Hardening and minimization make it difficult to exploit a vulnerability in a service by reducing the services that are running and removing or uninstalling unnecessary services.

 For example, applying carefully considered sets of recommendations from [CIS Amazon Linux 2 Benchmark - Level 2](https://aws.amazon.com/marketplace/pp/B084Q6BF6K?ref_=srh_res_product_title), and testing possible impacts on applications can reduce the attack surface of these instances running in Amazon EC2.

## Amazon EC2 – Linux – Role-Based Access Control (RBAC) and Discretionary Access Control (DAC)
<a name="amazon-ec2-linux-role-based-access-control-rbac-and-discretionary-access-control-dac"></a>

 RBAC and DAC provide least-privilege account profiles mediated by root that control which users can get access to your resources.

## Amazon EC2 – Windows – Device Guard
<a name="amazon-ec2-windows-device-guard"></a>

 With Windows Device Guard for your Amazon EC2 instance, you can specify which binaries are authorized to run on your server, including user mode and kernel mode binaries, which enhances AppLocker functionality.

## Microsoft Windows Security Baselines
<a name="microsoft-windows-security-baselines"></a>

 A security baseline is a group of Microsoft-recommended configuration settings. You can use security baselines to:
+  Set configuration settings. For example, you can use Group Policy to configure a device with the setting values specified in the baseline.
+  Make sure that user and device configuration settings are compliant with the baseline.

 For more information, see [Windows security baselines on the Microsoft Documentation site.](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-security-baselines)

## AWS Physical & Operational Security Policies & Processes
<a name="aws-physical-operational-security-policies-processes"></a>

 Amazon Web Services is responsible for protecting the global infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure comprises the hardware, software, networking, and facilities that run AWS services. Protecting this infrastructure is AWS’s number one priority, and while you can’t visit our data centers or offices to see this protection firsthand, we provide several reports from third-party auditors who have verified our compliance with a variety of computer security standards and regulations.

 For more information, see [AWS Compliance](https://aws.amazon.com/compliance), [AWS Overview of Security Processes](https://d1.awsstatic.com/whitepapers/aws-security-whitepaper.pdf), and [Data Center Controls](https://aws.amazon.com/compliance/data-center/controls/).

## Immutable Infrastructure – Short-Lived Environments
<a name="immutable-infrastructure-short-lived-environments"></a>

 In the case of Amazon EC2, Containers, and especially AWS Lambda, short environment lifetimes (when compared to traditional datacenters) mean that an environment being targeted at time t=”now” may not be the same as an environment being targeted in time t=”now\+5 minutes”. When environments are being rebuilt or refreshed every few minutes, it is a much more difficult task to make an attack payload persist.

 When your production environment does not have privileges configured, including for the network infrastructure, there is nothing for attackers to modify and your environment is more resilient to attacks.

## Load Balancing
<a name="load-balancing"></a>

 With load balancing, before an attacker can consistently get access to your resources, all the instances included in the load-balanced service need to be compromised by the attack. If one or more instances has not been compromised, the load balancer switches to an unaffected instance, which degrades the attack.

 For more information, see [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/).

## AWS Lambda, Amazon Simple Queue Service (Amazon SQS), AWS Step Functions
<a name="aws-lambda-amazon-simple-queue-service-amazon-sqs-aws-step-functions"></a>

 These services are orchestration mechanisms for containment.

 [AWS Lambda](https://aws.amazon.com/lambda/) lets you run code without provisioning or managing servers. You pay only for the compute time you consume—there is no charge when your code is not running. With AWS Lambda, you can run code for virtually any type of application or backend service, all with zero administration. Just upload your code and AWS Lambda takes care of everything required to run and scale your code with high availability. You can set up your code to automatically trigger from other AWS services or call it directly from any web or mobile app.

 [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. Amazon SQS eliminates the complexity and overhead associated with managing and operating message-oriented middleware, and empowers developers to focus on differentiating work. Using Amazon SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available. Get started with Amazon SQS in minutes using the AWS console, Command Line Interface or SDK of your choice, and three simple commands.

 [AWS Step Functions](https://aws.amazon.com/step-functions/) lets you coordinate multiple AWS services into serverless workflows so you can build and update apps quickly. Using AWS Step Functions, you can design and run workflows that stitch together services such as AWS Lambda and Amazon ECS into feature-rich applications. Workflows are made up of a series of steps: the output of one step is the input for the next step.

## AWS WAF
<a name="aws-waf"></a>

 [AWS WAF ](https://aws.amazon.com/waf/)is a web application firewall that helps protect your web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources.

## AWS container and abstract services
<a name="aws-container-and-abstract-services"></a>

 [AWS container and abstract services](https://aws.amazon.com/compliance/shared-responsibility-model/) prevent access to underlying infrastructure by both customers and threat actors, and segregate service instances while enabling customers to apply selective permissions to allow third parties to access them. This limits the scope and effect of any attack a threat actor could perpetrate using these services.

## Linux cgroups, namespaces, SELinux
<a name="linux-cgroups-namespaces-selinux"></a>

 SELinux and the technologies that support it (including cgroups and namespaces) can enforce capability profiles that prevent running processes from accessing files, network sockets, and other processes, using Mandatory Access Control. This means that, even if a running process is compromised, it can be prevented from accessing other resources on the OS instance, or even doing things expected of regular Unix processes (such as forking copies of itself or reading world-read files).

## Hypervisor-Level Guest-to-Guest and Guest-to-Host Separation
<a name="hypervisor-level-guest-to-guest-and-guest-to-host-separation"></a>

 The hypervisor for Amazon EC2 instances and other services is in-scope for PCI-DSS certification for separating different operating system instances from each other, and guest operating systems from itself. Hypervisor separation, and the additional technologies incorporated as modules into it (such as Security Groups), provide mechanisms to mitigate some risks of one compromised Amazon EC2 instance being used as a platform to compromise other instances.

## AWS Systems Manager State Manager
<a name="aws-systems-manager-state-manager"></a>

 [AWS Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html) helps you define and maintain consistent OS configurations such as firewall settings and anti-malware definitions to comply with your policies. You can monitor the configuration of a large set of instances, specify a configuration policy for the instances, and automatically apply updates or configuration changes.

## AWS Partner Network (APN) Offerings – File Integrity Monitoring
<a name="aws-partner-network-apn-offerings-file-integrity-monitoring"></a>

 File integrity monitoring (FIM) and enforcement are controls that help maintain the integrity of operating system files and application files by verifying the current file state and a known good baseline of these files. Check features of products carefully for enforcement or reversion capabilities. For information about AWS Marketplace solutions, see [File Integrity Monitoring on the AWS Marketplace](https://aws.amazon.com/marketplace/search/results?x=0&y=0&searchTerms=file+integrity+monitoring&page=1&ref_=nav_search_box).

## Third-Party WAF Integrations
<a name="third-party-waf-integrations"></a>

 Some examples of third-party tools that integrate with AWS WAF include Trend Micro, Imperva, and Alert Logic.

 For more information about third-party integrations with AWS WAF, see [AWS WAF Partners](https://aws.amazon.com/waf/partners/).

## AWS Config
<a name="aws-config"></a>

 [AWS Config](https://aws.amazon.com/config/) enables you to assess, audit, and evaluate the configurations of your AWS resources. AWS Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations. With AWS Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your overall compliance against the configurations specified in your internal guidelines. This enables you to simplify compliance auditing, security analysis, change management, and operational troubleshooting.

## AWS Config rules
<a name="aws-config-rules"></a>

 [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) are a configurable and extensible set of Lambda functions (for which source code is available) that trigger when an environment configuration change is registered by the AWS Config service. If AWS Config rules deem a configuration change to be undesirable, they can act to remediate it. In common with all other Lambda functions, AWS Config rules can be assigned IAM Roles with permissions that enable them to make appropriate remedial API calls.

## Amazon CloudWatch Events \+ Lambda
<a name="amazon-cloudwatch-events-lambda"></a>

 [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) occur when various states are detected (such as GuardDuty findings), and can be used to trigger Lambda functions in the same manner as AWS Config rules. If the Lambda functions deem an event to be undesirable, they can act to remediate it, using IAM Roles with the correct permissions to allow them to make appropriate remedial API calls.

## AWS Managed Services
<a name="aws-managed-services"></a>

 [AWS Managed Services](https://aws.amazon.com/managed-services/) monitors the overall health of your infrastructure resources, and handles the daily activities of investigating and resolving alarms or incidents. AWS Managed Services protects your information assets and helps keep your AWS infrastructure secure. With anti-malware protection, intrusion detection, and intrusion prevention systems, AWS Managed Services manages security policies per stack, and is able to quickly recognize and respond to any intrusion.

## CloudFormation \+ Service Catalog
<a name="cloudformation-service-catalog"></a>

 [AWS CloudFormation](https://aws.amazon.com/cloudformation) provides a common language for you to describe and provision all the infrastructure resources in your cloud environment. CloudFormation enables you to use a simple text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all regions and accounts. This file serves as the single source of truth for your cloud environment.

 [Service Catalog](https://aws.amazon.com/servicecatalog/)allows organizations to create and manage catalogs of IT services that are approved for use on AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures. Service Catalog allows you to centrally manage commonly deployed IT services, and helps you achieve consistent governance and meet your compliance requirements, while enabling users to quickly deploy only the approved IT services they need.

## AWS Systems Manager State Manager, or Third-Party or OSS File Integrity Monitoring Solutions on Amazon EC2
<a name="aws-systems-manager-state-manager-or-third-party-or-oss-file-integrity-monitoring-solutions-on-amazon-ec2"></a>

 [AWS Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html) is a secure and scalable configuration management service that automates the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define.

 File integrity monitoring (FIM) and enforcement are controls that help maintain the integrity of operating system files and application files by verifying the current file state and a known good baseline of these files. Check features of products carefully for enforcement or reversion capabilities. For information about AWS Marketplace solutions, see [File Integrity Monitoring on the AWS Marketplace](https://aws.amazon.com/marketplace/search/results?x=0&y=0&searchTerms=file+integrity+monitoring&page=1&ref_=nav_search_box).

## Third-Party Security Tools for Containers
<a name="third-party-security-tools-for-containers"></a>

 There are several third-party security tools available for containers offered by AWS Partners on the [AWS Marketplace](https://aws.amazon.com/marketplace/search/results?x=0&y=0&searchTerms=container+security). [AWS Container Competency Partners](https://aws.amazon.com/containers/partner-solutions/?partner-solutions-cards.sort-by=item.additionalFields.partnerNameLower&partner-solutions-cards.sort-order=asc&awsf.partner-solutions-filter-partner-usecase-finserv=use-case%23security-identity-compliance) help AWS customers better run their container workloads on AWS. These solutions extend our AWS container services by providing additional security, monitoring, and management capabilities.

## Third-Party Security Tools for AWS Lambda Functions
<a name="third-party-security-tools-for-aws-lambda-functions"></a>

 Two of the third-party security tools available for Lambda functions are offered by Check Point Software Technologies Ltd. and Palo Alto Networks.

 Please check the [AWS Marketplace](https://aws.amazon.com/marketplace) for a full, up-to-date list of AWS Partner offerings.

## AWS Partner Offerings – Behavioral Monitoring, Response Tools and Services
<a name="aws-partner-offerings-behavioral-monitoring-response-tools-and-services"></a>

 AWS Partner offerings, such as [Alert Logic](https://aws.amazon.com/marketplace/seller-profile?id=20e24245-5d10-4191-92f1-c7725d18a375) and [Trend Micro](https://aws.amazon.com/marketplace/seller-profile?id=934af31d-efde-4b34-bc44-2d477620a0c8), provide insight into the real threats in your environments.

## AWS Partner Offerings – Anti-Malware Protection
<a name="aws-partner-offerings-anti-malware-protection"></a>

 [AWS Technology Partner](https://aws.amazon.com/partners/technology/) anti-malware protection offerings help to detect and block malicious payloads.

## AWS Lambda Partners
<a name="aws-lambda-partners"></a>

 [AWS Lambda Partners](https://aws.amazon.com/lambda/partners/) provide services and tools that help customers build or migrate their solutions to a microservices based serverless architecture, without having to worry about provisioning or managing servers.

## AWS Container Partners – Security
<a name="aws-container-partners-security"></a>

 [AWS Container Competency Partners](https://aws.amazon.com/what-are-containers/partners/) have a technology product or solution on AWS that offers support to run workloads on containers. The product or solution integrates with AWS services in a way that improves the AWS customer's ability to run workloads using containers on AWS.

## AWS IoT Device Defender \+ AWS IoT SiteWise
<a name="aws-iot-device-defender-aws-iot-sitewise"></a>

 [AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender/) is a fully managed service that helps you secure your fleet of IoT devices. AWS IoT Device Defender continuously audits your IoT configurations to make sure that they aren’t deviating from security best practices.

 [AWS IoT SiteWise](https://aws.amazon.com/iot-sitewise/) is a managed service that makes it easy to collect, store, organize, and monitor data from industrial equipment at scale to help you make better, data-driven decisions.

 For more information, see [Configuration and vulnerability analysis in AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/vulnerability-analysis-and-management.html).

## AWS Secrets Manager
<a name="aws-secrets-manager"></a>

 [AWS Secrets Manager](https://aws.amazon.com/secrets-manager) helps you protect secrets needed to access your applications, services, and IT resources. The service enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. Users and applications retrieve secrets with a call to Secrets Manager APIs, eliminating the need to hardcode sensitive information in plain text.

## Amazon EC2 – Linux, Windows, FreeBSD – Address Space Layout Randomization (ASLR)
<a name="amazon-ec2-linux-windows-freebsd-address-space-layout-randomization-aslr"></a>

 Address space layout randomization (ASLR) is a technology that prevents shellcode from being successful. It does this by randomly offsetting the location of modules and certain in-memory structures. Although this can help prevent the exploitation of vulnerabilities, there are limits to how effective it is. Processors, and operating systems need to provide ASLR support, and on some operating systems, applications must opt in.

## Amazon EC2 – Linux, Windows, FreeBSD – Data Execution Prevention (DEP)
<a name="amazon-ec2-linux-windows-freebsd-data-execution-prevention-dep"></a>

 Data execution prevention (DEP) is a memory safety feature that makes it more difficult for malware to run. It prevents certain memory blocks, such as the stack, from being executed.

 For more information about DEP, see [Data Execution Prevention on Microsoft's Documentation site](https://docs.microsoft.com/en-us/windows/win32/memory/data-execution-prevention#:~:text=Data%20Execution%20Prevention%20(DEP)%20is,of%20memory%20as%20non%2Dexecutable.).

## Amazon EC2 – Windows – User Account Control (UAC)
<a name="amazon-ec2-windows-user-account-control-uac"></a>

 UACs, also known as least-privilege user account, make it more difficult for malware to install and run.

 For more information about UACs, see [How User Account Control works](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/how-user-account-control-works) on the Microsoft Documentation website.

## Amazon Simple Email Service Spam and Virus Protection
<a name="amazon-simple-email-service-spam-and-virus-protection"></a>

 Amazon Simple Email Service (Amazon SES) uses a number of spam and virus protection measures. It uses block lists to prevent mail from known spammers from entering the system. It also performs virus scans on every incoming email message that contains an attachment. Amazon SES makes its spam detection verdicts available to you, so you can decide if you trust each message. In addition to the spam and virus verdicts, Amazon SES provides the DKIM and SPF check results.

 Amazon SES uses in-house content filtering technologies to scan email content for spam and malware. In exceptional cases, accounts identified as sending spam or other low-quality email might be suspended, or Amazon SES may take such other action as it deems appropriate. When malware is detected, Amazon SES prevents these emails from being sent.

 For more information, see [Amazon SES FAQs](https://aws.amazon.com/ses/faqs/).

## AWS Auto Scaling
<a name="aws-auto-scaling"></a>

 [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) monitors your applications and automatically adjusts capacity to maintain steady, predictable performance at the lowest possible cost.

 If a *Respond* control automatically kills an instance of an operating environment (such as an Amazon EC2 instance, container, or Lambda function), AWS Auto Scaling creates new instances from reference images to replace it in line with load requirements.

## AWS Systems Manager State Manager, AWS Systems Manager Inventory, AWS Config
<a name="aws-systems-manager-state-manager-aws-systems-manager-inventory-aws-config"></a>

 [AWS Config](https://aws.amazon.com/config/) continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against your specified configurations.

 When attackers create new AWS assets, or if malware is installed with a regular package, the AWS Systems Manager Inventory identifies it and sends it to AWS Config for evaluation.

## Amazon EC2 Forward Proxy Servers
<a name="amazon-ec2-forward-proxy-servers"></a>

 A forward proxy server is an intermediary for requests from internal users and servers, often caching content to speed up subsequent requests. Companies usually implement proxy solutions to provide URL and web content filtering, IDS/IPS, data loss prevention, monitoring, and advanced threat protection.

## Outbound Proxy Partners
<a name="outbound-proxy-partners"></a>

 [Outbound proxy partner products](https://aws.amazon.com/marketplace/search/results?x=0&y=0&searchTerms=proxy+servers) such as Sophos UTM provide multiple security functions, including firewall, intrusion prevention, VPN, and web filtering. Sophos Outbound Gateway provides a distributed, fault-tolerant architecture to provide visibility, policy enforcement, and elastic scalability to outbound web traffic.

## Amazon GuardDuty \+ AWS Lambda \+ AWS WAF, Security Groups, NACLs
<a name="amazon-guardduty-aws-lambda-aws-waf-security-groups-nacls"></a>

 [Amazon GuardDuty](https://aws.amazon.com/guardduty) gives you intelligent threat detection by collecting, analyzing, and correlating billions of events from AWS CloudTrail, Amazon VPC Flow Logs, and DNS Logs across all of your associated AWS accounts. It then cross-references them with threat intelligence feeds from AWS’s Threat Intelligence team and third-party feeds.

 When an attack is detected by Amazon GuardDuty, AWS Lambda responders can be used to modify security configurations to block traffic associated with an attack in progress as well as isolate the potentially-compromised environment.

 For more information, see [How to use Amazon GuardDuty and AWS Web Application Firewall to automatically block suspicious hosts](https://aws.amazon.com/blogs/security/how-to-use-amazon-guardduty-and-aws-web-application-firewall-to-automatically-block-suspicious-hosts/)

## AWS DR Options
<a name="aws-dr-options"></a>

 The AWS Cloud supports many popular disaster recovery (DR) architectures, from *pilot light* environments that might be suitable for small customer workload data center failures, to *hot standby* environments that enable rapid failover at scale. With data centers in regions all around the world, AWS provides a set of cloud-based disaster recovery services designed to provide rapid recovery of your IT infrastructure and data.

 For more information about available disaster recover technology, see [CloudEndure Disaster Recovery](https://aws.amazon.com/disaster-recovery/) and [Disaster Recovery of Workloads on AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html).

## AWS Partners Offerings – SQL Behavioral Analytics Proxies
<a name="aws-partners-offerings-sql-behavioral-analytics-proxies"></a>

 Third-party behavioral analytics proxies for SQL, such as [SecuPi](https://www.secupi.com/), can detect unauthorized actions on SQL applications and act to constrain access when there is unexpected behavior.

## AWS Nitro Enclaves
<a name="aws-nitro-enclaves"></a>

 [AWS Nitro Enclaves](https://aws.amazon.com/ec2/nitro/nitro-enclaves/) enables customers to create isolated compute environments to further protect and securely process highly sensitive data such as personally identifiable information (PII), healthcare, financial, and intellectual property data within their Amazon EC2 instances. Nitro Enclaves uses the same Nitro Hypervisor technology that provides CPU and memory isolation for EC2 instances.

## AWS Key Management Service (AWS KMS) \+ AWS CloudHSM
<a name="aws-key-management-service-aws-kms-aws-cloudhsm"></a>

 AWS Key Management Service (AWS KMS)and AWS CloudHSM can prevent attackers from exfiltrating clear text data that has been encrypted, as well as crypto key material used to encrypt data.

 [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) makes it easy to manage encryption keys used to encrypt data stored by your applications regardless of where you store it.

 [AWS CloudHSM](https://aws.amazon.com/cloudhsm/) is a cloud-based hardware security module (HSM) that enables you to easily generate and use your own encryption keys on the AWS Cloud.

 For more information, see [AWS CloudHSM](https://aws.amazon.com/cloudhsm/).

## AWS KMS Key Policies
<a name="aws-kms-key-policies"></a>

 The primary method to [manage access to your AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/control-access-overview.html#managing-access) (formerly CMKs) is with policies. Policies are documents that describe who has access to what. Policies attached to an IAM identity are identity-based policies (or IAM polices), and policies attached to other kinds of resources are resource-based policies. In AWS KMS, you must attach resource-based policies to your AWS KMS keys. These are [key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html). All KMS CMKs have a key policy.

## AWS Network Firewall
<a name="aws-network-firewall"></a>

 [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) is a stateful, managed, network firewall and intrusion detection and prevention service for your virtual private cloud (VPC). Its flexible rules engine lets you define firewall rules that give you fine-grained control over network traffic, such as blocking outbound Server Message Block (SMB) requests to prevent the spread of malicious activity.

 AWS Network Firewall includes features that provide protections from common network threats. Its intrusion prevention system (IPS) provides active traffic flow inspection so you can identify and block vulnerability exploits using signature-based detection. AWS Network Firewall also offers web filtering that can stop traffic to known bad URLs and monitor fully qualified domain names.
