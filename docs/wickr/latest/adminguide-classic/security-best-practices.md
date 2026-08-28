---
source_url: https://docs.aws.amazon.com/wickr/latest/adminguide-classic/security-best-practices.html
---

This guide documents the classic version of the AWS Wickr administration console, released before March 13, 2025. For documentation on the new AWS Wickr administration console, see [ Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Security best practices for AWS Wickr
<a name="security-best-practices"></a>

Wickr provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.

To prevent potential security events associated with your use of Wickr, follow these best practices:
+ Implement least privilege access and create specific roles to be used for Wickr actions. Use IAM templates to create a role. For more information, see [AWS managed policies for AWS Wickr](security-iam-awsmanpol.md).
+ Access the AWS Management Console for Wickr by authenticating to the AWS Management Console first. Don't share your personal console credentials. Anyone on the internet can browse to the console, but they can't sign in or start a session unless they have valid credentials to the console.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
