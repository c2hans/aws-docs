---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-perimeter-security/perimeter-additional-services.html
---

# Additional AWS services for perimeter security
<a name="perimeter-additional-services"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

## Dynamic origins: Application Load Balancers
<a name="perimeter-additional-dynamic"></a>

You can configure CloudFront to use [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) origins for dynamic content delivery. This setup allows you to route requests to different Application Load Balancer origins based on various factors such as the request path, hostname, or query string parameters.

Application Load Balancer origins are deployed in the Application account. If your CloudFront distributions are in the Network account, you must set up cross-account permissions for the CloudFront distribution to access the Application Load Balancer origin. The logs from the Application Load Balancer are sent to the Log Archive account.

To help prevent users from directly accessing an Application Load Balancer without going through CloudFront, complete these high-level steps:
+ Configure CloudFront to add a custom HTTP header to requests that it sends to the Application Load Balancer, and configure the Application Load Balancer to forward only the requests that contain the custom HTTP header.
+ Use an AWS-managed prefix list for CloudFront from the Application Load Balancer security group. This limits the inbound HTTP/HTTPS traffic to your Application Load Balancer from only the IP addresses that belong to the CloudFront origin-facing servers.

For more information, see [Restrict access to Application Load Balancers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/restrict-access-to-load-balancer.html) in the CloudFront documentation.

## Static origins: Amazon S3
<a name="perimeter-additional-static"></a>

You can configure CloudFront to use Amazon S3 origins for static content delivery. These origins are deployed in the Application account. If your CloudFront distributions are in the Network account, you must set up cross-account permissions for the CloudFront distribution in the Network account to access the origins.

To verify that your static origin endpoints are accessed only through CloudFront and not directly through the public internet, you can use origin access control (OAC) configurations. For more information about restricting access, see [Restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the CloudFront documentation.

## AWS Firewall Manager
<a name="perimeter-additional-firewall"></a>

AWS Firewall Manager simplifies administration and maintenance tasks across multiple accounts and resources, including AWS WAF, AWS Shield Advanced, Amazon Virtual Private Cloud (Amazon VPC) security groups, AWS Network Firewall, and Amazon Route 53 Resolver DNS Firewall, for a variety of protections.

Delegate the** **Security Tooling account as the Firewall Manager default administrator account and use it to centrally manage AWS WAF rules and Shield Advanced protections across your organization accounts. Use Firewall Manager to centrally manage common AWS WAF rules while giving each application team flexibility to add application-specific rules to the web ACL. This helps enforce organization-wide security policies such as protection against common vulnerabilities while allowing application teams to add AWS WAF rules that are specific to their application.

Use Firewall Manager logging to centralize AWS WAF logs to an S3 bucket in the Security Tooling account, and replicate the logs to the Log Archive account so you can archive it for security investigations. In addition, [integrate Firewall Manager with AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-internal-providers.html)to centrally visualize configuration details and DDoS notifications in Security Hub CSPM.

For additional recommendations, see [AWS Firewall Manager](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html#tool-fms) in the *Security Tooling account* section of the *AWS SRA – core architecture* guide.

## AWS Security Hub CSPM
<a name="perimeter-additional-security-hub"></a>

The integration between Firewall Manager and Security Hub CSPM sends four types of findings to Security Hub CSPM:
+ Resources that aren't properly protected by AWS WAF rules
+ Resources that aren't properly protected by AWS Shield Advanced
+ Shield Advanced findings that indicate that a DDoS attack is under way
+ Security groups that are being used incorrectly

These findings from all organization member accounts are aggregated into the Security Hub CSPM delegated administrator (Security Tooling) account. The security tooling  account aggregates, organizes, and prioritizes your security alerts or findings in a single place. Use Amazon CloudWatch Events rules to send the findings to ticketing systems or create auto-remediations such as blocking malicious IP ranges.

For additional recommendations, see [AWS Security Hub CSPM](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html#tool-security-hub) in the *Security Tooling account* section of the *AWS SRA – core architecture* guide.

## Amazon GuardDuty
<a name="perimeter-additional-guardduty"></a>

You can use the thread intelligence provided by Amazon GuardDuty to [automatically update](https://aws.amazon.com/blogs/security/how-to-use-amazon-guardduty-and-aws-waf-v2-to-automatically-block-suspicious-hosts/) web ACLs in response to GuardDuty findings. For example, if GuardDuty detects suspicious activity, the automation can be used to update the entry in the AWS WAF IP sets and apply the AWS WAF web ACLs to affected resources to block communication from the suspicious host while you perform additional investigation and remediation. The Security Tooling account is the delegated administrator account for GuardDuty. Therefore, you should use an AWS Lambda function with cross-account permissions to update the AWS WAF IP sets in the Application account.

For additional recommendations, see [Amazon GuardDuty](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html#tool-guardduty) in the *Security Tooling account* section of the *AWS SRA – core architecture* guide.

## AWS Config
<a name="perimeter-additional-config"></a>

AWS Config is a prerequisite for Firewall Manager and is deployed in AWS accounts, including the Network account and Application account. In addition, use AWS Config Rules to verify that deployed resources are compliant with security best practices. For example, you could use an AWS Config rule to check if every CloudFront distribution is associated with a web ACL, or enforce all CloudFront distributions to be configured to deliver access logs to an S3 bucket.

For general recommendations, see [AWS Config](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html#tool-config) in the *Security Tooling account* section of the *AWS SRA – core architecture* guide.
