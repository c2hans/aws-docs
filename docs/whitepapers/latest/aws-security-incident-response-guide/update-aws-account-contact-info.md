---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/update-aws-account-contact-info.html
---

# Update AWS account contact information
<a name="update-aws-account-contact-info"></a>

 For each of your AWS accounts, it’s important to have accurate and up-to-date contact information so that the correct stakeholders receive important notifications from AWS on topics like security, billing, and operations. For each AWS account, you have a primary contact and alternate contacts for security, billing and operations. Differences between these contacts can be found in the [AWS Account Management Reference Guide](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html#manage-acct-update-contact-alternate).

 For details on managing alternate contacts, refer to the [AWS documentation on adding, changing, or removing alternate contacts](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-account-payment.html#manage-account-payment-alternate-contacts). It’s a best practice to use an email distribution list if your team manages billing, operations, and security-related issues. An email distribution list removes dependencies on one person, which can cause blockages if they are out of the office or leave the company. You should also verify that the email and account contact information, including the phone number, are well protected to defend against root account password resets and multi-factor authentication (MFA) resets.

 For customers using AWS Organizations, organization administrators can centrally manage alternate contacts for member accounts using the management account or a delegated administrator account without requiring credentials for each AWS account. You will also need to verify that newly created accounts have accurate contact information. Refer to the [Automatically update alternate contacts for newly created AWS accounts blog post](https://aws.amazon.com/blogs/mt/automatically-update-alternate-contacts-for-newly-created-aws-accounts/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
