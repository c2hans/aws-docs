---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/issues.html
---

# Issues
<a name="issues"></a>

 **Not sending requests from the correct context.**

 All calls to AWS Security Incident Response APIs must originate from an IAM principal in the service delegated administrator or membership account. Ensure that you are operating from the correct IAM principal in the AWS account that is your organization's AWS Security Incident Response delegated administrator or membership account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
