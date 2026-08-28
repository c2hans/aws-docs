---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/security.html
---

# Security
<a name="security"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

With IAM roles, you can assign granular access, policies, and permissions to services and users on the AWS Cloud. This solution creates IAM roles with least privileges, and these roles grant the solution’s resources with needed permissions.

## Data
<a name="data"></a>

All data stored in Amazon S3 buckets and DynamoDB tables have encryption at rest. Data in transit with Firehose are also encrypted.

## Protection capabilities
<a name="protection-capabilities"></a>

Web applications are vulnerable to a variety of attacks. These attacks include specially crafted requests designed to exploit a vulnerability or take control of a server; volumetric attacks designed to take down a website; or bad bots and scrapers programmed to scrape and steal web content.

This solution uses CloudFormation to configure AWS WAF rules, including AWS Managed Rules rule groups and custom rules, to block the following common attacks:
+  **AWS Managed Rules** - This managed service provides protection against common application vulnerabilities or other unwanted traffic. This solution includes [AWS Managed IP reputation rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-ip-rep.html), [AWS Managed baseline rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-baseline.html), and [AWS Managed use-case specific rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-use-case.html). You have the option of selecting one or more rules groups for your web ACL, up to the maximum web ACL capacity unit (WCU) quota.
+  **SQL injection** - Attackers insert malicious SQL code into web requests to extract data from your database. We designed this solution to block web requests that contain potentially malicious SQL code.
+  **XSS** - Attackers use vulnerabilities in a benign website as a vehicle to inject malicious client-site scripts into a legitimate user’s web browser. We designed this to inspect commonly explored elements of incoming requests to identify and block XSS attacks.
+  **HTTP floods** - Web servers and other backend resources are at risk of DDoS attacks, such as HTTP floods. This solution automatically invokes a rate-based rule when web requests from a client exceed a configurable quota. Alternatively, you can enforce this quota by processing AWS WAF logs using a Lambda function or Athena query.
+  **Scanners and probes** - Malicious sources scan and probe internet-facing web applications for vulnerabilities, by sending a series of requests that generate HTTP 4xx error codes. You can use this history to help identify and block malicious source IP addresses. This solution creates a Lambda function or Athena query that automatically parses CloudFront or ALB access logs, counts the number of bad requests from unique source IP addresses per minute, and updates AWS WAF to block further scans from addresses that reached the defined error quota.
+  **Known attacker origins (IP reputation lists)** - Many organizations maintain reputation lists of IP addresses operated by known attackers, such as spammers, malware distributors, and botnets. This solution leverages the information in these reputation lists to help you block requests from malicious IP addresses. In addition, this solution blocks attackers identified by IP reputation rule groups based on Amazon internal threat intelligence.
+  **Bots and scrapers** - Operators of publicly accessible web applications need to trust that the clients accessing their content identify themselves accurately, and that they use services as intended. However, some automated clients, such as content scrapers or bad bots, misrepresent themselves to bypass restrictions. This solution helps you identify and block bad bots and scrapers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Automations for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
