---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-perimeter-security/perimeter-individual-account.html
---

# Deploying perimeter services in individual Application accounts
<a name="perimeter-individual-account"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

The following diagram illustrates the architecture pattern where the perimeter services are deployed and managed independently in individual Application accounts.

![Deploying perimeter services into individual Application accounts.](http://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-perimeter-security/images/guide-img/36fc75a2-a16a-4cf6-bea6-724dfeddb825/images/3d839907-7ccf-4461-976d-695e5de9cb39.png)

There are several benefits of deploying the perimeter services into** **Application accounts:
+ This design provides the autonomy for individual workload accounts to customize service configurations based on their needs. This approach removes the dependency on a specialized team to implement changes to resources in a shared account, and enables developers in each team to manage configurations independently.
+ Each account has its own service quotas, so application owners don't have to work within the quotas of a shared account.
+ This design helps contain the impact of malicious activity by limiting it to a particular account and preventing the attack from spreading to other workloads.
+ It removes the risks of change, because the scope of impact is limited to just the workload in question. You can also use AWS Identity and Access Management (IAM) to limit the teams that can implement changes, so there's a logical separation between workload teams and the central networking team.
+ By decentralizing the implementation of network ingress and egress, but having common logical controls (by using services such as AWS Firewall Manager) you can tune network controls to specific workloads while continuing to meet a minimum standard of control objectives.

The following sections dive into each service and discuss architectural considerations.

## Amazon CloudFront
<a name="perimeter-individual-acct-cloudfront"></a>

In this deployment architecture, [Amazon CloudFront](https://aws.amazon.com/cloudfront/) configurations, including edge functions, are managed and deployed in the individual** **Application accounts**.** This verifies that each application owner and workload account has the autonomy to configure perimeter services based on the needs of their application.

The dynamic and static origins are located in the same** **Application account,** **and CloudFront distributions have account-level access to these origins. Logs from CloudFront distributions are stored locally in each Application account. Logs can be replicated to the Log Archive account to support compliance and regulatory needs.

## AWS WAF
<a name="perimeter-individual-acct-waf"></a>

In this deployment architecture, [AWS WAF](https://aws.amazon.com/waf/) is attached to the CloudFront distributions that are configured in the Application account. As with the previous pattern, we recommend that you use AWS Firewall Manager to centrally manage web ACLs and make sure that all resources are compliant. Common AWS WAF rules such as the AWS managed core rule set and the Amazon IP reputation list should be added as default. These rules are automatically applied to any eligible resource in the Application account.

In addition to the rules enforced by Firewall Manager, each application owner can add AWS WAF rules that are relevant to their application security to the web ACL. This allows for flexibility in each Application account** **while still retaining overall control in the Security Tooling account.

Use the Firewall Manager logging option to centralize logs and send them to an S3 bucket in the Security Tooling account. Each application team is provided access to review the AWS WAF dashboards for their application. You can set up the dashboard by using a service such as Amazon Quick Sight. If any false positives are identified or other updates to the AWS WAF rules are needed, you can add application-level AWS WAF rules to the web ACL that's deployed by Firewall Manager. The logs are replicated to the Log Archive account and archived for security investigations.

## AWS Global Accelerator
<a name="perimeter-individual-acct-global-accelerator"></a>

[AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) lets you create *accelerators* to improve the performance of your applications for local and global users. Global Accelerator provides you with static IP addresses that serve as fixed entry points to your applications that are hosted in one or more AWS Regions. You can associate these addresses with regional AWS resources or endpoints, such as Application Load Balancers, Network Load Balancers, EC2 instances, and Elastic IP addresses. This enables traffic to ingress to the AWS global network as close to your users as possible.

Global Accelerator doesn't currently support cross-account origins. Therefore, it is deployed into the same account as the origin endpoint. Deploy the accelerators in each Application account** **and add them as protected resources for AWS Shield Advanced in the same account. Shield Advanced mitigations will allow only valid traffic to reach the Global Accelerator listener endpoints.

## AWS Shield Advanced and Amazon Route 53 health checks
<a name="perimeter-individual-acct-health-checks"></a>

To configure [AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html) to help protect your CloudFront distributions, you need to subscribe each Application account to Shield Advanced. You should configure features such as access to the Shield Response Team (SRT) and proactive engagement at the account level, because they should be configured in the same account as the resource. Use Firewall Manager with auto-remediation to add your CloudFront distributions as protected resources, and apply the policy to each account. Route 53 health checks for each CloudFront distribution should be deployed in the same account and associated with the resource.

## Amazon Route 53 zones and ACM
<a name="perimeter-individual-acct-route53-acm"></a>

When you use services such as [CloudFront](https://aws.amazon.com/cloudfront/), the Application accounts require access to the account that hosts the root domain in order to create custom subdomains and to apply certificates issued by [ACM ](https://aws.amazon.com/certificate-manager/)or a third-party certificate. You can delegate a public domain from the central Shared Services account to individual Application accounts by using [Route 53](https://aws.amazon.com/route53/) zone delegation. Zone delegation gives each account the ability to create and manage application-specific subdomains such as API or static subdomains. The ACM in each account allows each Application** **account to manage the certificate vetting and verification processes (organization validation, extended validation, or domain validation) according to their needs.

## CloudFront access logs, Global Accelerator flow logs, and AWS WAF logs
<a name="perimeter-individual-acct-logs"></a>

In this pattern, we configure CloudFront access logs and Global Accelerator flow logs in S3 buckets in individual Application accounts. Developers who want to analyze the logs for performance tuning or false positive reduction will have direct access to these logs without having to request access to a central log archive. Locally stored logs can also support regional compliance requirements such as data residency or PII obfuscation.

Full AWS WAF logs are stored in the S3 buckets in the Log Archive account** **by** **using Firewall Manager logging. Application teams can view logs by using dashboards that are set up by using a service such as Amazon Quick Sight. In addition, each application team has access to the [sampled AWS WAF logs](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing-view-sample.html) from their own account for quick debugging.

We recommend that you replicate logs to a centralized data lake that's located in the Log Archive account. Aggregating the logs in a centralized data lake gives you a comprehensive view of all the traffic to your AWS WAF resources and distributions. This helps security teams centrally analyze and respond to global security threat patterns.

**Design considerations:**
+ This pattern shifts the responsibility of network and security administration to account owners and developers, which could add overhead to the development process.
+ There can be inconsistencies in decision-making. You should establish effective communications, templates, and training to make sure that the services are configured correctly and follow security recommendations.
+ There is a dependency on automation and clear expectations on the baseline security controls combined with the application-specific controls.
+ Use services such as Firewall Manager and AWS Config to make sure that the deployed architecture is compliant with security best practices. In addition, configure AWS CloudTrail monitoring to detect any misconfigurations.
+ Aggregating logs and metrics in a central place for analysis might introduce complexities.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
