---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/billing-considerations.html
---

# Billing considerations
<a name="billing-considerations"></a>

If you use AWS Organizations for the transition to multiple AWS accounts, you can use the [consolidated billing feature](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) (AWS Organizations documentation). This feature provides a single, combined bill that shows the charges across multiple accounts.

The following are billing best practices and recommendations for transitioning to multiple accounts:
+ If you need access to your historical billing data, before you accept the invitation to join an organization, create a [Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/cur-consolidated-billing.html) (AWS Cost and Usage Report documentation) to export the account's historical billing data to an Amazon Simple Storage Service (Amazon S3) bucket. After you accept the invitation to join the organization, the account's historical billing data is no longer accessible.
+ If you need to combine two organizations, such as for a merger or acquisition, you can use the [Account Assessment for AWS Organizations](https://aws.amazon.com/solutions/implementations/account-assessment-for-aws-organizations/) (AWS Solutions Library) to evaluate the resource-based policies in each organization and identify any potential issues before combining them.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
