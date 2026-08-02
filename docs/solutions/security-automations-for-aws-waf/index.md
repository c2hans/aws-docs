---
source_url: https://docs.aws.amazon.com//solutions/security-automations-for-aws-waf//index.html
---

# Security Automations for AWS WAF

Deploy a set of preconfigured AWS WAF rules to filter common web-based attacks

- **Version**: 4.1.4
- **Released**: 5/2026
- **Author**: AWS
- **Est. deployment time**: 15 mins
- **Estimated cost**: [See details](/solutions/latest/security-automations-for-aws-waf/cost.html)

## Overview

**Important: This solution will retire in December 2026. Deployments (via CloudFormation or GitHub) will remain operational, but customers will assume responsibility for maintenance and API-related updates post-retirement.** **Customers can explore using native [AWS WAF](https://console.aws.amazon.com/wafv2/) capabilities including [AWS Managed Rules](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups.html), native rate-based rules, and the AWS WAF Console for intuitive configuration and management. These native capabilities provide superior functionality, better performance, real-time updates, and enhanced security features compared to the solution.** **Customers running solution versions prior to v3.0.0 (which deployed AWS WAF Classic) should first migrate to AWS WAF v2 using the [AWS WAF migration documentation](https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-from-classic.html). Customers on v3.0.0 or later are already on AWS WAF v2 and can directly adopt native managed rules and console-based management.** Security Automations for AWS WAF automatically deploys a set of AWS WAF (web application firewall) rules that filter common web-based attacks. You can select from preconfigured protective features that define the rules included in an AWS WAF web access control list (ACL). Once deployed, AWS WAF protects your Amazon CloudFront distributions or Application Load Balancers by inspecting web requests. You can use AWS WAF to create custom, application-specific rules that block attack patterns to help ensure application availability, secure resources, and prevent excessive resource consumption. This AWS Solution supports the latest version of the AWS WAF ([AWS WAFV2](/waf/latest/APIReference/Welcome.html)) service API.

## Benefits

### Automatic WAF rules configuration

Automatically launch and configure the AWS WAF settings and protective features that you choose to include during initial deployment by using the AWS CloudFormation template.

### Log analysis

Activate AWS CloudFormation to provision an Amazon Athena query and a scheduled AWS Lambda function responsible for orchestrating Athena, processing result output, and updating AWS WAF.

### Build your own monitoring dashboard

Build a customized dashboard to visualize Amazon CloudWatch metrics emitted by this solution, and gain insights into the pattern of attacks and protection provided by AWS WAF.

## How it works

You can automatically deploy this architecture using the implementation guide and the accompanying AWS CloudFormation template.

[View implementation guide](/solutions/latest/security-automations-for-aws-waf/solution-overview.html)

![Architecture diagram](/images/solutions/security-automations-for-aws-waf/images/security-automations-for-aws-waf-1.png)

1. **Step 1**: **AWS Managed Rules (A)** - This component contains AWS Managed Rules IP reputation rule groups, baseline rule groups, and use-case specific rule groups. These rule groups protect against exploitation of common application vulnerabilities or other unwanted traffic, including those described in OWASP publications, without having to write your own rules.
1. **Step 2**: **Manual IP lists (B and C)** - These components create two AWS WAF rules. With these rules, you can manually insert IP addresses that you want to allow or deny. You can configure IP retention and remove expired IP addresses on allowed or denied IP sets using Amazon EventBridge rules and Amazon DynamoDB . For more information, refer to Configure IP retention on Allowed and Denied AWS WAF IP sets.
1. **Step 3**: **SQL Injection (D) and XSS (E)** - These components configure two AWS WAF rules that are designed to protect against common SQL injection or cross-site scripting (XSS) patterns in the URI, query string, or body of a request.
1. **Step 4**: **HTTP Flood (F)** - This component protects against attacks that consist of a large number of requests from a particular IP address, such as a web-layer DDoS attack or a brute-force login attempt. With this rule, you set a quota that defines the maximum number of incoming requests allowed from a single IP address within a default five-minute period (configurable with the **Athena Query Run Time Schedule** parameter). After this threshold is breached, additional requests from the IP address are temporarily blocked. You can implement this rule by using an AWS WAF rate-based rule, or by processing AWS WAF logs using a Lambda function or Athena query. For more information about the tradeoffs related to HTTP flood mitigation options, refer to Log parser options.
1. **Step 5**: **Scanner and Probe (G)** - This component parses application access logs searching for suspicious behavior, such as an abnormal amount of errors generated by an origin. Then it blocks those suspicious source IP addresses for a customer-defined period of time. You can implement this rule using a Lambda function or Athena query. For more information about the tradeoffs related to scanner and probe mitigation options, refer to Log parser options.
1. **Step 6**: **IP Reputation Lists (H)** - This component is the `IP Lists Parser` Lambda function that checks third-party IP reputation lists hourly for new ranges to block. These lists include the Spamhaus Don’t Route Or Peer (DROP) and Extended DROP (EDROP) lists, the Proofpoint Emerging Threats IP list, and the Tor exit node list.
1. **Step 7**: **Bad Bot (I)** - This component enhances bad bot detection by monitoring direct connections to an Application Load Balancer (ALB) or Amazon CloudFront, in addition to the honeypot mechanism. If a bot bypasses the honeypot and attempts to interact with ALB or CloudFront, the system analyzes request patterns and logs to identify malicious activity. When a bad bot is detected, its IP address is extracted and added to an AWS WAF block list to prevent further access. Bad bot detection operates through a structured logic chain, ensuring comprehensive threat coverage: - HTTP Flood Protection Lambda Log Parser – Collects bad bot IPs from log entries during flood analysis. - Scanner & Probe Protection Lambda Log Parser – Identifies bad bot IPs from scanner-related log entries. - HTTP Flood Protection Athena Log Parser – Extracts bad bot IPs from Athena logs, using partitions across query run. - Scanner & Probe Protection Athena Log Parser – Retrieves bad bot IPs from scanner-related Athena logs, using the same partitioning strategy. - Fallback Detection – If both HTTP Flood Protection and Scanner & Probe Protection are disabled, the system relies on the Log Lambda parser, which logs bot activity based on WAF label filters.
## Deploy with confidence

- **We'll walk you through it**: Get started fast. Read the implementation guide for deployment steps, architecture details, cost information, and customization options.

[Open guide](/solutions/latest/security-automations-for-aws-waf/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Open the CloudFormation template in the AWS Console to begin setting up the infrastructure you need. You'll be prompted to access your AWS account if you haven't yet logged in.

[Launch in the AWS Console](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=WAFSecurityAutomations&templateURL=https:%2F%2Fs3.amazonaws.com%2Fsolutions-reference%2Fsecurity-automations-for-aws-waf%2Flatest%2Faws-waf-security-automations.template&redirectId=SolutionWeb)

## Deployment options

- **Download implementation guide**: Follow the implementation guide for step-by-step actions to deploy this AWS Solution.

[Download Guide](/pdfs/solutions/latest/security-automations-for-aws-waf/security-automations-for-aws-waf.pdf)

- **Source code**: The source code for this AWS Solution is available in GitHub.

[Go to GitHub](https://github.com/awslabs/aws-waf-security-automations)

- **CloudFormation template**: View or modify the CloudFormation template to customize your deployment.

[Download template](https://s3.amazonaws.com/solutions-reference/security-automations-for-aws-waf/latest/aws-waf-security-automations.template?refid=sl_card)

---

## AWS Support

- [Get support for this AWS Solution](/solutions/latest/security-automations-for-aws-waf/contact-aws-support.html)

## RSS Feed

- [Subscribe now to get updates on the latest release.](https://solutions-reference.s3.us-east-1.amazonaws.com/security-automations-for-aws-waf/latest/rss.xml)
