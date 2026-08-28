---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/aws-security-hub-deployment.html
---

# AWS Security Hub deployment
<a name="aws-security-hub-deployment"></a>

AWS Security Hub deployment and configuration is a prerequisite for this solution. For more information about setting up AWS Security Hub CSPM, refer to [Setting up AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html) in the *AWS Security Hub User Guide.* This solution also supports [AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html) (non-CSPM version). For more information about setting up AWS Security Hub, refer to [Enabling Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-enable.html).

At minimum, you must have a working Security Hub configured in your primary account. You can deploy this solution in the same account (and AWS Region) as the Security Hub primary account. In each Security Hub primary and secondary account, you must also deploy the member template that allows AssumeRole permissions to the solution’s AWS Step Functions to run remediation runbooks in the account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
