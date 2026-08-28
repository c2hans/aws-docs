---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/solution-overview.html
---

# Automatically deploy a single web access control list that filters web-based attacks with Security Automations on AWS WAF
<a name="solution-overview"></a>

**Important**
 [Security Automations for AWS WAF](https://docs.aws.amazon.com/solutions/security-automations-for-aws-waf/) will retire in December 2026. Deployments (via CloudFormation or GitHub) will remain operational, but customers will assume responsibility for maintenance and API-related updates post-retirement. Customers can explore using native AWS WAF capabilities including [AWS Managed Rules](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups.html), native rate-based rules, and the [AWS WAF Console](https://console.aws.amazon.com/wafv2/) for intuitive configuration and management. These native capabilities provide superior functionality, better performance, real-time updates, and enhanced security features compared to the solution.
Customers running solution versions prior to v3.0.0 (which deployed AWS WAF Classic) should first migrate to AWS WAF v2 using the [AWS WAF migration documentation](https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-from-classic.html). Customers on v3.0.0 or later are already on AWS WAF v2 and can directly adopt native managed rules and console-based management.

The Security Automations for AWS WAF solution deploys a set of preconfigured rules to help you protect your applications from common web exploits. This solution’s core service, [AWS WAF](https://aws.amazon.com/waf/), helps protect web applications from attack techniques that can affect application availability, compromise security, or consume excessive resources. You can use AWS WAF to define customizable web security rules. These rules control which traffic to allow or block to web applications and application programming interfaces (APIs) deployed on AWS resources such as [Amazon CloudFront](https://aws.amazon.com/cloudfront/), [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/applicationloadbalancer/) (ALB). For more supported resource types, see [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.

Configuring AWS WAF rules can be challenging and burdensome to large and small organizations alike, especially for those who don’t have dedicated security teams. To simplify this process, the Security Automations for AWS WAF solution automatically deploys a single web access control list (ACL) with a set of AWS WAF rules designed to filter common web-based attacks. During initial configuration of this solution’s [AWS CloudFormation](https://aws.amazon.com/cloudformation/) template, you can specify which protective features to include. After you deploy this solution, AWS WAF inspects web requests to their existing CloudFront distribution(s) or ALB(s), and blocks them when applicable.

 **A CloudFormation template deploys a web ACL with AWS WAF filtering rules.**

![configuration web acl](http://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/images/configuration-web-acl.png)

This implementation guide discusses architectural considerations, configuration steps, and operational best practices for deploying this solution in the Amazon Web Services (AWS) Cloud. It includes links to CloudFormation templates that launch, configure, and run the AWS security, compute, storage, and other services required to deploy this solution on AWS, using AWS best practices for security and availability.

The information in this guide assumes working knowledge of AWS services such as AWS WAF, CloudFront, ALBs, and [AWS Lambda](https://aws.amazon.com/lambda/). It also requires basic knowledge of common web-based attacks and mitigation strategies.

**Note**
As of version 3.0.0, this solution supports the latest version of the AWS WAF service API ([AWS WAFV2](https://docs.aws.amazon.com/waf/latest/APIReference/Welcome.html)).

This guide is intended for IT managers, security engineers, DevOps engineers, developers, solutions architects, and website administrators.

**Note**
We recommend using this solution as a starting point for implementing AWS WAF rules. You can customize the [source code](https://github.com/aws-solutions/aws-waf-security-automations), add new custom rules, and leverage more [AWS WAF managed rules](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list.html) based on your needs.

Use this navigation table to quickly find answers to these questions:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this solution. The total cost for running this solution depends on the protection activated and the amount of data ingested, stored, and processed. |  [Cost](cost.md)  |
| Understand the security considerations for this solution. |  [Security](security.md)  |
| Know which AWS Regions are supported for this solution. |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
| View or download the CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution. |  [AWS CloudFormation template](aws-cloudformation-templates.md)  |
| Use Support to help you deploy, use, or troubleshoot the solution. |  [Support](contact-aws-support.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution |  [GitHub repository](https://github.com/aws-solutions/aws-waf-security-automations/)  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Automations for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
