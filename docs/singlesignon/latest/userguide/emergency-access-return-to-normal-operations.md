---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access-return-to-normal-operations.html
---

# Return to normal operations
<a name="emergency-access-return-to-normal-operations"></a>

 Check the [AWS Health Dashboard](https://health.aws.amazon.com/health/status) to confirm when the health of the IAM Identity Center service is restored. To return to normal operations, perform the following steps.

1. After the status icon for the IAM Identity Center service indicates that the service is healthy, sign in to IAM Identity Center.

1. If you can sign in to IAM Identity Center successfully, communicate to emergency access users that IAM Identity Center is available. Instruct these users to sign out and use the AWS access portal to sign back in to IAM Identity Center.

1. After all emergency access users sign out, in the IdP, disable the IdP federation application. We recommend that you perform this task after working hours.

1. Remove all users from the emergency access group in the IdP.

Your emergency access role infrastructure remains in place as a backup access plan, but it is now disabled.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
