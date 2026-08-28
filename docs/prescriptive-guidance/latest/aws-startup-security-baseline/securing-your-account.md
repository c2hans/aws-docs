---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/securing-your-account.html
---

# Securing your account
<a name="securing-your-account"></a>

Controls and recommendations in this section help keep your AWS account secure. They cover using AWS Identity and Access Management (IAM) users and roles (also known as *principals*) for both human and machine access, restricting the use of the root user, and requiring multi-factor authentication. In this section, you confirm that AWS has the contact information necessary to reach you regarding your account activity and status. You also set up monitoring services, such as AWS Trusted Advisor, AWS Identity and Access Management Access Analyzer, and AWS Budgets, so that you are notified of account activity and can respond if unauthorized or unexpected activity occurs.

**This section contains the following topics:**
+ [ACCT.01 Set account-level contacts to valid email distribution lists](acct-01.md)
+ [ACCT.02 Restrict use of the root user](acct-02.md)
+ [ACCT.03 Configure console access for each user](acct-03.md)
+ [ACCT.04 Assign permissions](acct-04.md)
+ [ACCT.05 Require multi-factor authentication to log in](acct-05.md)
+ [ACCT.06 Enforce a password policy](acct-06.md)
+ [ACCT.07 Deliver CloudTrail logs to a protected Amazon S3 bucket](acct-07.md)
+ [ACCT.08 Prevent public access to private Amazon S3 buckets](acct-08.md)
+ [ACCT.09 Delete unused VPCs, subnets, and security groups](acct-09.md)
+ [ACCT.10 Configure AWS Budgets to monitor your spending](acct-10.md)
+ [ACCT.11 Enable IAM Access Analyzer](acct-11.md)
+ [ACCT.12 Resolve AWS Trusted Advisor high-risk items](acct-12.md)
+ [ACCT.13 Use short-lived credentials for access to your AWS resources](acct-13.md)
+ [ACCT.14 Enable Amazon GuardDuty](https://apg-library.amazonaws.com/content-viewer/author/684f6a94-9fdf-4c45-961d-46bb264246ae#acct-14)
+ [ACCT.15 Enable AWS Security Hub](https://apg-library.amazonaws.com/content-viewer/author/684f6a94-9fdf-4c45-961d-46bb264246ae#acct-15)
+ [ACCT.16 Enable AWS Cost Anomaly Detection](https://apg-library.amazonaws.com/content-viewer/author/684f6a94-9fdf-4c45-961d-46bb264246ae#acct-16)
+ [ACCT.17 Restrict AWS API calls to used Regions only](https://apg-library.amazonaws.com/content-viewer/author/684f6a94-9fdf-4c45-961d-46bb264246ae#acct-17)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
